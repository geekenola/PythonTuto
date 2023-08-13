print('****welcome to ATM****')
name=input("What is your name: ")
no=input("Enter card number: ")
PIN=int(input('create your PIN (remember! 10000>=PIN>=1000 )'))
while PIN>=10000 and PIN=="":
    print("PIN is not valid or you did not enter your PIN!")
    PIN=int(input('create your PIN (remember! 10000>=PIN>=1000 )'))
    mobnum="+996505912004"
A1=int(input("Enter your PIN"))

while A1!=PIN:
    print("pin is not correct!")
    A1=int(input("Enter your PIN"))
print("Select an option: ")
print("1. Check Balance ")
print("2. Cash withdraw ")
print("3. Show user Details ")
print("4. Update Mobile no. ")
print("5. Exit ")

A2=int(input("Select one of these input 1-5" ))
S=45000.0

if A2==1:
    print(f"Your bank balance is :{S}")
elif A2==2:
    C=float(input("Enter the amount : "))
    print("Collect Your Cash")
    print(f"Available Balance : {S-C}")
    T=S-C    
elif A2==3:
    print("***User Details are:")
    print(f"-> Account number: {no}")
    print(f"-> Name: {name}")
    print(f"Balance: {T}")
    print(f"Mobile No: {mobnum}")
elif A2==4:
    B=input("Enter Old Mobile No: ")
    while B!=mobnum:
        print("Incorrect old mobile number!")
        A3=input("Enter old mobile number again!")
    B1=input("Enter new mobile number: ")
    print("Mobile update was successful!")
elif A2==5:
    print("bye, Thank you for using our ATM bank!")