import argparse
import requests
import csv
import numpy as math

class IncomeRequester:

    def get_input(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("states", nargs='?', help="comma separated list of US states (no whitespace)", default="check_string_for_empty", type=lambda x: x.split(','))
        group = parser.add_mutually_exclusive_group()
        group.add_argument('-a', '--avg', help="output format: weighted averages (default)", action='store_true')
        group.add_argument('-c', '--csv', help="output format: export to csv", action='store_true')
        args = parser.parse_args()
        return args

    def validate_input(self, arg_input):
        states = []
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

        if arg_input.states == ['check_string_for_empty']:
            print 'No US states provided. Input a list of states and desired format option.'
            print 'Input \'python bbmap.py -h\' or \'python bbmap.py --help\' for help.'
            quit()

        formatted_states = [x.lower() for x in arg_input.states]
        for s in formatted_states:
            if s not in valid_states:
                print 'Not a valid US state: ', s
                quit()
            else:
                states.append(s)
        return states

    def get_fips(self, state_input):
        fips = []
        url1 = 'https://www.broadbandmap.gov/broadbandmap/census/state/'
        for state in state_input:
            request1 = requests.get(url1+state+'?format=json')
            r1 = request1.json()
            fips.append(r1['Results']['state'][0]['fips'])
        fip_list = ','.join(map(str, fips))
        return fip_list

    def get_data(self, fip_input):
        result = []
        url2 = 'https://www.broadbandmap.gov/broadbandmap/demographic/jun2014/state/ids/'
        request2 = requests.get(url2+fip_input+'?format=json')
        r2 = request2.json()
        for x in r2['Results']:
            result.append(x)
        return result

    def export_csv(self, result_input):
        f = csv.writer(open("incomes.csv", "wb+"))
        f.writerow(["geographyName", "population", "households", "incomeBelowPoverty", "medianIncome"])
        for idx, val in enumerate(result_input):
            f.writerow([result_input[idx]['geographyName'],
                        result_input[idx]['population'],
                        result_input[idx]['households'],
                        result_input[idx]['incomeBelowPoverty'],
                        result_input[idx]['medianIncome']])
        return

    def weighted_average(self, result_input):
        income_avg = []
        households_weight = []
        for idx, val in enumerate(result_input):
            income_avg.append(float(result_input[idx]['incomeBelowPoverty']))
            households_weight.append(float(result_input[idx]['households']))
        weighted_avg = math.average(income_avg, weights=households_weight)
        return weighted_avg
