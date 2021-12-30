def convert_from_fnd_to_fnc(fnd):
    s = fnd.replace(" ", "")
    x = s.replace("+", "*")
    y = x.replace("'", "#")
    new = "(" + y + ")"
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
# fnd = "A' B' C + A' "
fnd = "C' D + A B' C + A' C D "
fnc = convert_from_fnd_to_fnc(fnd)
print("Formula in FNC :", fnc)  # (A+B') * (C'+D')


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
        #print('Yes, list contains duplicates')
        return 1
    else:
        #print('No duplicates found in list')
        return 0



print("Duplicate:", check_if_duplicates("1,2,3,4,4"))



def compute_minimized_form(matrix, nr_of_var):
    function = ""
    print("Nr of variables received in function:", nr_of_var)
    if nr_of_var == 3:
        # verificam incepand  de la cele mai mari blocuri
        if matrix[0, 0] == ('1' or '*') and matrix[0, 1] == ('1' or '*') and matrix[1, 0] == ('1' or '*') \
                and matrix[1, 1] == ('1' or '*'):
            function += "A' + "
            matrix[0, 0] = '0'
            matrix[0, 1] = '0'
            matrix[1, 0] = '0'
            matrix[1, 1] = '0'
        if matrix[0, 1] == ('1' or '*') and matrix[0, 2] == ('1' or '*')\
                and matrix[1, 1] == ('1' or '*') and matrix[1, 2] == ('1' or '*'):
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
                function += "A' B C D' + "
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


def f(a) :
    if (a == 'b' or 'a'):
        return "Yes"
    else:
        return "No"

print(f('c'))

