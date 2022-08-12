import  ipaddress
import  re


range_input = input('Input ip-range (format: 0.0.0.0/0): ')
octet_regex = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

current_ip = []
ipv4_range = ipaddress.ip_network(range_input)
for ip_in_range in ipv4_range.hosts():
    current_ip.append(ip_in_range)

ip_post_regex = list()
for i in current_ip:
    ip_post_regex.append(octet_regex.match(str(current_ip)))
    print(i)
