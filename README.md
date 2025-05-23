# Capital Crusader AI Voice Agent

This is a Python Flask-based AI voice assistant for outbound calls, using Twilio, OpenAI (ChatGPT), and ElevenLabs.

## Features
- Makes outbound or inbound calls via Twilio
- Uses ChatGPT for intelligent, no-pressure sales conversations
- Converts GPT responses to lifelike speech with ElevenLabs
- Automatically responds to customer replies

## Requirements
- Python 3.7+
- Twilio account with phone number
- OpenAI API key
- ElevenLabs API key and voice ID
- Render.com account (for free hosting)

## Setup

1. Clone the repo and navigate to the project directory.

```bash
git clone https://github.com/yourusername/ai-voice-agent.git
cd ai-voice-agent
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Set your environment variables:

```bash
export OPENAI_API_KEY=your_openai_key
export ELEVENLABS_API_KEY=your_elevenlabs_key
export ELEVENLABS_VOICE_ID=your_voice_id
export TWILIO_ACCOUNT_SID=your_twilio_sid
export TWILIO_AUTH_TOKEN=your_twilio_token
```

4. Run the Flask server:

```bash
gunicorn app:app
```

## Deploy to Render

1. Create a new Web Service on [Render](https://render.com).
2. Connect your GitHub repo.
3. Set:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
4. Add environment variables as listed above.

## Webhook Setup in Twilio

1. Go to Twilio Console → Phone Numbers → Active Number
2. Set Voice webhook to: `https://your-app.onrender.com/voice`
3. Method: POST

---

Built with Flask, Twilio, ElevenLabs, and the power of AI to elevate your automotive outreach. Let's ride!

