#Write a Python program to calculate the number of days between two dates.
# a.Sample dates : (2014, 7, 2), (2014, 7, 11)

from datetime import date
print((date(2014, 7, 2) - date(2014, 7, 11)).days)