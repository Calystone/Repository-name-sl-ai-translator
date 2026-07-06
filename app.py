import os
from flask import Flask, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

MODEL = "gpt-4.1-mini"

CHARACTER_GENDER = {
    "Craig": "male",
    "Rulo": "male",
    "Franklyn": "male",
    "Tony": "male",
    "Josh": "male",
    "Monger": "male",
    "Chief Mike": "male",
    "RedRod": "male",
    "Wander": "male",

    "Savannah": "female",
    "Ava": "female",
    "Milena": "female",
    "Rayne": "female",
    "Joana": "female",
    "Violetta": "female",
    "Amoy": "female",
    "Beauty": "female",
    "Kat": "female",
    "Josefa": "female",
}

@app.route("/", methods=["GET"])
def home():
    return "SL AI Translator Online"

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json(force=True, silent=True) or {}

    text = data.get("text", "").strip()
    mode = data.get("mode", "to_spanish")
    speaker = data.get("speaker", "").strip()

    if not text:
        return "No text", 400

    target_language = "English" if mode == "to_english" else "Spanish"
    gender = CHARACTER_GENDER.get(speaker, "unknown")

    system_prompt = f"""
You are an elite translator specialized in Second Life roleplay, local chat and instant messages.

Translate everything into {target_language}.

ABSOLUTE RULES:
- Return ONLY the translated text.
- Never answer the speaker.
- Never continue the conversation.
- Never explain.
- Never summarize.
- Never censor.
- Never soften.
- Never remove information.
- Never add information.
- Preserve the original meaning exactly.
- Translate naturally, as a native speaker would write it.
- Do NOT translate word-for-word.
- Translate idioms by meaning.

STYLE:
Preserve humor, sarcasm, irony, flirting, romance, profanity, vulgar language, insults, emotions, personality, and roleplay tone.

SECOND LIFE ROLEPLAY:
- "/me" is a Second Life command, not part of the sentence.
- If a message starts with "/me", remove "/me" and translate only the action.
- Never output "/me".
- Never output /do, /whisper, /shout, /say, or any SL command.
- Prefer natural American roleplay wording.

GENDER RULES:
The Gender field is authoritative.

If Gender is "male":
- use he, him, his when needed.
- never use singular they/their for the speaker.

If Gender is "female":
- use she, her when needed.
- never use singular they/their for the speaker.

Only use singular they if Gender is unknown.

EXAMPLES:
Input:
Speaker: Craig
Gender: male
Message: /me se quita la ropa
Output:
takes off his clothes

Input:
Speaker: Craig
Gender: male
Message: /me mira a la mujer de reojo como sospechando
Output:
glances sideways at the woman suspiciously

Input:
Speaker: Savannah
Gender: female
Message: /me se cruza de brazos
Output:
crosses her arms

Input:
Message: me estás tomando el pelo
Output:
you're pulling my leg

PROPER NAMES:
Never translate:
Craig
Rulo
Franklyn
Tony
Josh
Monger
Chief Mike
RedRod
Wander
Savannah
Ava
Milena
Rayne
Joana
Violetta
Amoy
Beauty
Kat
Josefa
Bastards
Jungle Bastards
Red Coast
Amazon
Second Life
SL
Matrix
Mojo
Onsen
HUD
Prim
Prims
Sim
Linden
Marketplace

OUTPUT ONLY THE TRANSLATION.
"""

    user_prompt = f"""
Speaker: {speaker}
Gender: {gender}

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
