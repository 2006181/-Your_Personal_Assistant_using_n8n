# 🤝 Your Personal Assistant using n8n

A chat-based personal assistant built with **n8n** (automation backend) and **Streamlit** (frontend UI). The Streamlit app sends your messages to an n8n webhook and displays the AI response in a clean chat interface.

🔗 **Repository:** [Your_Personal_Assistant_using_n8n](https://github.com/2006181/-Your_Personal_Assistant_using_n8n)

## ✨ Features

- 💡 Answer questions on various topics
- 📅 Arrange calendar events and meetings
- 📧 Read emails, send replies, and summarize them
- ✅ Manage tasks and to-do lists
- 📝 Take quick notes
- 💰 Track expenses and budgeting

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend / Automation:** n8n (webhook + AI agent)
- **Language:** Python 3.9+

## 🏗️ How It Works

```
User → Streamlit Chat UI → n8n Webhook → AI Agent / Tools → Response → Streamlit
```

1. The user types a message in the Streamlit chat input.
2. The app sends it as JSON (`{"message": "..."}`) to the n8n webhook.
3. n8n processes it and returns the output.
4. Streamlit displays the reply and keeps the chat history in `st.session_state`.

## 📁 Project Structure

```
.
├── app.py              # Streamlit app
├── requirements.txt    # Python dependencies
└── README.md
```
## Deployment link - https://q3xt3ntzfgofyjwupgvads.streamlit.app/

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/2006181/-Your_Personal_Assistant_using_n8n.git
cd -Your_Personal_Assistant_using_n8n
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set the n8n webhook URL

In `app.py`, set your webhook URL:

```python
WEBHOOK_URL = "http://localhost:5678/webhook/<your-webhook-id>"
```

### 4. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`.

## ☁️ Deployment (Streamlit Community Cloud)

1. Push this repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and click **New app**.
3. Select this repo, the `main` branch, and `app.py` as the main file.
4. Click **Deploy**.

> ⚠️ `localhost` URLs will not work on Streamlit Cloud. Your n8n instance must be publicly reachable (n8n Cloud, a VPS, or a tunnel like ngrok / Cloudflare Tunnel), and `WEBHOOK_URL` in `app.py` should point to that public URL.

## 📄 License

This project is licensed under the MIT License.

## 🙋 Author

**Rahul** — [GitHub](https://github.com/2006181)
