import numpy as np

def qc(df, obs=0.3):
    '''Filt data by observed rate (obs_num / all_num)'''
    if obs=='none':
        obs=0
    df = df.replace(0, np.nan)
    count_idx = df.count(axis=1)
    idx = count_idx[count_idx>=obs]
    return df.loc[idx,:]