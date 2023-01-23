import openai
from config import OPENAI_TOKEN
import pyttsx3
def airs(stext):
    openai.api_key = OPENAI_TOKEN
    response = openai.Completion.create(
        engine= "text-davinci-003",
        prompt= stext,
            temperature= 0.1,
            max_tokens=1000,
            top_p = 1,
            frequency_penalty=0,
            presence_penalty=0
    )
    content = response.choices[0].text.split('.')
    #print(content)
    return response.choices[0].text

while True:
    query = input("Panda: ")
    response = airs(query)
    print(response)
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()

