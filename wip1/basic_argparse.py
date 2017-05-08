import argparse

# Create argument parser to accept input from CLI
parser = argparse.ArgumentParser()
parser.add_argument("states", nargs='?', help="comma separated list of US states", default="check_string_for_empty", type=lambda x: x.split(','))
parser.add_argument('-a', '--avg', help="output format: averages (default)", action='store_true')
parser.add_argument('-c', '--csv', help="output format: export to csv", action='store_true')
args = parser.parse_args()

# Checks for no argument
if args.states == ['check_string_for_empty']:
    print 'No US states provided. Input a list of states and desired format option.'

# CSV export
elif args.csv:
    print 'generating csv'
    print args.states
    print type(args.states)

# Average
else:
    print 'calculating averages'
    print args.states
    print type(args.states)
