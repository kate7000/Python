import os, whois, re, json
from datetime import datetime

with open("domains.txt") as file:
    file_list = (file.readlines())

domains_list = [x.replace('\n', '') for x in file_list]

#print('{ "data": [', '\n', '{')
domain_dict = {}
for d in domains_list:
    w = whois.whois(d)
    if w.expiration_date is not None and type(w.expiration_date) is not list:
        diff_days = w.expiration_date - datetime.now()
        domain_dict[d] = diff_days.days
    elif type(w.expiration_date) == list:
        diff_days = w.expiration_date[0] - datetime.now()
        domain_dict[d] = diff_days.days
    #print('{', '\n','"name":','"%s",' % d,'\n','"days":','"%s",' % diff_days.days,'\n','},')
    
#print(']', '\n', '}')
domain_array = [{'name': i, 'days' : domain_dict[i]} for i in domain_dict]
print(type(domain_dict))
print(json.dumps(domain_array))
