#!/usr/bin/python3
from github.client import GithubClient
from repo.parser_v2 import RepoParser2
from repo.bad_ocp_reports_generator import ReportsGenerator


if __name__ == '__main__':
    username = 'rafaelcamarda'
    response = GithubClient.get_repos_by_user(username)

    if response['status_code'] == 200:
        repos = RepoParser2.parse(response['body'])
        report = ReportsGenerator.build("MARKDOWN", repos)
        print(report)
    else:
        print(response['body'])
