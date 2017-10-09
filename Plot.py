import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.io.json import json_normalize

class Plot():

    def __init__(self, jsonData):
        self.data = jsonData
        self.fig, self.ax = plt.subplots()

    def __autolabel(self, rects):
        """
        Código retirado da Doc da lib e adaptado para este caso
        """
        for rect in rects:
            height = rect.get_height()
            self.ax.text(rect.get_x() + rect.get_width()/2., 1.05 * height,
                    '%d' % int(height),
                    ha='center', va='bottom')

    # Exibe o valor gasto por certo estado em um certo ano
    def plot_state_year(self, state, year):
        pass
    
    # Exibe o valor gasto por todos os estados em todos os anos
    def plot_aState_aYear(self):
        pass
    
    # Exibe o valor médio de crescimento em um certo estado dentro de um período de tempo
    def plot_median(self, state, start, end):

        gasto = []
        for key in range(0, (end - start) + 1):
            a = int(str(self.data.allStates[state][str(start + key)])[0:5])
            gasto.append(a)
        bar = self.ax.bar(end - start, gasto, 0.30, color = 'r')        
        plt.show()  
        
    def plot_timeline(self, state, start, end):
        gasto = []
        for key in range(0, (end - start) + 1):
            a = int(str(self.data.allStates[state][str(start + key)])[0:5])
            gasto.append(a)
            pontos = np.arange(0, a)
            plt.title('Valores gastos em ' + state + ' no ano de ' + str(start + key))
            plt.ylabel('Gastos (Milhões)')
            plt.plot(pontos, 'C' + str(key), marker = 'o', ms = 7)
            plt.show()
        print('O crescimento médio anual neste período de tempo foi (Milhões): ' + str(np.median(gasto)))