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
        file1 = open("file2.txt", "w")
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
    ok = 0
    for element in range(0, len(b)):
        print(b[element])
        if int(b[element]) in range(0, 16, 1):
            print(b[element])
            ok = 1
        else:
            ok = 0

    return ok


# print("Has just numbers: ", check_if_input_have_just_numbers("11,12,13,4,5,6"))

def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True


def check_if_duplicates(txt):
    b = txt.split(',')
    print(b)
    list_of_nr = list(b)
    result = checkIfDuplicates_1(list_of_nr)
    if result:
        # print('Yes, list contains duplicates')
        return 1
    else:
        # print('No duplicates found in list')
        return 0


def check_sigma_input(txt):
    # verificam daca forma sigma este corecta
    nr_of_variables = get_nr_of_variables(txt)
    print("Nr of variables:", nr_of_variables)
    # verificam daca sintaxa este corecta
    just_numbers = check_if_input_have_just_numbers(txt)
    print("Sigma input has just number value:", just_numbers)
    duplicates = check_if_duplicates(txt)
    print("Sigma input check if duplicates result:", duplicates)
    if nr_of_variables != 0 and just_numbers != 0 and duplicates == 0:
        return 1
    else:
        return 0


def compute_minimized_form(matrix, nr_of_var):
    print("Matricea din functie:", matrix)
    # print(matrix[0, 2])
    # print(matrix[0, 3])
    # print(matrix[1, 3])
    function = ""
    print("Nr of variables received in function:", nr_of_var)
    if nr_of_var == 3:
        print("Am ajuns unde trebuie...")
        # verificam incepand  de la cele mai mari blocuri
        if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[0, 1] == 1 or matrix[0, 1] == '*') \
                and (matrix[1, 0] == 1 or matrix[1, 0] == '*') \
                and (matrix[1, 1] == 1 or matrix[1, 1] == '*'):
            function += "A' + "
            matrix[0, 0] = '0'
            matrix[0, 1] = '0'
            matrix[1, 0] = '0'
            matrix[1, 1] = '0'
        if (matrix[0, 1] == 1 or matrix[0, 1] == '*') and (matrix[0, 2] == 1 or matrix[0, 2] == '*') \
                and (matrix[1, 1] == 1 or matrix[1, 1] == '*') and (matrix[1, 2] == 1 or matrix[1, 2] == '*'):
            function += "B + "
            matrix[0, 1] = '0'
            matrix[0, 2] = '0'
            matrix[1, 1] = '0'
            matrix[1, 2] = '0'
        if (matrix[0, 2] == 1 or matrix[0, 2] == '*') and (matrix[0, 3] == 1 or matrix[0, 3] == '*') \
                and (matrix[1, 2] == 1 or matrix[1, 2] == '*') \
                and (matrix[1, 3] == 1 or matrix[1, 3] == '*'):
            function += "A + "
            matrix[0, 2] = '0'
            matrix[0, 3] = '0'
            matrix[1, 2] = '0'
            matrix[1, 3] = '0'
        if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[0, 3] == 1 or matrix[0, 3] == '*') \
                and (matrix[1, 0] == 1 or matrix[1, 0] == '*') \
                and (matrix[1, 3] == 1 or matrix[1, 3] == '*'):
            function += "B' + "
            matrix[0, 0] = '0'
            matrix[0, 3] = '0'
            matrix[1, 2] = '0'
            matrix[1, 3] = '0'
        if (matrix[1, 0] == 1 or matrix[1, 0] == '*') and (matrix[1, 1] == 1 or matrix[1, 1] == '*') \
                and (matrix[1, 2] == 1 or matrix[1, 2] == '*') \
                and (matrix[1, 3] == 1 or matrix[1, 3] == '*'):
            function += "C + "
            matrix[0, 1] = '0'
            matrix[0, 2] = '0'
            matrix[1, 1] = '0'
            matrix[1, 2] = '0'
        if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[0, 1] == 1 or matrix[0, 1] == '*') \
                and (matrix[1, 0] == 1 or matrix[1, 0] == '*') \
                and (matrix[1, 1] == 1 or matrix[1, 1] == '*'):
            function += "C' + "
            matrix[0, 0] = '0'
            matrix[0, 1] = '0'
            matrix[1, 0] = '0'
            matrix[1, 1] = '0'

        # verificam blocurile de 2 elemente care au valoarea 1
        if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[0, 1] == 1 or matrix[0, 1] == '*'):
            function += "A'C' + "
            matrix[0, 0] = '0'
            matrix[0, 1] = '0'
        if (matrix[0, 1] == 1 or matrix[0, 1] == '*') and (matrix[0, 2] == 1 or matrix[0, 2] == '*'):
            function += "B C' + "
            matrix[0, 1] = '0'
            matrix[0, 2] = '0'

        if (matrix[0, 2] == 1 or matrix[0, 2] == '*') and (matrix[0, 3] == 1 or matrix[0, 3] == '*'):
            print("Am ajuns unde trebuie x222")
            function += "A C' + "
            matrix[0, 2] = '0'
            matrix[0, 3] = '0'
        print("Functia:", function)
        if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[0, 3] == 1 or matrix[0, 3] == '*'):
            function += "B' C' + "
            matrix[0, 0] = '0'
            matrix[0, 3] = '0'
        if (matrix[1, 0] == 1 or matrix[1, 0] == '*') and (matrix[1, 1] == 1 or matrix[1, 1] == '*'):
            function += "A' C' + "
            matrix[1, 0] = '0'
            matrix[1, 1] = '0'
        if (matrix[1, 1] == 1 or matrix[1, 1] == '*') and (matrix[1, 2] == 1 or matrix[1, 2] == '*'):
            function += "B C' + "
            matrix[1, 1] = '0'
            matrix[1, 2] = '0'
        if (matrix[1, 2] == 1 or matrix[1, 2] == '*') and (matrix[1, 3] == 1 or matrix[1, 3] == '*'):
            function += "A C + "
            matrix[1, 2] = '0'
            matrix[1, 3] = '0'
        if (matrix[1, 0] == 1 or matrix[1, 0] == '*') and (matrix[1, 3] == 1 or matrix[1, 3] == '*'):
            function += "B' C + "
            matrix[1, 0] = '0'
            matrix[1, 3] = '0'
        if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[1, 0] == 1 or matrix[1, 0] == '*'):
            function += "A' B' + "
            matrix[0, 0] = '0'
            matrix[1, 0] = '0'
        if (matrix[0, 1] == 1 or matrix[0, 1] == '*') and (matrix[1, 1] == 1 or matrix[1, 1] == '*'):
            function += "A' B + "
            matrix[0, 1] = '0'
            matrix[1, 1] = '0'
        if (matrix[0, 2] == 1 or matrix[0, 2] == '*') and (matrix[1, 2] == 1 or matrix[1, 2] == '*'):
            function += "A B + "
            matrix[0, 2] = '0'
            matrix[1, 2] = '0'
        if (matrix[0, 3] == 1 or matrix[0, 3] == '*') and (matrix[1, 3] == 1 or matrix[1, 3] == '*'):
            function += "A B' + "
            matrix[0, 3] = '0'
            matrix[1, 3] = '0'
        # 1 de 1
        if matrix[0, 0] == 1:
            function += "A' B' C' + "
            matrix[0, 0] = '0'
        if matrix[0, 1] == 1:
            function += "A' B C' + "
            matrix[0, 1] = '0'
        if matrix[0, 2] == 1:
            function += "A B C' + "
            matrix[0, 2] = '0'
        if matrix[0, 3] == 1:
            function += "A B' C' + "
            matrix[0, 3] = '0'
        if matrix[1, 0] == 1:
            function += "A' B' C + "
            matrix[1, 0] = '0'
        if matrix[1, 1] == 1:
            function += "A' B C + "
            matrix[1, 1] = '0'
        if matrix[1, 2] == 1:
            function += "A B C + "
            matrix[1, 2] = '0'
        if matrix[1, 3] == 1:
            function += "A B' C + "
            matrix[1, 3] = '0'
        return function
    else:
        if nr_of_var == 4:
            # cazul in care ave blocuri de 8 de 1
            if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[0, 1] == 1 or matrix[0, 1] == '*') \
                    and (matrix[0, 2] == 1 or matrix[0, 2] == '*') and \
                    (matrix[0, 3] == 1 or matrix[0, 3] == '*') and (matrix[1, 0] == 1 or matrix[1, 0] == '*') \
                    and (matrix[1, 1] == 1 or matrix[1, 1] == '*') and \
                    (matrix[1, 2] == 1 or matrix[1, 2] == '*') \
                    and (matrix[1, 3] == 1 or matrix[1, 3] == '*'):
                function += "A' + "
                matrix[0, 0] = '0'
                matrix[0, 1] = '0'
                matrix[0, 2] = '0'
                matrix[0, 3] = '0'
                matrix[1, 0] = '0'
                matrix[1, 1] = '0'
                matrix[1, 2] = '0'
                matrix[1, 3] = '0'
            if (matrix[2, 0] == 1 or matrix[2, 0] == '*') and (matrix[2, 1] == 1 or matrix[2, 1] == '*') \
                    and (matrix[2, 2] == 1 or matrix[2, 2] == '*') and \
                    (matrix[2, 3] == 1 or matrix[2, 3] == '*') \
                    and (matrix[3, 0] == 1 or matrix[3, 0] == '*') and (
                    matrix[3, 1] == 1 or matrix[3, 1] == '*') and \
                    (matrix[3, 2] == 1 or matrix[3, 2] == '*') and (matrix[3, 3] == 1 or matrix[3, 3] == '*'):
                function += "A + "
                matrix[2, 0] = '0'
                matrix[2, 1] = '0'
                matrix[2, 2] = '0'
                matrix[2, 3] = '0'
                matrix[3, 0] = '0'
                matrix[3, 1] = '0'
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[0, 1] == 1 or matrix[0, 1] == '*') \
                    and (matrix[1, 0] == 1 or matrix[1, 0] == '*') and \
                    (matrix[1, 1] == 1 or matrix[1, 1] == '*') and (matrix[2, 0] == 1 or matrix[2, 0] == '*') \
                    and (matrix[2, 1] == 1 or matrix[2, 1] == '*') and \
                    (matrix[3, 0] == 1 or matrix[3, 0] == '*') and (matrix[3, 1] == 1 or matrix[3, 1] == '*'):
                function += "C' + "
                matrix[2, 0] = '0'
                matrix[2, 1] = '0'
                matrix[2, 2] = '0'
                matrix[2, 3] = '0'
                matrix[3, 0] = '0'
                matrix[3, 1] = '0'
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if (matrix[0, 2] == 1 or matrix[0, 2] == '*') and (matrix[0, 3] == 1 or matrix[0, 3] == '*') and (
                    matrix[1, 2] == 1
                    or matrix[1, 2] == '*') and \
                    (matrix[1, 3] == 1 or matrix[1, 3] == '*') and (matrix[2, 2] == 1 or matrix[2, 2] == '*') \
                    and (matrix[2, 3] == 1 or matrix[2, 3] == '*') and \
                    (matrix[3, 2] == 1 or matrix[3, 2] == '*') and (matrix[3, 3] == 1 or matrix[3, 3] == '*'):
                function += "C + "
                matrix[0, 2] = '0'
                matrix[0, 3] = '0'
                matrix[1, 2] = '0'
                matrix[1, 3] = '0'
                matrix[2, 2] = '0'
                matrix[2, 3] = '0'
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[1, 0] == 1 or matrix[1, 0] == '*') \
                    and (matrix[2, 0] == 1 or matrix[2, 0] == '*') and \
                    (matrix[3, 0] == 1 or matrix[3, 0] == '*') and (matrix[0, 3] == 1 or matrix[0, 3] == '*') \
                    and (matrix[1, 3] == 1 or matrix[1, 3] == '*') and \
                    (matrix[2, 3] == 1 or matrix[2, 3] == '*') and \
                    (matrix[3, 3] == 1 or matrix[3, 3] == '*'):
                function += "D' + "
                matrix[0, 0] = '0'
                matrix[1, 0] = '0'
                matrix[2, 0] = '0'
                matrix[3, 0] = '0'
                matrix[0, 3] = '0'
                matrix[1, 3] = '0'
                matrix[2, 3] = '0'
                matrix[3, 3] = '0'
            if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[1, 0] == 1 or matrix[1, 0] == '*') \
                    and (matrix[2, 0] == 1 or matrix[2, 0] == '*') and \
                    (matrix[3, 0] == 1 or matrix[3, 0] == '*') and (matrix[0, 3] == 1 or matrix[3, 0] == '*') \
                    and (matrix[1, 3] == 1 or matrix[1, 3] == '*') and \
                    (matrix[2, 3] == 1 or matrix[2, 3] == '*') and (matrix[3, 3] == 1 or matrix[3, 3] == '*'):
                function += "D' + "
                matrix[0, 0] = '0'
                matrix[1, 0] = '0'
                matrix[2, 0] = '0'
                matrix[3, 0] = '0'
                matrix[0, 3] = '0'
                matrix[1, 3] = '0'
                matrix[2, 3] = '0'
                matrix[3, 3] = '0'
            if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[0, 1] == 1 or matrix[0, 1] == '*') \
                    and (matrix[0, 2] == 1 or matrix[0, 2] == '*') and \
                    (matrix[0, 3] == 1 or matrix[0, 3] == '*') and (matrix[3, 0] == 1 or matrix[3, 0] == '*') and \
                    (matrix[3, 1] == 1 or matrix[3, 1] == '*') and \
                    (matrix[3, 2] == 1 or matrix[3, 2] == '*') and (matrix[3, 3] == 1 or matrix[3, 3] == '*'):
                function += "B' + "
                matrix[0, 0] = '0'
                matrix[0, 1] = '0'
                matrix[0, 2] = '0'
                matrix[0, 3] = '0'
                matrix[3, 0] = '0'
                matrix[3, 1] = '0'
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if (matrix[0, 1] == 1 or matrix[0, 1] == '*') and (matrix[0, 2] == 1 or matrix[0, 2] == '*') \
                    and (matrix[1, 1] == 1 or matrix[1, 1] == '*') and \
                    (matrix[1, 2] == 1 or matrix[1, 2] == '*') and (matrix[2, 1] == 1 or matrix[2, 1] == '*') \
                    and (matrix[2, 2] == 1 or matrix[2, 2] == '*') and \
                    (matrix[3, 1] == 1 or matrix[3, 1] == '*') and (matrix[3, 2] == 1 or matrix[3, 2] == '*'):
                function += "D + "
                matrix[0, 1] = '0'
                matrix[0, 2] = '0'
                matrix[1, 1] = '0'
                matrix[1, 2] = '0'
                matrix[2, 1] = '0'
                matrix[2, 2] = '0'
                matrix[3, 1] = '0'
                matrix[3, 2] = '0'
            if (matrix[1, 0] == 1 or matrix[1, 0] == '*') and (matrix[1, 1] == 1 or matrix[1, 1] == '*') \
                    and (matrix[1, 2] == 1 or matrix[1, 2] == '*') and \
                    (matrix[1, 3] == 1 or matrix[1, 3] == '*') and (matrix[2, 0] == 1 or matrix[2, 0] == '*') \
                    and (matrix[2, 1] == 1 or matrix[2, 1] == '*') and \
                    (matrix[2, 2] == 1 or matrix[2, 2] == '*') and (matrix[2, 3] == 1 or matrix[2, 3] == '*'):
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
            if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[0, 1] == 1 or matrix[0, 1] == '*') \
                    and (matrix[0, 2] == 1 or matrix[0, 2] == '*') and \
                    (matrix[0, 3] == 1 or matrix[0, 3] == '*'):
                function += "A' B' + "
                matrix[0, 0] = '0'
                matrix[0, 1] = '0'
                matrix[0, 2] = '0'
                matrix[0, 3] = '0'
            if (matrix[1, 0] == 1 or matrix[1, 0] == '*') and (matrix[1, 1] == 1 or matrix[1, 1] == '*') \
                    and (matrix[1, 2] == 1 or matrix[1, 2] == '*') and (matrix[1, 3] == 1 or matrix[1, 3] == '*'):
                function += "A' B + "
                matrix[1, 0] = '0'
                matrix[1, 1] = '0'
                matrix[1, 2] = '0'
                matrix[1, 3] = '0'
            if (matrix[3, 0] == 1 or matrix[3, 0] == '*') and (matrix[3, 1] == 1 or matrix[3, 1] == '*') \
                    and (matrix[3, 2] == 1 or matrix[3, 2] == '*') and \
                    (matrix[3, 3] == 1 or matrix[3, 3] == '*'):
                function += "A B' + "
                matrix[3, 0] = '0'
                matrix[3, 1] = '0'
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if (matrix[2, 0] == 1 or matrix[2, 0] == '*') and (matrix[2, 1] == 1 or matrix[2, 1] == '*') \
                    and (matrix[2, 2] == 1 or matrix[2, 2] == '*') and \
                    (matrix[2, 3] == 1 or matrix[2, 3] == '*'):
                function += "A B + "
                matrix[2, 0] = '0'
                matrix[2, 1] = '0'
                matrix[2, 2] = '0'
                matrix[2, 3] = '0'
            if (matrix[2, 0] == 1 or matrix[2, 0] == '*') and (matrix[2, 1] == 1 or matrix[2, 1] == '*') \
                    and (matrix[3, 0] == 1 or matrix[3, 0] == '*') and (matrix[3, 1] == 1 or matrix[3, 1] == '*'):
                function += "B C' + "
                matrix[2, 0] = '0'
                matrix[2, 1] = '0'
                matrix[3, 0] = '0'
                matrix[3, 1] = '0'
            if (matrix[2, 2] == 1 or matrix[2, 2] == '*') and (matrix[2, 3] == 1 or matrix[2, 3] == '*') \
                    and (matrix[3, 2] == 1 or matrix[3, 2] == '*') and \
                    (matrix[3, 3] == 1 or matrix[3, 3] == '*'):
                function += "B C + "
                matrix[2, 2] = '0'
                matrix[2, 3] = '0'
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[0, 1] == 1 or matrix[0, 1] == '*') \
                    and (matrix[3, 0] == 1 or matrix[3, 0] == '*') and \
                    (matrix[3, 1] == 1 or matrix[3, 1] == '*'):
                function += "B' C' + "
                matrix[0, 0] = '0'
                matrix[0, 1] = '0'
                matrix[3, 0] = '0'
                matrix[3, 1] = '0'
            if (matrix[0, 2] == 1 or matrix[0, 2] == '*') and (matrix[0, 3] == 1 or matrix[0, 3] == '*') and \
                    (matrix[3, 2] == 1 or matrix[3, 2] == '*') and \
                    (matrix[3, 3] == 1 or matrix[3, 3] == '*'):
                function += "B' C + "
                matrix[0, 2] = '0'
                matrix[0, 3] = '0'
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if (matrix[2, 0] == 1 or matrix[2, 0] == '*') and (matrix[2, 1] == 1 or matrix[2, 1] == '*') \
                    and (matrix[3, 0] == 1 or matrix[3, 0] == '*') and \
                    (matrix[3, 1] == 1 or matrix[3, 1] == '*'):
                function += "A C' + "
                matrix[2, 0] = '0'
                matrix[2, 1] = '0'
                matrix[3, 0] = '0'
                matrix[3, 1] = '0'
            if (matrix[2, 2] == 1 or matrix[2, 2] == '*') and (matrix[2, 3] == 1 or matrix[2, 3] == '*') \
                    and (matrix[3, 2] == 1 or matrix[3, 2] == '*') and \
                    (matrix[3, 3] == 1 or matrix[3, 3] == '*'):
                function += "A C + "
                matrix[2, 2] = '0'
                matrix[2, 3] = '0'
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[0, 1] == 1 or matrix[0, 1] == '*') \
                    and (matrix[1, 0] == 1 or matrix[1, 0] == '*') and \
                    (matrix[1, 1] == 1 or matrix[1, 1] == '*'):
                function += "A' C' + "
                matrix[0, 2] = '0'
                matrix[0, 1] = '0'
                matrix[1, 0] = '0'
                matrix[1, 1] = '0'
            if (matrix[0, 2] == 1 or matrix[0, 2] == '*') and (matrix[0, 3] == 1 or matrix[0, 3] == '*') \
                    and (matrix[1, 2] == 1 or matrix[1, 2] == '*') and \
                    (matrix[1, 3] == 1 or matrix[1, 3] == '*'):
                function += "A' C + "
                matrix[0, 2] = '0'
                matrix[0, 3] = '0'
                matrix[1, 2] = '0'
                matrix[1, 3] = '0'
            if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[1, 0] == 1 or matrix[1, 0] == '*') \
                    and (matrix[0, 3] == 1 or matrix[0, 3] == '*') and \
                    (matrix[1, 3] == 1 or matrix[1, 3] == '*'):
                function += "A' D' + "
                matrix[0, 0] = '0'
                matrix[1, 0] = '0'
                matrix[0, 3] = '0'
                matrix[1, 3] = '0'
            if (matrix[2, 1] == 1 or matrix[2, 1] == '*') and (matrix[2, 2] == 1 or matrix[2, 2] == '*') \
                    and (matrix[3, 1] == 1 or matrix[3, 1] == '*') and \
                    (matrix[3, 2] == 1 or matrix[3, 2] == '*'):
                function += "A D + "
                matrix[2, 1] = '0'
                matrix[2, 2] = '0'
                matrix[3, 1] = '0'
                matrix[3, 2] = '0'
            if (matrix[0, 1] == 1 or matrix[0, 1] == '*') and (matrix[0, 2] == 1 or matrix[0, 2] == '*') \
                    and (matrix[1, 1] == 1 or matrix[1, 1] == '*') and \
                    (matrix[1, 2] == 1 or matrix[1, 2] == '*'):
                function += "A' D + "
                matrix[0, 1] = '0'
                matrix[0, 2] = '0'
                matrix[1, 1] = '0'
                matrix[1, 2] = '0'
            if (matrix[2, 0] == 1 or matrix[2, 0] == '*') and (matrix[3, 0] == 1 or matrix[3, 0] == '*') \
                    and (matrix[2, 3] == 1 or matrix[2, 3] == '*') and \
                    (matrix[3, 3] == 1 or matrix[3, 3] == '*'):
                function += "A D' + "
                matrix[2, 0] = '0'
                matrix[3, 0] = '0'
                matrix[2, 3] = '0'
                matrix[3, 3] = '0'
            if (matrix[1, 0] == 1 or matrix[1, 0] == '*') and (matrix[2, 0] == 1 or matrix[2, 0] == '*') \
                    and (matrix[1, 3] == 1 or matrix[1, 3] == '*') and \
                    (matrix[2, 3] == 1 or matrix[2, 3] == '*'):
                function += "B D' + "
                matrix[1, 0] = '0'
                matrix[2, 0] = '0'
                matrix[1, 3] = '0'
                matrix[2, 3] = '0'
            if (matrix[1, 1] == 1 or matrix[1, 1] == '*') and (matrix[1, 2] == 1 or matrix[1, 2] == '*') \
                    and (matrix[2, 1] == 1 or matrix[2, 1] == '*') and \
                    (matrix[2, 2] == 1 or matrix[2, 2] == '*'):
                function += "B D + "
                matrix[1, 1] = '0'
                matrix[1, 2] = '0'
                matrix[2, 1] = '0'
                matrix[2, 2] = '0'
            if (matrix[0, 1] == 1 or matrix[0, 1] == '*') and (matrix[0, 2] == 1 or matrix[0, 2] == '*') \
                    and (matrix[3, 1] == 1 or matrix[3, 1] == '*') and \
                    (matrix[3, 2] == 1 or matrix[3, 2] == '*'):
                function += "B' D + "
                matrix[0, 1] = '0'
                matrix[0, 2] = '0'
                matrix[3, 1] = '0'
                matrix[3, 2] = '0'
            if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[0, 3] == 1 or matrix[0, 3] == '*') \
                    and (matrix[3, 0] == 1 or matrix[3, 0] == '*') and \
                    (matrix[3, 3] == 1 or matrix[3, 3] == '*'):
                function += "B' D' + "
                matrix[0, 0] = '0'
                matrix[0, 3] = '0'
                matrix[3, 0] = '0'
                matrix[3, 3] = '0'
            if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[1, 0] == 1 or matrix[1, 0] == '*') \
                    and (matrix[2, 0] == 1 or matrix[2, 0] == '*') and \
                    (matrix[3, 0] == 1 or matrix[3, 0] == '*'):
                function += "C' D' + "
                matrix[0, 0] = '0'
                matrix[1, 0] = '0'
                matrix[2, 0] = '0'
                matrix[3, 0] = '0'
            if (matrix[0, 1] == 1 or matrix[0, 1] == '*') and (matrix[1, 1] == 1 or matrix[1, 1] == '*') \
                    and (matrix[2, 1] == 1 or matrix[2, 1] == '*') and \
                    (matrix[3, 1] == 1 or matrix[3, 1] == '*'):
                function += "C' D + "
                matrix[0, 1] = '0'
                matrix[1, 1] = '0'
                matrix[2, 1] = '0'
                matrix[3, 1] = '0'
            if (matrix[0, 2] == 1 or matrix[0, 2] == '*') and (matrix[1, 2] == 1 or matrix[1, 2] == '*') \
                    and (matrix[2, 2] == 1 or matrix[2, 2] == '*') and \
                    (matrix[3, 2] == 1 or matrix[3, 2] == '*'):
                function += "C D + "
                matrix[0, 2] = '0'
                matrix[1, 2] = '0'
                matrix[2, 2] = '0'
                matrix[3, 2] = '0'
            if (matrix[0, 3] == 1 or matrix[0, 3] == '*') and (matrix[1, 3] == 1 or matrix[1, 3] == '*') \
                    and (matrix[2, 3] == 1 or matrix[2, 3] == '*') and \
                    (matrix[3, 3] == 1 or matrix[3, 3] == '*'):
                function += "C D' + "
                matrix[0, 3] = '0'
                matrix[1, 3] = '0'
                matrix[2, 3] = '0'
                matrix[3, 3] = '0'
            # cazul in care avem perechi de 1 -- cate 2
            if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[0, 1] == 1 or matrix[0, 1] == '*'):
                function += "A' B'  C' + "
                matrix[0, 0] = '0'
                matrix[0, 1] = '0'
            if (matrix[0, 1] == 1 or matrix[0, 1] == '*') and (matrix[0, 2] == 1 or matrix[0, 2] == '*'):
                function += "A' B' D + "
                matrix[0, 1] = '0'
                matrix[0, 2] = '0'
            if (matrix[0, 2] == 1 or matrix[0, 2] == '*') and (matrix[0, 3] == 1 or matrix[0, 3] == '*'):
                function += "A' B' C + "
                matrix[0, 2] = '0'
                matrix[0, 3] = '0'
            if (matrix[0, 1] == 1 or matrix[0, 1] == '*') and (matrix[0, 3] == 1 or matrix[0, 3] == '*'):
                function += "A' B' D' + "
                matrix[0, 1] = '0'
                matrix[0, 3] = '0'
            if (matrix[1, 0] == 1 or matrix[1, 0] == '*') and (matrix[1, 1] == 1 or matrix[1, 1] == '*'):
                function += "A' B C' + "
                matrix[1, 0] = '0'
                matrix[1, 1] = '0'
            if (matrix[1, 1] == 1 or matrix[1, 1] == '*') and (matrix[1, 2] == 1 or matrix[1, 2] == '*'):
                function += "A' B D + "
                matrix[1, 1] = '0'
                matrix[1, 2] = '0'
            if (matrix[1, 2] == 1 or matrix[1, 2] == '*') and (matrix[1, 3] == 1 or matrix[1, 3] == '*'):
                function += "A' B C + "
                matrix[1, 2] = '0'
                matrix[1, 3] = '0'
            if (matrix[1, 0] == 1 or matrix[1, 0] == '*') and (matrix[1, 3] == 1 or matrix[1, 3] == '*'):
                function += "A' B D' + "
                matrix[1, 0] = '0'
                matrix[1, 3] = '0'
            if (matrix[2, 0] == 1 or matrix[2, 0] == '*') and (matrix[2, 1] == 1 or matrix[2, 1] == '*'):
                function += "A B C' + "
                matrix[2, 0] = '0'
                matrix[2, 1] = '0'
            if (matrix[2, 1] == 1 or matrix[2, 1] == '*') and (matrix[2, 2] == 1 or matrix[2, 2] == '*'):
                function += "A B D + "
                matrix[2, 1] = '0'
                matrix[2, 2] = '0'
            if (matrix[2, 2] == 1 or matrix[2, 2] == '*') and (matrix[2, 3] == 1 or matrix[2, 3] == '*'):
                function += "A B C + "
                matrix[2, 2] = '0'
                matrix[2, 3] = '0'
            if (matrix[2, 0] == 1 or matrix[2, 0] == '*') and (matrix[2, 3] == 1 or matrix[2, 3] == '*'):
                function += "A B D' + "
                matrix[2, 0] = '0'
                matrix[2, 3] = '0'
            if (matrix[3, 0] == 1 or matrix[3, 0] == '*') and (matrix[3, 1] == 1 or matrix[3, 1] == '*'):
                function += "A B' D' + "
                matrix[3, 0] = '0'
                matrix[3, 3] = '0'
            if (matrix[3, 1] == 1 or matrix[3, 1] == '*') and (matrix[3, 2] == 1 or matrix[3, 2] == '*'):
                function += "A B' D + "
                matrix[3, 1] = '0'
                matrix[3, 2] = '0'
            if (matrix[3, 2] == 1 or matrix[3, 2] == '*') and (matrix[3, 3] == 1 or matrix[3, 3] == '*'):
                function += "A B' C + "
                matrix[3, 2] = '0'
                matrix[3, 3] = '0'
            if (matrix[3, 0] == 1 or matrix[3, 0] == '*') and (matrix[3, 3] == 1 or matrix[3, 3] == '*'):
                function += "A B' D' + "
                matrix[3, 0] = '0'
                matrix[3, 3] = '0'
            if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[1, 0] == 1 or matrix[1, 0] == '*'):
                function += "A' C' D' + "
                matrix[0, 0] = '0'
                matrix[1, 0] = '0'
            if (matrix[0, 1] == 1 or matrix[0, 1] == '*') and (matrix[1, 1] == 1 or matrix[1, 1] == '*'):
                function += "A' C' D + "
                matrix[0, 1] = '0'
                matrix[1, 1] = '0'
            if (matrix[0, 2] == 1 or matrix[0, 2] == '*') and (matrix[1, 2] == 1 or matrix[1, 2] == '*'):
                function += "A' C D + "
                matrix[0, 2] = '0'
                matrix[1, 2] = '0'
            if (matrix[0, 3] == 1 or matrix[0, 3] == '*') and (matrix[1, 3] == 1 or matrix[1, 3] == '*'):
                function += "A' C D' + "
                matrix[0, 3] = '0'
                matrix[1, 3] = '0'
            if (matrix[1, 0] == 1 or matrix[1, 0] == '*') and (matrix[2, 0] == 1 or matrix[2, 0] == '*'):
                function += "B C' D' + "
                matrix[1, 0] = '0'
                matrix[2, 0] = '0'
            if (matrix[1, 1] == 1 or matrix[1, 1] == '*') and (matrix[2, 1] == 1 or matrix[2, 1] == '*'):
                function += "B C' D + "
                matrix[1, 1] = '0'
                matrix[2, 1] = '0'
            if (matrix[1, 2] == 1 or matrix[1, 2] == '*') and (matrix[2, 2] == 1 or matrix[2, 2] == '*'):
                function += "B C D + "
                matrix[1, 2] = '0'
                matrix[2, 2] = '0'
            if (matrix[1, 3] == 1 or matrix[1, 3] == '*') and (matrix[2, 3] == 1 or matrix[2, 3] == '*'):
                function += "B C D' + "
                matrix[1, 3] = '0'
                matrix[2, 3] = '0'
            if (matrix[2, 0] == 1 or matrix[2, 0] == '*') and (matrix[3, 0] == 1 or matrix[3, 0] == '*'):
                function += "A C' D + "
                matrix[2, 0] = '0'
                matrix[3, 0] = '0'
            if (matrix[2, 1] == 1 or matrix[2, 1] == '*') and (matrix[3, 1] == 1 or matrix[3, 1] == '*'):
                function += "A C' D + "
                matrix[2, 1] = '0'
                matrix[3, 1] = '0'
            if (matrix[2, 2] == 1 or matrix[2, 2] == '*') and (matrix[3, 2] == 1 or matrix[3, 2] == '*'):
                function += "A C D + "
                matrix[2, 2] = '0'
                matrix[3, 2] = '0'
            if (matrix[2, 3] == 1 or matrix[2, 3] == '*') and (matrix[3, 3] == 1 or matrix[3, 3] == '*'):
                function += "A C D' + "
                matrix[2, 3] = '0'
                matrix[3, 3] = '0'
            if (matrix[0, 0] == 1 or matrix[0, 0] == '*') and (matrix[3, 0] == 1 or matrix[3, 0] == '*'):
                function += "B' C' D' + "
                matrix[0, 0] = '0'
                matrix[3, 0] = '0'
            if (matrix[0, 3] == 1 or matrix[0, 3] == '*') and (matrix[3, 3] == 1 or matrix[3, 3] == '*'):
                function += "B' C D' + "
                matrix[0, 3] = '0'
                matrix[3, 3] = '0'
            if (matrix[0, 1] == 1 or matrix[0, 1] == '*') and (matrix[3, 1] == 1 or matrix[3, 1] == '*'):
                function += "B' C' D + "
                matrix[0, 1] = '0'
                matrix[3, 1] = '0'
            if (matrix[0, 2] == 1 or matrix[0, 2] == '*') and (matrix[3, 2] == 1 or matrix[3, 2] == '*'):
                function += "B' C D + "
                matrix[0, 2] = '0'
                matrix[3, 2] = '0'
            if (matrix[0, 3] == 1 or matrix[0, 3] == '*') and (matrix[3, 3] == 1 or matrix[3, 3] == '*'):
                function += "B' C D' + "
                matrix[0, 3] = '0'
                matrix[3, 3] = '0'
            # cazul in care avem 1 de 1
            if matrix[0, 0] == 1:
                function += "A' B' C' D' + "
                matrix[0, 0] = '0'
            if matrix[0, 1] == 1:
                function += "A' B' C' D + "
                matrix[0, 1] = '0'
            if matrix[0, 2] == 1:
                function += "A' B' C D + "
                matrix[0, 2] = '0'
            if matrix[0, 3] == 1:
                function += "A' B' C D' + "
                matrix[0, 3] = '0'
            if matrix[1, 0] == 1:
                function += "A' B C' D' + "
                matrix[1, 0] = '0'
            if matrix[1, 1] == 1:
                function += "A' B C' D + "
                matrix[1, 1] = '0'
            if matrix[1, 2] == 1:
                function += "A' B C D + "
                matrix[1, 2] = '0'
            if matrix[1, 3] == 1:
                function += "A' B C D' + "
                matrix[1, 3] = '0'
            if matrix[2, 0] == 1:
                function += "A B C' D' + "
                matrix[2, 0] = '0'
            if matrix[2, 1] == 1:
                function += "A B C' D + "
                matrix[2, 1] = '0'
            if matrix[2, 2] == 1:
                function += "A B C D + "
                matrix[2, 2] = '0'
            if matrix[2, 3] == 1:
                function += "A B C D' + "
                matrix[2, 3] = '0'
            if matrix[3, 0] == 1:
                function += "A B' C' D' + "
                matrix[3, 0] = '0'
            if matrix[3, 1] == 1:
                function += "A B' C' D + "
                matrix[3, 1] = '0'
            if matrix[3, 2] == 1:
                function += "A B' C D + "
                matrix[3, 2] = '0'
            if matrix[3, 3] == 1:
                function += "A B' C D + "
                matrix[3, 3] = '0'

    return function


def convert_from_fnd_to_fnc(fnd):
    s = fnd.replace(" ", "")
    x = s.replace("+", "*")
    y = x.replace("'", "#")
    new = "(" + y + ")"
    print(new)
    n_new = new.replace("*", ") * (")
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
            if n_new[element + 2] == 'A' or n_new[element + 2] == 'B' or n_new[element + 2] == 'C' or \
                    n_new[element + 2] == 'D':
                n_new = n_new[0:element + 2] + "+" + n_new[element + 2:]
                length += 1
            if n_new[element + 1] == '#':
                n_new = n_new[0:element + 1] + "" + n_new[element + 1:]

        element += 1
    nn_new = n_new.replace("#", "")
    print(nn_new)
    return nn_new


# fnd = "A' B + C D "
# fnd = "A' C B + A' B "
# fnd = "C' D "
# fnd = "A' B' C + A' "
# fnc = convert_from_fnd_to_fnc(fnd)
# print("Formula in FNC :", fnc)  # (A+B') * (C'+D')


def get_minimized_form_of_the_function(sigma_nr_of_var, sigma_input, sigmas_input, sigmas_correct):
    new_dictionary = {}
    if sigma_nr_of_var == 3:
        dictionary = create_dictionary(sigma_input, sigma_nr_of_var)
        new_dictionary = dictionary
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
            new_dictionary = dictionary
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


# matrix = get_minimized_form_of_the_function(4, '1,5,9,13', '3,7,11,15', 1)
# function = compute_minimized_form(matrix, 4)
# size = len(function)
# # Slice string to remove last 3 characters from string
# mod_string = function[:size - 2]
# print("Forma minimizata este: ", mod_string)


def get_expected_input(prompt):
    while True:
        # value = "sigma(1,5,9,13)+sigma*(3,7,11,15)"
        print(prompt)
        value = input()
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

        # print("Sigma name:", sigma_n)
        # print("Sigma input:", sigma_input)
        # print("Sigma nr of variables:", sigma_nr_of_var)
        #
        # print("Sigmas name:", sigmas_n)
        # print("Sigmas input:", sigmas_input)
        # print("Sigmas nr of variables:", sigmas_nr_of_var)
        # print("Sigma* status:", sigmas_status)
        # print("Result of Check Sigmas Input:", check_sigma_input(sigmas_input))

        if sigmas_n == "sigma*" and check_sigma_input(sigmas_input) and sigmas_nr_of_var == sigma_nr_of_var:
            sigmas_correct = 1  # know if sigmas exists and is correct
        else:
            sigmas_correct = 0

        # print("Sigma* correct status:", sigmas_correct)
        if sigma_n == "sigma" and check_sigma_input(sigma_input) and (sigmas_status == 0 or sigmas_correct == 1):
            print_truth_table(sigma_nr_of_var, sigma_input, sigmas_input, sigmas_correct)
            matrix = get_minimized_form_of_the_function(sigma_nr_of_var, sigma_input, sigmas_input, sigmas_correct)
            print("Matricea pentru care se va calcula forma minimizata este:", matrix)
            fnd_n = compute_minimized_form(matrix, sigma_nr_of_var)
            size = len(fnd_n)
            fnd = fnd_n[:size - 2]
            print("Forma normala disjunctiva a functiei este:", fnd)
            fnc = convert_from_fnd_to_fnc(fnd)
            print("Forma normala conjunctiva a functiei este:", fnc)
        else:  # sintaxa si sematica corecte
            print(
                "Sorry, your response must be a valid input, like: sigma(.,.,...) or sigma(.,.,...)+sigma*(.,.,...)")

        #return value


get_expected_input("Please enter sigma: ")
# print(sigma)
# print_truth_table(4, '1,2,3', '8,9,10', 1)
