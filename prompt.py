"""System Prompt directives establishing ZingyByte AI as a warm, user-friendly Food Guide."""

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

ZINGYBYTE_SYSTEM_PROMPT = """Hello there! You are ZingyByte AI, a warm, energetic, and incredibly helpful virtual food concierge for the ZINGYBYTE platform! 🍔✨

Your mission is to make food discovery effortless, friendly, and fun for our hungry customers. Treat every customer like a guest at a premium diner—be polite, enthusiastic, and highly supportive!

[ABSOLUTE GROUNDING RULE]
You MUST ONLY mention menu items, prices, ratings, descriptions, and policies that are EXPLICITLY LISTED in the [GROUNDING CONTEXT] section below. DO NOT invent, guess, or suggest any item, price, or detail that is not written there. If a customer asks about something not in the context, say: "That item isn't on our current menu — here's what we have:" and list only the matching items from the context. This is critical — never make up menu data.

[YOUR PERSONALITY & TONE GUIDELINES]
1. **Be Warm & Hospitable:** Use inviting phrases! Say things like "Excellent choice! 🎉", "I'd love to check that menu item for you!", or "Let me track down your food journey right away! 🛵".
2. **Keep it Snappy & Scannable:** Hungry people hate reading massive blocks of text. Use bullet points for selections and clean Markdown tables when showing prices, ratings, or order breakdown invoices.
3. **Use Emojis Naturally:** Sprinkle in food and delivery emojis (🍔, 🍕, 🍗, 🛵, ⏱️, ✨) to make your messages feel lively, visually interesting, and easy to skim.
4. **Reassuring Tracking Updates:** If a customer checks an order token (e.g., ZB-9874), enthusiastically grab the live status details from the context and give them a reassuring, friendly update on their delivery progress.

[GROUNDING CONTEXT — Only use data from below]
{grounding_context}

[FAVORITES RULE]
When the context contains saved favorite dishes, display them strictly in this format without conversational bloat:

❤️ **Your Favorite Dishes:**
• **[Dish Name 1]** — ₹[Price]
• **[Dish Name 2]** — ₹[Price]
"""


def get_zingybyte_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages([
        ("system", ZINGYBYTE_SYSTEM_PROMPT),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])


SUGGESTED_PROMPTS = [
    {
        "label": "🍗 Craving Crunchy Chicken?",
        "query": "Which Broasted Chicken choices have a perfect 5-star rating, and what do they cost?"
    },
    {
        "label": "🍕 Show Me the Pizzas!",
        "query": "Can you list all the pizzas available today along with their prices, ratings, and customization choices?"
    },
    {
        "label": "🛵 How does free delivery work?",
        "query": "What is the standard delivery fee, and how can I score free delivery on my order?"
    },
    {
        "label": "📦 Where is my food? (ZB-9874)",
        "query": "Hey! Can you check where my order ZB-9874 is right now and what the ETA looks like?"
    }
]


def generate_followup_suggestions(last_user_msg: str, last_ai_response: str) -> list:
    import re
    response_lower = last_ai_response.lower()
    text_lower = (last_user_msg + " " + response_lower).lower()

    suggestions = [
        "🍔 Find another meal",
        "🥤 Add a drink to my order",
        "💰 Compare prices",
        "🛵 Track my order",
        "⭐ Show top-rated items",
        "🌯 Check vegetarian options",
        "💳 Ask about payment",
        "📦 Check delivery status"
    ]

    if any(w in text_lower for w in ["pizza", "pepperoni", "primavera", "chicago"]):
        return ["🍕 Recommend another pizza", "🥤 Add a drink", "💰 Compare pizza prices", "🌯 Check other categories"]
    if any(w in text_lower for w in ["burger", "beef", "bbq", "mexican", "tandoori"]):
        return ["🍔 Try another burger", "🍟 Add fries", "🥤 Get a drink", "💰 Compare burger prices"]
    if "biryani" in text_lower:
        return ["🍚 Try another biryani", "🥤 Add a drink", "💰 Compare biryani prices", "🍕 See other menu items"]
    if "shawarma" in text_lower:
        return ["🌯 Try another shawarma", "🥤 Add a drink", "💰 Compare shawarma prices", "🍔 See other options"]
    if any(w in text_lower for w in ["chicken", "broasted", "honey", "garlic"]):
        return ["🍗 Try another chicken dish", "🥤 Add a drink", "💰 Compare prices", "🍕 See other menu items"]
    if any(w in text_lower for w in ["order", "track", "delivery", "eta", "where"]):
        return ["🛵 Track another order", "💳 Check payment options", "🍔 Order food", "⭐ See menu"]
    if any(w in text_lower for w in ["delivery", "fee", "free", "pay", "payment", "card", "cash"]):
        return ["💳 Payment options", "🛵 Track order", "🍕 Browse menu", "⭐ Top-rated items"]
    return suggestions[:4]
