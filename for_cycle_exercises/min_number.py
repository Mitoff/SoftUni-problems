import sys

line = input()

current_num = 0
min_num = sys.maxsize

while line != "Stop":
    current_num = int(line)

    if current_num < min_num:
        min_num = current_num

    line = input()

print(min_num)