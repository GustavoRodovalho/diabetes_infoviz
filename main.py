import streamlit as st
from app.home import home
from app.dataset import dataset
from app.visualization import visualization
from app.team import team
from app.references import references

st.title(":red[ESTUDO DE PERFIL: DESENVOLVIMENTO DE DIABETES]")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    ":syringe: PÁGINA INICIAL",
    ":bulb: DATASET",
    ":chart_with_upwards_trend: VISUALIZAÇÃO",
    ":people_holding_hands: EQUIPE",
    ":book: REFERÊNCIAS"])

with tab1:
    home()

with tab2:
    dataset()

with tab3:
    visualization()

with tab4:
    team()

with tab5:
    references()