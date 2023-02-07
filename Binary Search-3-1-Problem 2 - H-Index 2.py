"""
FAANMG Problem #91 {Medium} 

275. H-Index II


# Time Complexity = O(log n)
# Space Complexity = O(1)

Did this code successfully run on Leetcode : Yes



@name: Rahul Govindkumar_RN27JUL2022
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        if citations == None or len(citations)==0:
            return 0
        
        n = len(citations)
        
        low = 0
        high = n-1
        
        while low <=high:

            mid = low +(high-low)//2
            diff = n - mid

            
            if citations[mid] == diff:
                return diff
            
            elif citations[mid] > diff:
                high = mid-1
                
            else:
                low = mid+1
                

        return n - low
        
 
    
 """
FAANMG Problem #91 {Medium} 

275. H-Index II


# Time Complexity = O(n)
# Space Complexity = O(1)


Did this code successfully run on Leetcode : Yes



@name: Rahul Govindkumar_RN27JUL2022
"""

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        if citations == None or len(citations)==0:
            return 0
        
        n = len(citations)
        
        for i in range(n):
            
            diff = n - i
            
            if diff <= citations[i]:
                return diff
            
        return 0
        