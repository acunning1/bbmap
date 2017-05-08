import argparse

states = []

# Create argument parser to accept input from CLI
def get_input():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument("states", nargs='?', help="comma separated list of US states", default="check_string_for_empty", type=lambda x: x.split(','))
    parser.add_argument('-a', '--avg', help="output format: averages (default)", action='store_true')
    parser.add_argument('-c', '--csv', help="output format: export to csv", action='store_true')
    args = parser.parse_args()

# Validate argument input
def validate_input(arg_input):
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
        print 'Input \'bbmap.py -h\' or \'bbmap.py --help\' for help.'
        quit()

    formatted_states = [x.lower() for x in arg_input.states]

    for s in formatted_states:
        if s not in valid_states:
            print 'Not a valid US state: ', s
            quit()
        else:
            states.append(s)

get_input()
validate_input(args)
print states

# print args
# print args.states
print args.csv
print args.avg
# print type(args)


# # Checks for no argument
# if args.states == ['check_string_for_empty']:
#     print 'No US states provided. Input a list of states and desired format option.'
#
# # CSV export
# elif args.csv:
#     print 'generating csv'
#     print args.states
#     print type(args.states)
#
# # Average
# else:
#     print 'calculating averages'
#     print args.states
#     print type(args.states)
