#!/usr/bin/python3
def uniq_add(my_list):
    unique_nums = set(my_list)  # Convert the list to a set to remove duplicates
    sum_result = sum(unique_nums)  # Compute the sum of unique integers
    return sum_result
