import json
import gradio as gr
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()  # take environment variables from .env file
client = OpenAI()     # uses OPENAI_API_KEY from environment

history = []


def generate_response(prompt):
    history.append({"role": "user", "content": prompt})

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content":
             "You are CodeGuru, a coding assistant created by vaishnavi. "
             "You explain coding concepts clearly and help with code problems."},
            *history
        ]
    )

    reply = completion.choices[0].message.content

    # add assistant reply to history
    history.append({"role": "assistant", "content": reply})

    return reply


interface = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=4, placeholder="Enter your prompt"),
    outputs="text",
)
interface.launch()
