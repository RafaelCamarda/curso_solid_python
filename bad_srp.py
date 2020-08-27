import requests
import json


class ListRepositories():

    API_BASE_URL = 'https://api.github.com'

    def __init__(self, user):
        self._user = user

    def get_repos_by_user(self):
        response = requests.get(
            f'{self.API_BASE_URL}/users/{self._user}/repos')
        if response.status_code == 200:
            return {"status_code": 200, "body": response.json()}
        else:
            return {"status_code": response.status_code, "body": "Error while getting repos"}

    def parse_response(self):
        response = self.get_repos_by_user()
        body = response["body"]
        if response['status_code'] == 200:
            for i in range(len(body)):
                print(
                    f'{body[i]["id"]} {body[i]["name"]} {body[i]["stargazers_count"]}')
        else:
            print(body)


repos = ListRepositories('rafaelcamarda')
repos.parse_response()
