from bottle import route, run, template, static_file, request, post
from issues import get_issues
import json

OPERATION_MODE = "tracker"

@route('/<name>')
def index(name):
    number_issues = 0
    
    if OPERATION_MODE == "standalone":
        return template('kanban', name=name, number_issues=number_issues)
    elif OPERATION_MODE == "tracker":
        
        issues = get_issues([name])
        
        return template('kanban', name=name, issues=issues, number_issues=len(issues), operation_mode=OPERATION_MODE)

@post('/issues')
def issues():
    project_name = request.POST.get('project_name')
    issues = get_issues([project_name])
    return json.dumps(issues)

@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static')

run(reloader=True, debug=True, host='localhost', port=80)