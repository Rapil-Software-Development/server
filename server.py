###############SERVER########################################
from http.server import BaseHTTPRequestHandler, HTTPServer

import pymysql.cursors

html = "<html><body>Hello</body></html>"

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_error(404, "Page Not Found {}".format(self.path))

def server_thread(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, ServerHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


###Підключення до бази даних#####

connection = pymysql.connect(host='yuzer.zzz.com.ua',
                             user='Yuz123',
                             password='Yura12345',
                             db='yuz3',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print("connected to the database!!")

if __name__ == '__main__':
    port = 8000
    print("Starting server at port %d" % port)
    server_thread(port)