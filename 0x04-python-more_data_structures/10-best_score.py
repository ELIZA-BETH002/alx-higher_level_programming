#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    max_value = max(a_dictionary.values())
    for best_k, v in a_dictionary.items():
        if max_value == v:
            return best_k
