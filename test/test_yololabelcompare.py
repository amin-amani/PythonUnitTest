
import unittest
import src


# or an object inside the antigravity module
from src.yololabelcompare import myobj

class testClass(unittest.TestCase):
    def test_add(self):
        obj =myobj()
        result=obj.add()
        self.assertEqual(result,3)
         

if __name__=='__main__':
    unittest.main()