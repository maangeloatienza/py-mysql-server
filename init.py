import wsgiref.simple_server
import json
from server.controllers.userController import index

def application(environ, start_response):
    path    = environ['PATH_INFO']
    method  = environ['REQUEST_METHOD']
    content_type = "application/json; charset=utf-8"
    response = dict()
    status="200 OK"

    if path == '/users':
        if method == 'POST':
            pass
        elif method == 'PUT':
            pass
        elif method == 'DELETE':
            pass
        else:
            content_type = "application/json"
            users = index()
            status = "200 OK" if len(users) else "401 OK"
            response = json.dumps(users).encode('utf-8')
            
    headers = [
        ("Content-Type",content_type),
        ("Content-Length",str(len(response)))
    ]

    start_response(status,headers)

    return [response]
            
if __name__ == "__main__":
    ws = wsgiref.simple_server.make_server(
        host="localhost",
        port=8021,
        app=application
    )

    ws.serve_forever()