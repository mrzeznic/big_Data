from bottle import Bottle, run, error

app = Bottle()

@app.route('/hello')
def hello():
    return "Hello World! This is your firts webpage"
@error(404)
def error404(error):
    return "Nothing here,sorry"

run(app, host='localhost', port=8080)
