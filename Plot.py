import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
from pandas.io.json import json_normalize

class Plot():
    def __init__(self, jsonData):
        self.data = jsonData

    # Exibe o valor gasto por certo estado em um certo ano
    def plot_state_year(self, state, year):

        gasto = str(self.data.allYears[str(year)][state])
        pontos = np.arange(0, int(gasto[0:6]))
        
        plt.title('Valores gastos: ' + state + ' no ano de ' + str(year))
        plt.ylabel('Gastos (Milhões)')
        plt.plot(pontos, 'C1', ms = 6)
        plt.show()
        print('O gasto foi de ' + gasto + ' no ano de ' + str(year))

    # Exibe o valor gasto por todos os estados em todos os anos
    def plot_aState_aYear(self):
        pass

    
    # Exibe o valor médio de crescimento entre dois estados, dentro de um período de tempo
    def verify_mean(self, state, state2, start, end):

        g1 = []
        g2 = []
        for key in range(0, (end - start) + 1):
            g1.append(self.data.allStates[state][str(start + key)])
        for key in range(0, (end - start) + 1):
            g2.append(self.data.allStates[state2][str(start + key)])
        
        plt.title('O crescimento médio dos gastos entre', state, 'e', state2)
        plt.ylabel('Gastos (Bilhões)')
        plt.plot(g1, 'C2', marker = 'o', ms = 6, label = state)
        plt.plot(g2, 'C3', marker = 'o', ms = 6, label = state2)
        plt.legend()
        plt.show()

    def plot_timeline(self, state, start, end):
        gasto = []
        for key in range(0, (end - start) + 1):
            a = self.data.allStates[state][str(start + key)]
            gasto.append(a)

        del a
        anos = np.arange(start, end + 1)
        y = np.arange(0, len(gasto))

        plt.title('Gastos: ' + str(state))
        plt.bar(y, gasto, align='center')
        plt.xticks(y, anos)
        plt.show()
        print('O crescimento médio anual dos gastos neste período de tempo foi: ' + str(np.mean(gasto)))