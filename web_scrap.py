import streamlit as st
import requests
from bs4 import BeautifulSoup

# 웹페이지에서 모든 텍스트 정보를 추출하는 함수
def scrape_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # 모든 텍스트 요소 추출
    text_elements = [element.get_text() for element in soup.find_all(string=True)]
    # 불필요한 공백 및 줄바꿈 제거
    text_elements = [element.strip() for element in text_elements if element.strip()]
    return text_elements

# Streamlit 애플리케이션 시작
st.title("전체 텍스트 웹 스크래퍼")

# 사용자로부터 URL 입력 받기
url = st.text_input("웹페이지 URL 입력:")

if st.button("데이터 스크랩"):
    if url:
        # 사용자가 URL을 입력한 경우
        try:
            scraped_data = scrape_text(url)
            # 결과 표시
            st.write("스크래핑 결과:")
            for data in scraped_data:
                st.write(data)
        except Exception as e:
            st.write("오류 발생:", e)
    else:
        st.write("URL을 입력해주세요.")
