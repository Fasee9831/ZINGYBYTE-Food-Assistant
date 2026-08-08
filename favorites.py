"""Favorites backend glue — save/get from the session `favorite_dishes` store.

Store schema (initialized in utils.init_app_state): ``st.session_state.favorite_dishes``
is a plain dict of {"Dish Name": Price}. All read/write paths go through this
single source of truth; the LLM gets the same store via ``knowledge._build_favorites_context``.
"""

import re
import uuid
from typing import Dict, List, Optional, Tuple
import streamlit as st
from knowledge import ZINGYBYTE_MENU, search_menu_dish

FETCH_FAVORITES = "FETCH_FAVORITES"

_FILLERS = {
    "i", "i'd", "me", "my", "mine", "the", "a", "an", "and", "or", "for",
    "to", "of", "in", "on", "as", "is", "make", "add", "save", "set", "mark",
    "keep", "want", "favorite", "favourite", "favorites", "favourites", "fav",
    "favs", "heart", "dish", "item", "food", "please", "now", "it", "this",
    "from", "menu", "list",
}


def _normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", (text or "").lower())


def _all_menu_items() -> List[Dict]:
    return [item for group in ZINGYBYTE_MENU.values() for item in group]


def get_user_id() -> str:
    if "user_id" not in st.session_state:
        st.session_state["user_id"] = uuid.uuid4().hex[:8]
    return st.session_state["user_id"]


def _favorites_store() -> Dict[str, float]:
    return st.session_state.setdefault("favorite_dishes", {})


def save_favorite(user_id: str, dish_name: str, price: float) -> None:
    """Persist a dish for a user: favorite_dishes[Dish Name] = price."""
    _favorites_store()[dish_name] = float(price)


def get_user_favorites(user_id: Optional[str] = None) -> List[Dict]:
    """Return [{name, price}] from the session store, in save order."""
    saved = _favorites_store()
    return [{"name": name, "price": int(price)} for name, price in saved.items()]


def detect_add_favorite_intent(user_input: str) -> Optional[str]:
    """Returns the extracted dish name when the message asks to save a favorite."""
    text = (user_input or "").strip()
    if not text:
        return None
    lower = text.lower()

    action_pattern = re.compile(
        r"\b(add|make|save|set|mark|keep)\b.{0,80}?"
        r"\b(?:favorite|favourite|fav)s?\b"
    )
    reverse_pattern = re.compile(
        r"\b(?:favorite|favourite|fav)s?\b.{0,40}?\b(add|save|set|mark|keep)\b"
    )
    if not (action_pattern.search(lower) or reverse_pattern.search(lower)):
        return None

    # Prefer an exact canonical menu-name match inside the sentence
    for item in _all_menu_items():
        if _normalize(item["name"]) in _normalize(text):
            return item["name"]

    # Fallback: chew off filler words around the dish phrase
    marker = re.search(r"\b(?:favorite|favourite|fav)s?\b", lower)
    region = lower[: marker.start()] if marker else lower
    region = re.sub(r"\b(add|make|save|set|mark|keep|please|the|a|an|me)\b", " ", region)
    region = region.replace("heart", " ")
    words = [w for w in region.split() if w not in _FILLERS]
    dish = " ".join(words).strip(" .,'\"!?")
    return dish if _plausible_dish(dish) else None


def _plausible_dish(dish: str) -> bool:
    dish = dish.strip()
    if not dish:
        return False
    n = _normalize(dish)
    for item in _all_menu_items():
        if _normalize(item["name"]) in n:
            return True
    return len(dish.split()) >= 2


def handle_add_favorite_request(user_input: str) -> Optional[Tuple[str, bool]]:
    """Process an add-to-favorites intent.

    Returns (reply_text, saved) when the message is an intent request,
    None when it's a normal chat query so the LLM path continues.
    """
    dish_phrase = detect_add_favorite_intent(user_input or "")
    if dish_phrase is None:
        return None

    dish = search_menu_dish(dish_phrase)
    if dish is None:
        return (
            f"I couldn't find **{dish_phrase.strip()}** on our current menu — "
            "let me know the exact dish name and I'll add it for you! 🍽️",
            False,
        )

    save_favorite(get_user_id(), dish["name"], dish["price"])
    return (f"I've added **{dish['name']}** to your favorites! ❤️", True)


def format_favorites_display(user_id: Optional[str] = None) -> str:
    """Clean bulleted list of saved favorites — dish name + price only."""
    favs = get_user_favorites(user_id)
    if not favs:
        return (
            "You haven't added any favorite dishes yet! Ask me to add dishes like "
            "*'Add Mexican Grilled Chicken & Cheese to my favorites'*."
        )
    lines = ["❤️ **Your Favorite Dishes:**"]
    for fav in favs:
        lines.append(f"• **{fav['name']}** — ₹{fav['price']}")
    return "\n".join(lines)