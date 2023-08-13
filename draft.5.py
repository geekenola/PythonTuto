name="Erzhigit"
Account_num="123456"
mobile_num="+996505912004"
PIN = "1234"
balance=50000.67

def welcome():
    print("*****Welcome to ATM*****")

def checking():
    Entery_pin=input("enter you PIN: ")
    while PIN !="1234":
        Entery_pin=input("Invalid PIN! Enter your PIN again: ")
        
def selection():
    print("Select an options: ")
    print("1. Check Balance ")
    print("2. Cash withdraw ")
    print("3. Show user Details ")
    print("4. Update Mobile no. ")
    print("5. Exit ")

def balance_check():
    global balance
    print(f"you balance is {balance}\n")

def cash_withdraw():
    global balance
    withdraw_amount=float(input("Enter the amount you want to withdraw: "))
    if withdraw_amount>balance:
        print("inufficient amount!")
    else:
        print("collect your cash!")
        balance=balance - withdraw_amount
        print(f"available amount: {balance}")

def user_details():
    print("***User Details are:")
    print(f"-> Account number: {Account_num}")
    print(f"-> Name: {name}")
    print(f"Balance: {balance}")
    print(f"Mobile No: {mobile_num}")

def new_mobile_num():
    old_num=input("Enter Old Mobile No: ")
    while old_num!=mobile_num:
        print("Incorrect old mobile number!")
        old_num=input("Enter old mobile number again!")
    new_mnum=input("Enter new mobile number: ")
    while new_mnum.isdigit() == False:
        new_mnum=input("Invalid new number! Enter new mobile number(AGAIN): ")
    print("Mobile update was successful!")

Entery_pin=input("enter you PIN: ")
while Entery_pin != "1234":
    Entery_pin=input("Invalid PIN! Enter your PIN again: ")
        

while True:
    selection()
    choice_num=input("Select an option (1,2,3,4,5): ")
    if choice_num=="1":
        balance_check()
    elif choice_num=="2":
        cash_withdraw()
    elif choice_num=="3":
        user_details()
    elif choice_num=="4":
        new_mobile_num()
    elif choice_num=="5":
        break
    else:
        print("Invalid choice. Please select a valid option.")
        