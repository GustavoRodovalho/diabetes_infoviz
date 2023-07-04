import numpy as np
import pandas as pd
from numpy import pi, cos, sin, arccos, arange
import plotly.express as px
import plotly.graph_objects as go 
import plotly.io as pio

def get_3Dpoints(d):
    '''
    Args:
        d: number of points to be projected on a sphere
    
    Returns
        x, y, z coordinates of d points points uniformly distributed on the surface of a sphere
    '''
    indices = arange(0, d, dtype=float) + 0.5
    phi = arccos(1 - 2*indices/d) # Latitude
    theta = pi * (1 + 5**0.5) * indices # Longitude
    x, y, z = cos(theta) * sin(phi), sin(theta) * sin(phi), cos(phi)
    df = pd.DataFrame({'x': x, 'y': y, 'z': z})
    
    return df

def Dataframe3DPreparation(S_hat, X, d, BPs, y, anchors_name):
    '''
    Args:
        S_hat: projected coordinates for each sample (m x 3)
        X: unit vectors of anchors (n x 3)
        d: number of anchors (n)
        BPs: number of boundary points
        y: column with labels (m,)
        anchors_name: anchor name label in the legend

    Returns:
        Dataframe that will be plotted
    '''
    
    frames = [y, S_hat]
    S_hat = pd.concat(frames, axis=1)
    X = X.reset_index()
    
    # Creates a "(n,)" array to label the anchors
    AnchorsLabel = np.append(X['index'], np.full(S_hat.shape[0],''))
    label = np.full((d), anchors_name)
    X['index'] = label

    # Get boundary points x, y and z coordinates (BPs x 3)
    C = get_3Dpoints(BPs) 
    C = pd.DataFrame(C)
    
    # Creates a sphere dataframe that has BPs x 4 ("index", filled by "sphere", "x", "y" and "z")
    label = np.full((BPs), 'sphere') 
    label = pd.DataFrame(label)
    label = label.rename(columns={0: 'index'})
    frames = [label, C]
    sphere = pd.concat(frames, axis=1)
    
    # Creates a frames dataframe that has m+n x 5 ("index", "x", "y", "z" and "AnchorsLabel") 
    frames = [X, S_hat]
    df = pd.concat(frames)
    df['AnchorsLabel'] = AnchorsLabel

    return df, sphere

def matrixNormalization(X):
    '''
    Quick MinMaxNormalization
    '''
    return ((X-X.min())/(X.max()-X.min()))*1

def get_X3Dmatrix(DS_names):
    '''
    Args:
        DS_names: column names of X input.
    Returns:
        A Pandas Dataframe with the x, y and z coordinates on the sphere for the column labels.
    '''
    
    DS_names = pd.DataFrame(DS_names)
    DS_names = DS_names.rename(columns={0: 'DS_names'})
    d = DS_names.size
    DS = get_3Dpoints(d)
    DS = pd.DataFrame(DS).round(6)
    frames = [DS_names, DS]
    X = pd.concat(frames, axis=1)
    X = X.set_index('DS_names')
    X.index.name = None
    
    return X

def Radviz2DMapping(S, X):
    '''
    Project S into X
    '''
    S_hat = S.dot(X)
    S_hat = S_hat.div(S.sum(axis=1), axis=0)
    
    return S_hat.fillna(0)

def plotRadviz3D(df, df_sphere, legend_title):
    '''
    Args:
        df: data + anchors points (m+n x 5)
        df_sphere: boundary points projected on the sphere (BPs x 4)
        legend_title: legend title
    
    Returns:
        Plotly radviz figure object
    '''
    pio.templates["draft"] = go.layout.Template(
        layout_annotations=
            [dict(name="draft watermark", text="",
                textangle=-30, opacity=0.1,
                font=dict(color="black", size=100), xref="paper",
                yref="paper", x=0.5, y=0.5, showarrow=False)
            ]
        )

    config = {'toImageButtonOptions': {
        'format': 'png', # png, svg, jpeg, webp, svg
        'filename': 'custom_image',
        'height': 1000,
        'width': 1000,
        'scale': 1 # Multiply title/legend/axis/canvas sizes by this factor
    }}

    # Chose the colors for the labels
    num_colors = len(df["index"].unique())
    color_sequence = px.colors.qualitative.Light24[:num_colors]

    df.rename(columns={'index': legend_title}, inplace=True)
    fig = px.scatter_3d(
        df,
        x='x', y='y', z='z',
        color=legend_title,
        color_discrete_sequence=color_sequence,
        text='AnchorsLabel')
    fig.add_trace(
        go.Scatter3d(
            mode='markers',
            marker=dict(size=0, color='white', opacity=0.1),
            x=df_sphere["x"], y=df_sphere["y"], z=df_sphere["z"],
            showlegend=False))

    # fig.show()

    return fig

def RadViz3D(y, X, BPs, legend_title="Outcome", anchors_name="Anchor\'s Names"):
    '''
    Args:
        y: column with labels (m,)
        X: original coordinates (m, n-1)
        BPs: number of boundary points

    Returns:
        Plotly figure object
    '''

    y.rename("index", inplace=True) 
    X = matrixNormalization(X)
    S = X # Normalized dataframe (m x n, being m = number of samples and n = number of features)
    DS_names = S.columns
    X = get_X3Dmatrix(DS_names) # Get anchors coordinates (n x 3)

    # Projection of S into the sphere coordinates
    S_hat = Radviz2DMapping(S, X) # m x 3
    d = DS_names.size # d = n

    # Gets the data + anchors points (= df) and the BPs in the sphere (= df_sphere)
    df, df_sphere = Dataframe3DPreparation(S_hat, X, d, BPs, y, anchors_name)

    fig = plotRadviz3D(df, df_sphere, legend_title)

    return fig