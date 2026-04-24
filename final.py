import streamlit as st
import requests
import re

st.set_page_config(page_title="CREVA Expense Splitter", layout="centered")

st.title("💸 CREVA - Smart Expense Splitter")

# 🔗 n8n webhook
WEBHOOK_URL = "https://bandishtijiya.app.n8n.cloud/webhook-test/finance"

# 🧠 Extract amount & people
def extract_data(text):
    text_lower = text.lower()

    # amount
    numbers = re.findall(r'\d+', text_lower)
    amount = int(numbers[0]) if numbers else 0

    # people
    people = 2
    match = re.search(r'(\d+)\s*(people|person)', text_lower)
    if match:
        people = int(match.group(1))

    return amount, people

# 📝 Input
user_input = st.text_input(
    "Enter your expense:",
    placeholder="Dinner 600 split between 3 people"
)

# 🚀 Button
if st.button("Split Expense"):

    if not user_input:
        st.warning("⚠️ Please enter something")
    else:
        amount, people = extract_data(user_input)

        if amount == 0:
            st.error("❌ Amount not detected (use numbers like 500)")
        else:
            st.info(f"💰 Amount: ₹{amount}")
            st.info(f"👥 People: {people}")

            payload = {
                "amount": amount,
                "people": people,
                "description": user_input
            }

            try:
                response = requests.post(WEBHOOK_URL, json=payload)

                st.success("✅ Expense sent to Splitwise")

                try:
                    st.json(response.json())
                except:
                    st.write(response.text)

            except Exception as e:
                st.error(f"❌ Error: {e}")