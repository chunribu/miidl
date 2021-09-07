import miidl
from .methods import auto, custom, none

def reshape(df, method='auto'):
    return getattr(miidl.reshaping, method)(df)

call = {
    'auto': auto,
    'custom': custom,
    'none': none
}