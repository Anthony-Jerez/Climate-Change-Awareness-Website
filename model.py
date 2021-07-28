import requests
url = "https://api.ambeedata.com/latest/by-postal-code"
def determine_air_quality(postal, country):
    querystring = {"postalCode": postal,"countryCode": country}
    headers = {
         'x-api-key': "a360a0c90a4df99f938befb309e16ff0b517b06562b8743e87f71cf001bce5f4",
         'Content-type': "application/json"
         }
    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.text
#print(response.text)


#def determine_air_quality(userLocation):

    #airqualities = {
       # "queens": "123",
        #"manhattan": "456",
        #"bronx": "789",
        #"brooklyn": "10",
       # "staten island": "11" 
    #}
    #for location in airqualities:
        #if userLocation.lower() == location: 
            #return airqualities[location]
        #else: 
            #return "Invalid Response"





