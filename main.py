import argparse
import atexit
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from reader import read_and_clean_excel
from generator_html import generate_html_file

def prepare_data(data_file):
    products = read_and_clean_excel(data_file)
    special_offers = {product['Название'] for product in products if product.get('Акция') == 'Выгодное предложение'}
    wines_dict = {product['Категория']: [] for product in products}
    
    for product in products:
        wines_dict[product['Категория']].append(product)
    
    return wines_dict, special_offers

def generate_and_serve(data_file, handler):
    wines_dict, special_offers = prepare_data(data_file)
    generate_html_file(wines_dict=wines_dict, special_offers=special_offers, age=10, year_suffix='лет')
    handler()

def custom_handler(data_file):
    def handler(*args):
        generate_and_serve(data_file, lambda: SimpleHTTPRequestHandler(*args))
    return handler

def delete_index_html():
    if os.path.exists('index.html'):
        os.remove('index.html')

def run_server(data_file):
    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, custom_handler(data_file))
    atexit.register(delete_index_html)
    print(f'Server is running at http://{server_address[0]}:{server_address[1]}')
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run the wine shop server.')
    parser.add_argument('--data-file', type=str, default='xlsx_file/wine3.xlsx')
    args = parser.parse_args()
    run_server(args.data_file)
