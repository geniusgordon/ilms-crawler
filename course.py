#!/usr/bin/env python

import os
import json
import requests
from pyquery import PyQuery
from login import login
from config import config
from util import format_html

def get_course_list(s):
    url = config.get('url', 'home')
    r = s.get(url)
    pq = PyQuery(r.content)
    items = pq('.mnuItem a')
    for i in items:
        c = i.attrib['href'].split('/')
        if len(c) == 3:
            print c[2], i.text

def get_homework_list(s, course):
    url = config.get('url', 'hwlist') % course
    r = s.get(url)
    pq = PyQuery(r.content)
    rows = pq('tr')[1:]
    for row in rows:
        print row.cssselect('td')[4].text_content().strip(), '\t', 
        print row.cssselect('td')[1].text_content().strip()

def get_forum_list(s, course, page=1):
    url = config.get('url', 'forum') % (course, page)
    r = s.get(url)
    pq = PyQuery(r.content)
    rows = pq('tr')[1:]
    for row in rows:
        if len(row.cssselect('td')) > 1:
            print row.cssselect('td')[0].text_content().strip(), '\t', 
            print row.cssselect('td')[1].text_content().strip()
    pages = len(pq('.page span')) - 2
    curr =  pq('.page .curr').text()
    print '%s of %s pages' % (curr, pages)

def get_post_detail(s, post):
    url = config.get('url', 'post')
    data = {'id': post}
    r = s.post(url, data=data)
    print '---'
    for item in json.loads(r.content)['posts']['items']:
        print '(', item['name'], item['date'], ')'
        print format_html(item['note']), '\n'
        if len(item['attach']) != 0:
            print '>> Attachments:'
            for attach in item['attach']:
                print ' ', attach['srcName']
                print ' ', config.get('url', 'attach') % attach['id'], '\n'
        print '---'

