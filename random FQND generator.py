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
print('How many Domain names to generate: ')
num_of_names = int(input())
print('How many characters maximum for the subdomain: ')
num_of_char = int(input())

i = 0
while i != num_of_names:
    i = i+1
    # generate 3 character subdomain
    characters = string.ascii_letters + string.digits
    subdomain = ''.join(random.choice(characters) for x in range(random.randrange(1, num_of_char))) # remove the random.randrange function to keep the same number of charters per try
    fqdn = subdomain + separator + basedomain
    print(fqdn)


    try: # Check for A record and let know if it exists or not
        result = dns.resolver.resolve(fqdn, 'A', raise_on_no_answer=False) 
        for ipval in result:
            print('IP', ipval.to_text())
    except dns.resolver.NXDOMAIN:
        print("Domain does not exist")
        pass        
sys.exit("End of Line")
