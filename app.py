from st_pages import Page, Section, show_pages, add_page_title
import streamlit as st  
show_pages(
    [
        Page("app.py", "Home", "🏠"),
        Page("web_scrap.py", "Web Scrap", ":paw_prints:"),
        Page("llama.py", "Llama2 7b", ":robot_face:"),    
    ]
)
st.title("Welcome!")
