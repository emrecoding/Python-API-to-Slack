import requests
import pprint
pp = pprint.PrettyPrinter(indent=4)
def slack_status():
   slack_url = "https://status.slack.com/api/v2.0.0/current"
   slack_resp = requests.get(slack_url)
   slack_data = slack_resp.json()
   if len(slack_data['active_incidents']) == 0:
       slack_status = {
           "status": slack_data['status']
       }
   else:
       slack_status = {
           #_active”: len(slack_data[‘active_incidents’]),
           "status": slack_data['status'],
           "updated_date": slack_data['date_updated'],
           "title": slack_data['active_incidents'][0]['title']
       }
   return slack_status
print(slack_status())
