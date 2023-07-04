import pandas as pd
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

    fig = px.scatter(
        df_pca,
        x="PC1",
        y="PC2",
        color=target,
        title=title,
        color_continuous_scale=px.colors.diverging.Picnic
        )
    fig.update_layout(
        xaxis_title=x_lab,
        yaxis_title=y_lab
    )

    return fig