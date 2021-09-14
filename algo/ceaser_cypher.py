def shift_amount(num):
    # print(num%26)
    return num%26

def ceaserCypher(string,key):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    new_string = ''
    for i in string:
        if i in alpha:
            new_string += alpha[shift_amount(alpha.index(i)+key)]

    print(new_string)
    return new_string


string = 'xyz'
key = 2

ceaserCypher(string,key)
