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

# loop for multiple iterations
i = 0
while i != 10: # change this number for how long this will loop for
    i = i+1
    # generate 3 character subdomain Change range in subdomain variable for more characters
    characters = string.ascii_letters + string.digits
    subdomain = ''.join(random.choice(characters) for i in range(3))
    fqdn = subdomain + separator + basedomain
    print(fqdn)


    try: # try sequence to see if domain exists, and if an exception is thrown it will say that the domain does not exist
        result = dns.resolver.resolve(fqdn, 'A', raise_on_no_answer=False) 
        for ipval in result:
            print('IP', ipval.to_text())
    except dns.resolver.NXDOMAIN:
        print("Domain does not exist")
        pass        
sys.exit("End of Line")
