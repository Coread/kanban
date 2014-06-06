from redmine import Redmine
from redmine_settings import server
from datetime import datetime
import pytz

server = Redmine(server['url'], username=server['username'], password=server['password'])


COLUMN_STATE_MAP = {
    'Reviewed': 'col_todo',
    'New': 'col_todo',
    'Closed': 'col_done',
    'Feedback': 'col_done',
    'Verify': 'col_done',
    'Needs Release': 'col_done',
    'In Progress': 'col_inprogress',
    'Duplicate': 'col_done',
    'Rejected': 'col_done',
    }


WEEK_SECONDS = 60 * 60 * 24 * 7


CACHE = {}


def issue(redmine_issue):

    then = redmine_issue.updated_on
    now = datetime.utcnow().replace(tzinfo=pytz.UTC)

    i = {
         'subject': redmine_issue.subject,
         'priority': redmine_issue.priority.name if redmine_issue.priority else 'None',
         'author': redmine_issue.author.name if redmine_issue.author else 'None',
         'assigned_to': redmine_issue.assigned_to.name if redmine_issue.assigned_to else 'None',
         'project': redmine_issue.project.name if redmine_issue.project else 'None',
         'id': redmine_issue.id,
         'status': redmine_issue.status.name if redmine_issue.status else 'None',
    }
    i['col'] = COLUMN_STATE_MAP[i['status']]

    if i['col'] == 'col_done' and (now - then).total_seconds() > WEEK_SECONDS:
        return None

    return i


def get_issues(project_names):
    issues = []
    now = datetime.now()

    for project_name in project_names:
        if project_name in CACHE:
            then, project_issues = CACHE[project_name]
            if (now - then).total_seconds() < 60:
                issues.extend(project_issues)
                print "using cache for {}".format(project_name)
                continue

        project = server.projects.get(project_name)
        project_issues = []
        for i in project.issues(status_id='*'):
            i_data = issue(i)
            if i_data:
                project_issues.append(i_data)

        CACHE[project_name] = (now, project_issues)

        issues.extend(project_issues)

    return issues
