import gradio as gr
import requests
import speech_recognition as sr

WEBHOOK_URL = "https://core2webcreva.app.n8n.cloud/webhook-test/expense"

# -------- TEXT FUNCTION --------
def send_text(text):
    if not text:
        return "⚠️ Please enter something"
    
    try:
        requests.post(WEBHOOK_URL, json={"text": text})
        return f"✅ Added: {text}"
    except:
        return "❌ Error sending data"


# -------- VOICE FUNCTION --------
def send_voice(audio_file):
    if audio_file is None:
        return "⚠️ Please record audio"

    try:
        r = sr.Recognizer()

        with sr.AudioFile(audio_file) as source:
            audio_data = r.record(source)

        text = r.recognize_google(audio_data)

        requests.post(WEBHOOK_URL, json={"text": text})

        return f"📝 You said: {text}\n✅ Added!"

    except Exception as e:
        return f"❌ Error: {str(e)}"


# -------- UI --------
with gr.Blocks() as app:
    gr.Markdown("# 💰 Smart Expense Tracker")

    with gr.Tab("Text Input"):
        text = gr.Textbox(placeholder="I spent 500 on food")
        out1 = gr.Textbox()
        btn1 = gr.Button("Submit")
        btn1.click(send_text, inputs=text, outputs=out1)

    with gr.Tab("Voice Input"):
        audio = gr.Audio(sources=["microphone"], type="filepath")
        out2 = gr.Textbox()
        btn2 = gr.Button("Submit Voice")
        btn2.click(send_voice, inputs=audio, outputs=out2)

app.launch()