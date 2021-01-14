#!/usr/bin/env python3
#
# Christopher Rodriguez
# CPSC 223p-03
# 2020-11-12
# chrisrod46@csu.fullerton.edu
#
"""DO NOT SUBMIT"""

def urlshortcode(num):

    def urlshortcode_help(num, num_ar):
        if num < 26:
            num_ar.append(chr(num + 97))

        elif num >= 26 and num < 52:
            num_ar.append(chr((num-26)+65))

        elif num >= 52 and num < 62:
            num_ar.append(str(num-52))

        elif num >= 62:
            urlshortcode_help( int(num/62), num_ar )
            urlshortcode_help(num % 62, num_ar)
        return num_ar
        #End of helper

    code_array = []
    short_code = ""
    urlshortcode_help(num, code_array)
    return short_code.join(code_array)


def orignalurl(changed):

    def orignalurl_help(string, list):
        count = 0

        for i in range(len(list)):
            if list[i].islower():
                count = count + (ord(list[i])-97)

            elif list[i].isupper():
                count = count + (ord(list[i])- 65 + 26)
            else:
                count = count + (int(list[i]) + 52)

        if len(list) > 1:
            return count + ( 61*( len(list)-1))

        return count
        #End of helper

    chan_list = []
    for i in range(len(changed)):
        chan_list.append(changed[i])

    return orignalurl_help(changed,chan_list)



import sys
def main():
    """This is the main function it will take in the number given """
    given = int(sys.argv[1])
    print("Final string")
    print(urlshortcode(given))

    after = urlshortcode(given)
    print(orignalurl(after))


if __name__ == '__main__':
    main()
