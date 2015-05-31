#!/usr/bin/env python

import os
import json
import requests
from pyquery import PyQuery
from login import login
from config import config
from util import format_html, download_attachment

def get_course_list(s):
    url = config.get('url', 'home')
    r = s.get(url)
    pq = PyQuery(r.content)
    items = pq('.mnuItem a')
    for i in items:
        c = i.attrib['href'].split('/')
        if len(c) == 3:
            print c[2], i.text
    print ''

def get_homework_list(s, course):
    url = config.get('url', 'hwlist') % course
    r = s.get(url)
    pq = PyQuery(r.content)
    rows = pq('tr')[1:]
    for row in rows:
        a = row.cssselect('td')[1].cssselect('a')[0]
        print a.attrib['href'].split('=')[-1], '\t',
        print row.cssselect('td')[4].text_content().strip(), '\t',
        print a.text_content().strip()
    print ''

def get_homework_detail(s, course, homework, download=False):
    url = config.get('url', 'hwdetail') % (course, homework)
    r = s.get(url)
    pq = PyQuery(r.content)
    title = pq('.curr').text()
    rows = pq('tr')[1:]
    print title
    print rows[4].cssselect('td')[1].text_content().strip()
    print '---'
    print rows[5].cssselect('td')[1].text_content().strip()
    print ''
    if len(rows[6].cssselect('a')) != 0:
        attachments = []
        print '>>Attachments'
        for a in rows[6].cssselect('a'):
            print ' ', a.attrib['href'].split('=')[-1], '\t',
            print a.text_content().strip()
            attachments.append(a.attrib['href'].split('=')[-1])
    print ''
    if download:
        for attach in attachments:
            download_attachment(s, attach, 'hw_'+homework)
        print ''

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
    if pages > 0:
        print '%s of %s pages' % (curr, pages)
    else:
        print '1 of 1 page'
    print ''

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
    print ''

def get_doc_list(s, course):
    url = config.get('url', 'doclist') % course
    r = s.get(url)
    pq = PyQuery(r.content)
    rows = pq('tr')[1:]
    for row in rows:
        a = row.cssselect('td')[1].cssselect('a')[0]
        print a.attrib['href'].split('=')[-1], '\t',
        print a.text_content().strip()
    print ''


