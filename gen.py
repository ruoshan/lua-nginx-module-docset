#!/usr/local/bin/python

import os, re, sqlite3
from bs4 import BeautifulSoup, NavigableString, Tag 

db = sqlite3.connect('./docSet.dsidx')
cur = db.cursor()

try:
    cur.execute('DROP TABLE searchIndex;')
except:
    pass

cur.execute('CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);')
cur.execute('CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);')

docpath = './Documents'

page = open(os.path.join(docpath,'index.html')).read()
soup = BeautifulSoup(page)

mainbody = soup.find('div', {'class': "markdown-body"})
directives = mainbody.find('a', {'id': "user-content-directives"}).parent.find_next_sibling('ul')
ngx_apis = mainbody.find('a', {'id': "user-content-nginx-api-for-lua"}).parent.find_next_sibling('ul')

for a in directives.find_all('a'):
    try:
        name = a.string
        path = "index.html" + a.attrs["href"]
        cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Directive', path))
    except:
        continue

for a in ngx_apis.find_all('a'):
    try:
        name = a.string
        path = "index.html" + a.attrs["href"]
        cur.execute('INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES (?,?,?)', (name, 'Interface', path))
    except:
        continue


db.commit()
db.close()
