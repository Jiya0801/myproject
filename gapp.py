import gradio as gr
import requests

WEBHOOK_URL = "https://core2webcreva.app.n8n.cloud/webhook/expense"

def send_expense(text):
    try:
        res = requests.post(
            WEBHOOK_URL,
            json={"text": text}
        )

        if res.status_code == 200:
            return f"✅ Added: {text}"
        else:
            return f"❌ Error: {res.text}"

    except Exception as e:
        return str(e)

with gr.Blocks() as app:
    gr.Markdown("## 💰 Smart Expense Tracker")

    inp = gr.Textbox(label="Enter expense")
    out = gr.Textbox(label="Status")

    btn = gr.Button("Submit")
    btn.click(send_expense, inp, out)

app.launch()