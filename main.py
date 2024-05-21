from http.server import HTTPServer, SimpleHTTPRequestHandler
from reader import read_and_clean_excel
from generator_html import generate_html_file
import atexit
import os

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

def delete_index_html():
    if os.path.exists('index.html'):
        os.remove('index.html')

if __name__ == '__main__':
    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
    atexit.register(delete_index_html)
    print(f'Server is running at http://{server_address[0]}:{server_address[1]}')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()
