#!/usr/bin/env python
# coding=utf-8
import json

import requests
import logging

from bs4 import BeautifulSoup
from adclick.utils.db_util import db



class Popads():
    def __init__(self, token):
        self.token = token

    def user_status(self):
        url = "https://www.popads.net/api/user_status"

        querystring = {"key": self.token}

        response = requests.request("GET", url, params=querystring)
        print(response.text)

    # TODO: campaign_list 同步到数据库
    def campaign_list(self):
        url = "https://www.popads.net/api/campaign_list"

        querystring = {"key": self.token}
        response = requests.request("GET", url, params=querystring)
        print(response.text)

        json_info = json.loads(response.text)
        for content in json_info['campaigns']:
            db.insertdata(content)

    def campaign_start(self, campaign_id):
        url = "https://www.popads.net/api/campaign_start"

        querystring = {"key": self.token, "campaign_id": campaign_id}

        response = requests.request("POST", url, params=querystring)

        print(response.text)

    def campaign_pause(self, campaign_id):
        url = "https://www.popads.net/api/campaign_pause"
        querystring = {"key": self.token, "campaign_id": campaign_id}
        response = requests.request("POST", url, params=querystring)

        print(response.text)

    def campaign_top_up(self, campaign_id, amount):
        url = "https://www.popads.net/api/campaign_top_up"

        querystring = {"key": self.token,
                       "campaign_id": campaign_id,
                       "amount": amount,
                       }
        response = requests.request("POST", url, params=querystring)

        print(response.text)

    def campaign_empty_budget(self, campaign_id, amount):
        url = 'https://www.popads.net/api/campaign_empty_budget'
        querystring = {
            "key": self.token,
            "campaign_id": campaign_id,
            "amount": amount,
        }
        response = requests.request("POST", url, params=querystring)

        print(response.text)

    def report_advertiser(self):
        url = 'https://www.popads.net/api/report_advertiser'
        querystring = {
            "key": self.token,
            "quick": "last_month",
            # "groups": "country,datetime:day"
            "groups": "campaign,website,datetime:day"
            #"groups": "campaign,website,datetime:day"
            # "groups": "campaign,datetime:day"
            #"groups": "website,datetime:day"
            # "groups": "country，campaign,datetime:day"
        }

        response = requests.request("POST", url, params=querystring)

        # print response
        # print '-'*30
        # print(response.text)
        # print '-' * 30
        json_info = json.loads(response.text)
        print json_info
        db.insertdata(json_info,'popads')
        # db.inserttoreprote(json_info)
        # for content in json_info:
        #     db.insertdata(content)

    def report_publisher(self):
        url = 'https://www.popads.net/api/report_publisher'
        querystring = {
            "key": self.token,
        }

        response = requests.request("POST", url, params=querystring)

        print(response.text)


if __name__ == "__main__":
    key = "5abaf88d3b905ec8226ee45b4a5d8e43cef466f9"
    popads = Popads(key)
    # popads.user_status()
    # popads.campaign_list()
    popads.report_advertiser()
