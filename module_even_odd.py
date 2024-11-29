def check(number=None):

    if not number.isdigit():
        return "You didn't enter a valid digit"
    else:
        if float(number) % 2 == 0:
            return "Its even"
            # return True
        else:
            return "Its odd"
            # return False
