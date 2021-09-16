#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) is str:

        roman_char = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        int_list = [roman_char[value] for value in roman_string]
        n = 0

        if len(int_list) == 1:
            return int_list[0]

        for i in range(1, len(int_list)):

            if i == 1:
                if int_list[i - 1] >= int_list[i]:
                    n += int_list[i - 1] + int_list[i]
                else:
                    n += int_list[i] - int_list[i - 1]
            else:
                if int_list[i - 1] == int_list[i]:
                    n += int_list[i]
                elif int_list[i - 1] > int_list[i]:
                    if (i == (len(int_list) - 1)) or \
                       (i < len(int_list) and int_list[i] >= int_list[i + 1]):
                        n += int_list[i]
                else:
                    n += int_list[i] - int_list[i - 1]
        return n
    return 0
