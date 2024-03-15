import random

print("Enter the number of friends joining (including you):")
num_of_friends = int(input())

if num_of_friends <= 0:
    print("\nNo one is joining for the party")
else:
    print("\nEnter the name of every friend (including you), each on a new line:")
    names_and_bills = {input(): 0 for _ in range(num_of_friends)}

    print("\nEnter the total bill value:")
    total_bill = float(input())
    split_bill = round(total_bill / num_of_friends, 2)
    names_and_bills = {name: split_bill for name in names_and_bills}

    print("\nDo you want to use the 'Who is lucky?' feature? Write Yes/No:")
    response = input().lower().strip()
    if response == 'yes':
        lucky_name = random.choice(list(names_and_bills.keys()))
        print(f"\n{lucky_name} is the lucky one!")
        revised_bill = round(total_bill / (num_of_friends - 1), 2)
        revised_dict = {name: revised_bill for name in names_and_bills}
        revised_dict.update({lucky_name: 0})
        print(f"\n{revised_dict}")
    else:
        print("\nNo one is going to be lucky")
        print(f"\n{names_and_bills}")
