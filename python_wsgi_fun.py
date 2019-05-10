# python 3 wsgi fun

from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server

def simple_app(environ, start_response):
    setup_testing_defaults(environ)

    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    ret = [("%s: %s\n" % (key, value)).encode("utf-8")
           for key, value in environ.items()]

#    l = int(environ.get('CONTENT_LENGTH')) if environ.get('CONTENT_LENGTH') else 0
#    body = environ['wsgi.input'].read(l) if l > 0 else ''

    return ret

with make_server('', 8000, simple_app) as httpd:
    print("Serving on port 8000...")
    httpd.serve_forever()

