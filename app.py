from flask import Flask, request, Response
import openai
import requests
import os

app = Flask(__name__)

# Load API keys from environment variables
openai.api_key = os.environ.get("OPENAI_API_KEY")
elevenlabs_api_key = os.environ.get("ELEVENLABS_API_KEY")
voice_id = os.environ.get("ELEVENLABS_VOICE_ID")

def get_gpt_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a confident and friendly car expert named Troy, the Capital Crusader. Always be helpful, no pressure."},
            {"role": "user", "content": user_input},
        ]
    )
    return response["choices"][0]["message"]["content"]

def get_elevenlabs_audio(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": elevenlabs_api_key,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.7,
            "similarity_boost": 0.75
        }
    }
    response = requests.post(url, json=data, headers=headers)
    return response.content

@app.route("/voice", methods=["POST"])
def voice():
    from twilio.twiml.voice_response import VoiceResponse, Gather

    resp = VoiceResponse()
    gather = Gather(input='speech', timeout=5, action='/gather', method='POST')
    gather.say("Hey! This is Troy at Capital GMC Buick Cadillac. I’ve got a quick offer for you. Want to hear more?")
    resp.append(gather)
    resp.say("No worries. Catch you next time, hero.")
    return Response(str(resp), mimetype='text/xml')

@app.route("/gather", methods=["POST"])
def gather():
    from twilio.twiml.voice_response import VoiceResponse

    user_input = request.form.get("SpeechResult", "No response")
    gpt_reply = get_gpt_response(user_input)
    audio = get_elevenlabs_audio(gpt_reply)

    with open("static/response.mp3", "wb") as f:
        f.write(audio)

    resp = VoiceResponse()
    resp.play("https://your-render-url.onrender.com/static/response.mp3")  # Replace this URL
    return Response(str(resp), mimetype='text/xml')

@app.route("/")
def index():
    return "AI Voice Agent is Running!"

if __name__ == "__main__":
    app.run(debug=True)
