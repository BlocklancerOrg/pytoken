import requests
import pandas as pd
import math
import pickle

class Token:

    def __init__(self, address):
        self.address = address

        addresses = []
        tokens = []

        url = "https://ethplorer.io/service/service.php?refresh=holders&data=" + self.address + "&page=tab%3Dtab-holders%26pageSize%3D100%26holders%1D3"  # change to whatever your url is

        data = requests.get(url)
        data = data.json()
        records = data["pager"]["holders"]["records"]
        num_pages = math.ceil(records / 100)

        for i in range(1, num_pages):
            print("processing page no. " + str(i) + " | " + str(num_pages))
            url = "https://ethplorer.io/service/service.php?refresh=holders&data=" + self.address + "&page=tab%3Dtab-holders%26pageSize%3D100%26holders%3D" + str(
                i)
            data = requests.get(url)
            data = data.json()

            for elem in data["holders"]:
                addresses.append(elem["address"])
                tokens.append(elem["balance"])

        txs_count = data["token"]["txsCount"]
        symbol = data["token"]["symbol"]
        transfers_count = data["token"]["transfersCount"]
        decimals = data["token"]["decimals"]
        holders_count = data["token"]["holdersCount"]
        total_supply = data["token"]["totalSupply"]

        data_tokenholders = {"address": addresses, "tokens": tokens}
        tokenholders = pd.DataFrame(data_tokenholders)

        self.txs_count = txs_count
        self.symbol = symbol
        self.transfers_count = transfers_count
        self.decimals = decimals
        self.holders_count = holders_count
        self.total_supply = total_supply
        self.tokenholders = tokenholders

    def __str__(self):
        head = "Address, Symbol,Total Supply,Decimals, Holders Count, Txs Count, Transfers Count \n"
        data = self.address + ", " + self.symbol + ", " + str(self.total_supply) + ", " + str(self.decimals) + ", " + str(self.holders_count) + ", " + str(self.txs_count) + ", " + str(self.transfers_count)

        return head + data

    def dump(self, path):
        pickle.dump(self, open(path, "wb"))

    def token_distribution_to_csv(self, path):
        self.tokenholders.to_csv(path, sep=",")




