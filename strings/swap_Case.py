import string

def swap_case(s):

    swapped_string = ""
    for char in s:
        if char in string.ascii_uppercase:
            swapped_string += char.lower()
        else:
            swapped_string += char.capitalize()
    return swapped_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)