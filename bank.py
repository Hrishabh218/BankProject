class Bank:
    b_name = 'Union Bank India'
    branch='Manikwar'
    IRFC= 'UBINO658875'
    ROI=0.1

    def __init__(self,name,accno,adhar,bal,pin) :
        self.name=name
        self.accno=accno
        self.adhar=adhar
        self.bal=bal
        self.pin=pin

    def change_pin(self):
        if self.pin == int(input('enter your pin :')):
            pin1= int(input('enter new your pin :'))
            pin2=int(input('re-enter new your pin :'))
    
            if pin1 == pin2:
                self.pin = pin1
                print('pin changed successfully') 
            else:
                print('pin not matched')

        else:
            print('invalid pin')

    def withdraw(self):
        if self.pin == int(input('enter your pin :')):
            amount=int(input('enter withdraw ammount :'))
            if self.bal>amount:
                print('amount withdraw successfully : ',amount)
                self.bal -= amount
                print('available balance is :', self.bal)

            else:
                print('enter valid amount')

        else:
            print('invalid pin')

    def deposit(self):
        if self.pin == int(input('enter your pin :')):
            amount=int(input('enter deposit ammount :'))
            
            self.bal += amount
            print('available balance is :', self.bal)

        else:
            print('invalid pin')

    def check_bal(self):
        if self.pin == int(input('enter your pin :')):
            
            print('available balance is :', self.bal)

        else:
            print('invalid pin')

        


    

        

C1=Bank('Ankit',397402010118017,1020304050,5000,6325)

# print(C1.bal)

# C1.change_pin()
# C1.withdraw()
# C1.deposit()
C1.check_bal()
print(C1.bal)



        

    
