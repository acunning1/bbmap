import requests

states = ['oregon', 'california', 'virginia']
fips = []
result = []
url1 = 'https://www.broadbandmap.gov/broadbandmap/census/state/'
url2 = 'https://www.broadbandmap.gov/broadbandmap/demographic/jun2014/state/ids/'
as_json = '?format=json'

# Request 1: Find FIPS ID
def get_fips(state_input):
    global fip_list
    for state in state_input:
        request1 = requests.get(url1+state+as_json)
        r1 = request1.json()
        fips.append(r1['Results']['state'][0]['fips'])
    fip_list = ','.join(map(str, fips))


# Request 2: Secondary request using FIPS
def get_data(fip_input):
    request2 = requests.get(url2+fip_input+as_json)
    r2 = request2.json()
    for x in r2['Results']:
        result.append(x)

get_fips(states)
get_data(fip_list)

# Debugging print statements

# print fip_list
# print type(fip_list)

# for idx, val in enumerate(result):
#     print result[idx]['geographyName']

print result[0]['geographyName']
print result[1]['geographyName']
print result[2]['geographyName']

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
