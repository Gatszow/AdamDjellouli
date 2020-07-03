

def linear_search(user_list: list, required_element, user=False):
    '''Linear Search Algorithm'''
    for index in range(len(user_list)):

        if user_list[index] == required_element:
            if user:
                return index+1
            return index

    return "{} is not in list".format(required_element)


def binary_search(user_list: list, required_element, user=False):
    '''Binary Search Algorithm'''
    leftside = 0
    rightside = len(user_list)

    while leftside <= rightside:
        middleoflist = leftside + int((rightside - leftside) / 2)

        if user_list[middleoflist] == required_element:
            if user:
                return middleoflist+1
            return middleoflist

        elif user_list[middleoflist] < required_element:
            leftside = middleoflist + 1

        else:
            rightside = middleoflist - 1

    return "{} is not in list".format(required_element)


class UsedTypeError(Exception):
    pass


def check(used_list: list, used_type):
    '''the check function checks if all elements of the list are of the same type'''
    try:
        if used_type == str or used_type == float or used_type == int or used_type == bool:
            numberofelements = 0
            elementsofthelist = len(used_list)
            for element in used_list:
                if type(element) is used_type:
                    numberofelements += 1
                    if numberofelements == elementsofthelist:
                        return True
                else:
                    return False
        else:
            raise UsedTypeError
    except UsedTypeError:
        return "You used wrong type!!!!" \
               "\nUse str, int, float or bool type."
