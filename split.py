import streamlit as st
import requests

st.title("💸 CREVA - Smart Expense Splitter")

# User input
user_input = st.text_input("Enter your expense:", placeholder="Dinner 600 split between 3 people")

if st.button("Split Expense"):
    if user_input:
        try:
            # 🔗 Replace with your webhook URL
            webhook_url = "https://bandishtijiya.app.n8n.cloud/webhook-test/finance"

            response = requests.post(
                webhook_url,
                json={"message": user_input}
            )

            if response.status_code == 200:
                st.success("✅ Expense added successfully!")

                st.json(response.json())
            else:
                st.error("❌ Failed to add expense")

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("⚠️ Please enter something")