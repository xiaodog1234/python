import sys
import requests
import json

if len(sys.argv) <= 1 or len(sys.argv)>= 3:
    sys.exit("Missing command-line argument")
try:
    float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
userNumber = float(sys.argv[1])



response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o= response.json()
#print(json.dumps(response.json(), indent=2))
#print(o["bpi"]["USD"]["rate_float"])
rate = o["bpi"]["USD"]["rate_float"]

print(f"${userNumber*float(rate):,.4f}")
