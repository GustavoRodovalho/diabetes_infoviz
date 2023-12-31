import streamlit as st
import pandas as pd
from functions.radviz import RadViz3D
from functions.pca import pca_vis
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
import plotly.figure_factory as ff
from utils.preprocess import load

def visualization():
    st.header(":bar_chart: VISUALIZAÇÕES")

    st.markdown("Nesta seção serão apresentadas as visualizações para responder as hipóteses já listadas na página inicial.")

    st.divider()

    # Rápido pré-processamento

    df = load("data/diabetes.csv")

    # Hipótese 1

    st.markdown("**1. A obesidade pode aumentar a resistência à insulina e afetar o funcionamento adequado do metabolismo da glicose, predispondo as pessoas ao desenvolvimento de diabetes. Dessa forma, há maior prevalência de diabetes em indivíduos com maior Índice de Massa Corporal (BMI)?**")

    # Matriz de gráficos de dispersão

    textd = ['não diabético' if cl==0 else 'diabético' for cl in df['Outcome']]

    scat_matrix = go.Figure(
        data=go.Splom(
            dimensions=[dict(label='Pregnancies', values=df['Pregnancies']),
                dict(label='Glucose', values=df['Glucose']),
                dict(label='BloodPress', values=df['BloodPressure']),
                dict(label='SkinThick', values=df['SkinThickness']),
                dict(label='Insulin', values=df['Insulin']),
                dict(label='BMI', values=df['BMI']),
                dict(label='PedigreeFunction', values=df['DiabetesPedigreeFunction']),
                dict(label='Age', values=df['Age'])],
            marker=dict(
                color=df['Outcome'],
                size=3,
                colorscale='Bluered',
                line=dict(width=0.5, color='rgb(230,230,230)')),
            text=textd,
            diagonal=dict(visible=False)))

    scat_matrix.update_layout(
        title={
            'text': "Matriz de Gráficos de Dispersão",
            'x': 0.5,
            'y': 0.9,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        dragmode='select',
        width=1000,
        height=1000,
        hovermode='closest')

    st.plotly_chart(scat_matrix, use_container_width=True)

    st.markdown("Considerando a relação do BMI com o Outcome observada nos múltiplos gráficos de dispersão, pode-se afirmar que a maioria dos pacientes diabéticos apresentam níveis de BMI acima de 25, representando sobrepeso ou obesidade.")

    st.divider()

    # Hipótese 2

    st.markdown("**2. A diabetes é uma síndrome metabólica, em que a insulina não consegue degradar as moléculas de glicose em velocidade constante, o que torna elevado os índices de açúcar no sangue. Com isso, pode-se afirmar que a glicose (Glucose) deve ser a variável mais significativa no desenvolvimento da doença?**")

    # RadViz

    y = df["Outcome"]
    X = df.drop(["Outcome"], axis=1)
    BPs = 10000

    radviz = RadViz3D(y, X, BPs, legend_title="Outcome", anchors_name="", two_cat=True)
    
    radviz.update_layout(
        title={
            'text': "RadViz 3D",
            'x': 0.5,
            'y': 0.9,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )
    
    st.plotly_chart(radviz)

    # PCA
    
    pca_2pc = pca_vis(
        df, target="Outcome",
        x_lab="Componente Principal 1",
        y_lab="Componente Principal 2",
        title="")

    pca_2pc.update_layout(
        title={
            'text': "Gráfico de Dispersão PCA",
            'x': 0.5,
            'y': 1,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )

    st.plotly_chart(pca_2pc)

    st.markdown("De acordo com o RadViz 3D, não há uma variável mais significativa que as outras pois os dados aparentemente se encontram equilibrados em relação às âncoras. A visualização do gráfico de dispersão das duas componentes principais do PCA representadas nas dimensões x e y também não revelou resultados que possibilitem essa conclusão.")

    st.divider()

    # Hipótese 3

    st.markdown("**3. É sabido que com a idade o corpo vai perdendo a capacidade de produzir insulina e diminuindo a sensibilidade em relação a ela. Dado isso, é possível afirmar que a maioria dos pacientes portadores da doença possuem idade (Age) acima dos 40 anos?**")

    # Gráfico de frequências

    fig = px.histogram(df, x='Age', color='Outcome', nbins=10,
                    labels={'Age': 'Age interval mean', 'Outcome': 'Outcome'},
                    title='',
                    category_orders={'Outcome': [0, 1]},
                    color_discrete_sequence=['blue', 'red'])

    fig.update_layout(
        barmode='group',
        title={
            'text': "Gráfico de Frequências",
            'x': 0.5,
            'y': 0.9,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )

    st.plotly_chart(fig)

    st.markdown("De acordo com o gráfico de frequências, a maior frequência de pacientes diabéticos é entre a segunda e terceira década de vida.")

    st.divider()

    # Hipótese 4

    st.markdown("**4. De acordo com a Associação Brasileira para o Estudo da Obesidade e Síndrome Metabólica (ABESO), [os indíviduos são considerados diabéticos quando apresentarem glicemia acima de 126 mg/dL](https://abeso.org.br/qual-o-valor-normal-da-glicemia-saiba-o-que-e-e-como-medir-corretamente/). A partir da base de dados, qual intervalo de nível de glicose (Glucose) acomete os pacientes com diabetes?**")

    # Parallel coordinates

    features = df.columns.tolist()
    features.remove("Outcome")
    
    parallel_coords = px.parallel_coordinates(
        df,
        dimensions=features,
        color="Outcome",
        color_continuous_scale=px.colors.diverging.Picnic,
        color_continuous_midpoint=0.5
        )

    parallel_coords.update_layout(
        title={
            'text': "Coordenadas Paralelas",
            'x': 0.5,
            'y': 1,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        margin=dict(l=50, r=50, t=50, b=50)
    )

    st.plotly_chart(parallel_coords)

    st.markdown("De acordo com o gráfico de coordenadas paralelas, o intervalo que compreende a maior parte dos pacientes diabéticos é entre 100 e 199 mg/dL.")