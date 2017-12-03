import requests
import pandas as pd
import math
from my_token import Token
import pickle

addresses = []
tokens = []

url = "https://ethplorer.io/service/service.php?refresh=holders&data=0x9a642d6b3368ddc662CA244bAdf32cDA716005BC&page=tab%3Dtab-holders%26pageSize%3D100%26holders%1D3"  # change to whatever your url is

data = requests.get(url)
data = data.json()
records = data["pager"]["holders"]["records"]
num_pages = math.ceil(records / 100)

for i in range(1,num_pages):
    print("processing page no. " + str(i) + " | " + str(num_pages))
    url = "https://ethplorer.io/service/service.php?refresh=holders&data=0x9a642d6b3368ddc662CA244bAdf32cDA716005BC&page=tab%3Dtab-holders%26pageSize%3D100%26holders%3D" + str(i)
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

data_tokenholders = {"address" : addresses, "tokens" : tokens}
tokenholders = pd.DataFrame(data_tokenholders)

t = Token(symbol, total_supply,decimals,holders_count, txs_count, transfers_count, tokenholders)
pickle.dump(t, open("./data/qtum.p", "wb"))
tokenholders.to_csv("./data/qtum.csv", sep = ",")
print(t)