import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from pandas.io.json import json_normalize

def plot_all_years(json_data):
    pass


def plot_all_states(json_data):
    pass


def plot_year(json_data, year):
    pass


def plot_state(json_data, state):
    data = json_normalize(json_data)
    
    valores = []
    anos = []
    
    for k in data:
        if k[10:-5] == state.upper():
           valores.append(data[k][0])
           anos.append(int(k[-4:]))
           name = k
    
    # Média de crescimento
    media = np.median(valores)
    
    plt.title('Valores totais gastos em: ' + name[10:-5])
    plt.xlabel('Anos')
    plt.ylabel('Gastos (Bilhões)')
    plt.plot(anos, valores)
    media_patch = mpatches.Patch(label='Média de crescimento anual (Milhões): ' + str(media)[0:3])
    plt.legend(handles=[media_patch])
    plt.show()