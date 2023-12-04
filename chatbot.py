import tkinter as tk
import openai

chave_api = ""

openai.api_key = chave_api

def enviar_mensagem(enviar_mensagem, lista_mensagens = []):
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
        )

    resposta =  openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = lista_mensagens,
    )

    return resposta["choices"][0][mesnagem]

lista_mensagens = []
while True:
    texto = input("Escreva sua mensagem aqui: ")

    if texto == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        lista_mensagens.append(resposta)
        print("Chatbot: ", resposta["content"])