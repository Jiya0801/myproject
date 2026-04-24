import streamlit as st
import requests
import time

# -- Page Config --
st.set_page_config(page_title="Creva 2.0 Finance", page_icon="🤖")

# -- Initialize State --
if 'page' not in st.session_state:
    st.session_state.page = "start"

# --- PAGE 1: THE START BUTTON ---
if st.session_state.page == "start":
    st.title("🤖 Creva 2.0: Finance Robot")
    st.write("Ensure n8n is 'Waiting for Webhook' before starting.")
    
    if st.button("INITIALIZE COMMAND CENTER", use_container_width=True):
        st.session_state.page = "main"
        st.rerun()

# --- PAGE 2: THE DASHBOARD ---
else:
    st.title("🏦 Finance Command Center")
    
    if st.button("⬅️ Shut Down"):
        st.session_state.page = "start"
        st.rerun()

    st.divider()
    
    user_input = st.text_input("Enter Finance Command (English/Marathi):")

    if st.button("Send to Robot", use_container_width=True):
        if user_input:
            with st.spinner('Accessing Finance Brain...'):
                # EXACT PATH: finance
                url = "http://localhost:5678/webhook-test/finance"
                
                try:
                    # We send the request and wait 15 seconds
                    response = requests.post(url, json={"message": user_input}, timeout=15)
                    
                    if response.status_code == 200:
                        data = response.json()
                        # Get the response from n8n
                        reply = data[0]['output']
                        st.subheader("🤖 Creva Says:")
                        st.success(reply)
                    else:
                        st.error(f"Error 404: n8n is not 'Listening'. Go back to n8n and click 'Listen for test event'.")
                except Exception as e:
                    st.error("Connection Failed: Ensure n8n is open and running on your PC.")
        else:
            st.warning("Please type a question first.")