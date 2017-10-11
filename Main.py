import json
import os
from Mapper import Mapper

class Main():
    def main(self):
        mapper = Mapper()
        file_name = 'government_alms.json'

        os.system('cd scraper && scrapy crawl alms_spider -o ../' + file_name)
        file = open(file_name, 'r')
        print('\n\nOpen', file_name, 'file...')
        data = file.read()
        print('Reading', file_name, 'file...')
        jsonData = json.loads(data)
        file.close()
        print('Loading objects from', file_name, 'file...')
        print('Close and remove', file_name, 'file...')
        os.remove('government_alms.json')
        api = {
        "allYears": mapper.map_by_year(jsonData),
        "allStates": mapper.map_by_state(jsonData)
        }
        file_name = 'api.json'
        print('\nGenerating', file_name, 'file...')
        api_data = json.dumps(api)
        file = open(file_name, 'w')
        file.write(api_data)
        file.close()
        print(file_name, 'file ready for review!')

if __name__ == '__main__':
    m = Main()
    m.main()