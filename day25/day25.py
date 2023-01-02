def snafu_to_decimal(string):
    dec = 0
    for index, x in enumerate(string[::-1]):
        if x == '=':
            dec += -2 * 5**(index)
        elif x == '-':
            dec += -1 * 5**(index)
        elif x == '1':
            dec += 1*5**(index)
        elif x == '2':
            dec += 2*5**(index)
    return dec


def decimal_to_snafu(integer):
    snafu = ''
    while integer:
        pass

def main():
    print(snafu_to_decimal('1=-0-2'))


if __name__ == '__main__':
    main()

# We need to return the sum of the inputs as a snafu number!