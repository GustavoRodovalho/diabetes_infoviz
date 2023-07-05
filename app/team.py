import streamlit as st

def team():
    st.header(":man-man-girl: EQUIPE")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Gustavo Rodovalho")
        st.image("https://static.streamlit.io/examples/cat.jpg")
        st.caption("Mestrando em Engenharia Mineral - PPGEMin.")

    with col2:
        st.header("Rafael Ferrari")
        st.image("https://static.streamlit.io/examples/dog.jpg")
        st.caption("Mestrando em Ciência de Dados - MECAI.")

    with col3:
        st.header("Renata Cecconi")
        st.image("https://static.streamlit.io/examples/owl.jpg")
        st.caption("Mestranda em Ciência de Dados - MECAI.")