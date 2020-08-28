import pandas as pd
import numpy as np
import scipy.stats as st

def get_correlated_metrics_long(df, thresh=0.6):
    corr_matrix = df.corr()
    corr_matrix = pd.DataFrame(np.tril(corr_matrix, -1),
                columns=corr_matrix.columns,
                index=corr_matrix.index)
    res = []
    thresh = 0.6
    for col in corr_matrix.columns:
            corr_col_abs = corr_matrix[col].abs()
            corr_col_abs = corr_col_abs[corr_col_abs >= thresh]
            temp = pd.DataFrame({'col2': corr_col_abs.index,
                                 'val': corr_col_abs.values})
            temp['col1'] = col
            if len(temp):
                res.extend(temp.values.tolist())
    res = pd.DataFrame(res, columns=['col1', 'corr', 'col2'])
    return res

def get_correlated_metrics(df, thresh=0.6):
    corr_matrix = df.corr()
    thresh=0.6
    df_corr = pd.DataFrame(np.tril(corr_matrix, -1),
                          columns=corr_matrix.columns,
                          index=corr_matrix.index)
    df_corr_melted = df_corr.reset_index().melt(id_vars='index')
    df_corr_melted = df_corr_melted[df_corr_melted['value']>= thresh]
    df_corr_melted = df_corr_melted.rename(columns={'index': 'col1',
                                                    'variable': 'col2',
                                                    'value': 'corr'})
    df_corr_melted = df_corr_melted.reset_index(drop=True)
    return df_corr_melted