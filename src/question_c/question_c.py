#write functions here, don't add input('') statements here!
def test_config():
    return True

def get_fahrenheit(celsius):

    for celsius in range(0, 21):
        fahrenheit = (9 / 5) * celsius + 32
        print(celsius, "\t", fahrenheit)

