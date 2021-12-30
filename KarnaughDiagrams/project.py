# perse input
# accepted sigma(...) or sigma(...)+sigma*(...)
import re
import numpy as np

get_bin = lambda x, n: format(x, 'b').zfill(n)


def decimal_to_binary(n):
    return "{0:b}".format(n)


def convert_from_string_into_arrray(txt):
    b = txt.split(',')
    # print(b)
    c = [int(numberString) for numberString in b]
    digits_array = c
    # print(digits_array)
    return digits_array


def create_dictionary(sigma_input, nr_of_variables):
    if nr_of_variables == 3:
        max_value = 7
    else:
        max_value = 15
    dictionary = {}
    print("Empty Dictionary: ")
    print(dictionary)
    for i in range(0, max_value + 1):
        dictionary[i] = 0
    # print(dictionary)

    digits_array = convert_from_string_into_arrray(sigma_input)
    # print(digits_array)
    for element in range(0, len(digits_array)):
        dictionary[digits_array[element]] = 1

    print(dictionary)
    return dictionary


def create_sigmas_dictionary(sigmas_input, dictionary):
    digits_array = convert_from_string_into_arrray(sigmas_input)
    print(digits_array)
    for element in range(0, len(digits_array)):
        dictionary[digits_array[element]] = '*'

    print(dictionary)
    return dictionary


def print_truth_table(nr_of_variables, sigma_input, sigmas_input, sigmas_check):
    dictionary = create_dictionary(sigma_input, nr_of_variables)

    if sigmas_check == 1:
        dictionary_s = create_sigmas_dictionary(sigmas_input, dictionary)
    else:
        dictionary_s = dictionary
    if nr_of_variables == 3:
        var = "ABC T" + '\n'
        file1 = open("file1.txt", "w")
        file1.writelines(var)
        for i in range(0, 8):
            # convert int into binary +  generate string using key-value from dictionary
            txt = get_bin(i, 3) + ' ' + str(dictionary_s.get(i)) + '\n'
            file1.writelines(txt)

        file1.close()
    else:
        file2 = open("file2.txt", "w")
        var = "ABCD T" + '\n'
        file2.writelines(var)
        for i in range(0, 16):
            txt = get_bin(i, 4) + ' ' + str(dictionary_s.get(i)) + '\n'
            file2.writelines(txt)
        file2.close()


def check_nr_of_variables(nr_of_variables):
    if nr_of_variables > 4 or nr_of_variables < 3:
        return 0
    else:
        return nr_of_variables


def get_nr_of_variables(txt):
    digits_array = convert_from_string_into_arrray(txt)
    # print(digits_array)
    maxim = 0
    for element in range(0, len(digits_array)):
        # print(digits_array[element])
        digit = digits_array[element]
        # print(digit)
        if digit > maxim:
            maxim = digit

    binary_value_of_max = decimal_to_binary(maxim)
    # print("Reprezentarea binara a mixumului este:", binary_value_of_max)
    nr_of_variables = len(binary_value_of_max)
    # print("Nr de variabile", nr_of_variables)
    return nr_of_variables


def check_if_input_have_just_numbers(txt):
    b = txt.split(',')
    print(b)
    ok = 1
    for element in (0, len(b) - 1):
        if '15' > b[element] > '0':
            ok = 1
        else:
            ok = 0
            break
    return ok


def check_sigma_input(txt):
    # verificam daca forma sigma este corecta
    nr_of_variables = get_nr_of_variables(txt)
    # verificam daca sintaxa este corecta
    just_numbers = check_if_input_have_just_numbers(txt)
    if nr_of_variables != 0 and just_numbers != 0:
        return 1
    else:
        return 0


def compute_minimized_form(matrix, nr_of_var):
    function = ""
    if nr_of_var == 3:
        # verificam incepand  de la cele mai mari blocuri
        if matrix[0, 0] == ('1' or '*') and matrix[0, 1] == ('1' or '*') and matrix[1, 0] == ('1' or '*') and matrix[
            1, 1] == ('1' or '*'):
            function += "A' + "
            matrix[0, 0] = '0'
            matrix[0, 1] = '0'
            matrix[1, 0] = '0'
            matrix[1, 1] = '0'
        if matrix[0, 1] == ('1' or '*') and matrix[0, 2] == ('1' or '*') and matrix[1, 1] == ('1' or '*') and matrix[
            1, 2] == ('1' or '*'):
            function += "B + "
            matrix[0, 1] = '0'
            matrix[0, 2] = '0'
            matrix[1, 1] = '0'
            matrix[1, 2] = '0'
        if matrix[0, 2] == ('1' or '*') and matrix[0, 3] == ('1' or '*') and matrix[1, 2] == ('1' or '*') and matrix[
            1, 3] == ('1' or '*'):
            function += "A + "
            matrix[0, 2] = '0'
            matrix[0, 3] = '0'
            matrix[1, 2] = '0'
            matrix[1, 3] = '0'
        if matrix[0, 0] == ('1' or '*') and matrix[0, 3] == ('1' or '*') and matrix[1, 0] == ('1' or '*') and matrix[
            1, 3] == ('1' or '*'):
            function += "B' + "
            matrix[0, 0] = '0'
            matrix[0, 3] = '0'
            matrix[1, 2] = '0'
            matrix[1, 3] = '0'
        if matrix[1, 0] == ('1' or '*') and matrix[1, 1] == ('1' or '*') and matrix[1, 2] == ('1' or '*') and matrix[
            1, 3] == ('1' or '*'):
            function += "C + "
            matrix[0, 1] = '0'
            matrix[0, 2] = '0'
            matrix[1, 1] = '0'
            matrix[1, 2] = '0'
        if matrix[0, 0] == ('1' or '*') and matrix[0, 1] == ('1' or '*') and matrix[1, 0] == ('1' or '*') and matrix[
            1, 1] == ('1' or '*'):
            function += "C' + "
            matrix[0, 0] = '0'
            matrix[0, 1] = '0'
            matrix[1, 0] = '0'
            matrix[1, 1] = '0'

        # verificam blocurile de 2 elemente care au valoarea 1
        if matrix[0, 0] == ('1' or '*') and matrix[0, 1] == ('1' or '*'):
            function += "A'C' + "
            matrix[0, 0] = '0'
            matrix[0, 1] = '0'
        if matrix[0, 1] == ('1' or '*') and matrix[0, 2] == ('1' or '*'):
            function += "B C' + "
            matrix[0, 1] = '0'
            matrix[0, 2] = '0'
        if matrix[0, 2] == ('1' or '*') and matrix[0, 3] == ('1' or '*'):
            function += "A C' + "
            matrix[0, 2] = '0'
            matrix[0, 3] = '0'
        if matrix[0, 0] == ('1' or '*') and matrix[0, 3] == ('1' or '*'):
            function += "B' C' + "
            matrix[0, 0] = '0'
            matrix[0, 3] = '0'
        if matrix[1, 0] == ('1' or '*') and matrix[1, 1] == ('1' or '*'):
            function += "A' C' + "
            matrix[1, 0] = '0'
            matrix[1, 1] = '0'
        if matrix[1, 1] == ('1' or '*') and matrix[1, 2] == ('1' or '*'):
            function += "B C' + "
            matrix[1, 1] = '0'
            matrix[1, 2] = '0'
        if matrix[1, 2] == ('1' or '*') and matrix[1, 3] == ('1' or '*'):
            function += "A C + "
            matrix[1, 2] = '0'
            matrix[1, 3] = '0'
        if matrix[1, 0] == ('1' or '*') and matrix[1, 3] == ('1' or '*'):
            function += "B' C + "
            matrix[1, 0] = '0'
            matrix[1, 3] = '0'
        if matrix[0, 0] == ('1' or '*') and matrix[1, 0] == ('1' or '*'):
            function += "A' B' + "
            matrix[0, 0] = '0'
            matrix[1, 0] = '0'
        if matrix[0, 1] == ('1' or '*') and matrix[1, 1] == ('1' or '*'):
            function += "A' B + "
            matrix[0, 1] = '0'
            matrix[1, 1] = '0'
        if matrix[0, 2] == ('1' or '*') and matrix[1, 2] == ('1' or '*'):
            function += "A B + "
            matrix[0, 2] = '0'
            matrix[1, 2] = '0'
        if matrix[0, 3] == ('1' or '*') and matrix[1, 3] == ('1' or '*'):
            function += "A B' + "
            matrix[0, 3] = '0'
            matrix[1, 3] = '0'
        # 1 de 1
        if matrix[0, 0] == ('1' or '*'):
            function += "A' B' C' + "
            matrix[0, 0] = '0'
        if matrix[0, 1] == ('1' or '*'):
            function += "A' B C' + "
            matrix[0, 1] = '0'
        if matrix[0, 2] == ('1' or '*'):
            function += "A B C' + "
            matrix[0, 2] = '0'
        if matrix[0, 3] == ('1' or '*'):
            function += "A B' C' + "
            matrix[0, 3] = '0'
        if matrix[1, 0] == ('1' or '*'):
            function += "A' B' C + "
            matrix[1, 0] = '0'
        if matrix[1, 1] == ('1' or '*'):
            function += "A' B C + "
            matrix[1, 1] = '0'
        if matrix[1, 2] == ('1' or '*'):
            function += "A B C + "
            matrix[1, 2] = '0'
        if matrix[1, 3] == ('1' or '*'):
            function += "A B' C + "
            matrix[1, 3] = '0'
    else:
        if nr_of_var == 4:
            # cazul in care ave blocuri de 8 de 1
            if matrix[0, 0] == ('1' or '*') and matrix[0, 1] == ('1' or '*') and matrix[0, 2] == ('1' or '*') and \
                    matrix[0, 3] == ('1' or '*') and matrix[1, 0] == ('1' or '*') and matrix[1, 1] == ('1' or '*') and \
                    matrix[1, 2] == ('1' or '*') and matrix[1, 3] == ('1' or '*'):
                function += "A' + "
                matrix[0, 0] = '0'
                matrix[0, 1] = '0'
                matrix[0, 2] = '0'
                matrix[0, 3] = '0'
                matrix[1, 0] = '0'
                matrix[1, 1] = '0'
                matrix[1, 2] = '0'
                matrix[1, 3] = '0'
            if matrix[2, 0] == ('1' or '*') and matrix[2, 1] == ('1' or '*') and matrix[2, 2] == ('1' or '*') and \
                    matrix[2, 3] == ('1' or '*') and matrix[3, 0] == ('1' or '*') and matrix[3, 1] == ('1' or '*') and \
                    matrix[3, 2] == ('1' or '*') and matrix[3, 3] == ('1' or '*'):
                function += "A + "
                matrix[2, 0] = '0'
                matrix[2, 1] = '0'
                matrix[2, 2] = '0'
                matrix[2, 3] = '0'
                matrix[3, 0] = '0'
                matrix[3, 1] = '0'
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if matrix[0, 0] == ('1' or '*') and matrix[0, 1] == ('1' or '*') and matrix[1, 0] == ('1' or '*') and \
                    matrix[1, 1] == ('1' or '*') and matrix[2, 0] == ('1' or '*') and matrix[2, 1] == ('1' or '*') and \
                    matrix[3, 0] == ('1' or '*') and matrix[3, 1] == ('1' or '*'):
                function += "C' + "
                matrix[2, 0] = '0'
                matrix[2, 1] = '0'
                matrix[2, 2] = '0'
                matrix[2, 3] = '0'
                matrix[3, 0] = '0'
                matrix[3, 1] = '0'
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if matrix[0, 2] == ('1' or '*') and matrix[0, 3] == ('1' or '*') and matrix[1, 2] == ('1' or '*') and \
                    matrix[1, 3] == ('1' or '*') and matrix[2, 2] == ('1' or '*') and matrix[2, 3] == ('1' or '*') and \
                    matrix[3, 2] == ('1' or '*') and matrix[3, 3] == ('1' or '*'):
                function += "C + "
                matrix[0, 2] = '0'
                matrix[0, 3] = '0'
                matrix[1, 2] = '0'
                matrix[1, 3] = '0'
                matrix[2, 2] = '0'
                matrix[2, 3] = '0'
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if matrix[0, 0] == ('1' or '*') and matrix[1, 0] == ('1' or '*') and matrix[2, 0] == ('1' or '*') and \
                    matrix[3, 0] == ('1' or '*') and matrix[0, 3] == ('1' or '*') and matrix[1, 3] == ('1' or '*') and \
                    matrix[2, 3] == ('1' or '*') and matrix[3, 3] == ('1' or '*'):
                function += "D' + "
                matrix[0, 0] = '0'
                matrix[1, 0] = '0'
                matrix[2, 0] = '0'
                matrix[3, 0] = '0'
                matrix[0, 3] = '0'
                matrix[1, 3] = '0'
                matrix[2, 3] = '0'
                matrix[3, 3] = '0'
            if matrix[0, 0] == ('1' or '*') and matrix[1, 0] == ('1' or '*') and matrix[2, 0] == ('1' or '*') and \
                    matrix[3, 0] == ('1' or '*') and matrix[0, 3] == ('1' or '*') and matrix[1, 3] == ('1' or '*') and \
                    matrix[2, 3] == ('1' or '*') and matrix[3, 3] == ('1' or '*'):
                function += "D' + "
                matrix[0, 0] = '0'
                matrix[1, 0] = '0'
                matrix[2, 0] = '0'
                matrix[3, 0] = '0'
                matrix[0, 3] = '0'
                matrix[1, 3] = '0'
                matrix[2, 3] = '0'
                matrix[3, 3] = '0'
            if matrix[0, 0] == ('1' or '*') and matrix[0, 1] == ('1' or '*') and matrix[0, 2] == ('1' or '*') and \
                    matrix[0, 3] == ('1' or '*') and matrix[3, 0] == ('1' or '*') and matrix[3, 1] == ('1' or '*') and \
                    matrix[3, 2] == ('1' or '*') and matrix[3, 3] == ('1' or '*'):
                function += "B' + "
                matrix[0, 0] = '0'
                matrix[0, 1] = '0'
                matrix[0, 2] = '0'
                matrix[0, 3] = '0'
                matrix[3, 0] = '0'
                matrix[3, 1] = '0'
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if matrix[0, 1] == ('1' or '*') and matrix[0, 2] == ('1' or '*') and matrix[1, 1] == ('1' or '*') and \
                    matrix[1, 2] == ('1' or '*') and matrix[2, 1] == ('1' or '*') and matrix[2, 2] == ('1' or '*') and \
                    matrix[3, 1] == ('1' or '*') and matrix[3, 2] == ('1' or '*'):
                function += "D + "
                matrix[0, 1] = '0'
                matrix[0, 2] = '0'
                matrix[1, 1] = '0'
                matrix[1, 2] = '0'
                matrix[2, 1] = '0'
                matrix[2, 2] = '0'
                matrix[3, 1] = '0'
                matrix[3, 2] = '0'
            if matrix[1, 0] == ('1' or '*') and matrix[1, 1] == ('1' or '*') and matrix[1, 2] == ('1' or '*') and \
                    matrix[1, 3] == ('1' or '*') and matrix[2, 0] == ('1' or '*') and matrix[2, 1] == ('1' or '*') and \
                    matrix[2, 2] == ('1' or '*') and matrix[2, 3] == ('1' or '*'):
                function += "B + "
                matrix[1, 0] = '0'
                matrix[1, 1] = '0'
                matrix[1, 2] = '0'
                matrix[1, 3] = '0'
                matrix[2, 0] = '0'
                matrix[2, 1] = '0'
                matrix[2, 2] = '0'
                matrix[2, 3] = '0'
            # cazul in care ave blocuri de 4 de 1
            if matrix[0, 0] == ('1' or '*') and matrix[0, 1] == ('1' or '*') and matrix[0, 2] == ('1' or '*') and \
                    matrix[0, 3] == ('1' or '*'):
                function += "A' B' + "
                matrix[0, 0] = '0'
                matrix[0, 1] = '0'
                matrix[0, 2] = '0'
                matrix[0, 3] = '0'
            if matrix[1, 0] == ('1' or '*') and matrix[1, 1] == ('1' or '*') and matrix[1, 2] == ('1' or '*') and \
                    matrix[1, 3] == ('1' or '*'):
                function += "A' B + "
                matrix[1, 0] = '0'
                matrix[1, 1] = '0'
                matrix[1, 2] = '0'
                matrix[1, 3] = '0'
            if matrix[3, 0] == ('1' or '*') and matrix[3, 1] == ('1' or '*') and matrix[3, 2] == ('1' or '*') and \
                    matrix[3, 3] == ('1' or '*'):
                function += "A B' + "
                matrix[3, 0] = '0'
                matrix[3, 1] = '0'
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if matrix[2, 0] == ('1' or '*') and matrix[2, 1] == ('1' or '*') and matrix[2, 2] == ('1' or '*') and \
                    matrix[2, 3] == ('1' or '*'):
                function += "A B + "
                matrix[2, 0] = '0'
                matrix[2, 1] = '0'
                matrix[2, 2] = '0'
                matrix[2, 3] = '0'
            if matrix[2, 0] == ('1' or '*') and matrix[2, 1] == ('1' or '*') and matrix[3, 0] == ('1' or '*') and \
                    matrix[3, 1] == ('1' or '*'):
                function += "B C' + "
                matrix[2, 0] = '0'
                matrix[2, 1] = '0'
                matrix[3, 0] = '0'
                matrix[3, 1] = '0'
            if matrix[2, 2] == ('1' or '*') and matrix[2, 3] == ('1' or '*') and matrix[3, 2] == ('1' or '*') and \
                    matrix[3, 3] == ('1' or '*'):
                function += "B C + "
                matrix[2, 2] = '0'
                matrix[2, 3] = '0'
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if matrix[0, 0] == ('1' or '*') and matrix[0, 1] == ('1' or '*') and matrix[3, 0] == ('1' or '*') and \
                    matrix[3, 1] == ('1' or '*'):
                function += "B' C' + "
                matrix[0, 0] = '0'
                matrix[0, 1] = '0'
                matrix[3, 0] = '0'
                matrix[3, 1] = '0'
            if matrix[0, 2] == ('1' or '*') and matrix[0, 3] == ('1' or '*') and matrix[3, 2] == ('1' or '*') and \
                    matrix[3, 3] == ('1' or '*'):
                function += "B' C + "
                matrix[0, 2] = '0'
                matrix[0, 3] = '0'
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if matrix[2, 0] == ('1' or '*') and matrix[2, 1] == ('1' or '*') and matrix[3, 0] == ('1' or '*') and \
                    matrix[3, 1] == ('1' or '*'):
                function += "A C' + "
                matrix[2, 0] = '0'
                matrix[2, 1] = '0'
                matrix[3, 0] = '0'
                matrix[3, 1] = '0'
            if matrix[2, 2] == ('1' or '*') and matrix[2, 3] == ('1' or '*') and matrix[3, 2] == ('1' or '*') and \
                    matrix[3, 3] == ('1' or '*'):
                function += "A C + "
                matrix[2, 2] = '0'
                matrix[2, 3] = '0'
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if matrix[0, 0] == ('1' or '*') and matrix[0, 1] == ('1' or '*') and matrix[1, 0] == ('1' or '*') and \
                    matrix[1, 1] == ('1' or '*'):
                function += "A' C' + "
                matrix[0, 2] = '0'
                matrix[0, 1] = '0'
                matrix[1, 0] = '0'
                matrix[1, 1] = '0'
            if matrix[0, 2] == ('1' or '*') and matrix[0, 3] == ('1' or '*') and matrix[1, 2] == ('1' or '*') and \
                    matrix[1, 3] == ('1' or '*'):
                function += "A' C + "
                matrix[0, 2] = '0'
                matrix[0, 3] = '0'
                matrix[1, 2] = '0'
                matrix[1, 3] = '0'
            if matrix[0, 0] == ('1' or '*') and matrix[1, 0] == ('1' or '*') and matrix[0, 3] == ('1' or '*') and \
                    matrix[1, 3] == ('1' or '*'):
                function += "A' D' + "
                matrix[0, 0] = '0'
                matrix[1, 0] = '0'
                matrix[0, 3] = '0'
                matrix[1, 3] = '0'
            if matrix[2, 1] == ('1' or '*') and matrix[2, 2] == ('1' or '*') and matrix[3, 1] == ('1' or '*') and \
                    matrix[3, 2] == ('1' or '*'):
                function += "A D + "
                matrix[2, 1] = '0'
                matrix[2, 2] = '0'
                matrix[3, 1] = '0'
                matrix[3, 2] = '0'
            if matrix[0, 1] == ('1' or '*') and matrix[0, 2] == ('1' or '*') and matrix[1, 1] == ('1' or '*') and \
                    matrix[1, 2] == ('1' or '*'):
                function += "A' D + "
                matrix[0, 1] = '0'
                matrix[0, 2] = '0'
                matrix[1, 1] = '0'
                matrix[1, 2] = '0'
            if matrix[2, 0] == ('1' or '*') and matrix[3, 0] == ('1' or '*') and matrix[2, 3] == ('1' or '*') and \
                    matrix[3, 3] == ('1' or '*'):
                function += "A D' + "
                matrix[2, 0] = '0'
                matrix[3, 0] = '0'
                matrix[2, 3] = '0'
                matrix[3, 3] = '0'
            if matrix[1, 0] == ('1' or '*') and matrix[2, 0] == ('1' or '*') and matrix[1, 3] == ('1' or '*') and \
                    matrix[2, 3] == ('1' or '*'):
                function += "B D' + "
                matrix[1, 0] = '0'
                matrix[2, 0] = '0'
                matrix[1, 3] = '0'
                matrix[2, 3] = '0'
            if matrix[1, 1] == ('1' or '*') and matrix[1, 2] == ('1' or '*') and matrix[2, 1] == ('1' or '*') and \
                    matrix[2, 2] == ('1' or '*'):
                function += "B D + "
                matrix[1, 1] = '0'
                matrix[1, 2] = '0'
                matrix[2, 1] = '0'
                matrix[2, 2] = '0'
            if matrix[0, 1] == ('1' or '*') and matrix[0, 2] == ('1' or '*') and matrix[3, 1] == ('1' or '*') and \
                    matrix[3, 2] == ('1' or '*'):
                function += "B' D + "
                matrix[0, 1] = '0'
                matrix[0, 2] = '0'
                matrix[3, 1] = '0'
                matrix[3, 2] = '0'
            if matrix[0, 0] == ('1' or '*') and matrix[0, 3] == ('1' or '*') and matrix[3, 0] == ('1' or '*') and \
                    matrix[3, 3] == ('1' or '*'):
                function += "B' D' + "
                matrix[0, 0] = '0'
                matrix[0, 3] = '0'
                matrix[3, 0] = '0'
                matrix[3, 3] = '0'
            if matrix[0, 0] == ('1' or '*') and matrix[1, 0] == ('1' or '*') and matrix[2, 0] == ('1' or '*') and \
                    matrix[3, 0] == ('1' or '*'):
                function += "C' D' + "
                matrix[0, 0] = '0'
                matrix[1, 0] = '0'
                matrix[2, 0] = '0'
                matrix[3, 0] = '0'
            if matrix[0, 1] == ('1' or '*') and matrix[1, 1] == ('1' or '*') and matrix[2, 1] == ('1' or '*') and \
                    matrix[3, 1] == ('1' or '*'):
                function += "C' D + "
                matrix[0, 1] = '0'
                matrix[1, 1] = '0'
                matrix[2, 1] = '0'
                matrix[3, 1] = '0'
            if matrix[0, 2] == ('1' or '*') and matrix[1, 2] == ('1' or '*') and matrix[2, 2] == ('1' or '*') and \
                    matrix[3, 2] == ('1' or '*'):
                function += "C D + "
                matrix[0, 2] = '0'
                matrix[1, 2] = '0'
                matrix[2, 2] = '0'
                matrix[3, 2] = '0'
            if matrix[0, 3] == ('1' or '*') and matrix[1, 3] == ('1' or '*') and matrix[2, 3] == ('1' or '*') and \
                    matrix[3, 3] == ('1' or '*'):
                function += "C D' + "
                matrix[0, 3] = '0'
                matrix[1, 3] = '0'
                matrix[2, 3] = '0'
                matrix[3, 3] = '0'
            # cazul in care avem perechi de 1 -- cate 2
            if matrix[0, 0] == ('1' or '*') and matrix[0, 1] == ('1' or '*'):
                function += "A' B'  C' + "
                matrix[0, 0] = '0'
                matrix[0, 1] = '0'
            if matrix[0, 1] == ('1' or '*') and matrix[0, 2] == ('1' or '*'):
                function += "A' B' D + "
                matrix[0, 1] = '0'
                matrix[0, 2] = '0'
            if matrix[0, 2] == ('1' or '*') and matrix[0, 3] == ('1' or '*'):
                function += "A' B' C + "
                matrix[0, 2] = '0'
                matrix[0, 3] = '0'
            if matrix[0, 1] == ('1' or '*') and matrix[0, 3] == ('1' or '*'):
                function += "A' B' D' + "
                matrix[0, 1] = '0'
                matrix[0, 3] = '0'
            if matrix[1, 0] == ('1' or '*') and matrix[1, 1] == ('1' or '*'):
                function += "A' B C' + "
                matrix[1, 0] = '0'
                matrix[1, 1] = '0'
            if matrix[1, 1] == ('1' or '*') and matrix[1, 2] == ('1' or '*'):
                function += "A' B D + "
                matrix[1, 1] = '0'
                matrix[1, 2] = '0'
            if matrix[1, 2] == ('1' or '*') and matrix[1, 3] == ('1' or '*'):
                function += "A' B C + "
                matrix[1, 2] = '0'
                matrix[1, 3] = '0'
            if matrix[1, 0] == ('1' or '*') and matrix[1, 3] == ('1' or '*'):
                function += "A' B D' + "
                matrix[1, 0] = '0'
                matrix[1, 3] = '0'
            if matrix[2, 0] == ('1' or '*') and matrix[2, 1] == ('1' or '*'):
                function += "A B C' + "
                matrix[2, 0] = '0'
                matrix[2, 1] = '0'
            if matrix[2, 1] == ('1' or '*') and matrix[2, 2] == ('1' or '*'):
                function += "A B D + "
                matrix[2, 1] = '0'
                matrix[2, 2] = '0'
            if matrix[2, 2] == ('1' or '*') and matrix[2, 3] == ('1' or '*'):
                function += "A B C + "
                matrix[2, 2] = '0'
                matrix[2, 3] = '0'
            if matrix[2, 0] == ('1' or '*') and matrix[2, 3] == ('1' or '*'):
                function += "A B D' + "
                matrix[2, 0] = '0'
                matrix[2, 3] = '0'
            if matrix[3, 0] == ('1' or '*') and matrix[3, 1] == ('1' or '*'):
                function += "A B' D' + "
                matrix[3, 0] = '0'
                matrix[3, 3] = '0'
            if matrix[3, 1] == ('1' or '*') and matrix[3, 2] == ('1' or '*'):
                function += "A B' D + "
                matrix[3, 1] = '0'
                matrix[3, 2] = '0'
            if matrix[3, 2] == ('1' or '*') and matrix[3, 3] == ('1' or '*'):
                function += "A B' C + "
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if matrix[3, 0] == ('1' or '*') and matrix[3, 3] == ('1' or '*'):
                function += "A B' D' + "
                matrix[3, 0] = '0'
                matrix[3, 3] = '0'
            if matrix[0, 0] == ('1' or '*') and matrix[1, 0] == ('1' or '*'):
                function += "A' C' D' + "
                matrix[0, 0] = '0'
                matrix[1, 0] = '0'
            if matrix[0, 1] == ('1' or '*') and matrix[1, 1] == ('1' or '*'):
                function += "A' C' D + "
                matrix[0, 1] = '0'
                matrix[1, 1] = '0'
            if matrix[0, 2] == ('1' or '*') and matrix[1, 2] == ('1' or '*'):
                function += "A' C D + "
                matrix[0, 2] = '0'
                matrix[1, 2] = '0'
            if matrix[0, 3] == ('1' or '*') and matrix[1, 3] == ('1' or '*'):
                function += "A' C D' + "
                matrix[0, 3] = '0'
                matrix[1, 3] = '0'
            if matrix[1, 0] == ('1' or '*') and matrix[2, 0] == ('1' or '*'):
                function += "B C' D' + "
                matrix[1, 0] = '0'
                matrix[2, 0] = '0'
            if matrix[1, 1] == ('1' or '*') and matrix[2, 1] == ('1' or '*'):
                function += "B C' D + "
                matrix[1, 1] = '0'
                matrix[2, 1] = '0'
            if matrix[1, 2] == ('1' or '*') and matrix[2, 2] == ('1' or '*'):
                function += "B C D + "
                matrix[1, 2] = '0'
                matrix[2, 2] = '0'
            if matrix[1, 3] == ('1' or '*') and matrix[2, 3] == ('1' or '*'):
                function += "B C D' + "
                matrix[1, 3] = '0'
                matrix[2, 3] = '0'
            if matrix[2, 0] == ('1' or '*') and matrix[3, 0] == ('1' or '*'):
                function += "A C' D + "
                matrix[2, 0] = '0'
                matrix[3, 0] = '0'
            if matrix[2, 1] == ('1' or '*') and matrix[3, 1] == ('1' or '*'):
                function += "A C' D + "
                matrix[2, 1] = '0'
                matrix[3, 1] = '0'
            if matrix[2, 2] == ('1' or '*') and matrix[3, 2] == ('1' or '*'):
                function += "A C D + "
                matrix[2, 2] = '0'
                matrix[3, 2] = '0'
            if matrix[2, 3] == ('1' or '*') and matrix[3, 3] == ('1' or '*'):
                function += "A C D' + "
                matrix[2, 3] = '0'
                matrix[3, 3] = '0'
            if matrix[0, 0] == ('1' or '*') and matrix[3, 0] == ('1' or '*'):
                function += "B' C' D' + "
                matrix[0, 0] = '0'
                matrix[3, 0] = '0'
            if matrix[0, 3] == ('1' or '*') and matrix[3, 3] == ('1' or '*'):
                function += "B' C D' + "
                matrix[0, 3] = '0'
                matrix[3, 3] = '0'
            if matrix[0, 1] == ('1' or '*') and matrix[3, 1] == ('1' or '*'):
                function += "B' C' D + "
                matrix[0, 1] = '0'
                matrix[3, 1] = '0'
            if matrix[0, 2] == ('1' or '*') and matrix[3, 2] == ('1' or '*'):
                function += "B' C D + "
                matrix[0, 2] = '0'
                matrix[3, 2] = '0'
            if matrix[0, 3] == ('1' or '*') and matrix[3, 3] == ('1' or '*'):
                function += "B' C D' + "
                matrix[0, 3] = '0'
                matrix[3, 3] = '0'
            # cazul in care avem 1 de 1
            if matrix[0, 0] == ('1' or '*'):
                function += "A' B' C' D' + "
                matrix[0, 0] = '0'
            if matrix[0, 1] == ('1' or '*'):
                function += "A' B' C' D + "
                matrix[0, 1] = '0'
            if matrix[0, 2] == ('1' or '*'):
                function += "A' B' C D + "
                matrix[0, 2] = '0'
            if matrix[0, 3] == ('1' or '*'):
                function += "A' B' C D' + "
                matrix[0, 3] = '0'
            if matrix[1, 0] == ('1' or '*'):
                function += "A' B C' D' + "
                matrix[1, 0] = '0'
            if matrix[1, 1] == ('1' or '*'):
                function += "A' B C' D + "
                matrix[1, 1] = '0'
            if matrix[1, 2] == ('1' or '*'):
                function += "A' B C D + "
                matrix[1, 2] = '0'
            if matrix[1, 3] == ('1' or '*'):
                function += "A' B C D + "
                matrix[1, 3] = '0'
            if matrix[2, 0] == ('1' or '*'):
                function += "A B C' D' + "
                matrix[2, 0] = '0'
            if matrix[2, 1] == ('1' or '*'):
                function += "A B C' D + "
                matrix[2, 1] = '0'
            if matrix[2, 2] == ('1' or '*'):
                function += "A B C D + "
                matrix[2, 2] = '0'
            if matrix[2, 3] == ('1' or '*'):
                function += "A B C D' + "
                matrix[2, 3] = '0'
            if matrix[3, 0] == ('1' or '*'):
                function += "A B' C' D' + "
                matrix[3, 0] = '0'
            if matrix[3, 1] == ('1' or '*'):
                function += "A B' C' D + "
                matrix[3, 1] = '0'
            if matrix[3, 2] == ('1' or '*'):
                function += "A B' C D + "
                matrix[3, 2] = '0'
            if matrix[3, 3] == ('1' or '*'):
                function += "A B' C D + "
                matrix[3, 3] = '0'

    return function

def convert_from_fnd_to_fnc(fnd):
    s = fnd.replace(" ", "")
    x = s.replace("+", "*")
    y = x.replace("'", "#")
    new = "(" + y + ")"
    n_new = new
    print(new)
    for element in range(0, len(new)):
        # print(new[element])
        if new[element] == '*':
            n_new = new[0:element] + ")" + "*" + "(" + new[element + 1:]
            print(n_new)
    length = len(n_new)
    print(length)
    element = 0
    while element < length:
        # for element in range(0, length):
        print("Lungimea sirului este: ", length)
        print(element)
        print(n_new[element])
        if n_new[element] == 'D' or n_new[element] == 'A' or n_new[element] == 'B' or n_new[element] == 'C':
            if n_new[element + 1] != '#' and n_new[element + 1] != "'":
                n_new = n_new[0:element + 1] + "'" + n_new[element + 1:]
                length += 1
            if n_new[element + 2] == 'A' or n_new[element + 2] == 'B' or n_new[element + 2] == 'C' or\
                    n_new[element + 2] == 'D':
                n_new = n_new[0:element + 2] + "+" + n_new[element + 2:]
                length += 1
            if n_new[element + 1] == '#':
                n_new = n_new[0:element + 1] + "" + n_new[element + 1:]

        element += 1
    nn_new = n_new.replace("#", "")
    print(nn_new)
    return nn_new


#fnd = "A' B + C D "
#fnd = "A' C B + A' B "
#fnd = "C' D "
fnd = "A' B' C + A' "
fnc = convert_from_fnd_to_fnc(fnd)
print("Formula in FNC :", fnc)  # (A+B') * (C'+D')


def get_minimized_form_of_the_function(sigma_nr_of_var, sigma_input, sigmas_input, sigmas_correct):
    new_dictionary = {}
    if sigma_nr_of_var == 3:
        dictionary = create_dictionary(sigma_input, sigma_nr_of_var)
        if sigmas_correct == 1:
            new_dictionary = create_sigmas_dictionary(sigmas_input, dictionary)
        arr = np.array([[new_dictionary.get(0), new_dictionary.get(2), new_dictionary.get(6), new_dictionary.get(4)],
                        [new_dictionary.get(1), new_dictionary.get(3), new_dictionary.get(7), new_dictionary.get(5)]])
        for x in arr:
            print(x)
    else:
        dictionary = {}
        new_dictionary = {}
        if sigma_nr_of_var == 4:
            dictionary = create_dictionary(sigma_input, sigma_nr_of_var)
            if sigmas_correct == 1:
                new_dictionary = create_sigmas_dictionary(sigmas_input, dictionary)
            arr = np.array(
                [[new_dictionary.get(0), new_dictionary.get(1), new_dictionary.get(3), new_dictionary.get(2)],
                 [new_dictionary.get(4), new_dictionary.get(5), new_dictionary.get(7), new_dictionary.get(6)],
                 [new_dictionary.get(12), new_dictionary.get(13), new_dictionary.get(15), new_dictionary.get(14)],
                 [new_dictionary.get(8), new_dictionary.get(9), new_dictionary.get(11), new_dictionary.get(11)]
                 ])
        print("Matricea de valori ale functiei:")
        for x in arr:
            print(x)

    # return function_formula
    return arr


matrix = get_minimized_form_of_the_function(4, '1,5,9,13', '3,7,11,15', 1)
function = compute_minimized_form(matrix, 4)
size = len(function)
# Slice string to remove last 3 characters from string
mod_string = function[:size - 2]
print("Forma minimizata este: ", mod_string)


def get_expected_input(prompt):
    while True:
        value = "sigma(1,5,9,13)+sigma*(3,7,11,15)"
        line = value
        line = line.replace('(', 'l')
        line = line.replace(')', 'l')
        line = line.replace('+', 'o')
        line = re.sub('o', '', line)
        cut = line.split('l')

        # print(cut)
        sigmas_status = 0

        sigmas_n = 0
        sigmas_input = 0
        sigmas_nr_of_var = 0

        sigma_n = cut[0]
        sigma_input = cut[1]
        sigma_nr_of_var = get_nr_of_variables(sigma_input)

        if len(cut) > 3:
            sigmas_status = 1
            sigmas_n = cut[2]
            sigmas_input = cut[3]
            sigmas_nr_of_var = get_nr_of_variables(sigmas_input)

        print("Sigma name:", sigma_n)
        print("Sigma input:", sigma_input)
        print("Sigma nr of variables:", sigma_nr_of_var)

        print("Sigmas name:", sigmas_n)
        print("Sigmas input:", sigmas_input)
        print("Sigmas nr of variables:", sigmas_nr_of_var)
        print("Sigma* status:", sigmas_status)

        if sigmas_n == "sigma*" and check_sigma_input(sigmas_input) and sigmas_nr_of_var == sigma_nr_of_var:
            sigmas_correct = 1  # know if sigmas exists and is correct
        else:
            sigmas_correct = 0

        print("Sigma* correct status:", sigmas_correct)
        # ???pb with sigma correct 0???
        if sigma_n == "sigma" and check_sigma_input(sigma_input) and (sigmas_status == 0 or sigmas_correct == 1):
            print_truth_table(sigma_nr_of_var, sigma_input, sigmas_input, sigmas_correct)
            function = get_minimized_form_of_the_function(sigma_nr_of_var, sigma_input, sigmas_input, sigmas_correct)
            # print_fnc(function)
            # print_fnd(function)
        else:  # sintaxa si sematica corecte
            print(
                "Sorry, your response must be a valid input, like: sigma(.,.,...) or sigma(.,.,...)+sigma*(.,.,...)")

        return value


sigma = get_expected_input("Please enter sigma: ")
print(sigma)
print_truth_table(4, '1,2,3', '8,9,10', 1)
