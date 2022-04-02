import sys
import argparse
import requests
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument("-check", type=str, dest='ipv4', required=True)
arguments = parser.parse_args()

clear = '\033[0m'
bold = '\033[01m'
magenta = '\033[95m'
red = '\033[31m'
green = '\033[92m'
yellow = '\033[93m'
blue = '\033[94m'

agentuser = {"User-Agent":"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.11 (KHTML, like Gecko) Iron/17.0.1000.0 Chrome/17.0.1000.0 Safari/535.11"}
ip  = arguments.ipv4
api = "http://ip-api.com/json/"
apicheck = "?fields=continent,country,countryCode,regionName,city,zip,isp,org,as,asname,reverse,proxy,hosting,query"


try:
        data = requests.get(api+ip+apicheck, headers=agentuser).json()
        sys.stdout.flush()

        red = red+bold
        magenta = magenta+bold
        blue = blue+bold
        yellow = yellow+bold
        os.system("clear")
        print(green,"We are checking ->", red,data['query']),(ip)
        print("Please wait...")
        print("Loading 10%")
        time.sleep(0.2)
        print("Loading 25%")
        time.sleep(0.2)
        print("Loading 35%")
        time.sleep(0.2)
        print("Loading 45%")
        time.sleep(0.2)
        print("Loading 55%")
        time.sleep(0.2)
        print("Loading 65%")
        time.sleep(0.2)
        print("Loading 75%")
        time.sleep(0.2)
        print("Loading 85%")
        time.sleep(0.2)
        print("Loading 95%")
        time.sleep(0.2)
        print("Loading 100%")
        time.sleep(0.2)
        os.system("clear")
        print(yellow, ("IP Address Info:"))
        print(green, "Reverse DNS:", red,data['reverse'])
        print(green, "Proxy:", red,data['proxy'])
        print("")
        print(yellow, ("Organisation Info:"))
        print(blue, "Hosting:", magenta,data['hosting'])
        print(blue, "Organisation:", magenta,data['org'])
        print(blue, "AS Number:", magenta,data['as'])
        print(blue, "AS Name:", magenta,data['asname'])
        print(blue, "ISP:", magenta,data['isp'])
        print("")
        print(yellow, ("Locations Info:"))
        print(blue, "Continent:", magenta,data['continent'])
        print(blue, "Country:", magenta,data['country'])
        print(blue, "CountryCode:", magenta,data['countryCode'])
        print(blue, "City:", magenta,data['city'])
        print(blue, "Region:", magenta,data['regionName'])
        print(blue, "Zip:", magenta,data['zip'])


except KeyboardInterrupt:
        os.system("clear")
        sys.exit(0)