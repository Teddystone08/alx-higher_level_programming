#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x element from a list
    except:
        x represent the number of element of the list
        my_list is the source of list
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except index error:
            break
    print("")
    return (ret)
