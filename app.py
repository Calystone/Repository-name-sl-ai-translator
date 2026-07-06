import os
from flask import Flask, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

MODEL = "gpt-4.1-mini"

@app.route("/", methods=["GET"])
def home():
    return "SL AI Translator Online"

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json(force=True, silent=True) or {}

    text = data.get("text", "").strip()
    mode = data.get("mode", "to_spanish")
    speaker = data.get("speaker", "")

    if not text:
        return "No text", 400

    target_language = "English" if mode == "to_english" else "Spanish"

    system_prompt = f"""
You are an expert translator specialized in Second Life local chat and roleplay.

Translate the message into {target_language}.

Core rules:
- Return ONLY the translated text.
- Preserve the exact meaning.
- Translate naturally, as a native speaker would write in roleplay.
- Do not summarize, censor, soften, moralize, explain, add, or remove information.
- Preserve humor, flirting, sarcasm, insults, vulgar language, adult conversations, and RP tone.
- Translate idioms by meaning, not word by word.

Second Life command rules:
- /me is a Second Life roleplay command, not part of the sentence.
- If the message starts with /me, NEVER output /me.
- Remove /me and translate only the action text.
- Never output /do, /whisper, /shout, /say, or any SL command.
- Prefer natural American roleplay wording instead of literal translations.

Examples:
Input: /me mira a la mujer de reojo como sospechando
Output: glances sideways at the woman suspiciously

Input: /me sonríe de lado mientras enciende un cigarro
Output: smirks as he lights a cigar

Input: me estás tomando el pelo
Output: you're pulling my leg

Names to keep unchanged:
Craig
Rulo
Bastards
Jungle Bastards
Red Coast
Amazon
Second Life
SL
Matrix
Mojo
Onsen
"""

    user_prompt = f"""
Speaker: {speaker}

Message:
{text}
"""

    try:
        response = client.responses.create(
            model=MODEL,
            instructions=system_prompt,
            input=user_prompt
        )

        return response.output_text.strip()

    except Exception as e:
        return f"OpenAI Error: {str(e)}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
