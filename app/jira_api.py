from jira import JIRA
from integration.settings_jira import *


def create_new_task_jira(description):
    jira_options = {'server': 'https://daenver.atlassian.net/'}
    jira = JIRA(basic_auth=(JIRA_USERNAME, JIRA_TOKEN), options=jira_options)

    # all_issues = jira.search_issues(
    #     "project=TI",
    #     startAt=0,
    #     maxResults=1000,
    #     validate_query=True,
    # )

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


# if __name__ == '__main__':
#     name = 'New task for test'
#     create_new_task(description=name)
