# This will create a 3 character subdomain of a domain name to see if it exists
# upcoming features includ more modular and a loop to do multiple runs
# Written by Mike "Shecky" K.

import sys
import random
import string
import dns as dns
from dns.rcode import NXDOMAIN
import dns.resolver

# ask for domain name
print('Enter domain name: ')
basedomain = input()
separator = '.'

# generate 3 character subdomain
characters = string.ascii_letters + string.digits
subdomain = ''.join(random.choice(characters) for i in range(3))
fqdn = subdomain + separator + basedomain
print(fqdn)


try:
    result = dns.resolver.resolve(fqdn, 'A', raise_on_no_answer=False) 
    for ipval in result:
        print('IP', ipval.to_text())
except dns.resolver.NXDOMAIN:
    print("Domain does not exist")    
sys.exit("End of Line")
