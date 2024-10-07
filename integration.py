import google.generativeai as genai
import json

genai.configure(api_key="")

model = genai.GenerativeModel('gemini-1.5-flash')

languages = ["en-us", "pt-br"]

language = languages[0]

colorTemperature = "cold, hot, neutral or earthy"

def search_color(hex) -> str:
    jsonToFill = {
    "Color": {
        "id": None,
        "name": None,
        "hexCode": hex,
        "rgbCode": None,
        "rybPercents": None,
        "colorimeter": None,
        "colorDescription": None,
        "twoColorsThatMatch": None,
        "colorTerminology": None
        }
    }
    json_string = json.dumps(jsonToFill)
    
    prompt = ("Complete this json:" + json_string + " \n considering the language: " + language + "\n, the hex code: " + hex + " \n and colorimeter: " + colorTemperature)
    #print(prompt)
    response = model.generate_content(prompt)
    responseFormated = response.text.replace("json", "").replace("```", "")

    print(responseFormated)
    
search_color("#30D5C8")
