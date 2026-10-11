import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="UPI Safety Coach | AI Scam Detector",
    page_icon="🛡️",
    layout="centered",
)

# Custom Professional Styling
st.markdown(
    """
    <style>
    .main {background-color: #f8f9fa;}
    .stAlert {border-radius: 12px;}
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
        border: 1px solid #e0e0e0;
        background-color: #ffffff;
        transition: 0.2s ease;
    }
    div.stButton > button:hover {
        border-color: #ff4b4b;
        color: #ff4b4b;
    }
    .scenario-card {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
        margin-bottom: 10px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# App Header
st.title("🛡️ UPI Safety Coach Chatbot")
st.markdown(
    "### *Your Personal AI Assistant to Stop UPI Scams Before You Lose Money*"
)
st.write(
    "Describe any suspicious UPI situation, payment request, or call below, or use the quick test buttons to evaluate common fraud tactics."
)

# Sidebar - Project Details & Safety Rules
with st.sidebar:
    st.image(
        "https://img.icons8.com/color/96/security-checked.png", width=70
    )
    st.header("📌 Project Overview")
    st.markdown(
        "**Target Goal:** To reduce digital payment fraud losses, empower students and families, and build everyday UPI safety awareness."
    )
    st.markdown("**Platform:** Python & Streamlit AI Web App")

    st.markdown("---")
    st.error(
        "⚠️ **SAFETY REMINDER**\nNever type your real UPI PIN, OTP, or bank passwords into any chat window!"
    )

    st.markdown("---")
    st.markdown("🚨 **Emergency Helpline:**")
    st.markdown("**National Cyber Helpline:** `1930`")
    st.markdown("**Official Portal:** [cybercrime.gov.in](https://cybercrime.gov.in)")

# Initialize Session State for Chat
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": (
            "Hello! I am your **UPI Safety Coach**. "
            "Did someone send you a suspicious link, ask for an OTP, or give you a strange QR code? "
            "Type your situation below or test a scenario using the buttons above!"
        ),
    }]

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Scam Analysis Engine (5 Core Scenarios)
def analyze_scam(user_input):
    text = user_input.lower()

    # Scenario 1: QR Code Trap
    if any(
        word in text
        for word in [
            "qr",
            "scan",
            "receive money",
            "cashback",
            "olx buyer",
            "sell",
        ]
    ):
        return (
            "🛑 **VERDICT: HIGH RISK (QR Code Payment Trap)**\n\n"
            "🔍 **Why it's a scam:** QR codes are **strictly for sending money**, never for receiving funds. Scanning a QR code and entering your UPI PIN will always deduct money from your account.\n\n"
            "🛡️ **What you should do:**\n"
            "1. Cancel the transaction immediately. Do not scan or enter your PIN.\n"
            "2. Block the user on the marketplace platform.\n"
            "3. If money was deducted, report immediately to **1930** or [cybercrime.gov.in](https://cybercrime.gov.in)."
        )

    # Scenario 2: OTP / PIN Phishing
    elif any(
        word in text for word in ["otp", "pin", "bank call", "block", "kyc"]
    ):
        return (
            "🛑 **VERDICT: HIGH RISK (OTP / PIN Phishing Scam)**\n\n"
            "🔍 **Why it's a scam:** Banks, RBI, and UPI apps **never** ask for your OTP, UPI PIN, or password over a call or message.\n\n"
            "🛡️ **What you should do:**\n"
            "1. Hang up the phone instantly. *Remember: OTP is Only To Yourself.*\n"
            "2. Block the caller's number.\n"
            "3. If you shared your PIN, change your UPI PIN immediately through your official payment app."
        )

    # Scenario 3: Screen Sharing App Scam
    elif any(
        word in text
        for word in [
            "anydesk",
            "teamviewer",
            "screen share",
            "remote",
            "quicksupport",
        ]
    ):
        return (
            "🛑 **VERDICT: CRITICAL RISK (Remote Access Fraud)**\n\n"
            "🔍 **Why it's a scam:** Screen-sharing apps allow fraudsters to view your live phone screen, access your banking apps, and steal money directly.\n\n"
            "🛡️ **What you should do:**\n"
            "1. Do **not** install any remote access app.\n"
            "2. If already installed, disconnect your internet immediately, uninstall the app, and secure your phone.\n"
            "3. Call **1930** right away."
        )

    # Scenario 4: Fake Customer Care
    elif any(
        word in text
        for word in ["customer care", "support", "google search", "helpline"]
    ):
        return (
            "🛑 **VERDICT: HIGH RISK (Fake Customer Care Impersonation)**\n\n"
            "🔍 **Why it's a scam:** Scammers buy sponsored search engine ads to display fake helpline numbers. Legitimate support never asks for a 'verification fee' to process a refund.\n\n"
            "🛡️ **What you should do:**\n"
            "1. Disconnect the call immediately.\n"
            "2. Only look for customer support inside the official help section of verified apps (e.g., Zomato, Paytm, GPay).\n"
            "3. Report fraudulent numbers to cybercrime authorities."
        )

    # Scenario 5: AI Deepfake Voice Scam
    elif any(
        word in text
        for word in ["voice", "accident", "emergency", "family", "deepfake"]
    ):
        return (
            "🛑 **VERDICT: HIGH RISK (AI Deepfake / Emergency Fraud)**\n\n"
            "🔍 **Why it's a scam:** Fraudsters use AI audio cloning tools to replicate family members' voices using short clips from social media to create fake emergencies.\n\n"
            "🛡️ **What you should do:**\n"
            "1. Stay calm and hang up.\n"
            "2. Cross-verify by calling your family member back directly on their standard phone number before sending money.\n"
            "3. Report suspicious voice scam attempts to **1930**."
        )

    # Fallback response
    else:
        return (
            "⚠️ **UNRECOGNIZED SITUATION**\n\n"
            "I couldn't match your exact situation, but remember the golden rule: **Never share your OTP/PIN, never scan QR codes to receive money, and never install remote-sharing apps.**\n\n"
            "If you suspect financial fraud, call the National Cyber Crime Helpline at **1930** or visit [cybercrime.gov.in](https://cybercrime.gov.in)."
        )


# Clean Section for Quick Test Scenarios
st.markdown("---")
st.markdown("### ⚡ Test Core Scenarios")
st.write("Click any test scenario below to simulate a user interaction:")

col1, col2, col3 = st.columns(3)
trigger_input = None

with col1:
    if st.button("📷 QR Code Scam"):
        trigger_input = "Someone sent me a QR code to receive money."
with col2:
    if st.button("🔑 OTP / KYC Call"):
        trigger_input = (
            "A caller said my account will be blocked unless I give my OTP."
        )
with col3:
    if st.button("💻 Screen Share"):
        trigger_input = (
            "Customer care asked me to download AnyDesk for a refund."
        )

col4, col5 = st.columns(2)
with col4:
    if st.button("🎧 Fake Support"):
        trigger_input = (
            "I called a support number from Google and they asked for a fee."
        )
with col5:
    if st.button("🗣️ AI Voice Scam"):
        trigger_input = (
            "I got an urgent call sounding like a relative asking for money."
        )

# User Chat Input
user_query = st.chat_input(
    "Type your suspicious situation here (e.g., 'Someone asked for my OTP')..."
)

if trigger_input:
    user_query = trigger_input

if user_query:
    # Save & display user message
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    # Generate & display assistant response
    bot_reply = analyze_scam(user_query)
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_reply}
    )
    with st.chat_message("assistant"):
        st.markdown(bot_reply)