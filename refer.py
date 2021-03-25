import time
class Atm_machine:
    def __init__(self,balance,pin):
        self.balance=balance
        self.pin=pin
        

    def swip_card(self):
        
    
        print("swip your card")
        #time.sleep(2.4)
        #pin=1234
        pin=int(input("Enter your 4 Digit pin:"))
        if pin==1234:
            
            print("""....WELCOME.....
            1.Balance Enquire
            2.Cash Withdrawl
            3.Deposite
            4.Change Pin
            5.Quit
            """) 
            option=int(input("enter your option:"))
            if option==1:
                self.check_balance()
            if option==2:
                self.withdrawl() 
            if option==3:
                self.deposit()
            if option==4:
                self.change_pin() 
            if option==5:
                self.quit()              
            return    
        else:
            print("incorrect pin number ")   
               
    def check_balance(self):
        #import pdb;pdb.set_trace()
        #balance = start_main()
        #option = start_main()
        #if option==1:
        
        print("A/c balance is ${}".format(self.balance))
        self.swip_card()
        #return option

            
    def withdrawl(self):        
        #if option==2:
            #import pdb;pdb.set_trace()
        print("A/c balance is ${}".format(self.balance))
        withdrawl_amount=int(input("Enter your withdrwal amount is :"))
        if withdrawl_amount>self.balance:
                #balance=(balance-withdrawl_amount)
            print("Current balance is less then your withdrawl")
        else: 
            self.balance=(self.balance-withdrawl_amount)

            print("""............Transaction Being Processed...........""")
            #time.sleep(2.4)
            print(""".............Collect Your Cash..........""")
            #time.sleep(2.4)
            print("your updated A/c balance is ${}".format(self.balance))
            self.swip_card()
                #option=int(input("enter your option:"))
    def deposit(self):
        #if option==3:
        print("A/c balance is ${}".format(self.balance))
        Deposit=int(input("Enter your deposite amount:"))
        if Deposit<0:
            print("invaild amount")
            
        else:
            self.balance=self.balance+Deposit
            print("your updated A/c balance is ${}".format(self.balance))
            self.swip_card()
                #option=int(input("enter your option:"))
    def change_pin(self):            
        #if option==4:
        pin=int(input("Enter your old pin:"))
        new_pin=int(input("Enter your new pin:"))
            
        if not pin == new_pin:
            print("your pin number changed")
            self.swip_card()    

        else:
            print("Invalid Pin Number")
                #option=int(input("enter your option:"))
            
    def quit(self):                    
        #if option==5:
        print("Thanks for your transaction")
            #option=int(input("enter your option:")
            
            
obj1=Atm_machine(50000,1234)
obj1.swip_card()   