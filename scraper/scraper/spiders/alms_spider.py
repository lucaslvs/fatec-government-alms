import scrapy
import datetime


class AlmsSpider(scrapy.Spider):
    name = 'alms_spider'
    start_urls = []
    url_base = 'http://www.portaldatransparencia.gov.br/PortalTransparenciaPesquisaAcaoUF.asp?codigoAcao=006O&codigoFuncao=08&NomeAcao=Transfer%EAncia+de+Renda+Diretamente+%E0s+Fam%EDlias+em+Condi%E7%E3o+de+Pobreza+e+Extrema+Pobreza+%28Lei+n%BA+10%2E836%2C+de+2004%29&Exercicio='
    url_code = ['006O&', '8442&']
    url_page = '&Pagina='
    actual_year = datetime.date.today().year

    for year in range(2004, actual_year + 1):
        for page in range(1, 3):
            if(year <= 2007):
                start_urls.append(
                    url_base[0:89] + url_code[0] + url_base[94:] + str(year) + url_page + str(page))
            else:
                start_urls.append(
                    url_base[0:89] + url_code[1] + url_base[94:] + str(year) + url_page + str(page))

    def parse(self, response):
        year = s = int(response.xpath('//b/text()').extract_first())
        all_states = response.css('tr td.firstChild ::text').extract()
        all_values = response.css('tr td.colunaValor ::text').extract()
        for s in range(6):
            all_states.remove(all_states[0])
        for v in range(2):
            all_values.remove(all_values[0])
        for line in range(len(all_states)):
            yield {
                'year': year,
                'state': all_states[line],
                'value': int(all_values[line].replace(".", "").replace(",", ".").strip()[:-3])
            }
