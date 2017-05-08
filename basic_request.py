import requests

# Request 1: Find FIPS ID
base_url1 = 'https://www.broadbandmap.gov/broadbandmap/census/state/'
states = 'oregon'

request1 = requests.get(base_url1+states+'?format=json')
r1 = request1.json()

fips = r1['Results']['state'][0]['fips']

# Request 2: Secondary request using FIPS
base_url2 = 'https://www.broadbandmap.gov/broadbandmap/demographic/jun2014/state/ids/'
request2 = requests.get(base_url2+fips+'?format=json')
r2 = request2.json()

# result = r2['Results'][0]


# Debugging print statements

# print result
# print type(result)

# for key in r2:
#     print key, 'corresponds to', r2[key]

print(request2.url)
print type(r2)
print 'State: ' + r2['Results'][0]['geographyName']
print 'Population: ' + str(r2['Results'][0]['population'])
print 'Households: ' + str(r2['Results'][0]['households'])
print 'Income Below Poverty: ' + str(r2['Results'][0]['incomeBelowPoverty'])
print 'Median Income: ' + str(r2['Results'][0]['medianIncome'])
