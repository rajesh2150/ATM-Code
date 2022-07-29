print('Welcome to Our ATM')
print("---------------------------------------")
a=10000 #var_amount
#name=Rajesh
n=int(input("Enter Your PIN :")); 
b=0000; #pin
if n==b:
   # c=(a-n); 

    option=int(input("1.Balance 2.Withdraw:"))
    if option==1:
         print('-------------------------------------')
         print("Available Balance is ",a); 
         print('-------------------------------------')
    elif option==2:
       # cash_type=input("Avalilable Cash Type is 1.100:");
        withdrawl_amount=int(input("Enter amount You want to withdraw:"));
        d=withdrawl_amount; 
        if d<=0:
          print("------------------------------------")
          print("Enter a Valid Amount")
          print("------------------------------------")
        elif d==0:
          print("------------------------------------")
          print("Amount Must Be Greater Than 0")
          print("------------------------------------")
        elif d>a:  
          print("------------------------------------")
           print("Insufficient Of Balance")
            print("------------------------------------")
        elif d>0 and d<=a:
          print("------------------------------------")
          print("Your amount is Debited of ",d);
          print('Welcome to Our ATM')
        print("---------------------------------------")
    else:
      print('-------------------------')
      print("Invalid Option Entered")
      print('-------------------------')
#user_name=input(" Enter Your Name:");
else:
    print('-------------------------------------')
    print("Invalid Pin Entered")
    print('-------------------------------------')
print("Thank Your For Visiting Our ATM");
print("Have a Great Day")
print("Made By Rajesh Korlapati")
