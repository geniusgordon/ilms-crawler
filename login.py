#!/usr/bin/env python

import os
import json
import pickle
import requests

from config import config

def get_user():
    user = config.items('user')
    return (user[0][1], user[1][1])

def login():
    user = get_user()
    url = config.get('url', 'login')
    s = load_session()
    if not s:
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

def load_session():
    filename = config.get('session', 'filename')
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return pickle.load(f)
    return None

def save_session(s):
    filename = config.get('session', 'filename')
    with open(filename, 'w') as f:
        pickle.dump(s, f)

if __name__ == '__main__':
    s = login()
    save_session(s)

