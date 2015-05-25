#!/usr/bin/env python

import argparse

from login import login
from course import *

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--list', help='list courses', action='store_true')
parser.add_argument('-c', '--course', help='course id')
parser.add_argument('-H', '--homework', help='show course homework', action='store_true')
parser.add_argument('-f', '--forum', help='show course forum', action='store_true')
parser.add_argument('-P', '--page', help='forum page')
parser.add_argument('-p', '--post', help='show post detail')
args = parser.parse_args()

s = login()

if args.list:
    get_course_list(s)

if args.homework:
    if not args.course:
        get_course_list(s)
        args.course = raw_input('course: ')
    get_homework_list(s, args.course)

if args.forum:
    if not args.course:
        get_course_list(s)
        args.course = raw_input('course: ')
    if not args.page:
        args.page = 1
    get_forum_list(s, args.course, args.page)

if args.post:
    get_post_detail(s, args.post)

