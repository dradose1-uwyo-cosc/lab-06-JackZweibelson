# Jack Zwiebelson
# UWYO COSC 1010
# Submission date: 11/4/2024
# Sources: 
# https://www.geeksforgeeks.org/zellers-congruence-find-day-date/
# I knew of Zeller's Congruence, just needed a refresher, so I provided the source I used.
# I used ChatGPT to generate line 12 because i was struggling to work with the operations
# ChatGPT generated line 18,19 I just could not fugre it out and ChatGPT guided me to this answer

weekdays = {0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday"}

def leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def valid(mon, day, year):
    if mon < 1 or mon >12 or day <1:
        return False
    days_in_month = [31, 29 if leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return day <= days_in_month[mon - 1]

while True:
     t = True
     mon = ""
     day = ""
     year = ""
     op1 = False
     op2 = False
     y = input("Type 'exit' or give me a date formatted MM/DD/YYYY: ")
     if y.strip().lower()== "exit":
          break
     for i in y:
        if i.isdigit():
                if op1 is False and op2 is False:
                        mon += i
                elif op1 is True and op2 is False:
                        day += i
                else:
                        year += i
        elif not i.isdigit() and i != "/":
            print("Please enter the correct format.")
            break
        elif not i.isdigit() and op1 is False:
            op1 = True
        elif not i.isdigit() and op1 is True:
            op2 = True
     else:
        day = int(day)
        mon = int(mon)
        year = int(year)

        if not valid(mon,day,year):
            print(f'{y} Invalid Date')
            continue

        if mon == 1 or mon ==2:
            mon += 12
            year -= 1 


# Using the same varibales as Zeller's Congruence Fomrula
        k = year % 100
        j = year // 100

        x = -1 +(day + (13 * (mon + 1) // 5) + k + (k // 4) + (j // 4) - 2 * j) % 7
        if t == True:
            print(f'{y} {weekdays[x]}')
