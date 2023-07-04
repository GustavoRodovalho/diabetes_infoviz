import streamlit as st
import pandas as pd
from functions.radviz import RadViz3D
from functions.pca import pca_vis
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
# from ..functions.mds import mds

def visualization():
    st.header(":bar_chart: VISUALIZAÇÕES")

    df = pd.read_csv("data/diabetes.csv")

    # RadViz

    y = df["Outcome"]
    X = df.drop(["Outcome"], axis=1)
    BPs = 10000

    radviz = RadViz3D(y, X, BPs, legend_title="Outcome", anchors_name="")
    
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
    
    st.divider()

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

    st.divider()

    # PCA
    
    pca_2pc = pca_vis(
        df, target="Outcome",
        x_lab="Componente Principal 1",
        y_lab="Componente Principal 2",
        title="")

    pca_2pc.update_layout(
        title={
            'text': "PCA Scatterplot",
            'x': 0.5,
            'y': 0.9,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )

    st.plotly_chart(pca_2pc)

    st.divider()

    # # Multidimensional scaling

    # X = df.drop('Outcome', axis=1)
    # y = df['Outcome']
    # mds_plot = mds(df)

    # mds_plot.update_layout(
    #     title={
    #         'text': "Multidimensional Scaling (MDS)",
    #         'x': 0.5,
    #         'y': 1,
    #         'xanchor': 'center',
    #         'yanchor': 'top'
    #     }
    # )

    # st.plotly_chart(mds_plot)

    # st.divider()