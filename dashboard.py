import streamlit as st
import requests

st.set_page_config(page_title="Creva 2.0", page_icon="🤖")

st.title("🤖 Creva 2.0 Finance Robot")
st.markdown("---")

# User Input
user_query = st.text_input("What should I do with your bills?", placeholder="e.g., Show my Splitwise groups")

if st.button("Execute Command"):
    if user_query:
        # This matches your Webhook Path 'finance' from image_136cdc.png
        url = "https://bandishtijiya.app.n8n.cloud/webhook-test/finance"
        
        with st.spinner("Talking to n8n..."):
            try:
                # We send the message and a sessionId for your Memory node
                payload = {"message": user_query, "sessionId": "jiya_session"}
                response = requests.post(url, json=payload, timeout=25)
                
                if response.status_code == 200:
                    # Extract the AI's response text
                    result = response.json()
                    # AI Agent usually returns a list; we want the 'output'
                    final_text = result[0].get('output', "Action completed!")
                    st.success(f"**Creva says:** {final_text}")
                else:
                    st.error(f"Error {response.status_code}: Did you click 'Listen for test event' in n8n?")
            
            except Exception as e:
                st.error("Connection Failed! Make sure n8n is running and you have the 'Respond to Webhook' node added.")
    else:
        st.warning("Please enter a command first.")