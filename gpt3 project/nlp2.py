import json
import openai
from config import OPENAI_TOKEN
import pyttsx3

# Load the definitions from the JSON file
with open('definitions_prepared.jsonl') as json_file:
    definitions = json.load(json_file)

# Create a dictionary to store the prompts and completions
prompt_completions = {}
for definition in definitions:
    prompt_completions[definition['prompt']] = definition['completion']

def generate_response(prompt):
    openai.api_key = OPENAI_TOKEN
    # Check if the prompt is in our dictionary
    if prompt in prompt_completions:
        # Use the corresponding completion from the dictionary as the prompt
        prompt = prompt_completions[prompt]
    else:
        # Add an additional sentence to the prompt
        prompt = "We are talking about aviation, you will be AIRS, or Aeronautical Information Response System. Do your best to provide correct answers to my questions"
    # generate a response using the prompt
    response = openai.Completion.create(
        engine= "text-davinci-003",
        prompt=prompt,
        temperature= 0.1,
        max_tokens=1000,
        top_p = 1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text

while True:
    query = input("Panda: ")
    response = generate_response(query)
    print(response)
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()