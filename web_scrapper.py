# This program is Developed by Simon Muthungu (Symon_of_Africa)
# It scrapes a fake jobs wesite (https://realpython.github.io/fake-jobs/) gets the job titles and returns
# that info and writes it into a csv file!

import requests 
from bs4 import BeautifulSoup as bs
import csv

# querrying the jobs site
req = requests.get('https://realpython.github.io/fake-jobs/')
if req.status_code == 200:
    soup = bs(req.content, 'lxml')
else: 
    print('something went not quite right!')

roles = soup.find_all('h2', class_='title is-5') # job titles are stores in this class name

# making the roles list into individual dictionary objects and storing them as objects in another list
# for us to use dictwriter on them

job_roles = []
count = 1
for role in roles:
    obj = {}
    obj['Job Number'] = count
    count += 1
    obj['role'] = role.text 
    job_roles.append(obj)

# writing the results to a csv file
filename = 'job-roles.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f, ['Job Number', 'role'])
    w.writeheader()

    w.writerows(job_roles)
    print('Done!')