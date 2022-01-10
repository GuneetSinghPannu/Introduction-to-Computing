Python 3.9.9 (main, Nov 19 2021, 00:00:00) 
[GCC 11.2.1 20210728 (Red Hat 11.2.1-1)] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> marks = []
>>> marks.append(int(input('Enter marks of first student: ')))
Enter marks of first student: 34
>>> marks.append(int(input('Enter marks of second student: ')))
Enter marks of second student: 42
>>> marks.append(int(input('Enter marks of third student: ')))
Enter marks of third student: 12
>>> marks.append(int(input('Enter marks of fourth student: ')))
Enter marks of fourth student: 47
>>> marks.append(int(input('Enter marks of fifth student: ')))
Enter marks of fifth student: 26
>>> marks.sort()
>>> print('Marks in sorted order: ', marks)
Marks in sorted order:  [12, 26, 34, 42, 47]
>>> 