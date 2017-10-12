# fatec-government-alms
Um Scraper desenvolvido em Python com utilizando Scrapy, Numpy, Pandas e Matplotlib, que busca os gastos com o programa Bolsa Família, com dados de 2004 em diante.

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
pip install -r requirements.txt
```

## Executando

>Para executar o script para extração, estruturação e o arquivo com os dados em fortamto *JSON* execute:

```py
python main.py
```



## Utilização - Plots

Para utilizar os métodos de plot é necessário criar um objeto da classe Plot.
```python
from util.plot import Plot
plt = Plot()
```

A utilização das classes é bastante simples, veja:

Para fazer o plot do gráfico de gastos dentro de um período de tempo, em um certo estado, basta utilizar:

```python
plt.plot_timeline('BAHIA', 2004, 2007)
```
![GitHub Logo](/images/plot_timeline.png)

O plot do gráfico de comparação de gastos entre estados use:
```python
plt.verify_mean('BAHIA', 'ESPIRITO SANTO', 2004, 2007)
```
![GitHub Logo](/images/plot_verify_mean.png)

Caso queira gerar os gastos de um único estado, em todos os anos, use:
```python
plt.plot_only_out('SÃO PAULO')
```
![GitHub Logo](/images/plot_only_out.png)

Se necessário gerar o gasto em um ano específico, use:
```python
plt.plot_state_year('SERGIPE', 2007)
```
![GitHub Logo](/images/plot_state_year.png)


Por fim se necessário exibir todos os dados, e um comparativo de representação entre os estados e seus gastos, use:
```python
plt.plot_total()
```
![GitHub Logo](/images/plot_total.png)
