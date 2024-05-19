from http.server import HTTPServer, SimpleHTTPRequestHandler
from reader import read_excel_file
from generator_html import generate_html

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        products = read_excel_file('wine2 (2).xlsx')
        wines_dict = {}
        for product in products:
            category = product['Категория']
            if category in wines_dict:
                wines_dict[category].append(product)
            else:
                wines_dict[category] = [product]
        generate_html(wines_dict, age=10, year_suffix='лет')
        super().do_GET()

if __name__ == '__main__':
    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, CustomHTTPRequestHandler)
    print('Server is ready')
    httpd.serve_forever()
