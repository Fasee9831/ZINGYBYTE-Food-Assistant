# 🍔 ZingyByte AI — Your Food Buddy

A friendly AI food assistant that helps customers explore menus, track orders, and get food recommendations — powered by **Streamlit**, **LangChain**, and **Groq AI**.

---

## ✨ Features

- **AI Food Assistant** — Ask about menu items, prices, ratings, and customizations
- **Live Order Tracking** — Check mock order status with IDs like `ZB-9874`
- **FAQ Answers** — Get instant answers about delivery fees, policies, and payment options
- **Fast Streaming Responses** — Responses appear word-by-word in real-time
- **Premium UI** — Dark glassmorphic design with floating food animations
- **Conversation History** — Auto-saved chats with search, rename, and time-based grouping
- **Conversation Summary** — One-tap summary of your current chat
- **Favorites** — Save dishes with ❤️ and ask "Show my favorite dishes" anytime
- **Follow-up Suggestions** — Context-aware question suggestions after each response
- **Regenerate Answer** — Re-generate the last AI response anytime
- **Message Actions** — Like / dislike / share any AI reply
- **Keyboard Shortcuts** — `Ctrl+K` to focus chat, `Ctrl+Shift+K` to focus search
- **Auto-Summary** — Long conversations are summarized to keep responses fast

---

## 🚀 How to Run Locally

### 1. Get the code
```bash
git clone https://github.com/YOUR_USERNAME/zingybyte-ai.git
cd zingybyte-ai
```

### 2. Install requirements
```bash
pip install -r requirements.txt
```

### 3. Add your Groq API key

Create a folder and file:
```
.streamlit/secrets.toml
```

Paste this inside (get a free key at https://console.groq.com):
```toml
GROQ_API_KEY = "gsk_your_api_key_here"
```

### 4. Run the app
```bash
streamlit run app.py
```

Open **http://localhost:8501** in your browser.

---

## ☁️ Deploy on Streamlit Cloud (Free)

1. Push this repo to GitHub
2. Go to https://share.streamlit.io
3. Click **New app** → select your repo → set main file to `app.py`
4. Go to **Settings → Secrets** and add:
```toml
GROQ_API_KEY = "gsk_your_api_key_here"
```
5. Click **Deploy** — your app is live!

---

## 📂 Files Explained

| File | What it does |
|------|-------------|
| `app.py` | Main app — connects UI, chat logic, and streaming |
| `chat.py` | Talks to Groq AI, handles streaming and summaries |
| `config.py` | Settings — page config, logging |
| `knowledge.py` | Menu catalog, FAQs, and mock order data |
| `prompt.py` | AI personality instructions and suggested questions |
| `styles.py` | All the CSS for the dark premium look |
| `ui.py` | Renders sidebar, top bar, menu drawer, hero screen, and chat bubbles |
| `utils.py` | Session state and conversation management |
| `favorites.py` | Favorite-dish storage, lookups, and formatting |

---

## 💬 Try These Questions

Click the suggestion cards on the home screen or type:

> Which Broasted Chicken choices have a 5-star rating and what do they cost?

> Can you list all pizzas with prices, ratings, and customization options?

> What is the delivery fee and how do I get free delivery?

> Where is my order ZB-9874?

---

## 🛠 Tech Stack

- **Frontend**: Streamlit + custom CSS
- **AI Engine**: LangChain + Groq API
- **Model**: `llama-3.1-8b-instant`

---

## 📝 License

MIT License
