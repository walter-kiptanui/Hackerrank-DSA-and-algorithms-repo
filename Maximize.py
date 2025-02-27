"""
You are given a function . You are also given  lists. The  list consists of  elements.

You have to pick one element from each list so that the value from the equation below is maximized:

%

 denotes the element picked from the  list . Find the maximized value  obtained.

 denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format

The first line contains  space separated integers  and .
The next  lines each contains an integer , denoting the number of elements in the  list, followed by  space separated integers denoting the elements in the list.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

def maximize(lists, M):
    combinations = product(*lists)
    f = lambda x:x*x
    S = max(sum(f(x) for x in combination)%M for combination in combinations)
    return S
    
if __name__=='__main__':
    K, M = map(int, input().split())
    lists = [list(map(int, input().split()[1:])) for _ in range(K)]
    
    print(maximize(lists, M))
    


