import numpy as np

def ridge_regression(X, y, regularization):
    """ Implements Ridge regularization in least squares regression"""
    XTX_regularized = np.linalg.inv(X.T.dot(X) + np.diag([regularization] * X.shape[1]))
    p = XTX_regularized.dot(X.T).dot(y)
    return p
    
