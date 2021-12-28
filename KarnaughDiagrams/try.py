import ast
getallen = '12, 3, 7, 25, 771, 45, 6, 98, 55, 546'

for number in ast.literal_eval(getallen):
    if number %2 == 0:
        print(f'{int(number)} is even')
    else:
        print(f'{int(number)} is odd')

# def check_sigma_input(my_string):
#     comas_string = my_string[1::2]
#     digits_string = my_string[::2]
#     arr = list(my_string)
#     print(arr)
#     print(comas_string)
#     print(digits_string)
#     for element in range(0, len(comas_string)):
#         print(comas_string[element])
#         if comas_string[element] == ',':
#             ok1 = True
#         else:
#             ok1 = False
#     for element in range(0, len(digits_string)):
#         print(digits_string[element])
#         if digits_string[element].isdigit():
#             ok2 = True
#         else:
#             ok2 = False
#     # verificam daca nr de variabile e ok
#     check_if_sigma_is_correct(arr)
#     if ok1 and ok2 is True:
#         return True
#     else:
#         return False


 # first_index_of_cl_par = value.index(")")
        # second_index_of_op_par = value.find("(", value.find("(") + 1)
        # second_index_of_cl_par = value.find(")", value.find(")") + 1)
        # sigma_input = value[6:first_index_of_cl_par:1]
        # sigmas_input = value[second_index_of_op_par + 1:second_index_of_cl_par - 1:1]
        # if (value.index("sigma") == 0 and
        #     value.index("(") == 5 and check_sigma_input(sigma_input) and
        #     (value.endswith(")") or (
        #             value[first_index_of_cl_par + 1] == "+" and value.index("sigma*") == first_index_of_cl_par + 2 and
        #             check_sigma_input(sigmas_input) and value.endswith(")")
        #     )
        #     )) is False:



 # line = value
 #        line = line.replace('(', 'l')
 #        line = line.replace(')', 'l')
 #        line = line.replace('+', 'o')
 #        line = re.sub('o', '', line)
 #
 #        cut = line.split('l')
 #        print(cut)
 #        sigma_v = cut[0]
 #        sigma_input = cut[1]
 #        sigmas_status = 0
 #        sigma_nr_of_var = get_nr_of_variables(sigma_input)
 #        if len(cut) > 3:
 #            sigmas_status = 1
 #            sigmas_v = cut[2]
 #            sigmas_input = cut[3]
 #            sigmas_nr_of_var = get_nr_of_variables(sigmas_input)
 #
 #            print(sigmas_v)
 #            print(sigmas_input)
 #            print(sigma_v)
 #            print(sigma_input)
 #        if sigmas_v == "sigma*" and check_sigma_input(sigmas_input) and sigmas_nr_of_var == sigma_nr_of_var:
 #                sigmas_correct = 1  # know if sigmas exists and is correct
 #            else:
 #                sigmas_correct = 0
 #
 #            if (sigma_v == "sigma" and check_sigma_input(sigma_input) and (
 #                    sigmas_status == 0 or sigmas_correct == 1)) is False:
 #                print(
 #                    "Sorry, your response must be a valid input, like: sigma(.,.,...) or sigma(.,.,...)+sigma*(.,.,...)")
 #                continue
 #            else:
 #                # print_truth_table(sigma_nr_of_var, sigma_input, sigmas_input, sigmas_correct)
 #                break

        # try:
        #     # value = input(prompt)
        #     value = "sigma(1,5,9,13)+sigma*(3,7,11,15)"
        # except ValueError:
        #     print("Sorry, I didn't understand that.")
        #     continue
