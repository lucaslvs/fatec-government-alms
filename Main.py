import json
import os
from Mapper import Mapper
from Menu import Menu

class Main():
    def main(self):
        mapper = Mapper()
        menu = Menu()

        os.system('cd scraper && scrapy crawl alms_spider -o ../government_alms.json')
        file = open('government_alms.json', 'r')
        data = file.read()
        jsonData = json.loads(data)
        file.close()
        os.remove('government_alms.json')

        api = {
        "allYears": mapper.map_by_year(jsonData),
        "allStates": mapper.map_by_state(jsonData)
        }

        api_data = json.dumps(api)
        file = open('api.json', 'w')
        file.write(api_data)
        file.close()
        menu.showMenu(jsonData)

if __name__ == '__main__':
    m = Main()
    m.main()