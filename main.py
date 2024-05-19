from http.server import HTTPServer, SimpleHTTPRequestHandler
from reader import read_and_clean_excel
from generator_html import generate_html_file

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        products = read_and_clean_excel('xlsx_file/wine3.xlsx')
        wines_dict = {}
        special_offers = set()
        
        for product in products:
            category = product['Категория']
            if category in wines_dict:
                wines_dict[category].append(product)
            else:
                wines_dict[category] = [product]
            if product.get('Акция') == 'Выгодное предложение':
                special_offers.add(product['Название'])
        
        generate_html_file(wines_dict=wines_dict, special_offers=special_offers, age=10, year_suffix='лет')
        super().do_GET()

if __name__ == '__main__':
    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
    print(f'http://{server_address[0]}:{server_address[1]}')
    httpd.serve_forever()
