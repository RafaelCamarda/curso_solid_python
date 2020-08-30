#!/usr/bin/python3
from github.client import GithubClient

from repo.parser_v2 import RepoParser
from repo.reports_generator import ReportsGenerator
from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MarkdownGenerator

from models.member import Member
from models.manager import Manager


if __name__ == '__main__':
    username = 'rafaelcamarda'
    response = GithubClient.get_repos_by_user(username)

    if response['status_code'] == 200:
        repos = RepoParser.parse(response['body'])
        report = ReportsGenerator.build(MarkdownGenerator, repos)
        print(report)
    else:
        print(response['body'])

    member = Member('rafaelcamarda', 'rafael@test.com')
    print(member.members())
    manager = Manager('rafaelcamarda', 'rafael@test.com')
    print(manager.members())
