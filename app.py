import json
import os
from map_reduce.mapper import map_by_year


def main():
    os.system('cd scraper && scrapy crawl alms_spider -o ../government_alms.json')
    file = open('government_alms.json', 'r')
        data = file.read()
        json_data = json.loads(data)
        file.close()

        json_all_years = map_by_year(json_data)

        for year in json_all_years:
            print(year)
            for state in json_all_years[year]:
                print(state.items())

if __name__ == '__main__':
    main()
