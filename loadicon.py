import os
import sys

envurl = os.environ.get('SITEURL')
argurl = None;
siteurl = None;

if len(sys.argv) > 1:
 argurl = sys.argv[1]

if envurl is None:
  if argurl is not None:
   siteurl = argurl
   print('No Enviroment variable SITEURL. Arg: ' + argurl) 
else:
  siteurl = envurl

if siteurl is None:
  print('No Site Url')
else:
  filename = "favicon.ico"

  print('Download FavIcon for Site: ' + siteurl)
  faviconurl = siteurl + "/" + filename
  print('Full url: ' + faviconurl)

import requests
r = requests.get(faviconurl, allow_redirects=True)
open(filename, 'wb').write(r.content)

print('FavIcon downloaded!')