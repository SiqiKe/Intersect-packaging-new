import numpy as np


def rescale(input_array):
    """Rescales an array from 0 to 1.

    Takes an array as input, and returns a corresponding array scaled so that 0
    corresponds to the minimum and 1 to the maximum value of the input array.
    """
    low = np.min(input_array)
    high = np.max(input_array)
    output_array = (input_array - low) / (high - low)
    return output_array