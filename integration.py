import google.generativeai as genai

genai.configure(api_key="AIzaSyAfCSIH59x2jjSdgUPGWlIbHbczXP_dWb4")

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Qual o codigo hex da cor azul")

print(response.text)
