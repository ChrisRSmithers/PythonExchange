import quandl
import pandas
fileIn = open('quandlAPIKey.txt', 'r')

apiKey = fileIn.read()
quandl.ApiConfig.api_key = apiKey
quandl.ApiConfig.api_version = '2015-04-09'
data = quandl.get("BOE/XUDLTWS")
print(data.tail(50))