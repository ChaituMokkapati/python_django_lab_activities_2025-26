from bottle import route, run

@route("/")
def index():
    return "<h1>Hello, World!</h1><p>This is a sample web page built with Bottle Framework.</p>"

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True, reloader=True)
