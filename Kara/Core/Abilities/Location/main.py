# geolocation (ip to location)
import geocoder
# Kara Weather
from .weather import forcast, sunFormat


# weather at a location
def location(Kara):
    # customizable opening words
    opening = 'You Are'

    # location specified
    if 'in' in command:
        # split command
        cmdSplit = command.split()
        pos = cmdSplit.index('in')
        # get city
        city = cmdSplit[pos + 1]
    else:
        # get current location from ip
        g = geocoder.ip('me')
        city = g.city


    # "Today in brisbane you can expect light rain"
    line = '{} in {} you can expect {}'.format(opening, city)
    Kara.speak(line)