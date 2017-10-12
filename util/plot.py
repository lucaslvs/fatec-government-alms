import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()

class Plot():
    def __init__(self, jsonData):
        self.data = jsonData
        self.anos = self.data.allYears.dropna().keys()
        self.nomes = self.data.allStates.dropna().keys()

    # Exibe o valor gasto por certo estado em um certo ano
    def plot_state_year(self, state, year):

        gasto = str(self.data.allYears[str(year)][state])
        pontos = np.arange(0, int(gasto[0:6]))

        plt.rcParams['font.size'] = 7.0
        plt.title('Valores gastos: ' + state + ' no ano de ' + str(year))
        plt.ylabel('Gastos (Milhões)')
        plt.plot(pontos, 'C1', ms = 6)
        plt.show()
        print('O gasto foi de ' + gasto + ' no ano de ' + str(year))

    # Exibe o gasto individual de certo estado em todos os anos
    def plot_only_out(self, state):

        g1 = []
        for i in range(0, len(self.anos)):
            g1.append(self.data.allStates[state][self.anos[i]])

        plt.figure(1, figsize=(6,6))
        plt.rcParams['font.size'] = 7.0
        plt.title('Crescimento de gastos individual')
        scat_plot = plt.scatter(g1[:-1], self.anos[:-1], alpha = 1.0, c = self.anos[:-1], label = state)
        plt.ylabel('Anos (Intervalo de 2 anos)')
        plt.xlabel('Gastos (Milhões) - Dividido por 100000 para facilitar a visualização')
        plt.xticks(g1[::2])
        plt.legend()
        plt.show()
        print('Quantidade de valores gastos com os favorecidos no estado de ' + state + ' no período de 2004 a 2017')

    # Exibe o valor médio de crescimento entre dois estados, dentro de um período de tempo
    def verify_mean(self, state, state2, start, end):

        g1 = []
        g2 = []

        for key in range(0, (end - start) + 1):
            g1.append(self.data.allStates[state][str(start + key)])
            g2.append(self.data.allStates[state2][str(start + key)])

        anos = np.arange(start, end + 1)
        y = np.arange(0, len(g1))

        plt.figure(1, figsize=(6,6))
        plt.rcParams['font.size'] = 7.0
        plt.title('Comparação entre o crescimento dos gastos de ' + state + ' e ' + state2)
        plt.ylabel('Gastos (Milhões)')
        plt.plot(g1, 'C2', marker = 'o', ms = 6, label = state)
        plt.plot(g2, 'C3', marker = 'o', ms = 6, label = state2)
        plt.xticks(y, anos)
        plt.legend()
        plt.show()


    def plot_percent_year(self, state, start, end):
        g1 = []

        for key in range(0, (end - start) + 1):
            g1.append(self.data.allStates[state][str(start + key)])

        anos = np.arange(start, end + 1)

        plt.figure(1, figsize=(8,8))
        plt.rcParams['font.size'] = 6.0
        plt.title('Representação dos gastos nos anos entre ' + str(start) + ' e ' + str(end) + ' em ' + state)
        plt.axis('equal')
        plt.pie(g1, labels = anos, autopct = "%1.1f%%")
        plt.show()
        

    def plot_timeline(self, state, start, end):
        gasto = []
        for key in range(0, (end - start) + 1):
            a = self.data.allStates[state][str(start + key)]
            gasto.append(a)

        del a
        anos = np.arange(start, end + 1)
        y = np.arange(0, len(gasto))

        plt.figure(1, figsize=(6,6))
        plt.rcParams['font.size'] = 7.0
        plt.title('Gastos: ' + str(state))
        plt.bar(y, gasto, align='center')
        plt.xticks(y, anos)
        plt.show()
        print('O crescimento médio anual dos gastos neste período de tempo foi: ' + str(np.mean(gasto)))

    def plot_total(self):

        tmp = 0
        gt = []
        for i in range(0, len(self.nomes)):
            for j in range(0, len(self.anos)):
               tmp += float(self.data.allStates[self.nomes[i]][self.anos[j]])

            gt.append(tmp)
            tmp = 0

        plt.figure(1, figsize=(10,10))
        plt.rcParams['font.size'] = 6.0
        plt.title('Representatividade dos gastos de todos os estados de 2004 a 2017')
        plt.axis('equal')
        plt.pie(gt, labels = self.nomes, autopct = "%1.1f%%")
        plt.show()
