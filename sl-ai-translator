from flask import Flask, request
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/")
def home():
    return "SL AI Translator Online"

@app.post("/translate")
def translate():

    data = request.json

    text = data.get("text","")
    mode = data.get("mode","to_spanish")
    speaker = data.get("speaker","")

    if mode == "to_english":

        instructions = """
Translate into natural American English.

Keep:
- RP actions
- emotions
- jokes
- slang
- names

Return ONLY the translation.
"""

    else:

        instructions = """
Translate into natural Spanish.

Keep:
- RP
- emotions
- names
- slang

Return ONLY the translation.
"""

    response = client.responses.create(
        model="gpt-5.5",
        instructions=instructions,
        input=text
    )

    return response.output_text
