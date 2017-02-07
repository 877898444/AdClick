#!/usr/bin/env python
# coding=utf-8

import requests
import json
import logging

class Exoclick():
    def __init__(self, username, password, api_token):
        self.username = username
        self.password = password
        self.api_token = api_token
        self.url = "https://api.exoclick.com/v1/login"

    def login(self):
        payload = {
            "username": self.username,
            "password": self.password,
            "api_token": self.api_token
        }
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
        }
        response = requests.request("POST", self.url, data=json.dumps(payload), headers=headers)
        resp = json.loads(response.text)

        self.Authorization = resp['type'] + ' ' + resp['token']

    # TODO: campaign list 同步到数据库
    def campaigns(self):
        url = "https://api.exoclick.com/v1/campaigns"
        headers = {
            'content-type': "application/json",
            'cache-control': "no-cache",
            'Authorization': self.Authorization,
        }
        response = requests.request("GET", url, headers=headers)

        print(response.text)


if __name__ == "__main__":
    username = "jetmobo"
    password = "Ihave2cars$"
    api_token = "b76374416f5db01c5ddeeef59f2aa42756d3b58e"
    exoclick = Exoclick(username, password, api_token)
    exoclick.login()
    exoclick.campaigns()
