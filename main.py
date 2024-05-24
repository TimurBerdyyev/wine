from http.server import HTTPServer, SimpleHTTPRequestHandler
from reader import read_and_clean_excel
from generator_html import generate_html_file
import atexit
import os

def setup_wine_data():
    products = read_and_clean_excel('xlsx_file/wine3.xlsx')
    wines_dict = {}
    special_offers = set()
    
    for product in products:
        category = product['Категория']
        if category not in wines_dict:
            wines_dict[category] = []
        wines_dict[category].append(product)
        if product.get('Акция') == 'Выгодное предложение':
            special_offers.add(product['Название'])
    
    generate_html_file(wines_dict=wines_dict, special_offers=special_offers, age=10, year_suffix='лет')

def cleanup():
    if os.path.exists('index.html'):
        os.remove('index.html')

def main():
    setup_wine_data()
    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    atexit.register(cleanup)
    print(f'Server is running at http://{server_address[0]}:{server_address[1]}')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()

if __name__ == '__main__':
    main()