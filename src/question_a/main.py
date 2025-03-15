#add import
import question_a

def main():

    num = input("Enter a number: ")
    result = question_a.get_sum_of_evens(int(num))

    print(result)

main()
