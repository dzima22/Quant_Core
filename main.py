from Data.Providers.ecb.provider import ECBProvider

ecb = ECBProvider()

data = ecb.get_exchange_rate("USD")
print(data)