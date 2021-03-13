# https://storage.googleapis.com/coding-competitions.appspot.com/HC/2020/hashcode_2020_online_qualification_round.pdf

def read_google_hash_input_2020(filename):
    """
    Function created to get data from input file for Google Hash 2020
    https://storage.googleapis.com/coding-competitions.appspot.com/HC/2020/hashcode_2020_online_qualification_round.pdf

    Parameters
    ----------
    filename : String
        name of input file - example : "this_is_an_example.txt"

    Returns
    -------
    total_book_count : Integer
        Int representing total number of books
    total_library_count : Integer
        Int representing total number of libraries
    total_day_count : Integer
        Int representing total number of days
    book_scores : Dictionary
        Dict representing scores of all books
    library_dict : Dictionary
        Dict representing all libraries with related metrics
    """
    input_file = open(filename, 'r')
    input_lines = input_file.read().splitlines()
    input_data = [x.split() for x in input_lines]

    total_book_count = int(input_data[0][0])
    total_library_count = int(input_data[0][1])
    total_day_count = int(input_data[0][2])

    book_scores = {}
    for n, book in enumerate(input_data[1]):
        book_scores[str(n)] = int(book)
    book_scores = dict(sorted(book_scores.items(), reverse=True, key=lambda item: item[1]))

    input_data = input_data[2:]
    library_dict = {}
    cur_lib = 0
    for n, line in enumerate(input_data):
        if line == []:
            continue
        if n % 2 == 0:
            book_count, signup_days, ship_count = int(line[0]), int(line[1]), int(line[2])
            library_dict[cur_lib] = {'stats': {'book_count': book_count,
                                               'signup_days': signup_days, 'shipping': ship_count},
                                     'bookset': []}
        else:
            library_dict[cur_lib]['bookset'] = line
            cur_lib += 1
    return total_book_count, total_library_count, total_day_count, book_scores, library_dict

###############################################################################
### Original Code - prior to putting in a function ###
### contained helpful print states while creating/debugging

# input_file = open('a_example.txt','r')
# # input_file = open('b_read_on.txt','r')
# # input_file = open('c_incunabula.txt','r')
# # input_file = open('d_tough_choices.txt','r')
# # input_file = open('e_so_many_books.txt','r')
# # input_file = open('f_libraries_of_the_world.txt','r')
# input_lines = input_file.read().splitlines()
# # print(input_lines)
# # print(len(input_lines))
# input_data = [x.split() for x in input_lines] # list comprehension, let's go!
# # for line in input_lines:
# #     input_data.append(line.split())
# # print(input_data)
# total_book_count = int(input_data[0][0])
# total_library_count = int(input_data[0][1])
# total_day_count =  int(input_data[0][2])
# # print("There are",total_book_count,"books,",
# #       total_library_count, "libraries, and",
# #       total_day_count,"days for scanning.")
# book_scores = {}
# for n, book in enumerate(input_data[1]):
#     book_scores[str(n)] = int(book)
# book_scores=dict(sorted(book_scores.items(),reverse=True, key=lambda item: item[1]))
# # print("The scores of the books are:\n",book_scores)
# input_data = input_data[2:]
# # print(input_data)
# library_dict = {}
# # library:{'stats':{'book_count':5, 'signup_days':2, 'ship_days':2}
# #          'books':[0,1,2,3,4]}
# cur_lib = 0
# for n, line in enumerate(input_data):
#     if line == []:
#         continue
#     if n % 2 == 0:
#         book_count,signup_days,ship_count = int(line[0]),int(line[1]),int(line[2])
#         library_dict[cur_lib]={'stats':{'book_count':book_count,
#                                         'signup_days':signup_days, 'shipping':ship_count},
#                                'bookset':[]}
#     else:
#         library_dict[cur_lib]['bookset'] = line
#         cur_lib += 1
# # print("Library dictionary",library_dict)
