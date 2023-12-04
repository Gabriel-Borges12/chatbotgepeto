import tkinter as tk
import openai

chave_api = "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"

openai.api_key = chave_api

def enviar_mensagem(mensagem, lista_mensagens=[]):
    lista_mensagens.append(
        {"role": "user", "content": mensagem}
    )

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=lista_mensagens,
    )

    return resposta["choices"][0]["message"]["content"]

lista_mensagens = []
while True:
    texto = input("Escreva sua mensagem aqui: ")

    if texto == "sair":
        break
    else:
        resposta = enviar_mensagem(texto, lista_mensagens)
        lista_mensagens.append({"role": "assistant", "content": resposta})
        print("Chatbot: ", resposta)
