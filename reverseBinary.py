#!/usr/bin/python

# Author: Forrest Alvarez

import sys

class reverser(object):

    def reverseIt(self, inNum):
        self.inNum = inNum
        revNum = int(((bin(int(self.inNum))[2:][::-1])), 2)
        return(revNum)

if not sys.stdin.isatty():
    data = sys.stdin.readlines()
    revInstance = reverser()
    for i in data:
        print(revInstance.reverseIt(i))
if __name__ == '__main__' and sys.stdin.isatty():
    revInstance = reverser()
    print(revInstance.reverseIt(47))
