Python 3.9.9 (main, Nov 19 2021, 00:00:00) 
[GCC 11.2.1 20210728 (Red Hat 11.2.1-1)] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> gInc = float(input("Enter your gross income: "))
Enter your gross income: 45000
>>> depen = int(input("Enter number of dependents"))
Enter number of dependents4
>>> stdDed = 10000
>>> depDed = 3000
>>> taxInc = gInc - stdDed - (depen*depDed)
>>> tax = taxInc/5
>>> print('Your income tax is : ', tax)
Your income tax is :  4600.0
>>> 