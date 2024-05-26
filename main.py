from http.server import HTTPServer, SimpleHTTPRequestHandler
from reader import read_and_clean_excel
from generator_html import generate_html_file
from year_suffix import calculate_year_suffix
from collections import defaultdict
import atexit
import os
from datetime import datetime

def get_winery_age(foundation_year):
    current_year = datetime.now().year
    return current_year - foundation_year

def create_wine_html_report(data_file, special_offer, foundation_year):
    products = read_and_clean_excel(data_file)
    wine_categories = defaultdict(list)
    special_offers = set()

    for product in products:
        category = product['Категория']
        wine_categories[category].append(product)
        if product.get('Акция') == special_offer:
            special_offers.add(product['Название'])

    age = get_winery_age(foundation_year)
    year_suffix_age= calculate_year_suffix(age)

    generate_html_file(wine_categories=wine_categories, special_offers=special_offers, age=age, year_suffix=year_suffix_age)


def cleanup():
    if os.path.exists('index.html'):
        os.remove('index.html')


def main():
    data_file = os.getenv('WINE_DATA_FILE', 'xlsx_file/wine3.xlsx')
    special_offer = os.getenv('SPECIAL_OFFER', 'Выгодное предложение')
    foundation_year = int(os.getenv('FOUNDATION_YEAR', 1923))

    create_wine_html_report(data_file, special_offer, foundation_year)

    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    atexit.register(cleanup)
    print(f'Server is running at http://{server_address[0]}:{server_address[1]}')
    httpd.serve_forever()

if __name__ == '__main__':
    main()
