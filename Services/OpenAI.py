import google.generativeai as genai
import openai
from Services.ListenAndSpeak import Speak
import eel
import json
from Services.api_key import api_key1, api_key2
genai.configure(api_key = api_key1)
def formatrection(jso):
    temp = json.loads(jso)
    return temp['reaction']

def formatresponse(jso):
    temp = json.loads(jso)
    return temp['response']
def AI(query):
    query = 'prompt:'+query+r'response-format should be json {response:{},reaction:{}} reaction should be from sad,happy,confused,dont add any new json field keep it to the format,any response should not contain " '
    try:
        openai.api_key = api_key2
        response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=query ,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        temp = response["choices"][0]["text"]
        # temp = json.loads(temp)
        # rection = temp["reaction"]
        # respose = temp["response"]
        # print(temp)
        # print(rection)
        # print(respose)
        # Speak(response["choices"][0]["text"])
        eel.js_function(formatrection(temp))
        Speak(formatresponse(temp))
        
    except:
        generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 512,
        }
        model = genai.GenerativeModel(model_name="gemini-pro",
                                    generation_config=generation_config)
        
        convo = model.start_chat()
        convo.send_message(query)
        resp = (convo.last.text).replace('*', ' ')
        Speak(resp)
        


