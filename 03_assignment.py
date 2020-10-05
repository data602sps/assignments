'''
Assignment #3
1. Add / modify code ONLY between the marked areas (i.e. "Place code below"). Do not modify or add code elsewhere.
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. To run unit tests simply use the below command after filling in all of the code:
    python 03_assignment.py
4. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
5. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
6. Do not use global variables
7. Use the test cases to infer requirements wherever feasible - not all exercises will have test cases
'''
import csv, json, math, pandas as pd, requests, unittest, uuid


# ------ Create your classes here \/ \/ \/ ------

#BankAccount class declaration below here




# Box class declaration below here


    
    
# ------ Create your classes here /\ /\ /\ ------




def exercise01():
    '''
    Create a class called BankAccount that has four attributes: bankname, firstname, lastname, and balance. 
    The default balance should be set to 0.  (Create your class above.)

    In addition, create ...
    - A method called depost() that allows the user to make deposts into their balance. 
    - A method called withdrawal() that allows the user to withdraw from their balance. 
    - Withdrawls may not exceed the available balance.  Hint: consider a conditional argument in your withdrawl() method.
    - Use the __str__() method in order to display the bank name, owner name, and current balance.

    In the function of exercise01():
    - Make a series of deposts and withdraws to test your class (below).

    '''

    # ------ Place code below here \/ \/ \/ ------
    class BankAccount:
        def __init__(self, bankname, firstname, lastname, balance=0):
            self.firstname = firstname
            self.lastname = lastname
            self.bankname = bankname
            self.balance = balance
            
        def deposit(self, amount):
            self.balance += amount
            return amount
        
        def withdrawal(self, amount):
            if self.balance - amount > 0:
                self.balance -= amount
                return amount
            else:
                return 'Your withdrawal amount is exceeds your account limit!'
            
        def __str__(self):
            print(f"{self.first} {self.last} bankaccount in {self.bankname} has balance {self.balance}")



    # ------ Place code above here /\ /\ /\ ------





def exercise02():

    '''
        Create a class Box that has attributes length and width that takes values for length and width upon construction (instantiation via the constructor). 
        Make sure to use Python 3 semantics. 
       
        In addition, create...
        - A method called render() that prints out to the screen a box made with asterisks of length and width dimensions
        - A method called invert() that switches length and width with each other
        - Methods get_area() and get_perimeter() that return appropriate geometric calculations
        - A method called double() that doubles the size of the box. Hint: Pay attention to return value here
        - Implement __eq__ so that two boxes can be compared using ==. Two boxes are equal if their respective lengths and widths are identical.
        - A method print_dim that prints to screen the length and width details of the box
        - A method get_dim that returns a tuple containing the length and width of the box
        - A method combine() that takes another box as an argument and increases the length and width by the dimensions of the box passed in
        - A method get_hypot() that finds the length of the diagonal that cuts throught the middle
        
        In the function exercise02():
        - Instantiate 3 boxes of dimensions 5,10 , 3,4 and 5,10 and assign to variables box1, box2 and box3 respectively 
        - Print dimension info for each using print_dim()
        - Evaluate if box1 == box2, and also evaluate if box1 == box3, print True or False to the screen accordingly
        - Combine box3 into box1 (i.e. box1.combine())
        - Double the size of box2
        - Combine box2 into box1
        - Using a for loop, iterate through and print the tuple received from calling box2's get_dim()
        - Find the size of the diagonal of box2
'''

    # ------ Place code below here \/ \/ \/ ------
    class Box:
        def __init__(self, length, width):
            self.length = length
            self.width = width
    
        def render(self):
            print('*' * self.width)
        
        
        def invert(self):
            self.length, self.width = self.width, self.length
        
        def get_area(self):
            return self.length * self.width
            
        def get_perimeter(self):
            return 2*(self.length + self.width)
        
        def double(self):
            self.length = 2 * self.length
            self.width = 2 * self.width 
            return 
    
        def __eq__(self, another):
            return self.length == another.length and self.width == another.width
    
        def print_dim(self):
            print(f"length = {self.length}")
            print(f"width = {self.width}")


        def get_dim(self):
            return (self.length, self.width)
    
        def combine (self,another):
            self.length = self.length + another.length
            self.width = self.width + another.width
        

    box1 = Box(5,10)
    box2 = Box(3,4)
    box3 = Box(5,10)

    box1.print_dim()     
    box2.print_dim() 
    box3.print_dim()      
        
    box1.__eq__(box2)
    box1.__eq__(box3)

    box1.combine(box3)
 
    box2.double()
 
    box2.combine(box1)

    print(box2.get_dim())






    # ------ Place code above here /\ /\ /\ ------





def exercise03():
    '''
    1. Read about avocado prices on Kaggle (https://www.kaggle.com/neuromusic/avocado-prices/home)
    2. Load the included avocado.csv file and display every line to the screen
    3. Use the imported csv library
    '''

    # ------ Place code below here \/ \/ \/ ------
    url = "https://www.kaggle.com/neuromusic/avocado-prices/home?select=avocado.csv"
    data = pd.read_csv(url,sep =',')
    data.describe()    
    
    
    # ------ Place code above here /\ /\ /\ ------


class TestAssignment3(unittest.TestCase):

    def test_exercise02(self):
        print('Testing exercise 2')
        b1, b2, b3 = exercise02()
        self.assertEqual(b1.get_length(),16)
        self.assertEqual(b1.get_width(),28)
        self.assertTrue(b1==Box(16,28))
        self.assertEqual(b2.get_length(),6)
        self.assertEqual(b2.get_width(),8)
        self.assertEqual(b3.get_length(),5)
        self.assertEqual(b2.get_hypot(),10)
        self.assertEqual(b1.double().get_length(),32)
        self.assertEqual(b1.double().get_width(),112)
        self.assertTrue(6 in b2.get_dim())
        self.assertTrue(8 in b2.get_dim())
        self.assertTrue(b2.combine(Box(1,1))==Box(7,9))

        
    def test_exercise03(self):
        print('Exercise 3 not tested')
        exercise03()
     

if __name__ == '__main__':
    unittest.main()
