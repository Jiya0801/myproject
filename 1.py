import requests
import json

# 1. The "Phone Number" for n8n
# This must match your Webhook Test URL exactly
URL = "http://localhost:5678/webhook-test/bot"

def ask_creva(user_text):
    # 2. The "Envelope" 
    # We put your text inside a key called "message"
    payload = {
        "message": user_text
    }
    
    print(f"--- Sending to Creva: {user_text} ---")

    try:
        # 3. Sending the data to n8n
        response = requests.post(URL, json=payload)
        
        # 4. Checking the reply
        if response.status_code == 200:
            print("Creva's Reply:", response.text)
        else:
            print(f"Error: n8n returned status code {response.status_code}")
            print("Check if n8n 'Execute Workflow' is active!")
            
    except Exception as e:
        print("Error: Could not connect to n8n. Make sure n8n is running on your PC.")

# --- RUN THE TEST ---
if __name__ == "__main__":
    # You can change this text to anything!
    my_message = "Hello Creva, तू कसा आहेस? आज आपण पैसे वाटूया का?"
    ask_creva(my_message)