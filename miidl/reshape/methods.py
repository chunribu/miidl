from math import sqrt, ceil
from warnings import WarningMessage, warn

def edge(n_feature, width=None, devide=4):
    if type(width) is int:
        if width**2 >= n_feature:
            if width % devide == 0:
                return width
            else:
                warn(f"Width of {width} seems not a good choice.", Warning)
                return width
        else:
            warn(f"Width of {width} seems a bad choice. Chenged to auto mode.", Warning)
            width = None

    if width is None:
        width = ceil(sqrt(n_feature))
        while True:
            if width % devide == 0:
                return width
            else:
                width += 1

def integrate(df, patch):
    return df

def auto(df):
    n_feature = len(list(df))
    n_sample = len(df.index)
    width = edge(n_feature)
    patch = width**2 - n_feature
    df = integrate(df, patch)
    features = list(df)
    ndarr = df.to_numpy()
    ndarr = ndarr.reshape(n_sample, width, width)
    return ndarr, features

def custom(df, width):
    n_feature = len(list(df))
    n_sample = len(df.index)
    width = edge(n_feature, width)
    patch = width**2 - n_feature
    df = integrate(df, patch)
    features = list(df)
    ndarr = df.to_numpy()
    ndarr = ndarr.reshape(n_sample, width, width)
    return ndarr, features
