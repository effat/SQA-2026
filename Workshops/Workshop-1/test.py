import unittest
import source  # type: ignore


class TestCalc(unittest.TestCase):
    def testSub1(self):
        self.assertEqual(1, source.performSub(3, 2), "Bug in code, check please!")
        

    def testSub2(self):
        self.assertEqual(4, source.performSub(6, 2), "Bug in code, check please!")
        
    def testAdd1(self):
        self.assertEqual(4, source.performAdd(1, 3), "Bug in code, check please!")
        
    def testAdd1(self):
        self.assertEqual(4, source.performAdd(1, 3), "Bug in code, check please!")
        
    
   
   
if __name__ == '__main__': 
    unittest.main()
