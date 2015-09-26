import os
import sys
import requests
import html2text

from pyquery import PyQuery
from config import config

def format_html(s):
    return html2text.html2text(s)
    # pq = PyQuery(s)
    # r = []
    # for p in pq.contents():
    #     try:
    #         if p.tag != 'br':
    #             r.append(p.text_content())
    #     except:
    #             r.append(p)
    # # for _r in r:
    #     # print _r
    # return '\n'.join(r)

def download_attachment(s, attachment, directory=None):
    url = config.get('url', 'attach') % attachment
    r = s.get(url, stream=True)
    filename = requests.utils.unquote(
            r.headers['content-disposition']).split('\'')[-1]
    size = float(r.headers['content-length'])
    cnt = 1
    path = 'downloads/'
    if directory:
        path = path + directory + '/'
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path+filename, 'w') as f:
        for chunk in r.iter_content(chunk_size=1024):
            f.write(chunk)
            cli_progress(filename, cnt*1024.0/size*100)
            cnt += 1
    print ''

def cli_progress(filename, progress, bar_length=20):
    percent = progress / 100.0
    if percent > 1.0:
        percent = 1.0
    hashes = '#' * int(round(percent * bar_length))
    spaces = ' ' * (bar_length - len(hashes))
    sys.stdout.write('\r%s: [%s] %s%%' % (filename, hashes+spaces, round(percent*100)))
    sys.stdout.flush()

