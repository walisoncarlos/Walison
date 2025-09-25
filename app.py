import streamlit as st
from openai import OpenAI
import os

# Configuração do cliente OpenAI (pega chave das secrets)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Configuração da página
st.set_page_config(page_title="Chat com LLM", page_icon="🤖")
st.title("🤖 Chat com LLM (via OpenAI API)")

# Histórico da conversa
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": "Você é um assistente útil e criativo."}
    ]

# Mostrar o histórico no chat
for msg in st.session_state["messages"]:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])

# Entrada do usuário
user_input = st.chat_input("Digite sua pergunta...")

if user_input:
    # Adiciona a pergunta
    st.session_state["messages"].append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Chamada à API da OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # pode trocar por gpt-3.5-turbo ou outro
        messages=st.session_state["messages"]
    )

    answer = response.choices[0].message.content

    # Adiciona a resposta
    st.session_state["messages"].append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)
