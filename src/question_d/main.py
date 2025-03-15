#add import
import question_d

def main():

    age = input("Enter an age: ")
    result = question_d.get_person_category(int(age))
    print(result)

main ()