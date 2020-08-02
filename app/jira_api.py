from jira import JIRA
from integration.settings_jira import *


def create_new_task_jira(description):
    jira_options = {'server': 'https://daenver.atlassian.net/'}
    jira = JIRA(basic_auth=(JIRA_USERNAME, JIRA_TOKEN), options=jira_options)

    new_task = jira.create_issue(
        fields={
            'project': {'key': 'TI'},
            'issuetype': {
                "name": "Task"
            },
            'summary': description,
            'description': description,
        }
    )

    return new_task
