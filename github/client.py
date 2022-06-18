import requests
import json


class GithubCliient():

    API_BASE_URL = 'https://api.github.com'

    @classmethod
    def get_repos_by_user(self, user):
        response = requests.get(
            f'{self.API_BASE_URL}/users/{user}/repos')
        return {"status_code": response.status_code,
                "body": response.json() if response.status_code == 200 else "Error while getting repos"}
