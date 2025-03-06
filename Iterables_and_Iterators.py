"""
The itertools module standardizes a core set of fast, memory efficient tools that are useful by
themselves or in combination. Together, they form an iterator algebra making it possible to construct 
specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.

You are given a list of N lowercase English letters. For a given integer K, you can select any K indices 
(assume 1-based indexing) with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: 'a'.

Input Format

The input consists of three lines. The first line contains the integer N, denoting the length of the list. 
The next line consists of N space-separated lowercase English letters, denoting the elements of the list.

The third and the last line of input contains the integer K, denoting the number of indices to be selected.

Output Format

Output a single line consisting of the probability that at least one of the K indices selected contains the letter:''.

"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

if __name__ == '__main__':
    N = int(input())
    list_N = input().strip().split()
    K = int(input())
    
    result = list(combinations(list_N, K))
    comb_length = len(result)
    my_sum = 0
    for combination in result:
        if 'a' in combination:
            my_sum += 1
    print(my_sum/comb_length)