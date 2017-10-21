import numpy as np
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
from bokeh.io import output_file, output_notebook, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, LogColorMapper, BasicTicker, ColorBar,
    DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)
from bokeh.models.mappers import ColorMapper, LinearColorMapper
from bokeh.palettes import Viridis5

class Plot():
    def __init__(self, jsonData):
        self.data = jsonData
        self.anos = self.data.allYears.dropna().keys()
        self.nomes = self.data.allStates.dropna().keys()

    # Pega os valores gastos de determinado ano em todos os estados
    def __appendData(self, ano):
        nomes = ['ACRE', 'ALAGOAS', 'AMAPÁ', 'AMAZONAS', 'BAHIA', 'CEARÁ',
           'DISTRITO FEDERAL', 'ESPÍRITO SANTO', 'GOIÁS', 'MARANHÃO',
           'MATO GROSSO', 'MATO GROSSO DO SUL', 'MINAS GERAIS', 'PARANÁ',
           'PARAÍBA', 'PARÁ', 'PERNAMBUCO', 'PIAUÍ', 'RIO DE JANEIRO',
           'RIO GRANDE DO NORTE', 'RIO GRANDE DO SUL', 'RONDÔNIA', 'RORAIMA',
           'SANTA CATARINA', 'SERGIPE', 'SÃO PAULO', 'TOCANTINS']
        gasto = []
        for i in range(0, len(self.data['allStates'][14:])):
            gasto.append(self.data['allStates'][nomes[i]][str(ano)] / 10000000)
        return gasto

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

    def plot_map(self, estados, ano):
        lati = []
        long = []
        for i in range(0, len(estados)):
            lati.append(estados['Latitude'][i])
            long.append( estados['Longitude'][i])
        vinculo = self.__appendData(ano)
        map_options = GMapOptions(lat=-16.1610697, lng=-59.8988937, map_type="roadmap", zoom=5)
        plot = GMapPlot(
            x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options
        )
        plot.title.text="Mapa de gastos do Brasil de " + ano
        # Para pegar uma chave acesse:
        # https://developers.google.com/maps/documentation/javascript/get-api-key
        plot.api_key="API GOOGLE"

        source = ColumnDataSource(
        data=dict(
            lat=lati,
            lon=long,
            size=vinculo,
            color=vinculo
            )
        )
        color_mapper = LinearColorMapper(palette=Viridis5)
        circle = Circle(x="lon", y="lat", size="size", fill_color={'field': 'color', 'transform': color_mapper}, fill_alpha=0.4, line_color=None)
        plot.add_glyph(source, circle)
        color_bar = ColorBar(color_mapper=color_mapper, ticker=BasicTicker(),
                             label_standoff=12, border_line_color=None, location=(0,0))
        plot.add_layout(color_bar, 'right')
        plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
        output_notebook()

        show(plot)
