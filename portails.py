# -*- coding: utf-8 -*-
import re
import mwclient
import json
from mwclient import page

portail = re.compile(u"{{Portail\|[\w|\|| |'|à|ç|é|è|ê|ë|ï|î|û|ù]+}}")
separation = re.compile("{cod{Portail\||}}|\|")
site = mwclient.Site('fr.wikipedia.org')

def portails(string):
    search = portail.search(string)
    if search is not None:
        return separation.split(search.group())
    else:
        print "No portal found"
        return[]

def portailsDe(pages):
    result = {}
    for title in pages:
        if len(title) > 0:
            result[title] = {}
            print title
            page = site.Pages[title.decode('utf-8')]
            result[title]["Portails"] = [i for i in portails(page.text()) if len(i) > 0]
    with open("dump.json", "w") as file:
        data = json.dumps(result, indent=2)
        file.write(data)
    return result

def aPortails():
    with open("input.txt") as file:
        input = file.read()
        sep = re.compile("\n")
        portailsDe(sep.split(input))

print aPortails()
