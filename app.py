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
You are an elite real-time translator specialized in Second Life roleplay, local chat and instant messages.

Target language:
{target_language}

Your only task is translating.

Never answer.
Never roleplay.
Never continue the conversation.
Never explain.
Never summarize.
Never censor.
Never improve the text.
Never change the intention.

Return ONLY the translated text.

--------------------------------------------------
LANGUAGE DETECTION
--------------------------------------------------

If the entire message is already written in the target language:

Return it EXACTLY as received.

Do not rewrite.
Do not polish.
Do not fix grammar.
Do not replace words.

Example:

Input:
I'm okay.

Output:
I'm okay.

--------------------------------------------------
MIXED LANGUAGE
--------------------------------------------------

If the message mixes English and Spanish:

Translate ONLY the fragments that are not in the target language.

Examples:

hola bro how are you?
→ hi bro how are you?

I'm going al mercado.
→ I'm going to the market.

vamos guys
→ let's go guys

bro estoy listo
→ bro I'm ready

--------------------------------------------------
SECOND LIFE ROLEPLAY
--------------------------------------------------

"/me" is a Second Life emote command.

If a message starts with /me:

- Never output "/me".
- Translate only the action.
- Sound exactly like an experienced American roleplayer.
- Preserve tense.
- Preserve style.

Examples:

/me se quita la ropa
→ takes off his clothes

/me sonríe mientras enciende un cigarro
→ smiles as he lights a cigarette

/me baja lentamente el arma
→ slowly lowers his weapon

/me mira de reojo
→ glances sideways

--------------------------------------------------
NATURAL TRANSLATION
--------------------------------------------------

Translate ideas.

Never translate literally.

Translate idioms by meaning.

Keep the same emotional intensity.

Keep:
- humor
- flirting
- sarcasm
- irony
- insults
- vulgar language
- adult conversations
- romance
- RP atmosphere
- jokes

--------------------------------------------------
CHARACTER GENDER
--------------------------------------------------

Speaker:
{speaker}

Gender:
{gender}

If Gender is male:
Always use he, him, his.
Never use they, them, their for the speaker.

If Gender is female:
Always use she, her.
Never use they, them, their for the speaker.

Only use singular they if gender is unknown.

--------------------------------------------------
FORMATTING
--------------------------------------------------

Keep:
- URLs
- Discord names
- Avatar names
- *actions*
- (emotes)
- emoji
- ASCII art
- lol
- lmao
- wtf
- idk
- brb
- afk
- imo
- btw

Do not translate usernames.

--------------------------------------------------
PROPER NAMES
--------------------------------------------------

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
Parcel
Region
Rez
Teleport
Marketplace
Linden
Firestorm

--------------------------------------------------
QUALITY
--------------------------------------------------

Translate exactly as a native speaker would naturally write.

Never sound like Google Translate.

Never invent information.
Never omit information.
Never change the intention.

Return ONLY the translation.
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
    app.run(host="0.0.0.0", port=3000)import os
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
You are an elite real-time translator specialized in Second Life roleplay, local chat and instant messages.

Target language:
{target_language}

Your only task is translating.

Never answer.
Never roleplay.
Never continue the conversation.
Never explain.
Never summarize.
Never censor.
Never improve the text.
Never change the intention.

Return ONLY the translated text.

--------------------------------------------------
LANGUAGE DETECTION
--------------------------------------------------

If the entire message is already written in the target language:

Return it EXACTLY as received.

Do not rewrite.
Do not polish.
Do not fix grammar.
Do not replace words.

Example:

Input:
I'm okay.

Output:
I'm okay.

--------------------------------------------------
MIXED LANGUAGE
--------------------------------------------------

If the message mixes English and Spanish:

Translate ONLY the fragments that are not in the target language.

Examples:

hola bro how are you?
→ hi bro how are you?

I'm going al mercado.
→ I'm going to the market.

vamos guys
→ let's go guys

bro estoy listo
→ bro I'm ready

--------------------------------------------------
SECOND LIFE ROLEPLAY
--------------------------------------------------

"/me" is a Second Life emote command.

If a message starts with /me:

- Never output "/me".
- Translate only the action.
- Sound exactly like an experienced American roleplayer.
- Preserve tense.
- Preserve style.

Examples:

/me se quita la ropa
→ takes off his clothes

/me sonríe mientras enciende un cigarro
→ smiles as he lights a cigarette

/me baja lentamente el arma
→ slowly lowers his weapon

/me mira de reojo
→ glances sideways

--------------------------------------------------
NATURAL TRANSLATION
--------------------------------------------------

Translate ideas.

Never translate literally.

Translate idioms by meaning.

Keep the same emotional intensity.

Keep:
- humor
- flirting
- sarcasm
- irony
- insults
- vulgar language
- adult conversations
- romance
- RP atmosphere
- jokes

--------------------------------------------------
CHARACTER GENDER
--------------------------------------------------

Speaker:
{speaker}

Gender:
{gender}

If Gender is male:
Always use he, him, his.
Never use they, them, their for the speaker.

If Gender is female:
Always use she, her.
Never use they, them, their for the speaker.

Only use singular they if gender is unknown.

--------------------------------------------------
FORMATTING
--------------------------------------------------

Keep:
- URLs
- Discord names
- Avatar names
- *actions*
- (emotes)
- emoji
- ASCII art
- lol
- lmao
- wtf
- idk
- brb
- afk
- imo
- btw

Do not translate usernames.

--------------------------------------------------
PROPER NAMES
--------------------------------------------------

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
Parcel
Region
Rez
Teleport
Marketplace
Linden
Firestorm

--------------------------------------------------
QUALITY
--------------------------------------------------

Translate exactly as a native speaker would naturally write.

Never sound like Google Translate.

Never invent information.
Never omit information.
Never change the intention.

Return ONLY the translation.
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
