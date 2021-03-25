import unittest
import Banking 

class Test_Banking(unittest.TestCase):
    def test_deposit(self):
        
        self.deposit_amount=1000
        min_deposit=10000

        message = "Invalid ."

 
        self.assertLessEqual(self.deposit_amount,min_deposit,message)


    def test_withdraw(self):
        self.withdraw_amount =500
        self.balance =1000

        message = "Insufficient balance"

        self.assertLess(self.withdraw_amount,self.balance,message)


if __name__ =='__main__':
    unittest.main()        