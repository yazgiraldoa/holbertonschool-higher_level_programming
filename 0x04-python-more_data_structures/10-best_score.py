#!/usr/bin/python3


def best_score(a_dictionary):

    if a_dictionary:
        values_list = list(a_dictionary.values())
        keys_list = list(a_dictionary.keys())
        max_v = max(values_list)
        return keys_list[values_list.index(max_v)]
    return None
