from input_function import read_google_hash_input_2020
from test_input import test_google_hash_input_2020

# Input files                        # book libraries days
a = 'a_example.txt'                  # 6 2 7
b = 'b_read_on.txt'                  # 100000 100 1,000
c = 'c_incunabula.txt'               # 100000 10000 100,000
d = 'd_tough_choices.txt'            # 78600 30000 30,001
e = 'e_so_many_books.txt'            # 100000 1000 200
f = 'f_libraries_of_the_world.txt'   # 100000 1000 700
all_files = [a,b,c,d,e,f]

#####################################
### Set a single file to run here ###
#####################################
file = b # set file
run_file = False # set run or not
run_file = True # set run or not

if run_file:
    total_book_count, total_library_count, total_day_count, book_scores, library_dict = read_google_hash_input_2020(file)
    single_score = test_google_hash_input_2020(total_book_count, total_library_count, total_day_count, book_scores, library_dict)
    print("Score is",single_score,"for file",file,"\n")

#################################
### Set all files to run here ###
#################################
run_all = False # set run or not
# run_all = True # set run or not

if run_all:
    scores = {}
    for file in all_files:
        total_book_count, total_library_count, total_day_count, book_scores, library_dict = read_google_hash_input_2020(file)
        score = test_google_hash_input_2020(total_book_count, total_library_count, total_day_count, book_scores, library_dict)
        scores[file] = score
    final_score = sum(scores.values())
    print("Score dict:",scores)
    print("The final total score is:",final_score)
    
# The first time I ran all the problems together my score was 6,653,796
# I was mostly just trying to solve the problem and get an answer.
# I did not optimize. (nor would I have had time to in the real comp, as a solo at least)
# Score dict: {'a_example.txt': 21,
#              'b_read_on.txt': 651200,
#              'c_incunabula.txt': 830438,
#              'd_tough_choices.txt': 4103775,
#              'e_so_many_books.txt': 536459,
#              'f_libraries_of_the_world.txt': 531903}
