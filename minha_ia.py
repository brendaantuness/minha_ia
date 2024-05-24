#Rodar esse código no google Colab https://colab.research.google.com/
#Acessar o link https://aistudio.google.com/app/apikey com uma conta google para gerar sua API Key

!pip install -q google-generativeai
import google.generativeai as genai

from google.colab import userdata

GOOGLE_GEMINI_API_KEY = 'sua_chave_aqui'

genai.configure(api_key=GOOGLE_GEMINI_API_KEY)

#Lista os modelos disponiveis do Gemini
#for m in genai.list_models():
#  if 'generateContent' in m.supported_generation_methods:
#    print(m.name)

model = genai.GenerativeModel("gemini-1.5-pro-latest")

#Teste de pergunta direta
#response = model.generate_content("Como posso ficar craque em Python?")
#print(response)
#response.text

#Teste pergunta interativa
#chat = model.start_chat(history=[])

#prompt = input("Como posso te ajudar hoje?")

#while prompt != "fim":
#  response = chat.send_message(prompt)
#  print(response.text)
#  prompt = input("Como posso te ajudar hoje?")
