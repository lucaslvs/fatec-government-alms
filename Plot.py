import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pandas.io.json import json_normalize

class Plot():

    def __init__(self, jsonData):
        self.data = jsonData

    def plot_state_year(self, state, year):
        pass
    
    def plot_aState_aYear(self):
        pass
    
    def plot_timeline(self, state, start, end):
        pass