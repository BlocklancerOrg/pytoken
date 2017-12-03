import requests
import pandas as pd
import math
import pickle

class Token:

    def __init__(self, address):
        self.address = address
        url = " https://api.ethplorer.io/getTokenInfo/" + self.address + "?apiKey=freekey"
        data = requests.get(url)
        data = data.json()
        records = data["holdersCount"]
        self.num_pages = math.ceil(records / 100)
        self.symbol = data["symbol"]
        self.decimals = data["decimals"]
        self.holders_count = data["holdersCount"]
        self.total_supply = data["totalSupply"]
        self.name = data["name"]
        self.owner = data["owner"]
        self.total_in = data["totalIn"]
        self.total_out = data["totalOut"]
        self.issuances_count = data["issuancesCount"]

    def __init__(self, address, num_pages, symbol, decimals, holders_count, total_supply, name, owner, total_in, total_out, issuances):
        self.address = address
        self.num_pages = num_pages
        self.symbol = symbol
        self.decimals = decimals
        self.holders_count = holders_count
        self.total_supply = total_supply
        self.name = name
        self.owner = owner
        self.total_in = total_in
        self.total_out = total_out
        self.issuances_count = issuances

    def compute_tokenhoder_distribution(self):
        addresses = []
        tokens = []

        for i in range(1, self.num_pages):
            print("processing page no. " + str(i) + " | " + str(self.num_pages))
            url = "https://ethplorer.io/service/service.php?refresh=holders&data=" + self.address + "&page=tab%3Dtab-holders%26pageSize%3D100%26holders%3D" + str(
                i)
            data = requests.get(url)
            data = data.json()

            for elem in data["holders"]:
                addresses.append(elem["address"])
                tokens.append(elem["balance"])

        data_tokenholders = {"address": addresses, "tokens": tokens}
        self.tokenholders = pd.DataFrame(data_tokenholders)
        return self.tokenholders


    def __str__(self):
        head = "Address, Symbol,Total Supply,Decimals, Holders Count,  Name, TotalIn, TotalOut,  IssuancesCount \n"
        data = self.address + ", " + self.symbol + ", " + str(self.total_supply) + ", " + str(self.decimals) + ", " + str(self.holders_count) +  ", " + self.name + ", " + str(self.total_in) + ", " + str(self.total_out) +  ", " + str(self.issuances_count)

        return head + data

    def dump(self, path):
        pickle.dump(self, open(path, "wb"))

    def token_distribution_to_csv(self, path):
        self.tokenholders.to_csv(path, sep=",")




