from .IO import read
from .QC import qc
from .normalization import normalize
from .imputation import impute
from .reshaping import reshape
from .modeling import buildmodel
from .interpretation import explain
from .networking import buildnet
from .utils import run_as_command

class MData:
    def __init__(self) -> None:
        pass

    def read(self):
        pass
    
    def qc(self):
        pass
    
    def normalize(self):
        pass
    
    def impute(self):
        pass
    
    def reshape(self):
        pass
    
    def buildmodel(self):
        pass
    
    def explain(self):
        pass
    
    def buildnet(self):
        pass
    
    def save(self):
        pass
    


__all__ = [IO, QC, normalization, imputation, reshape, modeling, interpretation, networking]
__author__ = "chunribu@mail.sdu.edu.cn"

if __name__ == "__main__":
    run_as_command()