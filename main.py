#!/usr/bin/python3
from github_client import GithubClient
from repo_parser import RepoParser


if __name__ == '__main__':
    username = 'rafaelcamarda'
    response = GithubClient.get_repos_by_user(username)

    if response['status_code'] == 200:
        RepoParser.parse(response['body'])
    else:
        print(response['body'])
