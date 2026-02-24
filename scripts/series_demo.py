import pandas as pd
import numpy as np

def create_series_from_list(data_list):
    series = pd.Series(data_list)
    return series

def create_series_from_array(data_array):
    series = pd.Series(data_array)
    return series

def create_series_with_index(data_list, index_list):
    series = pd.Series(data_list, index=index_list)
    return series

def main():
    # From list
    numbers_list = [10, 20, 30, 40, 50]
    series1 = create_series_from_list(numbers_list)
    print("Series from list:\n", series1, "\n")
    
    # From NumPy array
    numbers_array = np.array([100, 200, 300, 400])
    series2 = create_series_from_array(numbers_array)
    print("Series from NumPy array:\n", series2, "\n")
    
    # Custom index
    custom_index_series = create_series_with_index(numbers_list, ['a','b','c','d','e'])
    print("Series with custom index:\n", custom_index_series)
    print("Access 'c':", custom_index_series['c'])

if __name__ == "__main__":
    main()