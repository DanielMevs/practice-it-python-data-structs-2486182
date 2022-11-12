from collections import deque
import math 

def isPalindrone(dequeString):
    for i in range(math.floor(len(dequeString)/2)):
        del i
        leftItem = dequeString.popLeft()
        rightItem = dequeString.pop()
        # print('leftItem: ', leftItem)
        # print('rightItem: ', rightItem)
        if leftItem != rightItem:
            print('This word is not a palindrome')
            return False
    print('This word is a palindrome')
    return True

def main():
    #add code here
    testString = 'Tacocat'
    dequeString = deque(testString)
    return isPalindrone(dequeString=dequeString)

if __name__ == "__main__":
    main()