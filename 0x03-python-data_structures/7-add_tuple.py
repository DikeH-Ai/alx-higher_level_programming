#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    if len(list_a) == 1:
        list_a.append(0)
    elif len(list_a) < 1:
        list_a = [0, 0]

    if len(list_b) == 1:
        list_b.append(0)
    elif len(list_b) < 1:
        list_b = [0, 0]

    dataset_a = list_a[0] + list_b[0]
    dataset_b = list_a[1] + list_b[1]
    return (dataset_a, dataset_b)


if __name__ == "__main__":
    add_tuple(tuple_a=(), tuple_b=())
