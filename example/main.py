from dist.my_token import Token

contract_address = "0x9a642d6b3368ddc662CA244bAdf32cDA716005BC" #QTUM

t = Token(contract_address)
print(t)

#t.dump("./data/qtum.p")
#t.token_distribution_to_csv("./data/qtum.csv")