import math
import unittest
import random

#def wallis(i) :
  
        #x = int(input())
        #p=2.0
        #for x in range(1,i+1) :
            #l = (2.0 * i)/(2.0 * i - 1.0)
            #r = (2.0 * i)/(2.0 * i + 1.0)
            #t = (4.0*i*i)/((4.0*i*i)-1.0)
            #p = p*t
def wallis(n):
        pi = 0.0   
        for i in range(1, n):
            x = 4 * (i ** 2)
            y = x - 1
            z = float(x) / float(y)
            if (i == 1):
                pi = z
            else:
                pi *= z
        pi *= 2
        return pi

            
            
        return p
def monte_carlo(n) :
 
    #a = int(input())
    poc = 0
    pos = 0
    for i in range(0,n) :
        x = random.random()
        y = random.random()
        d = x*x + y*y
        if d<=1 :
          poc +=1
        pos +=1
        i +=1
    pi = 4 * (poc/pos)
    return pi
     
        
        
        
    

class TestWallis(unittest.TestCase):
    
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
   
            
    
if __name__ == "__main__":
    unittest.main()
