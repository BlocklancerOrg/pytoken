import requests
import math
from my_token import Token

class Tokenhelper():

    def get_top_tokens(self, limit = 50, criteria = "cap"):
        url = "https://api.ethplorer.io/getTop?apiKey=freekey&criteria=" + criteria + "&limit=" + str(50)
        data = requests.get(url)
        data = data.json()
        tokens = []
        for token in data["tokens"]:
            print(token)
            data = token
            address = data["address"]
            records = data["holdersCount"]
            num_pages = math.ceil(records / 100)
            symbol = data["symbol"]
            decimals = data["decimals"]
            holders_count = data["holdersCount"]
            total_supply = data["totalSupply"]
            name = data["name"]
            owner = data["owner"]
            try:
                total_in = data["totalIn"]
            except KeyError:
                total_in = 0

            try:
                total_out = data["totalOut"]
            except KeyError:
                total_out = 0
            issuances_count = data["issuancesCount"]
            t = Token(address, num_pages, symbol, decimals, holders_count, total_supply, name, owner, total_in, total_out, issuances_count)
            tokens.append(t)
        return tokens