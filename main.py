from http.server import HTTPServer, SimpleHTTPRequestHandler
from generator_html import generate_html


class CustomHTTPReqestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        generate_html()
        super().do_GET()


if __name__ == '__main__':
    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, CustomHTTPReqestHandler)
    print('порт готов')
    httpd.serve_forever()