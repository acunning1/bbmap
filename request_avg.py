import requests
import numpy as math

# Request 1: Find FIPS ID
base_url1 = 'https://www.broadbandmap.gov/broadbandmap/census/state/'
states = ['oregon', 'california', 'virginia']
fips = []

for state in states:
    request1 = requests.get(base_url1+state+'?format=json')
    r1 = request1.json()
    fips.append(r1['Results']['state'][0]['fips'])

fip_list = ','.join(map(str, fips))

# Request 2: Secondary request using FIPS
base_url2 = 'https://www.broadbandmap.gov/broadbandmap/demographic/jun2014/state/ids/'
request2 = requests.get(base_url2+fip_list+'?format=json')
r2 = request2.json()

# Parse JSON result

# result = list containing dictionaries
result = []

for x in r2['Results']:
    result.append(x)

# Perform weighted average

income_avg = []
households_weight = []

for idx, val in enumerate(result):
    income_avg.append(float(result[idx]['incomeBelowPoverty']))
    households_weight.append(float(result[idx]['households']))

weighted_avg = math.average(income_avg, weights=households_weight)

# Debugging print statements

# print weighted_avg
# print type(weighted_avg)

print 'Income below poverty weighted average: ', weighted_avg*100, '%'

# print income_avg
# print type(income_avg)
# print households_weight
# print type(households_weight)

# for idx, val in enumerate(result):
#     print result[idx]['geographyName']

# print result[0]['geographyName']
# print result[1]['geographyName']
# print result[2]['geographyName']

# for p in result:
#     print p

# print result
# print type(result)
#
# print result[0]
# print type(result[0])


# for key in r2:
#     print key, 'corresponds to', r2[key]

# print(request2.url)
# print type(r2)
# print 'State: ' + r2['Results'][0]['geographyName']
# print 'Population: ' + str(r2['Results'][0]['population'])
# print 'Households: ' + str(r2['Results'][0]['households'])
# print 'Income Below Poverty: ' + str(r2['Results'][0]['incomeBelowPoverty'])
# print 'Median Income: ' + str(r2['Results'][0]['medianIncome'])
