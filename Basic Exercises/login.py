print("""*****  
Login
*****""")

sys_id = "sumere20"
sys_password = "51259363712Es."
hearth = 10

while True:
    id = input("ID: ")
    password = input("Password: ")
    if id == sys_id and password == sys_password:
        print("Welcome {}\n".format(id))
        break
    else:
        hearth -= 1
        if(hearth > 0):
            print("ID or Password is uncorrect, Please try again.\n")
            q = 'e'
            while q != 'y' or q !='n':
                q = input("Do you want to continue(y/n): ")
                if(q != 'n' and q != 'y'):
                    print("Please enter a correct value")
                else:
                    break
            if(q == 'n'):
                print("Goodbye")
                break
        else:
            print("ID or Password is uncorrect system locked\n")
            break