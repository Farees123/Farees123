# personal budget Trakker

# expense trakker
expense_category = {'food': 15000, 'transport': 5000 , 'clothing': 2000, 'cooking': 2000, 'electricity': 2000, 'furnishing': 2000}
# Taking input from the user.
User_menu=input("Enter the option that you want to choose: ")

# handling each case 
if User_menu=="all expenses":
    print(expense_category)
elif User_menu=="add all expenses":
    total = sum(expense_category.values())
    print("the total sum is:",total)
elif User_menu=="add an expense":
    new_category=input("Enter the category which you want to add: ")
    new_amount=int(input("enter the amount which you want to assign to this category: "))
    expense_category[new_category]=new_amount
    print(F"added{new_category}with{new_amount}")
elif User_menu=="delete an expense":
    delete_category=input("Enter the category which you want to deleate.")
    if delete_category in expense_category:
        del expense_category[delete_category]
        print(f"{delete_category}has been deleted.")
    else:
        print("the category was not found.")
elif User_menu=="exit":
    print("Thank you for using our service!")
else:
    print("invalid option.")