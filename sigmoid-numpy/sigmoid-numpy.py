import numpy as np
import math

def sigmoid(x):
    """
    The sigmoid function is one of the simplest and most widely used activation functions in machine learning. It takes any real number and maps it smoothly into the range (0, 1).
    """
    arr = np.asarray(x)
    return 1/(1+math.e ** (-arr))
    pass