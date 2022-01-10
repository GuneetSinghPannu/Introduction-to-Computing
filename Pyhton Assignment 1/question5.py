Python 3.9.9 (main, Nov 19 2021, 00:00:00) 
[GCC 11.2.1 20210728 (Red Hat 11.2.1-1)] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
>>> color.pop(3)
'Black'
>>> color
['Red', 'Green', 'White', 'Pink', 'Yellow']
>>> color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
>>> color = color[0:3] + ['Purple'] + color[5:]
>>> color
['Red', 'Green', 'White', 'Purple', 'Yellow']
>>> 