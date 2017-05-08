import requests
import numpy as math
import csv

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

def export_csv(result_input):
    f = csv.writer(open("incomesOOP.csv", "wb+"))
    f.writerow(["geographyName", "population", "households", "incomeBelowPoverty", "medianIncome"])
    for idx, val in enumerate(result_input):
        f.writerow([result_input[idx]['geographyName'],
                    result_input[idx]['population'],
                    result_input[idx]['households'],
                    result_input[idx]['incomeBelowPoverty'],
                    result_input[idx]['medianIncome']])
    print 'CSV generated: incomes.csv'
    quit()

# Perform weighted average calculation
def weighted_average(result_input):
    income_avg = []
    households_weight = []
    for idx, val in enumerate(result_input):
        income_avg.append(float(result_input[idx]['incomeBelowPoverty']))
        households_weight.append(float(result_input[idx]['households']))
    weighted_avg = math.average(income_avg, weights=households_weight)
    print 'Percentage households below poverty line: ', weighted_avg*100, '%'
    quit()

get_fips(states)
get_data(fip_list)
export_csv(result)
#weighted_average(result)
