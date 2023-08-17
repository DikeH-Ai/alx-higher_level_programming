#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = list(sorted(a_dictionary.items()))
    for i in new_dict:
        print(f"{i[0]}: {i[1]}")


if __name__ == "__main__":
    print_sorted_dictionary(a_dictionary={})
