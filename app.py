import json
import requests
import streamlit as st
st.title("Chat with Memory Llama :llama:")
model = 'llama2:7b-chat' 
# Initialize context_chat in session state if it doesn't exist
if 'context_chat' not in st.session_state:
    st.session_state['context_chat'] = []

if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Access and update context_chat from session state
context_chat = st.session_state['context_chat']
def generate(prompt, context):
    response = ""
    r = requests.post('http://localhost:11434/api/generate',
                      json={
                          'model': model,
                          'prompt': prompt,
                          'context': context,
                      },
                      stream=True)
    r.raise_for_status()

    for line in r.iter_lines():
        body = json.loads(line)
        response_part = body.get('response', '')
        response += response_part

        print(response_part, end='', flush=True) 
        if 'error' in body:
            raise Exception(body['error'])

        if body.get('done', False):
            return response, body['context']
    
def main():
    global context_chat
    user_input = st.chat_input("Enter a prompt: ")
    if not user_input:
        exit()
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)
    
    
    print()
    
    response, context_chat = generate(user_input, st.session_state['context_chat'])
    st.session_state['context_chat'] = context_chat
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

    print()

if __name__ == "__main__":
    main()