from methods import IncomeRequester

i = IncomeRequester()

args = i.get_input()
fips = i.get_fips(i.validate_input(args))
result = i.get_data(fips)

if args.csv:
    i.export_csv(result)
    print 'Generated CSV file: incomes.csv'
    quit()
else:
    print 'Percentage households below poverty line: ', i.weighted_average(result)*100, '%'
    quit()
