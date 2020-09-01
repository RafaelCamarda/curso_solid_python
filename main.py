from github.client import GithubCliient
from repo.parser import RepoParser
from repo.reports_generator import ReportsGenerator
from repo.reports.html_generator import HTMLGenerator
from repo.reports.markdown_generator import MarkdownGenerator
from repo.reports.writer import ReportWriter

from models.member import Member
from models.manager import Manager

if __name__ == '__main__':
    username = 'rafaelcamarda'
    response = GithubCliient.get_repos_by_user(username)

    if response['status_code'] == 200:
        repos = RepoParser.parse(response['body'])
        markdown_report = ReportsGenerator.build(MarkdownGenerator, repos)
        html_report = ReportsGenerator.build(HTMLGenerator, repos)
        ReportWriter.write(markdown_report)

        print(html_report)
        print(markdown_report)
    else:
        print(response['body'])

    member = Member('rafaelcamarda', 'rafael@test.com')
    manager = Manager('manager', 'manager@test.com')

    print(member.members())

    print(member.work())
    print(manager.work())
