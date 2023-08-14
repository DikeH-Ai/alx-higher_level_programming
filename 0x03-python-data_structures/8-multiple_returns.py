#!/usr/bin/python3
def multiple_returns(sentence):
    my_list = [None, None]
    if len(sentence) == 0:
        my_list[1] = None
    else:
        my_list[1] = sentence[0]
    my_list[0] = len(sentence)
    my_tuple = tuple(my_list)
    return my_tuple


if __name__ == "__main__":
    multiple_returns(sentence)
