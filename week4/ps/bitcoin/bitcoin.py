import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit("Invalid usage")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Invalid amount")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=87d5b56f1ac04959e11861934ddda051fb68c9c271821b9bf5ef2de9f4dd8c2e")

except requests.RequestException:
    sys.exit("Error occured")

dict_response = response.json()
price = float(dict_response["data"]["priceUsd"])*n
print(f"${price:,.4f}")