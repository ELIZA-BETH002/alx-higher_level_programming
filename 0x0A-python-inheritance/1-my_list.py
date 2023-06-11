#!/usr/bin/python3

class MyList(list):

    def print_sorted(self):

        sorted_list = self[:]

        n = len(sorted_list)

        for i in range(n):

            for j in range(0, n-i-1):

                if sorted_list[j] > sorted_list[j+1]:

                    sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]

        print(sorted_list)
