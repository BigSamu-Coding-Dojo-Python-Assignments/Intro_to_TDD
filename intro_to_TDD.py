# import the python testing framework
import unittest

# Excercise 1
# reverseList - Write a function that reverses the values in the list (without creating a temporary array).
# Example: reverseList([1,3,5]) should return [5,3,1]
# Example Test: assertEqual( reverseList([1,3,5]), [5,3,1] )
# Add at least 3 other test cases

print ("\n")
print ("*"*100)
print ("I) Running Test for reverseList Function")
print ("*"*100,"\n",)

# Function
def reverseList(list):
    for i in range(int(len(list)/2)):
       list[i], list[len(list)-i-1] = list[len(list)-i-1],list[i]
    return list

# Test of Function
class reverseArrayTests(unittest.TestCase):
    # Test 1 - List of Numbers
    def testOne(self):
        self.assertEqual(reverseList([1,2,3]), [3,2,1])
    # Test 2 - List of Lists
    def testTwo(self):
        self.assertEqual(reverseList([[1,2,3],[4,5,6],[7,8,9]]),[[7,8,9],[4,5,6],[1,2,3]])
    # Test 3 - List of Characters
    def testThree(self):
        self.assertEqual(reverseList(["h","e","l","l","o"]),["o","l","l","e","h"])

if __name__ == '__main__':
    unittest.main(reverseArrayTests(), exit = False) # this runs our tests
    
print ("\n")
print ("*"*100)
print ("II) Running Test for isPalindrome Function")
print ("*"*100,"\n",)

# Excercise 2
# isPalindrome - Write a function that checks whether the given word is a palindrome (a word that spells the same backward).
# Example: isPalindrome("racecar") should return True
# Example Test: assertEqual( isPalindrome("racecar"), True ) or assertTrue( isPalindrome("racecar"))
# Example Test: assertFalse( isPalindrome("rabcr") ).
# Add at least 5 other test cases

def isPalindrom(word):
    reversedWord = word[::-1] #slice operator is used in this case
    if word == reversedWord:
        return True
    else:
        return False

class isPalindromTests(unittest.TestCase):
    # Test 1 - Word "hello"
    def testOne(self):
        self.assertEqual(isPalindrom("hello"), False)
    # Test 2 - Word "civic"
    def testTwo(self):
        self.assertEqual(isPalindrom("civic"),True)
    # Test 3 - Word "stats"
    def testThree(self):
        self.assertEqual(isPalindrom("stats"),True)
    # Test 4 - Word "mountain"
    def testFour(self):
        self.assertEqual(isPalindrom("mountain"),False)
    # Test 5 - Word "refer"
    def testFive(self):
        self.assertEqual(isPalindrom("refer"),True)

if __name__ == '__main__':
    unittest.main(isPalindromTests(), exit = False) # this runs our tests


# Excercise 3
# coins - Write a function that determines how many quarters, dimes, nickels, and pennies to give to a customer for a change where you minimize the number of coins you give out.
# Example: given 87 cents, result should be 3 quarters, 1 dime, 0 nickel and 2 pennies
# Example Test: assertEqual( coin(87), [3,1,0,2] )
# Add at least 5 other test cases

print ("\n")
print ("*"*100)
print ("III) Running Test for coins Function")
print ("*"*100,"\n",)

def coins(amount):

    amount_resting = amount # rest of division

    quarters = int(amount_resting/25) # number of quarter
    amount_resting = amount_resting - quarters*25
    dimes = int(amount_resting/10) # number of dimes
    amount_resting = amount_resting - dimes*10
    nickels = int(amount_resting/5) # number of nickels
    amount_resting = amount_resting - nickels*5
    pennies = int(amount_resting/1) # number of pennies
    
    change = [quarters,dimes,nickels,pennies] #list that is going to return with the number of quarters, dimes, nickels, and pennies

    return change

class coinsTests(unittest.TestCase):
    # Test 1 - 87 cents
    def testOne(self):
        self.assertEqual(coins(87), [3,1,0,2])
    # Test 2 - 100 cents
    def testTwo(self):
        self.assertEqual(coins(100),[4,0,0,0])
    # Test 3 - 8 cents
    def testThree(self):
        self.assertEqual(coins(8),[0,0,1,3])
    # Test 4 - 44 cents
    def testFour(self):
        self.assertEqual(coins(44),[1,1,1,4])
    # Test 5 - 15 cents
    def testFive(self):
        self.assertEqual(coins(15),[0,1,1,0])

if __name__ == '__main__':
    unittest.main(coinsTests(), exit=False) # this runs our tests

# Excercise 4
# BONUS - factorial - Write a recursive function that returns the factorial of a given number. Remember that the factorial of a number is the product of all the numbers between 1 and the given number (eg. 4! = 4*3*2*1).
# Example: factorial(5) should return 120.
# Add at least 3 test cases

print ("\n")
print ("*"*100)
print ("IV) Running Test for Factorial Function")
print ("*"*100,"\n",)

def factorial(number):

    if (number > 0):
        result = number*factorial(number-1)
    elif number == 0:
        result = 1
    else:
        print("The argument given for the function has to be a number equal or greater than 0")
        result = False

    return result

class factorialTests(unittest.TestCase):
    # Test 1 - Factorial of 5
    def testOne(self):
        self.assertEqual(factorial(5), 120)
    # Test 2 - Factorial of 0
    def testTwo(self):
        self.assertEqual(factorial(0),1)
    # Test 3 - Factorial of -1
    def testThree(self):
        print("Test 3 - Testing number less than 0")
        self.assertEqual(factorial(-1),False)


if __name__ == '__main__':
    unittest.main(factorialTests(), exit=False) # this runs our tests

# Excercise 5
# BONUS - fibonacci - Write a recursive function that accepts a number, n, and returns the nth Fibonacci number from the sequence. The first two Fibonacci numbers are 0 and 1. Every number after that is calculated by adding the previous 2 numbers from the sequence. (i.e. 0, 1, 1, 2, 3, 5, 8, 13, 21 ...)
# Example: fibonacci(5) should return 5 (for n = 5 in the sequence the result is 5).
# Add at least 3 test cases

print ("\n")
print ("*"*100)
print ("V) Running Test for Fibonacci Function")
print ("*"*100,"\n",)

def fibonacci(n):

    #Fibonacci sequence is define as a[n]=a[n-1]+a[n-2], where a[0]=0 and a[1]=1
    
    if n == 0:
        fibonacciNumber = 0
    elif n == 1:
        fibonacciNumber = 1
    else:
        fibonacciNumber=fibonacci(n-1)+fibonacci(n-2)
    
    return fibonacciNumber

class fibonacciTests(unittest.TestCase):
    # Test 1 - Fibonacci of 5
    def testOne(self):
        self.assertEqual(fibonacci(5),5)
    # Test 2 - Fibonacci of 0
    def testTwo(self):
        self.assertEqual(fibonacci(0),0)
    # Test 3 - Fibonacci of 9
    def testThree(self):
        self.assertEqual(fibonacci(9),34)


if __name__ == '__main__':
    unittest.main(fibonacciTests(), exit=False) # this runs our tests
