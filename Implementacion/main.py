#Imports
from fastapi import FastAPI
from warning_messages import display_warning
from detoxify_model import analyze_text
from chatgpt_API import chatgpt, main, __prompt
from detoxify import Detoxify

#Input content
print("User content:")
user_content = input()
model = Detoxify('original')

#Bbro API
app = FastAPI()

@app.get("/bbro")

def sistema(content):
    #funcion detoxify
    tox_rate = analyze_text(content, model)

    #if ofensivo --> función chatGPT
    if (tox_rate == True ):
        label = chatgpt(content)
    else:
        label = "innofensive"

    #label --> función warning
    display_warning(label)