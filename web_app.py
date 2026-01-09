from quart import Quart, render_template_string, request, redirect, url_for, session
from src.gpt_client import chat_with_gpt
from openai import OpenAI
from dotenv import load_dotenv
import os
import asyncio
import logging
logging.basicConfig(level=logging.DEBUG)

load_dotenv()

app = Quart(__name__)
app.secret_key = os.getenv("SECRET_KEY")
key = os.getenv("OPENAI_API_KEY")
if not key:
    raise RuntimeError("OPENAI_API_KEY not found! Is .env file loaded?")
  
# Templates inline for simplicity (you can move them to HTML files)
form_template = """
<!doctype html>
<title>{{ step_title }}</title>
<h2>{{ step_title }}</h2>
<pre>{{ gpt_output }}</pre>
<form method="post">
  <input type="text" name="user_input" required autofocus>
  <button type="submit">Next</button>
</form>
"""

summary_template = """
<!doctype html>
<title>Character Summary</title>
<h2>Character Summary</h2>
<pre>{{ summary }}</pre>
"""

@app.route('/')
async def index():
    session.clear()
    return redirect(url_for('choose_race'))

@app.route('/race', methods=['GET', 'POST'])
async def choose_race():
    if request.method == 'POST':
        session['race'] = (await request.form)['user_input']
        return redirect(url_for('choose_class'))

    prompt = "You are a D&D assistant. Help the user choose a race..."
    gpt_output = await asyncio.to_thread(chat_with_gpt, prompt)
    return await render_template_string(form_template, step_title="Choose Race", gpt_output=gpt_output)

@app.route('/class', methods=['GET', 'POST'])
async def choose_class():
    if request.method == 'POST':
        session['char_class'] = (await request.form)['user_input']
        return redirect(url_for('choose_background'))

    race = session.get('race', 'Human')
    prompt = f"The user has chosen the race '{race}'. Now help them choose a class..."
    gpt_output = await asyncio.to_thread(chat_with_gpt, prompt)
    return await render_template_string(form_template, step_title="Choose Class", gpt_output=gpt_output)

@app.route('/background', methods=['GET', 'POST'])
async def choose_background():
    if request.method == 'POST':
        session['background'] = (await request.form)['user_input']
        return redirect(url_for('show_summary'))

    race = session.get('race')
    char_class = session.get('char_class')
    prompt = f"The user has chosen race '{race}' and class '{char_class}'. Now help choose a background..."
    gpt_output = await asyncio.to_thread(chat_with_gpt, prompt)
    return await render_template_string(form_template, step_title="Choose Background", gpt_output=gpt_output)

@app.route('/summary')
async def show_summary():
    race = session.get('race')
    char_class = session.get('char_class')
    background = session.get('background')
    prompt = f"Create a summary for a D&D character with Race: {race}, Class: {char_class}, Background: {background}..."
    summary = await asyncio.to_thread(chat_with_gpt, prompt)
    return await render_template_string(summary_template, summary=summary)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
