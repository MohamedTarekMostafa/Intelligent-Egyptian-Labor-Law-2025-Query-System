import streamlit as st
import requests

st.title("نظام الاستعلام الذكي عن قانون العمل المصري 2025")
user_question =  st.text_input("اسأل اي شئ يخص قانون العمل المصري 2025 ")

if st.button("Ask"):
    if user_question:
        with st.spinner("LOADING....."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/ask", 
                    json={"question": user_question}
                )
                if response.status_code == 200:
                    answer = response.json().get("answer")
                    st.write("Answer")
                    st.info(answer)
                else:
                    st.error("there is a problem for calling server")
            except:
                st.error("please ensure that you are using uvicorn")