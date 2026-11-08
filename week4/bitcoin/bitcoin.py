import requests
import sys

if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

argument = sys.argv[1]

try:
    number = float(argument)
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=2be077950d6c1ee9890342cebfd4a7805fcc35a54eacabf152b4d002929a6ad8")
    bitcoin_info = response.json()
    price = float(bitcoin_info['data']['priceUsd'])
    total = price * number
    print(f"${total:,.4f}")

except requests.RequestException:
    sys.exit("Could not reach the API")
