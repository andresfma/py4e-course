import re

op = open("regex_sum_1798868.txt")
t_str = list()

#loop through the file for the numbers
for lines in op :
    lines = lines.rstrip()
    x = re.findall('[0-9]+', lines)
    if len(x) == 0 : continue
    t_str.extend(x)

#pass from string to integer the list 't_str'
t_int = list(map(int, t_str))

print(sum(t_int))