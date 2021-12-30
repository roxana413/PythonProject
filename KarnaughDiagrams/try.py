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
