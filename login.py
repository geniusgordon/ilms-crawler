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
            save_session(s)
            print "Logged in...\n"
        except:
            print 'Login Failure...\n'
            exit(1)
    return s

def load_session():
    filename = config.get('session', 'filename')
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            print 'Load session...\n'
            return pickle.load(f)
    return None

def save_session(s):
    filename = config.get('session', 'filename')
    with open(filename, 'w') as f:
        pickle.dump(s, f)

if __name__ == '__main__':
    s = login()
    save_session(s)

