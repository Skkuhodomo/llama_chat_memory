import streamlit as st 
def sidebar():
    conn = st.connection('mysql', type='sql')
    df = conn.query('SELECT * from chat;', ttl=600)
    for row in df.itertuples():
        chat_ids = df['chat_id'].tolist()


    st.sidebar.header("Chat History")
    for chat_id in chat_ids:
        url = f"/chat/{chat_id}"  # chat_id를 포함한 URL 생성
        if st.sidebar.button(f"Chat {chat_id}"):
            st.experimental_set_query_params(chat_id=chat_id)  # 클릭한 chat_id를 URL에 추가
            st.experimental_rerun()  # 페이지를 다시로드하여 변경된 URL로 이동
