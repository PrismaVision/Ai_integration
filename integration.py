from http.client import responses
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
        "name": None, #Nome da cor
        "hexCode": hex, ##Código hexadecimal da cor
        "rgbCode": None, # Código RGB correspondente a cor
        "RYBColor": None, # Cor correspondente no sistema de cores RYB
        "colorimeter": None, #Um exemplo de medição de cores de acordo com a cor
        "colorDescription": None, #Uma breve descrição da cor
        "twoColorsThatMatchHex": None, #Duas cores que combinam com a cor
        "colorTerminology": None #Termo de classificação da terminologia para a cor 
        }
    }
    json_string = json.dumps(jsonToFill)
    
    Prompt2 = (f"Complete this information translate to  the language:{language}: id,name,hexCode {hex},rgbCode ,RYB Color percent ,colorimeter,color Temperature,colorDescription,two Colors ThatMatch Hex, colorTerminology and return it in a Json")
    Prompt = (f"Complete this json: {json_string} \n considering the language: { language } \n, the hex code:  {hex}   \n , colorimeter:  {colorTemperature} and return all this prompt in format JSON ")

#teste
def generate_prompts(language, hex):
    prompts = []
    
    for _ in range(3):
        prompt = (f"Complete this information translate to the language {language}:  id, name, hexCode {hex}, rgbCode, RYB Color percent, colorimeter,color Temperature, colorDescription, two Colors That Match Hex, colorTerminology and return it in a Json")
        prompts.append(prompt)
        response = model.generate_content(prompt)
       teste=  print(response.text)
    return prompts
#result = generate_prompts(language, hex)


for i, response in enumerate(responses, 1):
    print(f"Prompt {i}:\n{responses.text}\n")





#teste/

    #response = model.generate_content(Prompt2)
   # responseFormated = response.text.replace("json", "").replace("```", "")

   # print(language,response.text) 
    
search_color("#cd4309")
