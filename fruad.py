import streamlit as st
import requests

st.title("🔍 Fraud Detection System")

message = st.text_area("Enter your message:")

if st.button("Check Fraud"):

    if message.strip() == "":
        st.warning("Please enter message")
    else:
        url =" https://core2webcreva.app.n8n.cloud/webhook-test/fraud-check"

        payload = {
            "message": message
        }

        try:
            res = requests.post(url, json=payload)

            st.write("Response Status:", res.status_code)

            data = res.json()

            st.subheader("Result")

            st.write(data)

        except Exception as e:
            st.error(e)