"""
Task

Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

Input Format

The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and xi, the price of the shoe.

"""


def money_earned(shoe_sizes, customers):    
    total_money = 0
    for shoe_size, price in customers:
        if shoe_size in shoe_sizes: 
            total_money += price
            shoe_sizes.remove(shoe_size)
    return total_money

if __name__ == '__main__':
    X = int(input())
    shoe_sizes = list(map(int, input().split()))
    N = int(input())
    
    customers = [tuple(map(int, input().split())) for _ in range(N)]    
               
    print(money_earned(shoe_sizes, customers))  