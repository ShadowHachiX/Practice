from lxml import html
import requests

page = requests.get('https://assess.cyber-fasttrack.org/challenge-files/clock-pt1?verify=o%2FnPfkj2Hc67xdKP0Zb46g%3D%3D.html')
tree = html.fromstring(page.content)
          
print page
