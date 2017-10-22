# fatec-government-alms
Um Scraper desenvolvido em Python com utilizando Scrapy, Numpy, Pandas e Matplotlib, que busca os gastos com o programa Bolsa Família, com dados de 2004 em diante.

Criado por:
 * Felipe Menino;
 * Lucas Varless.

## Objetivo

Tem o objetivo de coletar os dados de gastos do bolsa família por estado e facilitar a exibição dessas informações

## Configurando ambiente

>Entre no repositório e crie um ambiente virtual com o virtualenv:

```sh
cd fatec-government-alms
virtualenv venv
```

>Ative o ambiente virtual:

```sh
source venv/bin/activate
```

>Instale as dependências:

```sh
pip install -r requiriments.txt
```
## Configurando API

Há plot que será necessrio utilizar a API do Google, então, acesse:
https://developers.google.com/maps/documentation/javascript/get-api-key

Pegue a chave de sua API e insira no arquivo <code>plot.py</code>, para que assim a visualização possa ser feita.

## Executando

>Para executar o script para extração, estruturação e o arquivo com os dados em fortamto *JSON* execute:

```py
python main.py
```

## Utilização - Plots

>Para utilizar os métodos de plot é necessário criar um objeto da classe Plot.
```python
from util.plot import Plot
plt = Plot()
```

>A utilização das classes é bastante simples, veja:

>Para fazer o plot do gráfico de gastos dentro de um período de tempo, em um certo estado, basta utilizar:

```python
plt.plot_timeline('BAHIA', 2004, 2007)
```
![GitHub Logo](/images/plot_timeline.png)

>O plot do gráfico de comparação de gastos entre estados use:
```python
plt.verify_mean('BAHIA', 'RORAIMA', 2004, 2007)
```
![GitHub Logo](/images/plot_verify_mean.png)

>Caso queira gerar os gastos de um único estado, em todos os anos, use:
```python
plt.plot_only_out('SÃO PAULO')
```
![GitHub Logo](/images/plot_only_out.png)

>Se necessário gerar o gasto em um ano específico, use:
```python
plt.plot_state_year('SERGIPE', 2007)
```
![GitHub Logo](/images/plot_state_year.png)

>Se quiser verificar qual a porcentagem de gasto de cada ano de um determinado estado utilize
```python
plt.plot_percent_year('RORAIMA', 2004, 2014)
```
![GitHub Logo](/images/plot_percent_year.png)

>Se necessário exibir todos os dados, e um comparativo de representação entre os estados e seus gastos, use:
```python
plt.plot_total()
```
![GitHub Logo](/images/plot_total.png)

>Por fim, há a possibilidade de exbir um mapa com os pontos dos estados e seus gastos:

```python
plt.plot_map(aux, '2016')
```
![GitHub Logo](/images/mapTotal.png)

OBS: Para usar esta função é necessário adicionar uma chave de API do Google Maps no código <code>plot.py</code>
