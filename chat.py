import streamlit as st

query_params = st.experimental_get_query_params()
conn = st.connection('mysql', type='sql')
# chat_id가 있는지 확인하고 값을 가져옴
if "chat_id" in query_params:
    chat_id = query_params["chat_id"][0]
    st.write(f"Chat ID: {chat_id}")
else:
    st.write("Chat ID not found in URL")
    # sidebar에서 request 줌. 거기서 chat_id를 받아옴
st.set_page_config(page_title=f"chat{chat_id}", page_icon= "{:llama:}")
# This page is for continuing the chat with the Memory Llama

