# !/usr/bin/env python
# coding=utf-8

from adclick.lib import Exoclick
from adclick.lib import Popads


if __name__ == "__main__":
    username = "jetmobo"
    password = "Ihave2cars$"
    api_token = "b76374416f5db01c5ddeeef59f2aa42756d3b58e"
    exoclick = Exoclick(username, password, api_token)
    exoclick.login()
    exoclick.campaigns()