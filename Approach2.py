# Using the set 

"""
Using sets will discard all elements duplicate entries and then use that
to count each type of socks and later split by dividing by two and store
the results in a variable as a final return pair number.

"""

n = 9
def sockMerchant(n, ar):
    socks_pairs = 0
    # convert arr into a set and sote in a variable
    set_in_arr = set(ar)
    for i in set_in_arr:  # iterate through the new variable
        socks_pairs += int(ar.count(i) / 2)  #count the number of pairs in
    
    return socks_pairs   # return the results


arr = [10, 20, 20 ,10,  10, 30 ,50 , 10 , 20]

