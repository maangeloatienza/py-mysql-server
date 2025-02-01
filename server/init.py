import wsgiref.simple_server
from server.controllers.userController import index

def application(environ, startResponse):
    path    = environ['PATH_INFO']
    method  = environ['REQUEST_METHOD']
    content_type = "application/json"
    response = dict()
    
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
            response = users
            
    headers = [
        ("Content-Type",content_type),
        ("Content-Length",str(len(response)))
    ]

    startResponse(status,headers)

    return [response]
            
if __name__ == "__main__":
    ws = wsgiref.simple_server.make_server(
        host="localhost",
        port=8021,
        app=application
    )

    ws.serve_forever()