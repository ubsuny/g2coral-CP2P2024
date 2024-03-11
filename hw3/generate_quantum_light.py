import numpy as np
from numpy.random import default_rng
import pandas as pd

def create_dataframe(num_photon_detections = 100, num_detectors = 4):
    # Generate column names for detectors
    columns = [f"detector{i}" for i in range(1, num_detectors + 1)]
    
    # Create a dictionary with False values for each column
    data = {col: [False] * num_photon_detections for col in columns}
    
    # Create the DataFrame
    df = pd.DataFrame(data)
    return df

def generate_data(data_frame):

  rng = default_rng()
  keys = data_frame.columns.tolist()
  

  for i in range(len(data_frame)):
    coloumn_index = rng.choice(a=keys, size=None, replace=True, p=None)
    data_frame.at[i, coloumn_index ] = True

  return data_frame
