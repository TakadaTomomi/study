from bottle import route, run, template
from datetime import datetime

@route('/hello')
def hello():
    now = datetime.now()
    return template('hello_template', now=now)

run(host='localhost', port=8880, debug=True)