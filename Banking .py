import time
class Banking:



    def __init__(self):
        self.balance= 0
        self.deposit_amount=0
        self.withdraw_amount=0
        
    def welcome(self):
        print("---WELCOME---")
        time.sleep(1)
        print("Insert Card")
        time.sleep(1)
        print("Do not remove your card while transaction")
        time.sleep(2)
        user_input = input("Please Enter your PIN number: ")
        if len(user_input)!=4:
            print("incorrect pin,try again")
            
        else:
            print("1.Deposit Amount ")
            print("2.Withdraw Amount")
            print("3.Balance Enquiry")
            print("4.Exit")
    
                
  
    def main(self):
            user_input2=int(input("Enter the option :"))

            if user_input2==1:
                self.deposit()
    
            if user_input2==2:
                self.withdraw()

            if user_input2==3:
                self.enquiry_balance()    
            
            if user_input2==4:
                self.exit()
            
            
            
            else:
                print("incorrect")

                return self.main()
                 
      

    def deposit(self):
        
        #import pdb;pdb.set_trace()
        print("---Deposit---")
        self.deposit_amount=int(input('Enter the amount to deposit:'))
        if self.deposit_amount <=100:
            print("invalid")
        else:    
            print("Please wait while your transaction is processing....")
            time.sleep(2)
            if self.deposit_amount <=10000:
                self.balance += self.deposit_amount
                print('You have successfully deposited ₹ %d' %self.balance)
                self.main()
            else:
                print("Invalid")
                self.main()
                return self.balance
             
                
    def withdraw(self): 
       
        
        print("---Withdraw---")
        self.withdraw_amount=int(input('Enter the amount to withdraw:'))
        print("Please wait while your transaction is processing....")
        time.sleep(3)
        self.balance = self.deposit_amount
        if(self.withdraw_amount > self.balance):
            print('Transaction Failed,Insufficient Balance')
            self.main()
            return self.balance
          
        else:    
            print("please collect your cash")
            return self.main()
            
            

    def enquiry_balance(self):
        print("---Balance Enquiry---")
        self.balance-=self.withdraw_amount
        print('Your Remaining Balance = ₹%d' %self.balance)
        self.main()
        return self.balance
        
        

    def exit(self):
        print("Thankyou visit again")
       

    
banking=Banking()
banking.welcome()
banking.main()



