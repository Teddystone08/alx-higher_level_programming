#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x element from a list
    except:
        x represent the number of element of the list
        my_list is the source of list
    """
    list = 0
    i = 0
    while (i < x):
        try:
            print(my_list[i], end="")
            list += 1
        except:
            i += 1
    print()
    return list
