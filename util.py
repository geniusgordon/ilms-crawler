from pyquery import PyQuery

def format_html(s):
    pq = PyQuery(s)
    r = []
    for p in pq.contents():
        try:
            if p.tag != 'br':
                r.append(p.text_content())
        except:
            r.append(p)
    # for _r in r:
        # print _r
    return '\n'.join(r)

