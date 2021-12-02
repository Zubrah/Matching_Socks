# Matching Socks Algorithim
# Scenario  and Problem Statements found in README.md

# My First Interpretation. 

"""
Matching socks would clearly mean matchung socks in pair of two elements that makes a pair of socks
from a given array of socks and finding the maximum number of possible matches/ pairs and leaving lone
elements as unpaired.

Things to consider here;
1. What is the maximum number of pairs of socks to be determined?
2. What would be best efficient way to pair the socks assuming no repetions is allowed?
3. What would be the best time complexity for the algorithm
4. Is sorting required first for the algorithm to work best?
"""

# Implementation.






# define the function 
def Matching_Socks(arr, arr_sizes):
    # dict to store the matching
    socks_buckets = {}
    for i in range(arr_sizes): 
        if arr.count(arr[i]) > 1:
            socks_buckets[arr[i]] = arr.count(arr[i])
    
    # use a hashset to match the socks pairs with key and values
    for key, value in socks_buckets.items():
        if socks_buckets[key] % 2 != 0:
            socks_buckets[key] = socks_buckets[key] - 1
            
    # values from keys matched
    values = socks_buckets.values()
    total = round(sum(values) / 2)
    return total
            
     
 
 # socks stored in an array
  
arr = [10, 20, 20 ,10,  10, 30 ,50 , 10 , 20]

arr_sizes = len(arr)
   
Matching_Socks(arr, arr_sizes)
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
