#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniq_int = set(my_list)
    for number in uniq_int:
        sum += number
        return sum
