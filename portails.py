# -*- coding: utf-8 -*-
import re
import mwclient
from mwclient import page

portail = re.compile("{{Portail[\w|\|| |'|à|ç|é|è|ê|ë|ï|î|û|ù]+}}")
separation = re.compile("{{Portail\||}}|\|")
site = mwclient.Site('fr.wikipedia.org')

pagesTitles = ["Nicole Abar", "Juliette Adam", "Marie-Jo Bonnet"]
refPortails = ["LGBT"]

def portails(string):
    search = portail.search(string)
    if search is not None:
        return separation.split(search.group())
    else:
        print string
        return[]

def portailsDe(pages):
    result = {}
    for title in pagesTitles:
        result[title] = {}
        print title
        result[title]["Portails"] = [i for i in portails(site.Pages[title].text()) if len(i) > 0]
    return result

def aPortails():
    return ""

print portailsDe(pagesTitles)


