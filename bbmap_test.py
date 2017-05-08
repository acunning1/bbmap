# Import libraries
import argparse
import requests
import csv
import numpy as math

# Create argument parser to accept input from CLI
parser = argparse.ArgumentParser()
parser.add_argument("states", nargs='?', help="comma separated list of US states (no whitespace)", default="check_string_for_empty", type=lambda x: x.split(','))
group = parser.add_mutually_exclusive_group()
group.add_argument('-a', '--avg', help="output format: weighted averages (default)", action='store_true')
group.add_argument('-c', '--csv', help="output format: export to csv", action='store_true')
args = parser.parse_args()

# Check for no argument or invalid state name
valid_states = [
             'alabama','alaska','arizona','arkansas','california','colorado',
             'connecticut','delaware','florida','georgia','hawaii','idaho',
             'illinois','indiana','iowa','kansas','kentucky','louisiana',
             'maine','maryland','massachusetts','michigan','minnesota',
             'mississippi','missouri','montana','nebraska','nevada',
             'new hampshire','new jersey','new mexico','new york',
             'north carolina','north dakota','ohio','oklahoma','oregon',
             'pennsylvania','rhode island','south  carolina','south dakota',
             'tennessee','texas','utah','vermont','virginia','washington',
             'west virginia','wisconsin','wyoming'
             ]
states = []

if args.states == ['check_string_for_empty']:
    print 'No US states provided. Input a list of states and desired format option.'
    print 'Input \'bbmap.py -h\' or \'bbmap.py --help\' for help.'
    quit()

formatted_states = [x.lower() for x in args.states]

for s in formatted_states:
    if s not in valid_states:
        print 'Not a valid US state: ', s
        quit()
    else:
        states.append(s)

# API Request 1: Find FIPS IDs
base_url1 = 'https://www.broadbandmap.gov/broadbandmap/census/state/'
fips = []

for state in states:
    request1 = requests.get(base_url1+state+'?format=json')
    r1 = request1.json()
    fips.append(r1['Results']['state'][0]['fips'])

fip_list = ','.join(map(str, fips))

# API Request 2: Secondary request using FIPS list
base_url2 = 'https://www.broadbandmap.gov/broadbandmap/demographic/jun2014/state/ids/'
request2 = requests.get(base_url2+fip_list+'?format=json')
r2 = request2.json()

result = []
for x in r2['Results']:
    result.append(x)

# Perform CSV export
if args.csv:
    f = csv.writer(open("incomes.csv", "wb+"))
    f.writerow(["geographyName", "population", "households", "incomeBelowPoverty", "medianIncome"])

    for idx, val in enumerate(result):
        f.writerow([result[idx]['geographyName'],
                    result[idx]['population'],
                    result[idx]['households'],
                    result[idx]['incomeBelowPoverty'],
                    result[idx]['medianIncome']])
    print 'CSV generated: incomes.csv'
    quit()

# Perform weighted average calculation
else:
    income_avg = []
    households_weight = []

    for idx, val in enumerate(result):
        income_avg.append(float(result[idx]['incomeBelowPoverty']))
        households_weight.append(float(result[idx]['households']))

    weighted_avg = math.average(income_avg, weights=households_weight)
    print 'Percentage households below poverty line: ', weighted_avg*100, '%'
    quit()
