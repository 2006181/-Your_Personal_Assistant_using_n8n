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

### 3. Add your secrets

The webhook URL and the app password are **not stored in the code**. They are read from Streamlit secrets:

```python
WEBHOOK_URL = st.secrets["WEBHOOK_URL"]
APP_PASSWORD = st.secrets["APP_PASSWORD"]
```

Create a file `.streamlit/secrets.toml` in the project folder (this file is git-ignored and never uploaded):

```toml
WEBHOOK_URL = "https://your-n8n-url/webhook/<your-webhook-id>"
APP_PASSWORD = "your-strong-password"
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
4. Open **Advanced settings → Secrets** and add:
   ```toml
   WEBHOOK_URL = "https://your-n8n-url/webhook/<your-webhook-id>"
   APP_PASSWORD = "your-strong-password"
   ```
5. Click **Deploy**.

> ⚠️ `localhost` URLs will not work on Streamlit Cloud. Your n8n instance must be publicly reachable (n8n Cloud, a VPS, or a tunnel like ngrok / Cloudflare Tunnel).

## 🔒 Privacy & Security

This assistant is connected to personal accounts (such as Gmail) through n8n, so the **entire app is password protected**.

- On opening the app, a login screen asks for a password. The chat and all features load only after the correct password is entered.
- The password and the n8n webhook URL are stored in `.streamlit/secrets.toml` (local) and Streamlit Cloud Secrets (deployed). They are never committed to GitHub.
- `.streamlit/secrets.toml` is listed in `.gitignore`.
- No personal email data is stored in this repository.

### Tips

- Do not share the password or the webhook URL publicly.
- Use a strong password and change it if you have shared it with someone.
- For public demos, connect a dummy Gmail account instead of a personal inbox.

## 📄 License

This project is licensed under the MIT License.

## 🙋 Author

**Rahul** — [GitHub](https://github.com/2006181)
