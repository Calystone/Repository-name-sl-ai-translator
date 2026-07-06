import os
from flask import Flask, request
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.get("/")
def home():
    return "SL AI Translator Online"

@app.post("/translate")
def translate():
    data = request.get_json(force=True, silent=True) or {}

    text = data.get("text", "").strip()
    mode = data.get("mode", "to_spanish")
    speaker = data.get("speaker", "Unknown")

    if not text:
        return "No text received", 400

    target_language = "English" if mode == "to_english" else "Spanish"

    system_prompt = f"""
You are an expert translator for Second Life chat and roleplay.

Translate the message into {target_language}.

Rules:
- Return only the translation.
- Translate naturally, as a native speaker would say it.
- Preserve the exact meaning.
- Do not summarize, censor, moralize, soften, add, or remove anything.
- Preserve jokes, flirting, insults, profanity, sarcasm, adult language, and roleplay tone.
- Translate idioms by meaning, not word by word.
- Keep /me actions, *emotes*, names, usernames, and places unchanged when appropriate.
- Keep these names unchanged: Craig, Rulo, Bastards, Jungle Bastards, Red Coast, Amazon, Matrix, Second Life, SL, Mojo, Onsen.
"""

    user_prompt = f"""
Speaker: {speaker}
Original text:
{text}
"""

    try:
        response = client.responses.create(
            model="gpt-5.4-mini",
            instructions=system_prompt,
            input=user_prompt,
        )
        return response.output_text.strip()

    except Exception as e:
        return f"AI error: {str(e)}", 500
