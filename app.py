import json
import os
from mapper import *
from menu import *


def main():
    os.system('cd scraper && scrapy crawl alms_spider -o ../government_alms.json')
    file = open('government_alms.json', 'r')
    data = file.read()
    json_data = json.loads(data)
    file.close()
    os.system('rm -rf government_alms.json')

    api = {
        "allYears": map_by_year(json_data),
        "allStates": map_by_state(json_data)
    }

    api_data = json.dumps(api)
    file = open('api.json', 'w')
    file.write(api_data)
    file.close()

    """
    Ao executar o script app.py, será gerado os dados referentes ao total de gastos
    por ano e por estado no arquivo api.json. Os dados sobre os municípios ainda não
    está implementado, mas os gráficos já ser gerados com os dados carregados no dicionário
    json_data abaixo.
    Segue abaixo um exemplo da estrutura gerada no arquivo api.json:

    {
    "allYears": {
      "2004": {
        "ACRE": 27226375,
        "ALAGOAS": 189508653,
        "AMAPÁ": 14265182,
        "AMAZONAS": 94222154,
        "BAHIA": 773454801,
        "CEARÁ": 566840981,
        "DISTRITO FEDERAL": 15607260,
        "ESPÍRITO SANTO": 81890933,
        "GOIÁS": 102114665,
        "MARANHÃO": 380306559,
        "MATO GROSSO": 55566882,
        "MATO GROSSO DO SUL": 41301670,
        "MINAS GERAIS": 578283626,
        "PARÁ": 243308958,
        "PARAÍBA": 244271199,
        "PARANÁ": 223411130,
        "PERNAMBUCO": 433972608,
        "PIAUÍ": 225632494,
        "RIO DE JANEIRO": 154106640,
        "RIO GRANDE DO NORTE": 174037874,
        "RIO GRANDE DO SUL": 211686201,
        "RONDÔNIA": 35180214,
        "RORAIMA": 11306147,
        "SANTA CATARINA": 83187027,
        "SÃO PAULO": 424645928,
        "SERGIPE": 96125511,
        "TOCANTINS": 51796265
      },
      ...
    },
    "allStates": {
      "ACRE": {
        "2004": 27226375,
        "2007": 48500926,
        "2006": 43525797,
        "2005": 33317415,
        "2008": 61903935,
        "2009": 70482395,
        "2010": 77713856,
        "2011": 88720220,
        "2012": 121943068,
        "2013": 176948772,
        "2014": 211943516,
        "2015": 223457560,
        "2016": 247542449,
        "2017": 151521226
      },
      ...
    }
  }

  Por motivos de organização os métodos de geração de gráficos podem ser implementados no arquivo plot.py 
  """
    menu(json.loads(api_data))

if __name__ == '__main__':
    main()
