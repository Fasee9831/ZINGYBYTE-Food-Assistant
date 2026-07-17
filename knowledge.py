"""Structured operational knowledge base containing the parsed ZINGYBYTE menu and business FAQs."""

from typing import Dict, Any, List

# Strict menu schema mapped directly from the verified menu card datasets
ZINGYBYTE_MENU: Dict[str, List[Dict[str, Any]]] = {
    "Biryani": [
        {"name": "Malabar Biryani", "price": 280, "rating": 4.5, "customisable": False, "desc": "A Kerala special with short-grain rice and coconut flavors."},
        {"name": "Chicken Biryani", "price": 249, "rating": 5.0, "customisable": False, "desc": "Juicy chicken pieces cooked with rich spices."},
        {"name": "Afghani Biryani", "price": 350, "rating": 4.7, "customisable": False, "desc": "Mild, creamy flavors with dry fruits."}
    ],
    "Cool Drinks": [
        {"name": "Lemonade", "price": 99, "rating": 4.7, "customisable": False, "desc": "When life gives you lemons, make a refreshing lemonade!"},
        {"name": "Blueberry Mojito", "price": 59, "rating": 5.0, "customisable": False, "desc": "Sweet blueberries add a burst of color and flavor."},
        {"name": "Cold Soda", "price": 99, "rating": 4.8, "customisable": False, "desc": "Fizz up your day with a cold soda."}
    ],
    "Burgers": [
        {"name": "Mexican Grilled Chicken & Cheese", "price": 179, "rating": 4.9, "customisable": True, "desc": "Every bite takes you to the streets of Mexico — no passport needed!"},
        {"name": "Tandoori Twist", "price": 259, "rating": 5.0, "customisable": True, "desc": "Chicken patty marinated in tandoori spices, mint chutney, and fresh onions."},
        {"name": "BBQ Chicken Beef Burger", "price": 349, "rating": 4.8, "customisable": True, "desc": "Smoky BBQ sauce, chicken, and beef in one bite."}
    ],
    "Pizza": [
        {"name": "Primavera Pizza", "price": 99, "rating": 4.9, "customisable": False, "desc": "Fresh, colorful, and bursting with flavor — that's Primavera Pizza perfection!"},
        {"name": "Pepperoni Pizza", "price": 250, "rating": 4.6, "customisable": True, "desc": "One slice of pepperoni, and you're hooked."},
        {"name": "Chicago Deep Dish Pizza", "price": 369, "rating": 4.8, "customisable": True, "desc": "Deep dish pizza variant featuring hearty sauce structures and thick golden crust margins."}
    ],
    "Broasted Chicken": [
        {"name": "Classic Broasted Chicken", "price": 149, "rating": 4.8, "customisable": False, "desc": "That crunch you hear says it all. Pure classic broasted goodness."},
        {"name": "Garlic Broasted Chicken", "price": 249, "rating": 4.7, "customisable": False, "desc": "Every bite brings crispy perfection with a warm garlic kick you'll keep craving."},
        {"name": "Honey Glazed Broasted Chicken", "price": 149, "rating": 5.0, "customisable": False, "desc": "The perfect blend of crispy texture and honeyed sweetness in every satisfying bite."}
    ],
    "Shawarma": [
        {"name": "Chicken Shawarma", "price": 180, "rating": 5.0, "customisable": False, "desc": "Juicy chicken, bold flavors, and pure shawarma satisfaction wrapped in soft bread."},
        {"name": "Peri Peri Shawarma", "price": 220, "rating": 4.8, "customisable": False, "desc": "Spicy, juicy, and wrapped with a fiery peri peri kick—this shawarma is made to heat up your cravings."},
        {"name": "Mixed Meat Shawarma", "price": 280, "rating": 4.7, "customisable": False, "desc": "Juicy chicken and tender beef wrapped together with bold spices."}
    ],
    "Sandwich": [
        {"name": "Grilled Cheese Sandwich", "price": 99, "rating": 4.7, "customisable": False, "desc": "Perfectly toasted bread hugging layers of melted cheese."},
        {"name": "Cloud Egg Toast", "price": 129, "rating": 5.0, "customisable": False, "desc": "Light, fluffy eggs floating over golden toast."},
        {"name": "Spice-Kissed Paneer Pocket", "price": 149, "rating": 4.6, "customisable": True, "desc": "Tender paneer, gentle spices, and warm bread creating cozy comfort."}
    ]
}

ZINGYBYTE_FAQS: List[Dict[str, str]] = [
    {"question": "What is the standard delivery fee?", "answer": "ZINGYBYTE charges a flat platform delivery fee of ₹40 inside a 5km radius. Orders above ₹500 unlock free delivery."},
    {"question": "How long do deliveries take?", "answer": "Standard urban dispatches typically complete within 30 to 45 minutes depending on real-time kitchen backlogs and transit traffic parameters."},
    {"question": "What is the cancellation policy?", "answer": "Orders can be modified or fully cancelled within exactly 60 seconds of confirmation window verification via the app dashboard. Post this window, items enter active processing lines and cannot be recalled."},
    {"question": "What payment formats are integrated?", "answer": "We safely process all standard international credit/debit cards, UPI protocols (GooglePay, PhonePe), net banking nodes, and Cash on Delivery (COD)."}
]

MOCK_ORDERS: Dict[str, Dict[str, Any]] = {
    "ZB-9874": {"status": "Out for Delivery", "eta": "12 mins", "courier": "Rahul K.", "total": 549},
    "ZB-1102": {"status": "In the Kitchen (Baking)", "eta": "24 mins", "courier": "Assigning...", "total": 369},
    "ZB-4491": {"status": "Delivered", "eta": "Completed", "courier": "Anand S.", "total": 180}
}

def query_knowledge_context(user_query: str) -> str:
    """Performs an optimized contextual match across menu, logs, and FAQs."""
    context_chunks = []
    query_lower = user_query.lower()

    # 1. Search specific item blocks to highlight relevant categories
    found_specific_category = False
    for category, items in ZINGYBYTE_MENU.items():
        if category.lower() in query_lower or any(item["name"].lower() in query_lower for item in items):
            found_specific_category = True
            chunk = f"### Category Highlight: {category}\n"
            for item in items:
                cust_status = "Customisable" if item['customisable'] else "Fixed Preparation"
                chunk += f"- **{item['name']}**: ₹{item['price']} | {item['rating']} ⭐ | {cust_status}\n  *Description*: {item['desc']}\n"
            context_chunks.append(chunk)

    # 2. Check across corporate FAQ guidelines
    for faq in ZINGYBYTE_FAQS:
        if any(word in query_lower for word in faq["question"].lower().replace('?', '').split() if len(word) > 4):
            context_chunks.append(f"### FAQ Context:\n**Q:** {faq['question']}\n**A:** {faq['answer']}")

    # 3. Intercept active order tracking identifier parameters
    is_order_query = False
    for order_id, telemetry in MOCK_ORDERS.items():
        if order_id.lower() in query_lower:
            is_order_query = True
            context_chunks.append(
                f"### Live Order Telemetry [{order_id}]:\n"
                f"- **Current Status**: {telemetry['status']}\n"
                f"- **Estimated Delivery Time (ETA)**: {telemetry['eta']}\n"
                f"- **Assigned Courier Agent**: {telemetry['courier']}\n"
                f"- **Transaction Invoice Amount**: ₹{telemetry['total']}\n"
            )

    # 4. If they ask for menu, suggestions, or we haven't found any specific category/order, show full catalog!
    general_triggers = ["menu", "detail", "food", "eat", "hungry", "suggest", "recommend", "option", "what", "have", "list", "crav"]
    wants_menu = any(trigger in query_lower for trigger in general_triggers)
    
    if wants_menu or (not found_specific_category and not is_order_query):
        context_chunks.append("### Full ZINGYBYTE Menu Catalog")
        for category, items in ZINGYBYTE_MENU.items():
            chunk = f"\n#### {category}\n"
            for item in items:
                cust_status = "Customisable" if item['customisable'] else "Fixed Preparation"
                chunk += f"- **{item['name']}**: ₹{item['price']} | {item['rating']} ⭐ | {cust_status}\n  *Description*: {item['desc']}\n"
            context_chunks.append(chunk)

    if not context_chunks:
        return "### ZINGYBYTE Baseline Profile Info:\nGeneral user interaction. Provide general support for ordering from the ZINGYBYTE catalog."
        
    return "\n\n".join(context_chunks)