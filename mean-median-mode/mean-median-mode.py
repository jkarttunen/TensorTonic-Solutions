import numpy as np

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    arr = np.array(x)
    (sorted, idx, counts) = np.unique(arr, return_index=True, return_counts=True)
    index = idx[np.argmax(counts)]
    mode = arr[index]
    return np.mean(x), np.median(x), mode
    pass