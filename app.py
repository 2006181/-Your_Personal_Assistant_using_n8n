import streamlit as st
import requests

# ---------- Page config ----------
st.set_page_config(
    page_title="Your Personal Assistant",
    page_icon="🤝",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ---------- Webhook URL ----------
WEBHOOK_URL = st.secrets["WEBHOOK_URL"]  # replace with your n8n webhook URL

# ---------- Session state for message history ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- Sidebar ----------
with st.sidebar:
    st.header("⚙️ Controls")
    st.caption("Manage your chat session")
    if st.button("🗑️ Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.divider()
    st.metric("Messages in chat", len(st.session_state.messages))
    st.divider()
    st.caption("Powered by n8n + Streamlit ⚡")

# ---------- Title ----------
st.title("🤝 Your Personal Assistant")
st.caption("Your AI-powered helper for everyday work")

# ---------- Subheader + what the assistant can do ----------
st.subheader("What can your personal assistant do?")

features = [
    ("💡", "Answer questions", "Answer questions on various topics."),
    ("📅", "Calendar", "Arrange Calendar events and meetings."),
    ("📧", "Emails", "Read your emails and send replies, can even summarize them for you."),
    ("✅", "Tasks", "Manage your tasks and to-do lists."),
    ("📝", "Notes", "Take quick notes for you."),
    ("💰", "Expenses", "Track your expenses and budgeting."),
]

cols = st.columns(3)
for i, (icon, title, text) in enumerate(features):
    with cols[i % 3]:
        with st.container(border=True):
            st.markdown(f"### {icon}")
            st.markdown(f"**{title}**")
            st.caption(text)

st.divider()

# ---------- Chats subheader ----------
st.subheader("💬 Chat with your assistant")

# ---------- Show the messages in chat history ----------
for message in st.session_state.messages:
    avatar = "🧑‍💻" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# ---------- Chat input box ----------
user_message = st.chat_input("Type your message here...")

# ---------- If user sends a message ----------
if user_message:
    with st.chat_message("user", avatar="🧑‍💻"):
        st.markdown(user_message)
        # append the user message to message history
        st.session_state.messages.append({"role": "user", "content": user_message})

    # send the user message to the n8n webhook
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):
            try:
                response = requests.post(
                    WEBHOOK_URL,
                    json={"message": user_message},
                    timeout=60,
                )
                response.raise_for_status()

                # get the AI response from webhook
                ai_response = response.json()[0]["output"]

            except requests.exceptions.ConnectionError:
                ai_response = "⚠️ n8n webhook se connect nahi ho paya. Check karo n8n chal raha hai ya nahi."
            except requests.exceptions.Timeout:
                ai_response = "⏳ Request time out ho gayi. Dobara try karo."
            except Exception as e:
                ai_response = f"⚠️ Kuch error aaya: {e}"

        # display the AI response in chat
        st.markdown(ai_response)
        # append the AI response to message history
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
