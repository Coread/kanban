from bottle import route, run, template, static_file

@route('/<name>')
def index(name):
    number_issues = 0
    return template('kanban', name=name, number_issues=number_issues)

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static')

run(reloader=True, host='localhost', port=80)