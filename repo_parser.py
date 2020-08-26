from repo import Repo


class RepoParser():
    @classmethod
    def parse(cls, response):
        for i in range(len(response)):
            repo = response[i]
            repo = Repo(repo["id"], repo["name"], repo["stargazers_count"])
            print(repo)
