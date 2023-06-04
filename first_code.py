while True:
    number_one = input("Enter Your First Number= ")
    number_two = input("Enter Your Second Number= ")
    calculation = input("Calculation '+' '-' '*' '/' = ")
    try:
        num_one = float(number_one)
        num_two = float(number_two)
        if calculation == '+':
            print(num_one + num_two)
        elif calculation == '-':
            print(num_one - num_two)
        elif calculation == '*':
            print(num_one * num_two)
        elif calculation == '/':
            print(num_one / num_two)
        else:
            print("Invalid Input")
        Exit = input('do you want to continue?: Enter yes or no ')
        if Exit == 'yes':
            continue
        else:
            break
    except:
        print("Enter Number Only")
        Exit = input('do you want to continue?: Enter yes or no ')
        if Exit == 'yes':
            continue
        else:
            break