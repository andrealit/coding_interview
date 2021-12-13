# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # check if each node knows the current node and 
        # if current down't know the other node
        
        # split into two: check to find a celebrity
        person = 0
        for i in range(1, n):
            if knows(i, person) and not knows(person, i):
                continue
            else:
                person = i
        for j in range(person):
            if not knows(j, person) or knows(person, j):
                return -1
        return person
    
    # time complexity: O(n) and space complexity: O(1)