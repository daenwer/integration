import requests
import json
from integration.settings_github import *


def get_repos(*args, **kwargs):
    repo = args[0]
    last_commit = requests.get(f'https://api.github.com/repos/daenwer/{repo}/commits/master')
    last_commit_json = json.loads(last_commit.text)
    name = last_commit_json.get('commit').get('author').get('name')
    files = ""
    for file in last_commit_json.get('files'):
        files = files + file.get('filename') + ', '
    files = files.rstrip()
    return {'name': name, 'files': files}


def github_eval(command, message):
    return eval(f'{command}("{message}")')
