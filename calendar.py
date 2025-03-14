"""
Task

You are given a date. Your task is to find what the day is on that date.

Input Format

A single line of input containing the space separated month, day and year, 
respectively, in MM DD YYYY   format.

Constraints

Output Format

Output the correct day in capital letters.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

if __name__ == '__main__':
    
    month, day, year = map(int, input().split())
    days = {        
        0 : "Monday",
        1 : "Tuesday",
        2 : "Wednesday",
        3 : "Thursday",
        4 : "Friday",
        5 : "Saturday",
        6 : "Sunday",
    }
    
    my_day = calendar.weekday(year, month, day)
    print(days[my_day].upper())