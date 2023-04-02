import requests
import pprint
def digital_ocean_status():
   do_url = 'https://status.digitalocean.com/api/v2/status.json'
   do_resp = requests.get(do_url).json()
   last_updated = do_resp['page']['updated_at']
   d = do_resp['status']['description']
   i = do_resp['status']['indicator']
   test = {"description": d, "status": i, "last_update":last_updated}
   print(test)
   return {"description": d, "status": i, "last_updated": last_updated}
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(digital_ocean_status())
