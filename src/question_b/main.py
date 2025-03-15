#add import
import question_b

def main():

    kilometers = int(input("Enter kilometers: "))
    minutes = int(input("Enter minutes: "))

    result = question_b.get_miles_per_hour(kilometers, minutes)
    print("Miles per hour:", result)

main()