import re                        

with open( 'log.txt', 'r') as log_file:              #opens log file in a readable format
    log_data = log_file.read()

ip_pattern= r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'    #search pattern that matches ips

ips = re.findall(ip_pattern, log_data)               
print(ips)                                           #returns list of ips

for ip in ips:                                       #list out ips line by line
    print(ip)