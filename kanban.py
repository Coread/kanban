from bottle import route, run, template, static_file, request, post
from issues import get_issues
import json
from redmine_settings import server, cache_projects
import time
from threading import Thread
OPERATION_MODE = "tracker"


@route('/<name>')
def index(name):
    number_issues = 0

    if OPERATION_MODE == "standalone":
        return template('kanban', name=name, number_issues=number_issues)
    elif OPERATION_MODE == "tracker":
        return template(
            'kanban',
            name=name,
            operation_mode=OPERATION_MODE,
            site_url=server['url']
        )


@post('/issues')
def issues():
    project_names = request.POST.get('project_names')
    project_names = json.loads(project_names)
    issues = get_issues(project_names)
    return json.dumps(issues)


@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='static')


def update_cache():
    try:
        get_issues(cache_projects)
        time.sleep(60)
    except Exception as e:
        print e


cache_thread = Thread(target=update_cache)
cache_thread.daemon = True
cache_thread.start()
run(reloader=True, debug=True, host='0.0.0.0', port=80)
