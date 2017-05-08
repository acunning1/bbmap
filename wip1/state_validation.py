# State validator

raw_states = ['oregon', 'CalifoRnia', 'virginia', 'tenNessee', 'aLabama', 'veRmont', 'new york', 'texas']

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

formatted_states = [x.lower() for x in raw_states]

for s in formatted_states:
    if s in valid_states:
        print 'Valid state'
    else:
        print 'Not a valid state'
