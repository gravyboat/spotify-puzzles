import unittest
import os
import sys

sys.path.insert(0, '../') # Using this because we don't have test discovery in 2.6

testValue = 47

class testReverseBinary(unittest.TestCase):

    def setUp(self):
        self.testValue = testValue

    def test_reverser(self):
        from reverseBinary import reverser
        reverseInstance = reverser()
        reversedTestValue = reverseInstance.reverseIt(self.testValue)
        print(reversedTestValue)
        self.assertEqual(reversedTestValue, 61, 'values do not match')

if __name__ == '__main__':
    unittest.main()
