import requests
import json
url = "https://api.ambeedata.com/latest/by-postal-code"
def determine_air_quality(postal, country):
    querystring = {"postalCode": postal,"countryCode": country}
    headers = {
         'x-api-key': "a360a0c90a4df99f938befb309e16ff0b517b06562b8743e87f71cf001bce5f4",
         'Content-type': "application/json"
         }
    response = requests.request("GET", url, headers=headers, params=querystring)
    response = response.text
    response = json.loads(response)
    return "City: " + response['stations'][0]['city'] + ", Country: " + response['stations'][0]['countryCode'] + ", CO: " + str(round(response['stations'][0]['CO'], 2)) + ", NO2: " + str(round(response['stations'][0]['NO2'], 2)) + ", Ozone: " + str(round(response['stations'][0]['OZONE'], 2)) + ", PM10: " + str(round(response['stations'][0]['PM10'], 2))\
    + ", PM25: " + str(round(response['stations'][0]['PM25'],2)) + ", SO2: " + str(round(response['stations'][0]['SO2'], 2)) + ", Pollutant: " + response['stations'][0]['aqiInfo']['pollutant']+ ", Concentration: " + str(round(response['stations'][0]['aqiInfo']['concentration'],2))\
    + ", Category: " + response['stations'][0]['aqiInfo']['category']   

def recycle(recycleFreq):
    if recycleFreq == "Never":
        return "You do not recycle. To reduce your Carbon Footprint, you should try recycling any plastics, cans, boxes or paper products. Recycling helps reduce Green House Gas emissions and reduces energy Consumption"
    elif recycleFreq == "Occasionally":
        return "You Occasionally recycle. Try to recycle more often to reduce your carbon footprint. Recycling helps reduce Green House Gas emissions and reduces energy Consumption"
    elif recycleFreq == "Often" or recycleFreq == "Always":
        return f"You {recycleFreq} recycle! Recycling helps reduce Green House Gas emissions and reduces energy Consumption."
    else:
        return "Recycling helps reduce Greenhouse Gas emissions and reduces energy Consumption"
def reusableProducts(reusable):
    if reusable == "Never":
        return "You do not use reusable products. Try to use reusable products such as water bottles, shopping bags and straws. Using reusable products helps reduce waste, and Greenhouse gas emissions, which helps keep the planet clean."
    elif reusable == "Occasionally":
        return "You Occasionally use reusable products. Using reusable products helps reduce waste, and Greenhouse gas emissions, which helps keep the planet clean."
    elif reusable == "Often":
        return "You often use reusable products! Using reusable products helps reduce waste, and Greenhouse gas emissions, which helps keep the planet clean."
    elif reusable == "Always":
        return "You Always use Reusable products when possible! Using reusable products are a great water to reduce all types of pollution!"
    else:
        return ""
def dietType(diet):
    if diet == "vegan" or diet == "vegetarian":
        return f"You are a {diet}. Meat consumption is responsible for releasing greenhouse gases such as methane, CO2, and nitrous oxide. Being {diet} helps reduce your carbon footprint, and helps reduce pollution!"
    elif diet == "nBeef":
        return "Beef accounts for nearly half of agricultural emissions and about 3.7%% of the US total carbon emission. Cutting beef from your diet helps reduce carbon emissions and nearly every form of pollution, and it's healthier."
    elif diet == "sMeat":
        return "You occasionally consume meat. Reducing meat consumption is a good way to reduce your carbon footprint"
    elif diet == "oMeat":
        return "You often consume Meat products. Meat and dairy specifically accounts for around 14.5%% of global greenhouse gas emissions. You don't have to go vegan, however reducing your meat consumption can help reduce pollution and carbon emissions, and may even have benefits to your health."
    else:
        return ""
def transportation(trans):
    if trans == "bus" or trans == "train":
        return f"Your most frequent form of transportation is by {trans}. Taking public transportation reduces carbon emissions and can limit congestion in cities."
    elif trans == "Walking" or trans == "Biking":
        return f"Your most frequent form of transportation is {trans}. {trans} is a healthy form of transportation and helps reduce your carbon footprint."
    elif trans == "car":
        return "Using a personal vehicle is often necessary, however also contributes to climate change. Whenever possible, try to use public transportation or walk."
    else: 
        return ""    
    
    #response = requests.request("GET", url, headers=headers, params=querystring)
    #return response.text
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





