#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lister = map(lambda a: replace if a == search else a, my_list)
    return list(lister)


if __name__ == '__main__':
    search_replace(my_list=[], search=0, replace=0)
