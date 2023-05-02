import os, whois, re, json
from datetime import datetime

with open("domains.txt") as file:
    file_list = (file.readlines())

domains_list = [x.replace('\n', '') for x in file_list]

#print('{ "data": [', '\n', '{')
domain_dict = {}
for d in domains_list:
    w = whois.whois(d)
    diff_days = w.expiration_date - datetime.now()
    #print('{', '\n','"name":','"%s",' % d,'\n','"days":','"%s",' % diff_days.days,'\n','},')
    domain_dict[d] = diff_days.days
    
#print(']', '\n', '}')
domain_array = [{'name': i, 'days' : domain_dict[i]} for i in domain_dict]
print(type(domain_dict))
print(json.dumps(domain_array))
