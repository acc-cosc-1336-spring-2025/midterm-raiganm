#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_miles_per_hour(kilometers, minutes):
    
    if kilometers < 0 or minutes < 0:
        return "Invalid arguments"
    else:
        miles = kilometers * .621371
        hours = minutes / 60
        return miles / hours
