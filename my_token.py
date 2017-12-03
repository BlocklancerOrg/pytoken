class Token:

    def __init__(self, symbol, total_supply, decimals, holdersCount, txsCount, transfersCount, tokenholders):
        self.symbol = symbol
        self.total_supply = total_supply
        self.decimals = decimals
        self.holdersCount = holdersCount
        self.txsCount = txsCount
        self.transfersCount = transfersCount
        self.tokenholders = tokenholders

    def __str__(self):
        return self.symbol + ", " + str(self.total_supply) + ", " + str(self.decimals) + ", " + str(self.holdersCount) + ", " + str(self.txsCount) + ", " + str(self.transfersCount)
