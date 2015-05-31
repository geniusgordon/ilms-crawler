#!/usr/bin/env python

import os
import json
import requests
import sys

from config import config

def get_user():
    user = config.items('user')
    return (user[0][1], user[1][1])

def login():
    user = get_user()
    url = config.get('url', 'login')
    s = requests.Session()
    r = s.post(url, data={'account': user[0], 'password': user[1]})
    try:
        if json.loads(r.text)['ret']['status'] == 'false':
            raise
        print "Logged in...\n"
        return s
    except:
        print 'Login Failure...'
	exit(1)

if __name__ == '__main__':
    login()

