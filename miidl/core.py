from .IO import read as _read
from .QC import qc as _qc
from .normalization import normalize as _normalize
from .imputation import impute as _impute
from .reshaping import reshape as _reshape
from .modeling import buildmodel as _buildmodel
from .interpretation import explain as _explain
import pandas as pd
import numpy as np


def _is_df(a):
    return True if type(a) is pd.DataFrame else False

def dataset_split(dataset, labels, train_proportion=0.7):
    n_all = len(labels)
    n_select = round(n_all * train_proportion)
    idx_all = range(n_all)
    idx_train = np.random.choice(n_all, size=n_select, replace=False)
    idx_test = list(set(idx_all) - set(idx_train))
    return dataset[idx_train], labels[idx_train], dataset[idx_test], labels[idx_test]

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

    def read(self, fname, role='all', group_col='Group'):
        if role=='all':
            self.full_data = _read(fname)
            self.full_y = self.full_data[group_col]
            self.full_X = self.full_data.drop(columns=group_col).T
            self.full_data = self.full_data.T
        elif role=='train':
            self.train_data = _read(fname)
            self.train_y = self.train_data[group_col]
            self.train_X = self.train_data.drop(columns=group_col).T
            self.train_data = self.train_data.T
        elif role=='test':
            self.test_data = _read(fname)
            self.test_y = self.test_data[group_col]
            self.test_X = self.test_data.drop(columns=group_col).T
            self.test_data = self.test_data.T
        else:
            print(f"Illegal role: {role}!")
    
    def qc(self, obs=0.3):
        bf, af = 0, 0
        if _is_df(self.full_data):
            bf = len(list(self.full_X))
            self.full_X = _qc(self.full_X, obs)
            af = len(list(self.full_X))
        if _is_df(self.train_data):
            if _is_df(self.test_data):
                combined_X = pd.concat([self.train_X, self.test_X], sort=False)
                bf = len(list(combined_X))
                combined_X = _qc(combined_X, obs)
                af = len(list(combined_X))
                self.train_X = combined_X.loc[self.train_y.index,:]
                self.test_X = combined_X.loc[self.test_y.index,:]
        print(f'Number of features: from {bf} to {af}.')
    
    def normalize(self, method='log2p'):
        if _is_df(self.full_data):
            self.full_X = _normalize(self.full_X, method)
        if _is_df(self.train_data):
            if _is_df(self.test_data):
                self.train_X = _normalize(self.train_X, method)
                self.test_X = _normalize(self.test_X, method)
    
    def impute(self, method='none'):
        if _is_df(self.full_data):
            self.full_X = _impute(self.full_X, method)
        if _is_df(self.train_data):
            if _is_df(self.test_data):
                self.train_X = _impute(self.train_X, method)
                self.test_X = _impute(self.test_X, method)
    
    def reshape(self, method='auto', train_proportion=0.7):
        if _is_df(self.full_data):
            full_X, self.features = _reshape(self.full_X, method)
            uniq_label = list(set(self.full_y))
            self.full_y = [uniq_label.index(i) for i in self.full_y]
            for i, v in enumerate(uniq_label):
                self.labels[i] = v
            self.train_X, self.train_y, self.test_X, self.test_y = dataset_split(full_X, self.full_y, train_proportion)
        if _is_df(self.train_data):
            if _is_df(self.test_data):
                self.train_X, self.features = _reshape(self.train_X, method)
                self.test_X, self.features = _reshape(self.test_X, method)
                uniq_label = list(set(self.train_y))
                self.train_y = [uniq_label.index(i) for i in self.train_y]
                self.test_y = [uniq_label.index(i) for i in self.test_y]
                for i, v in enumerate(uniq_label):
                    self.labels[i] = v
    
    def buildmodel(self, method='default'):
        self.model = _buildmodel(self.train_X, self.train_y, self.test_X, self.test_y, method, self.train_X.shape[-1], len(set(self.labels)))
    
    def explain(self, method='IntegratedGradients'):
        if type(self.model) is not None:
            for i in range(len(self.test_y)):
                attr = _explain(self.model, self.test_X[i], method, target=len(set(self.labels)))
                self.attributions.append(attr)    

    def save(self):
        pass
    