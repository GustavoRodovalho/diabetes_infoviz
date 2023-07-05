import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from utils.preprocess import load

def dataset():
    st.header(":woman: PIMA INDIANS DIABETES")

    st.markdown("""
    O conjunto de dados é originalmente do National Institute of Diabetes and Digestive and Kidney Diseases. Seu propósito era ser utilizado para prever se um paciente tem ou não diabetes, com base em certas medidas diagnósticas. Várias restrições foram aplicadas à seleção dessas instâncias a partir de um banco de dados maior. Em particular, todas as pacientes são mulheres com pelo menos 21 anos de idade e de origem indígena Pima.
    """)

    df = pd.read_csv("data/diabetes.csv")

    st.dataframe(
        df,
        column_config={
            "Pregnancies": st.column_config.ProgressColumn(
                label="Pregnancies",
                width="small",
                help="Número de gravidezes da paciente",
                format="%d",
                min_value=int(df["Pregnancies"].min()),
                max_value=int(df["Pregnancies"].max()),
            ),
            "Glucose": st.column_config.ProgressColumn(
                label="Glucose",
                width="small",
                help="Concentração de glicose plasmática",
                format="%d",
                min_value=int(df["Glucose"].min()),
                max_value=int(df["Glucose"].max()),
            ),
            "BloodPressure": st.column_config.ProgressColumn(
                label="BloodPressure",
                width="small",
                help="Pressão sanguínea",
                format="%d",
                min_value=int(df["BloodPressure"].min()),
                max_value=int(df["BloodPressure"].max()),
            ),
            "SkinThickness": st.column_config.ProgressColumn(
                width="small",
                help="Espessura de pele",
                format="%d",
                min_value=int(df["SkinThickness"].min()),
                max_value=int(df["SkinThickness"].max()),
            ),
            "Insulin": st.column_config.ProgressColumn(
                width="small",
                help="Nível de insulina",
                format="%d",
                min_value=int(df["Insulin"].min()),
                max_value=int(df["Insulin"].max()),
            ),
            "BMI": st.column_config.ProgressColumn(
                width="small",
                help="Índice de Massa Corporal (IMC)",
                format="%.1f",
                min_value=int(df["BMI"].min()),
                max_value=int(df["BMI"].max()),
            ),
            "DiabetesPedigreeFunction": st.column_config.ProgressColumn(
                width="small",
                help="Predisposição genética de desenvolver diabetes",
                format="        %f",
                min_value=int(df["DiabetesPedigreeFunction"].min()),
                max_value=int(df["DiabetesPedigreeFunction"].max()),
            ),
            "Age": st.column_config.ProgressColumn(
                width="small",
                help="Idade da paciente",
                format="%d",
                min_value=int(df["Age"].min()),
                max_value=int(df["Age"].max()),
            ),
            "Outcome": st.column_config.CheckboxColumn(
                width="small",
                help="Indica se a paciente possui diabetes",
            )
        },
        hide_index=True,
    )

    st.divider()

    st.header(":clipboard: DESCRIÇÃO DAS VARIÁVEIS DO DATASET")

    st.markdown("""
    - Pregnancies: número de gravidezes (numérica)
    - Glucose: concentração de glicose plasmática em 2 horas em um teste oral de tolerância à glicose (mg/dL) (numérica)
    - BloodPressure: pressão sanguínea (numérica)
    - SkinThickness: espessura da pele (numérica)
    - Insulin: insulina sérica de 2 horas (mu U/ml); níveis de insulina no soro 2 horas após a administração de glicose (numérica)
    - BMI: índice de massa corporal (IMC) (numérica)
    - DiabetesPedigreeFunction: probabilidade de desenvolimento de diabetes por hereditariedade (numérica)
    - Age: idade (numérica)
    - Outcome: 1 = diabético / 0 = não diabético (categórica)
    """)

    st.divider()

    st.header(":mag_right: ANÁLISE EXPLORATÓRIA DOS DADOS")

    st.markdown("""
    Durante a análise exploratória dos dados, observou-se que haviam registros com valor nulo nos atributos Glucose, BloodPressure, SkinThickness, Insulin e BMI. É sabido que para os dados analisados neste artigo valores iguais a zero, em módulo, representam uma inconsistência. Logo, como pré-processamento, realizou-se a substituição destes valores pela média de seu atributo correspondente.
    """)

    # Rápido pré-processamento
    
    df = load("data/diabetes.csv")

    # Mapa de calor da matriz de correlação

    corr_matrix = df.corr()

    heatmap = go.Heatmap(
        z=corr_matrix.values,
        x=corr_matrix.columns,
        y=corr_matrix.index,
        colorscale="Reds",
    )

    fig = go.Figure(data=[heatmap])

    fig.update_layout(
        title={
            'text': "Mapa de Calor de Correlação do Pima Indian Diabetes Dataset",
            'x': 0.5,
            'y': 0.9,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )

    st.plotly_chart(fig)
