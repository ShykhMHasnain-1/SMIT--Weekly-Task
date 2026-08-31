import csv
import os

folder_path = r"E:\AI_Data Science\Projects\Expense"

Categories_List = {
    1: "Food",
    2: "Transport",
    3: "Shopping",
    4: "Utility_Bills",
    5: "Entertainment",
    6: "Education",
    7: "Medical",
    8: "Travel"
}

def Show_Categories():
    print("*"*50)
    print("1.Food")
    print("2.Transport")
    print("3.Shopping")
    print("4.Utility Bills")
    print("5.Entertainment")
    print("6.Education")
    print("7.Medical")
    print("8.Travel")
    print("9.Other")
    print("*"*50)

def Read_Category_File(category_name):
    Total = 0
    file_path = os.path.join(folder_path, f"{category_name}_Expense.csv")

    if not os.path.exists(file_path):
        print(f"No expenses found yet for {category_name}.")
        return

    with open(file_path, "r") as file:
        expense = csv.reader(file)
        for rows in expense:
            if not rows:
                continue
            Spending_Amount = int(rows[1])
            Spending_Date = rows[2]
            Total += Spending_Amount
            print(f"Date: {Spending_Date} ,, Amount:{Spending_Amount}")

    print(f"Total Spending In {category_name} is Rs.{Total}")

def Search_By_Category():
    Show_Categories()
    user_category = int(input("Enter Choice(1/2/3/4/5/6/7/8/9):"))
    print("*"*50)

    if user_category in Categories_List:
        Read_Category_File(Categories_List[user_category])
    elif user_category == 9:
        expense_category = input("Please Enter The Expense Category Name That You Have Added In Add Expense"
        "(First Letter Must Be Capital):")
        Read_Category_File(expense_category)
    else:
        print("Invalid Option!!!...")

def Write_Category_File(category_name, Expense_Amount, Expense_Date_Input):
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, f"{category_name}_Expense.csv")

    with open(file_path, "a", newline="") as file:
        expense = csv.writer(file)
        expense.writerow([category_name, Expense_Amount, Expense_Date_Input])

    print(f"Amount Of Rs.{Expense_Amount} Spend On {category_name} On Date:{Expense_Date_Input}")
    print(f"------- Expense Added In File : {category_name}_Expense.csv -------")

def Categories():
    Expense_Date_Input = input("Enter The Date:")

    Show_Categories()
    user_category = int(input("Enter Choice(1/2/3/4/5/6/7/8/9):"))
    print("*"*50)

    if user_category in Categories_List:
        category_name = Categories_List[user_category]
        Expense_Amount = int(input(f"Enter The Amount In {category_name} Expense: "))
        Write_Category_File(category_name, Expense_Amount, Expense_Date_Input)

    elif user_category == 9:
        expense_category = input("Please Enter The Expense Category Name:")
        Expense_Amount = int(input(f"Enter The Spending Amount In {expense_category} Expense: "))
        Write_Category_File(expense_category, Expense_Amount, Expense_Date_Input)

    else:
        print("Invalid Options!!!...")

def Add_Expense():
    Categories()
    Menu()

def View_Expense():
    file_in_folder = os.listdir(folder_path)
    for files in file_in_folder:
        if files.endswith(".csv"):
            total = 0
            Category = files.replace("_Expense.csv", "")
            full_file_path = os.path.join(folder_path, files)
            with open(full_file_path, "r") as expense_file:
                read_file = csv.reader(expense_file)
                for total_expense in read_file:
                    if not total_expense:
                        continue
                    total += int(total_expense[1])
            print(f"Category:{Category}  ,,  Expense:{total}")

def Total_Expense():
    grandtotal = 0
    file_in_folder = os.listdir(folder_path)
    for files in file_in_folder:
        if files.endswith(".csv"):
            total = 0
            Category = files.replace("_Expense.csv", "")
            full_file_path = os.path.join(folder_path, files)
            with open(full_file_path, "r") as expense_file:
                read_file = csv.reader(expense_file)
                for total_expense in read_file:
                    if not total_expense:
                        continue
                    total += int(total_expense[1])
            print(f"Category:{Category}  ,,  Expense:{total}")
            grandtotal += total
    print("The GrandTotal Of The Expenses In Expense Folder is : Rs.", grandtotal)

def Menu():
    while True:
        print("="*50)
        print(" "*10,"Personal Expense Tracker")
        print("="*50)
        print(" "*20,"Menu")
        print("="*50)
        print("1.Add Expense\n2.View Expense\n3.Total Expense\n4.Search By Category\n5.Exit")
        print("="*50)
        try:
            user_choice = int(input("Enter Choice (1/2/3/4/5):"))
            print("="*50)
        except ValueError:
            print("Enter Number Only!!")
            continue
        if user_choice == 1:
            Add_Expense()
        elif user_choice == 2:
            View_Expense()
        elif user_choice == 3:
            Total_Expense()
        elif user_choice == 4:
            Search_By_Category()
        elif user_choice == 5:
            break

if __name__ == "__main__":
    os.makedirs(folder_path, exist_ok=True)
    Menu()