print('****Welcome to ATM****')
name = "Erzhigit"
no=123456
mobnum="+996505912004"
PIN="1221"
PIN_Entery=int(input("Enter your PIN: "))
while True:
    if PIN_Entery!=PIN:
        print("PIN is not valid or you did not enter your PIN!")
        PIN=int(input('Enter your PIN (remember! 10000>=PIN>=1000 )'))
    elif PIN_Entery==PIN:
        break
print("Select an options: ")
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