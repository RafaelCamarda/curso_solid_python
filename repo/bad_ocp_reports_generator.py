from .reports.html_generator import HTMLGenerator
from .reports.markdown_generator import MarkdownGenerator


class ReportsGenerator():
    @classmethod
    def build(cls, type, repos):
        if type == "HTML":
            return HTMLGenerator.build(repos)
        elif type == "MARKDOWN":
            return MarkdownGenerator.build(repos)
        else:
            cls.__print_repos(repos)

    @staticmethod
    def __print_repos(repos):
        for repo in repos:
            print(repo)
