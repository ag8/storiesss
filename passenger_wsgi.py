import os
import sys


sys.path.insert(0, os.path.dirname(__file__))


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    message = '<!DOCTYPE html><html><head><title>Python test</title></head><body>'
    version = 'How are you doing? I\'m running python %s\n' % sys.version.split()[0]
    response = ''.join([message, "<p>", version, "</p></body></html>"])
    return [response.encode()]
