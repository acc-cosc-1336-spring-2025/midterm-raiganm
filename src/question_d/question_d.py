#write functions here, don't add input('') statements here!
def test_config():
     return True

def get_person_category(age):

    category = ''

    if age >= 0 and age <= 1:
        category = "Infant"
    elif age >= 2 and age <= 12:
        category = "Child"
    elif age >= 13 and age <= 19:
        category = "Teenager"
    elif age >= 20 and age <= 125:
        category = "Adult"
    else:
        category = "Invalid Age"

    return category