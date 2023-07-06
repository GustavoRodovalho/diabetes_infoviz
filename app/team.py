import streamlit as st

def team():
    st.header(":man-man-girl: EQUIPE")
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("Gustavo Rodovalho")
        st.image("https://media.licdn.com/dms/image/C4D03AQHIDz4XFBs-Ow/profile-displayphoto-shrink_200_200/0/1624586584999?e=1694044800&v=beta&t=Zn9xaNowsEC0EeNDTzy97tKg8MA-eGelgPSI6OfpoHk")
        st.caption("Mestrando em Engenharia Mineral - PPGEMin.")

    with col2:
        st.header("Rafael Ferrari")
        st.image("https://media.licdn.com/dms/image/C4E03AQFanoFtnedCxw/profile-displayphoto-shrink_200_200/0/1625500020503?e=1694044800&v=beta&t=VYcNBFq4d0342DAhWv4h3ROygAdN2PxSKmiI0CDKlZU")
        st.caption("Mestrando em Ciência de Dados - MECAI.")

    with col3:
        st.header("Renata Cecconi")
        st.image("https://media.licdn.com/dms/image/D4D03AQEJzHChlK1ydA/profile-displayphoto-shrink_200_200/0/1669078225612?e=1694044800&v=beta&t=5xeAhTTnpVqhc4dD3gruUJuhPOBQDqJIGsgqB50rXh4")
        st.caption("Mestranda em Ciência de Dados - MECAI.")