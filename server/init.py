import wsgiref.simple_server

def application(env, startResponse):
    response = b"Test"

    status= "200 OK"

    headers = [("Content-Type","text/html")]

    startResponse(status,headers)

    return [response]
            
if __name__ == "__main__":
    ws = wsgiref.simple_server.make_server(
        host="localhost",
        port=8021,
        app=application
    )

    ws.serve_forever()