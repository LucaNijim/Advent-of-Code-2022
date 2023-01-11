def matcher(snafu):
    """Takes in an iterable of snafu characters (=, -, 0, 1, 2) and outputs the iterable as a list
    but replacing the single char strings with the corresponding integer."""
    new_list = []
    for num in snafu:
        match num:
            case '0':
                app = 0
            case '-':
                app = -1
            case '=':
                app = -2
            case '1':
                app = 1
            case '2':
                app = 2
            case _:
                app = num
        new_list.append(app)
    return new_list


def add2snafu(s, num):
    """This function takes in two snafu numbers, s and num, and outputs their sum as a snafu number."""
    s, num = matcher(s[::-1]), matcher(num[::-1])
    # This reverses the strings
    if len(s) >= len(num):
        for _ in range(len(s) - len(num)):
            num.append(0)
    else:
        for _ in range(len(num) - len(s)):
            s.append(0)
    new_num = []
    carry = 0

    # New sum will be the return value
    # Carry would be the carry in the same sense as standard addition

    for i, _ in enumerate(s):
        # This loop determines the next digit
        if -2 <= (our_sum := (matcher(s)[i] + matcher(num)[i] + carry)) <= 2:
            new_num.append(our_sum)
            carry = 0
        elif our_sum > 2:
            carry = 1
            new_num.append(our_sum - 5)
        elif our_sum < -2:
            carry = -1
            new_num.append(our_sum + 5)
    new_num.append(carry)
    new_num.reverse()
    ret_string = ''
    for val in new_num:
        match val:
            case -2:
                ret_string += '='
            case -1:
                ret_string += '-'
            case 0:
                ret_string += '0'
            case 1:
                ret_string += '1'
            case 2:
                ret_string += '2'
    return ret_string


def add_n_snafu(list_of_args):
    """This function extends the add2snafu function to sum an iterable of n snafu numbers"""
    num = '0'
    for arg in list_of_args:
        num = add2snafu(num, arg)
    while num[0] == '0':  # This loop strips the extra 0s
        num = num[1:]
    return num


def main():
    with open('day25input.txt') as file:
        print(add_n_snafu(list(x.strip(' \n') for x in file.readlines())))


if __name__ == '__main__':
    main()