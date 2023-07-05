import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def pca_vis(
    df:pd.DataFrame,
    target:str,
    x_lab:str = "PC1",
    y_lab:str = "PC2",
    title:str = "Principal Component Analysis (PCA)"
    ):
    '''Create a plotly figure with the 2 principal components of PCA'''
    
    features = df.columns.tolist()
    target = target
    features.remove(target)
    X = df[features].values
    y = df[target].values
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)
    df_pca = pd.DataFrame(data=X_pca, columns=["PC1", "PC2"])
    df_pca[target] = y

    loadings = pca.components_.T * np.sqrt(pca.explained_variance_)

    x_range = np.max(X_pca[:, 0]) - np.min(X_pca[:, 0])/2
    y_range = np.max(X_pca[:, 1]) - np.min(X_pca[:, 1])/2

    fig = px.scatter(
        df_pca,
        x="PC1",
        y="PC2",
        color=target,
        title=title,
        color_continuous_scale=px.colors.diverging.Picnic
        )

    for i, feature in enumerate(features):
        fig.add_annotation(
            ax=0, ay=0,
            axref="x", ayref="y",
            x=loadings[i, 0]*x_range,
            y=loadings[i, 1]*y_range,
            showarrow=True,
            arrowsize=1,
            arrowhead=2,
            xanchor="right",
            yanchor="top",
            opacity=0.2
        )
        fig.add_annotation(
            x=loadings[i, 0]*x_range,
            y=loadings[i, 1]*y_range,
            ax=0, ay=0,
            xanchor="center",
            yanchor="bottom",
            text=feature,
            yshift=5,
        )

    fig.update_layout(
        xaxis_title=x_lab,
        yaxis_title=y_lab
    )

    return fig