from .IO import read
from .QC import qc
from .normalization import normalize
from .imputation import impute
from .reshaping import reshape
from .modeling import buildmodel
from .interpretation import explain
from .utils import run_as_command

import pandas as pd

def _is_df(a):
    return True if type(a) is pd.DataFrame else False

class MData:
    def __init__(self):
        self.full_data = None
        self.train_data = None
        self.test_data = None
        self.full_X = None
        self.full_y = None
        self.train_X = None
        self.train_y = None
        self.test_X = None
        self.test_y = None
        self.model = None
        self.attributions = []
        self.features = None
        self.labels = {}

    def __repr__(self) -> str:
        if _is_df(self.full_data):
            print(self.full_data)
            return str(self.full_data.shape)
        if _is_df(self.train_data):
            print(self.train_data)
            if _is_df(self.test_data):
                print(self.test_data)
                return 'Train: '+str(self.train_data.shape)+'; Test: '+str(self.test_data.shape)
        return '0'

    def read(self, fname, role='all', group_col='group'):
        if role=='all':
            self.full_data = read(fname)
            self.full_y = self.full_data[group_col]
            self.full_X = self.full_data.drop(columns=group_col)
        elif role=='train':
            self.train_data = read(fname)
            self.train_y = self.train_data[group_col]
            self.train_X = self.train_data.drop(columns=group_col)
        elif role=='test':
            self.test_data = read(fname)
            self.test_y = self.test_data[group_col]
            self.test_X = self.test_data.drop(columns=group_col)
        else:
            print(f"Illegal role: {role}!")
    
    def qc(self, obs=0.3):
        bf, af = 0, 0
        if _is_df(self.full_data):
            bf = len(list(self.full_X))
            self.full_X = qc(self.full_X, obs)
            af = len(list(self.full_X))
        if _is_df(self.train_data):
            if _is_df(self.test_data):
                combined_X = pd.concat([self.train_X, self.test_X], sort=False)
                bf = len(list(combined_X))
                combined_X = qc(combined_X, obs)
                af = len(list(combined_X))
                self.train_X = combined_X.loc[self.train_y.index,:]
                self.test_X = combined_X.loc[self.test_y.index,:]
        print(f'Number of features: from {bf} to {af}.')
    
    def normalize(self, method='log2p'):
        if _is_df(self.full_data):
            self.full_X = normalize(self.full_X, method)
        if _is_df(self.train_data):
            if _is_df(self.test_data):
                self.train_X = normalize(self.train_X, method)
                self.test_X = normalize(self.test_X, method)
    
    def impute(self, method='none'):
        if _is_df(self.full_data):
            self.full_X = impute(self.full_X, method)
        if _is_df(self.train_data):
            if _is_df(self.test_data):
                self.train_X = impute(self.train_X, method)
                self.test_X = impute(self.test_X, method)
    
    def reshape(self, method='auto'):
        if _is_df(self.full_data):
            pass
        if _is_df(self.train_data):
            if _is_df(self.test_data):
                pass
    
    def buildmodel(self, method='default'):
        self.model = buildmodel(self.train_X, self.train_y, self.test_X, self.test_y, method)
    
    def explain(self, method='IntegratedGradients', target=2):
        if type(self.model) is not None:
            for i in range(len(self.test_y)):
                attr = explain(self.model, self.test_X[i], method, target=len(set(self.test_y)))
                self.attributions.append(attr)
        pass
    
    def save(self):
        pass
    

__all__    = [read, qc, normalize, impute, reshape, buildmodel, explain, MData]
__author__ = "chunribu@mail.sdu.edu.cn"

if __name__ == "__main__":
    run_as_command()