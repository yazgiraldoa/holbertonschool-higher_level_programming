#!/usr/bin/python3
"""
Defining an inherited class
"""


class MyList(list):
    """
    Class MyList that inherits from list
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        new_list = self.copy()
        new_list.sort()
        print(new_list)
