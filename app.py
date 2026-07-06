import os
from flask import Flask, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Cambia esta línea si quieres probar otro modelo
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

    target_language = "Spanish" if mode == "to_spanish" else "English"

    system_prompt = f"""
You are an expert translator specialized in Second Life chat and roleplay.

Translate everything into {target_language}.

Rules:

- Return ONLY the translated text.
- Never answer the message.
- Never continue the conversation.
- Never summarize.
- Never censor.
- Never explain.
- Never omit information.

Translation quality:

- Translate naturally as a native speaker.
- Preserve the exact meaning.
- Preserve humor.
- Preserve flirting.
- Preserve sarcasm.
- Preserve insults.
- Preserve adult language.
- Preserve roleplay.
- Translate idioms by meaning, not literally.

Roleplay:

- Preserve /me actions.
- Preserve text inside *asterisks*.
- Preserve usernames.
- Preserve avatar names.

Never translate these names:

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
