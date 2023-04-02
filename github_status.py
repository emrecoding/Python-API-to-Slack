# from functions import find_actor, actors
import requests, pprint, os, json
pp = pprint.PrettyPrinter(indent=4)
def github_status():
   ## syntax
   ##requests.get(url, header, data)
   github_status = requests.get('https://www.githubstatus.com/api/v2/status.json')
   status_r = github_status.json()
   if status_r['status']['indicator'] == 'none':
       description = status_r['status']['description']
       indicator = status_r['status']['indicator']
   else:
       description = status_r['status']['description']
       indicator = status_r['status']['indicator']
   print(description, indicator)
   return description, indicator
github_status()
