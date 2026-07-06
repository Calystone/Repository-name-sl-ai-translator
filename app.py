import os
from flask import Flask, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

@app.route("/", methods=["GET"])
def home():
    return "SL AI Translator Online"

@app.route("/translate", methods=["POST"])
def translate():

    data = request.get_json(force=True, silent=True) or {}

    text = data.get("text", "").strip()
    mode = data.get("mode", "to_spanish")
    speaker = data.get("speaker", "")

    if text == "":
        return "No text", 400

    target_language = "Spanish"

    if mode == "to_english":
        target_language = "English"

    system_prompt = f"""
You are an expert translator specialized in Second Life chat and roleplay.

Translate everything into {target_language}.

IMPORTANT:

- Return ONLY the translated text.
- Never answer the message.
- Never continue the conversation.
- Never summarize.
- Never censor.
- Never explain.
- Never omit information.

Translation style:

- Translate naturally as a native speaker.
- Preserve the exact meaning.
- Preserve humor.
- Preserve flirting.
- Preserve sarcasm.
- Preserve insults.
- Preserve adult conversations.
- Preserve vulgar language.
- Preserve roleplay.

Roleplay:

- Preserve /me actions.
- Preserve text between *asterisks*.
- Preserve usernames.
- Preserve avatar names.

Do NOT translate these proper names:

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

If an idiom exists, translate its meaning instead of translating word by word.

Output ONLY the translation.
"""

    user_prompt = f"""
Speaker:
{speaker}

Message:
{text}
"""

    try:

        response = client.responses.create(
            model="gpt-5.5-mini",
            instructions=system_prompt,
            input=user_prompt
        )

        return response.output_text.strip()

    except Exception as e:
        return f"OpenAI Error: {str(e)}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
