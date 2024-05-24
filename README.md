
Melhorias no Código Python para Atividade (0 a 5 pontos de recuperação)

Introdução

Este guia apresenta sugestões de melhorias para o código Python fornecido, com o objetivo de aprimorar sua legibilidade, eficiência e robustez. A pontuação final para recuperação da média (de 0 a 5 pontos) dependerá da quantidade e da qualidade das implementações realizadas.

Melhorias Sugeridas

1. Importação Simplificada

Python

from google.generativeai import GenerativeModel, Chat

Use o código com cuidado.

content\_copy

Descrição:

Importa diretamente as classes GenerativeModel e Chat do módulo google.generativeai, evitando a necessidade de importar o módulo completo.

Benefícios:

Simplifica o código e torna-o mais legível.

Reduz a quantidade de linhas de código.

1. Gerenciamento de Chave API

Python

import os

GOOGLE\_GEMINI\_API\_KEY = os.environ.get("GOOGLE\_GEMINI\_API\_KEY")

if not GOOGLE\_GEMINI\_API\_KEY:

raise ValueError("Chave API do Gemini não definida.")

genai.configure(api\_key=GOOGLE\_GEMINI\_API\_KEY)

Use o código com cuidado.

content\_copy

Descrição:

Armazena a chave API do Gemini em uma variável de ambiente para evitar sua exposição no código.

Utiliza a função os.environ.get() para acessá-la.

Verifica se a chave API foi definida e levanta um erro se não for.

Benefícios:

Protege a chave API de ser exposta no código.

Facilita o gerenciamento da chave API, permitindo que ela seja armazenada em um local seguro.

1. Verificação de Modelos Disponíveis

Python

disponiveis = genai.list\_models()

modelos\_com\_generate\_content = []

for modelo in disponiveis:

if "generateContent" in modelo.supported\_generation\_methods:

modelos\_com\_generate\_content.append(modelo)

if not modelos\_com\_generate\_content:

print("Nenhum modelo com suporte para generateContent encontrado.")

exit()

print("Modelos disponíveis com generateContent:")

for modelo in modelos\_com\_generate\_content:

print(f"- {modelo.name}")

Use o código com cuidado.

content\_copy

Descrição:

Utiliza um loop for com a função genai.list\_models() para listar os modelos disponíveis.

Filtra os modelos por aqueles que suportam o método generateContent.

Exibe uma mensagem se nenhum modelo com generateContent for encontrado.

Exibe uma lista dos modelos disponíveis com generateContent.

Benefícios:

Permite que o usuário visualize os modelos disponíveis antes de escolher um.

Evita que o usuário tente usar um modelo que não suporta a funcionalidade desejada.

1. Seleção Interativa de Modelo

Python

while True:

print("\nSelecione um modelo:")

for i, modelo in enumerate(modelos\_com\_generate\_content):

print(f"{i + 1}. {modelo.name}")

try:

escolha = int(input("Sua escolha: "))

except ValueError:

print("Entrada inválida. Digite um número.")

continue

if 1 <= escolha <= len(modelos\_com\_generate\_content):

modelo\_selecionado = modelos\_com\_generate\_content[escolha - 1]

break

else:

print("Modelo inválido. Tente novamente.")

model = GenerativeModel(modelo\_selecionado.name)

Use o código com cuidado.

content\_copy

Descrição:

Permite que o usuário selecione o modelo desejado dentre os disponíveis com generateContent.

Utiliza um loop while para repetir a seleção até que o usuário escolha um modelo válido.

Valida a entrada do usuário e exibe mensagens de erro em caso de entrada inválida.

Seleciona o modelo escolhido pelo usuário e cria um objeto GenerativeModel.

Benefícios:

Torna a interface mais amigável para o usuário.

Permite que o usuário escolha o modelo que melhor atende às suas necessidades.

1. Exemplo de Geração de Conteúdo

Python

prompt = input("Digite um prompt para gerar conteúdo: ")

response = model.generate\_content(prompt)

print(f"Resposta do modelo:\n{response.text}")

Use o código com cuidado.

content\_copy

Descrição:

Apresenta um exemplo de geração de conteúdo utilizando o modelo selecionado.

Permite que o usuário defina o prompt.

Gera o conteúdo
