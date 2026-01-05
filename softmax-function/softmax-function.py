import numpy as np
def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    axis = x.ndim -1
    max = np.max(x, axis=axis, keepdims=True)
    exp = x -max
    divider = np.sum(np.e ** (exp), axis=axis, keepdims=True)
    return np.e **(x-max) / divider
    pass