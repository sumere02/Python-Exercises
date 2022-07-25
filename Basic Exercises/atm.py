import sys
print("""*******************
ATM
*******************

IS BANK

1. BALANCE AMOUNT

2. CASH DEPOSIT

3. CASH WITHDRAW

4. CARD RETURN

*******************""")

card_password = "4051"
card_balance = 23500
number = 5

while number > 0:
    password = input("Card Password: ")
    if(password == card_password):
        while True:
            operation = int(input("Operation: "))
            if(operation == 1):
                print("Balance: {} $".format(card_balance))
            elif(operation == 2):
                amount = float(input("Amount: "))
                card_balance += amount
            elif(operation == 3):
                amount = float(input("Amount: "))
                if(amount < card_balance):
                    print("Unvalid amount\n")
                else:
                    card_balance -= amount
            elif(operation == 4):
                print("Goodbye")
                break
            else:
                print("Please enter valid operation")
            while True:
                q = input("Do you want to continue(y/n): ")
                if(q != 'y' and q != 'n'):
                    print("Please enter valid input")
                else:
                    break
            if(q == 'n'):
                print("Goodbye")
                sys.exit()
    else:
        number -= 1
        if(number > 0):
            print("Chance left {}".format(number))
            print("Wrong password, Try again")
        else:
            print("Card locked")
