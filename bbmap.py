# bbmap.py
# Broadbandmap.gov API requester
#
# Created by Andy Cunningham
# 5/8/17


# Import IncomeRequester class
from methods import IncomeRequester

# Create IncomeRequester object
i = IncomeRequester()

# Accept input, validate input, request income data
args = i.get_input()
fips = i.get_fips(i.validate_input(args))
result = i.get_data(fips)

# Export CSV or perform weighted average depending on option input
if args.csv:
    i.export_csv(result)
    print 'Generated CSV file: incomes.csv'
    quit()
else:
    print 'Percentage households below poverty line: ', i.weighted_average(result)*100, '%'
    quit()
