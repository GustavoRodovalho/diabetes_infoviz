import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from scipy.spatial.distance import cdist
from sklearn.decomposition import PCA
import plotly.express as px

def multidim_scaling(
    data:pd.DataFrame or np.ndarray,
    k:int = 2,
    learning_rate:float = 0.1,
    num_iterations:int = 5000,
    metric:str = 'euclidean'):

    '''
    Project multidimensional data into k dimensions using MDS. PCA included as initialization.
    '''

    # Normalization
    scaler = MinMaxScaler()
    norm_data = scaler.fit_transform(data)

    # Calculate the distance matrix between samples, from the M x N matrix (ds)
    ds = cdist(norm_data, norm_data, metric=metric)

    # Project the data into K dimensions using PCA
    pca = PCA(n_components=k)
    locations = pca.fit_transform(norm_data)

    # Calculate the distance matrix between samples, from the M x K matrix (ls)
    ls = cdist(locations, locations, metric=metric)

    # Compute the initial stress
    stress = np.sum((ds - ls) ** 2) / np.sum(ds ** 2)
    # print("Stress before optimization:", stress)

    # Optimization loop
    iterations = 0

    for iteration in range(num_iterations):
        # Calculate the gradient of the stress function with respect to the locations
        gradient = 2 * np.dot((ls - ds), locations - locations.mean(axis=0)) / np.sum(ds ** 2)
        locations -= learning_rate * gradient
        ls = cdist(locations, locations, metric=metric)

        # Calculate the new stress value
        new_stress = np.sum((ds - ls) ** 2) / np.sum(ds ** 2)
        if new_stress >= stress:
            break
        stress = new_stress

        iterations += 1

    # print("Final stress:", stress, "Number of iterations:", iterations)
    
    return locations

def mds(df: pd.DataFrame):
    '''Returns a Plotly scatterplot figure object'''

    projected = multidim_scaling(df)

    fig = px.scatter(x=projected[:,0], y=projected[:,1])

    fig.update_xaxes(title_text="Dimension 1")
    fig.update_yaxes(title_text="Dimension 2")

    return fig