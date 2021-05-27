class Atm(object):
    def __init__(self):
        self.balance= int(50000)


    def balanceEnquiry(self):
        print("Balance: ", self.balance)
        

    def withdraw(self):
        d=input("Enter the amount of withdrawal: ")
        x=int(d)
        print("Amount Withdrawn Successfully!!")
        db=self.balance-x
        print("Amount Withdrawn: ", x)
        print("Current Account Balance: ",db)
    
    def deposit(self):
        f=input("Enter the amount to be desposited: ")
        g=int(f)
        print("Amount Deposited Successfully!!")
        db=self.balance+g
        print("Amount Deposited: ", g)
        print("Current Account Balance Left: ",db)
    

AtmServerConnect=Atm()
pin=0000
print("Hint: PIN is 0000")
x=input("Enter PIN: ")
vv=int(x)
if vv==pin:
    gg=input("These are the codes for the following function: withdraw: 1, deposit: 2, balance enquiry: 3, Type the code: ")
    ff=int(gg)
    if ff==1:
        AtmServerConnect.withdraw()
    elif ff==2:
        AtmServerConnect.deposit()
    elif ff==3:
        AtmServerConnect.balanceEnquiry()
    else:
        print("Invalid Code Entered!")
else:
    print("Wrong PIN")