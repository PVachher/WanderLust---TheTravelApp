def get_weather(name):
    import urllib2, urllib, json
    dict = {}
    baseurl = "https://query.yahooapis.com/v1/public/yql?"
    yql_query = 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="'+name+' india")'
    yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
    result = urllib2.urlopen(yql_url).read()
    data = json.loads(result)
    k =data['query']
    for z in k:
        print z, k[z]
    temp = data['query']['results']['channel']['units']
    loc =  data['query']['results']['channel']['location']
    wind = data['query']['results']['channel']['wind']
    atmosphere = data['query']['results']['channel']['atmosphere']
    astronomy = data['query']['results']['channel']['astronomy']
    d = {}
    #print data['query']['results']['channel']['item']['lat']
    lat = data['query']['results']['channel']['item']['lat']
    long = data['query']['results']['channel']['item']['long']
    forecast = data['query']['results']['channel']['item']['forecast']

    dict['temp'] = temp
    dict['loc'] = loc
    dict['wind'] = wind
    dict['atmospher'] = atmosphere
    dict['astronomy'] = astronomy
    dict['lat'] = lat
    dict['long'] = long
    dict['forecast'] = forecast
    return dict

print get_weather('Delhi')

    