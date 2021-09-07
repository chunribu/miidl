import miidl
from .methods import default, none

def buildmodel(X_train=None, y_train=None, X_test=None, y_test=None, method='default'):
    return getattr(miidl.modeling, method)(X_train, y_train, X_test, y_test)

call = {
    'default': default, 
    # 'custom': custom, 
    'none': none
}