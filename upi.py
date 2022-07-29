pin=int(0000);
user_name=input("Enter your name :")
user_pin=int(input("Enter Your pin :"));
balance=int(10000);
if pin==user_pin:
    print('')
    print("Welocome",user_name)
    option=int(input(" 1.Balance 2.Send :"));
    if option==2:
        amount=int(input("Enter Amount to Send :"))
        if amount>balance:
                 print('-----------------------------------------')
                 print('You Entered Wromg Amount and Enter correctly')
                 print('-----------------------------------------')

        elif amount==0:
                print('-----------------------------------------')
                print("Amount Must Be Greater Than zero")
                print('-----------------------------------------')

        elif amount<=0:
            print('-----------------------------------------')
            print(' Negative Amount Not Valid ')
            print('-----------------------------------------')

       # c=balance-amount
        else:
            PIN1=int(input("Enter Your PIN:"))
            if PIN1==pin:
                 c=balance-amount
                 print('---------------------------------------------')
                 print("Your amount ",amount,"Debited Successfully")
                 print('---------------------------------------------')

                 print("Your Remaing balance is:",c);
        #elif amount>=balance:
                #print('You Entered Wromg Amount and Enter correctly')
       # elif amount==0:
                #print("Enter Greater Than zero")
            else:
               print('---------------------------------------------------')
               print("Entered PIN is Wrong And Enter A Correct PIN")
               print('---------------------------------------------------')
    
    else:
        print('')
        print('-----------------------------------------')
        print("Your Balance is",balance)
        print('-----------------------------------------')

else:
    print("Pin Not Valid")
print('Made By Rajesh Korlapati')
print("Thank you ")
