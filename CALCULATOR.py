def calculator() :
    print("-------------------------CALCULATOR-------------------------")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (base ^ exponent)")
    print("6. Exit")

    while True :
        print(" ")
        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == '6':
            print("Exiting calculator. Goodbye!")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = num1 + num2
            print("sum : ",num1,"+",num2,"=",result)
        elif choice == '2':
            result = num1 - num2
            print("difference : ",num1,"-",num2,"=",result)
        elif choice == '3':
            result = num1 * num2
            print("multiplication : ",num1,"*",num2,"=",result)
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print("division : ",num1,"/",num2,"=",result)
            else:
                print("Error! Division by zero is not allowed.")
        elif choice == '5':
            result = num1 ** num2
            print("taking power ",num2,"of ",num1,"we get",result)
        else:
            print("Invalid choice. Please try again.")

calculator()
