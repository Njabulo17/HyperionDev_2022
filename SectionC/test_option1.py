import unittest
import option1


class MyTestCase(unittest.TestCase):

    def test_numeric_to_word01(self):
        
        results = option1.numeric_to_word(12)
        expected = "twelve"
        
        self.assertEqual(results, expected)


    def test_numeric_to_word02(self):
        
        results = option1.numeric_to_word(1)
        expected = "one"
        
        self.assertEqual(results, expected)
 
    
    def test_numeric_to_word03(self):
        
        results = option1.numeric_to_word(1000)
        expected = "one thousand"
        self.assertEqual(results, expected)


if __name__ == '__main__':
    unittest.main()
