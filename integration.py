import random
import google.generativeai as genai
genai.configure(api_key="AIzaSyBAocn-QIdMLH5baVfbuWtvwvXIk_jG8rE")
model = genai.GenerativeModel('gemini-1.5-flash')
#Nome da cor
#Código hexadecimal da cor
#Código RGB correspondente a cor
#Cor correspondente no sistema de cores RYB
#Um exemplo de medição de cores de acordo com a cor
#Uma breve descrição da cor
#Duas cores que combinam com a cor
#Termo de classificação da terminologia para a cor



languages = ["en-us", "pt-br","es-es","cmn"]
language = languages[3]
colorTemperature = "cold, hot, neutral or earthy"

hex = f"#{random.randint(0x100000, 0xFFFFFF):06X}"

def color_prompt(hex):
    resposta = []
    Prompt = (f"Complete this information translate to  the language:{language}: name,hexCode {hex},rgbCode ,RYB Color percent ,colorimeter,according to  {colorTemperature}choose one of these ,color Description,two Colors That Match Hex, colorTerminology and return it in a Json")

    for i in range(3):
        response = model.generate_content(Prompt)
        resposta.append(response.text)

    print(resposta[2])

color_prompt(hex)



