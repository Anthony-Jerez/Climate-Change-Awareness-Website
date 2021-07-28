def determine_air_quality(userLocation):

    airqualities = {
        "queens": "123",
        "manhattan": "456",
        "bronx": "789",
        "brooklyn": "10",
        "staten island": "11" 
    }
    for location in airqualities:
        if userLocation == location: 
            return airqualities[location]





