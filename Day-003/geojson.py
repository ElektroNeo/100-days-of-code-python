import urllib.request, urllib.parse, urllib.error
import json

# Service URL
serviceUrl = 'https://geocode-maps.yandex.ru/1.x/?apikey='
# API Key of service
apiKey = '21a2d581-....-4232-....-3bf46f0e84f4'

# Run infinite
while True:
    # Get address
    add = input('Enter location: ')
    # Check for min 3 character
    if len(add) < 3:
        break

    # Set URL
    url = serviceUrl + apiKey + '&format=json' + '&' + urllib.parse.urlencode({'geocode': add}) + '&lang=en-US'
    print('Retrieving', url)

    # Request
    uh = urllib.request.urlopen(url)
    # Decode data
    data = uh.read().decode()

    # Print length of data
    print('Retrieved', len(data), 'characters')

    # Check for any error
    try:
        js = json.loads(data)
    except:
        print('Something Wrong!')
        continue
    
    # Continue if nothing found
    if js['response']['GeoObjectCollection']['metaDataProperty']['GeocoderResponseMetaData']['found'] == '0':
        print('!!! Nothing Found !!!')
        continue
    
    # Get position
    pos = js['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    # Split position with space
    pos = pos.split()
    # Get name
    name = js['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['name']
    # Get description
    description = js['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['description']

    # Print datas
    print('Name:', name)
    print('Description:', description)
    print('Position:', pos[1], pos[0])



