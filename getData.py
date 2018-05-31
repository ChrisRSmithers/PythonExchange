import quandl
fileIn = open('quandlAPIKey.txt', 'r')
fileOut = open('storedData.txt', 'w')

apiKey = fileIn.read()
quandl.ApiConfig.api_key = apiKey
quandl.ApiConfig.api_version = '2015-04-09'
data = quandl.get("EIA/PET_RWTC_D")
fileOut.write(data)