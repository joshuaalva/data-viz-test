import matplotlib.pyplot as plt 

def budgetProgram(): 
    print("Budgeting Program")
    print("---------------")

    expenses = {}

    while True: 
        category = input("Input a new expense category or type DONE: ")
        if category.lower() == "done":
            break
        if category.lower() == " ": 
            print("Category can not be empty. Try Again.")
            continue 

        try: 
            cost = int(input("Input the cost of the expense category: "))
            if cost < 0: 
                print("Price cannot be negative. Try Again.")
                continue 
        except ValueError:
            print("Must enter a whole number try again")
            continue 

        if category in expenses: 
            expenses[category] += cost
        else: 
            expenses[category] = cost

# visualize 

    labels = list(expenses.keys())
    slices = list(expenses.values())
    plt.pie(slices, labels = labels, autopct="%1.1f%%", startangle = 40, shadow = True)
    plt.show()

budgetProgram()
