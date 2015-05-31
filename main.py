#!/usr/bin/env python

import argparse

from login import login
from course import *

def clist(s, args):
    get_course_list(s)

def hwlist(s, args):
    if not args.course:
        get_course_list(s)
        args.course = raw_input('course: ')
    get_homework_list(s, args.course)

def hwdetail(s, args):
    if not args.course:
        get_course_list(s)
        args.course = raw_input('course: ')
    if not args.homework:
        get_homework_list(s, args.course)
        args.homework = raw_input('homework: ')
    get_homework_detail(s, args.course, args.homework, args.download)

def doclist(s, args):
    if not args.course:
        get_course_list(s)
        args.course = raw_input('course: ')
    get_doc_list(s, args.course)

def docdetail(s, args):
    if not args.course:
        get_course_list(s)
        args.course = raw_input('course: ')
    if not args.doc:
        get_doc_list(s, args.course)
        args.doc = raw_input('doc: ')
    get_doc_detail(s, args.course, args.doc, args.download)

def forum(s, args):
    if not args.course:
        get_course_list(s)
        args.course = raw_input('course: ')
    get_forum_list(s, args.course, args.page)

def post(s, args):
    get_post_detail(s, args.post)

parser = argparse.ArgumentParser(description='A nthu ilms command line tool')
subparser = parser.add_subparsers()

p = subparser.add_parser('clist', help='list course')
p.set_defaults(func=clist)

p = subparser.add_parser('hwlist', help='list homeworks')
p.add_argument('-c', '--course', help='course id')
p.set_defaults(func=hwlist)

p = subparser.add_parser('hwdetail', help='show homework detail')
p.add_argument('-c', '--course', help='course id')
p.add_argument('-H', '--homework', help='homework id')
p.add_argument('-d', '--download', action='store_true', help='download homework attackments')
p.set_defaults(func=hwdetail)

p = subparser.add_parser('doclist', help='list documents')
p.add_argument('-c', '--course', help='course id')
p.set_defaults(func=doclist)

p = subparser.add_parser('docdetail', help='show document detail')
p.add_argument('-c', '--course', help='course id')
p.add_argument('-D', '--doc', help='document id')
p.add_argument('-d', '--download', action='store_true', help='download document attackments')
p.set_defaults(func=docdetail)

p = subparser.add_parser('forum', help='show course forum')
p.add_argument('-c', '--course', help='course id')
p.add_argument('-p', '--page', default=1, help='forum page')
p.set_defaults(func=forum)

p = subparser.add_parser('post', help='show post detail')
p.add_argument('-p', '--post', required=True, help='post id')
p.set_defaults(func=post)

args = parser.parse_args()

s = login()
args.func(s, args)


