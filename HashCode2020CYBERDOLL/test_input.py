# https://storage.googleapis.com/coding-competitions.appspot.com/HC/2020/hashcode_2020_online_qualification_round.pdf

def test_google_hash_input_2020(total_book_count, total_library_count, total_day_count, book_scores, library_dict,PRINT_SELECT = False):
    """
    Function to solve Google Hash 2020

    Parameters
    ----------
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
    PRINT_SELECT : Boolean
        Bool determines if print statements are printed. Not recommended for large inputs.
    Returns
    -------
    score : Integer
        Int representing the score of all books sent based on parameters
    """
    print("There are",total_book_count,"books,",
          total_library_count, "libraries, and",
          total_day_count,"days for scanning.")
    if total_day_count > 5000:
        print("If the above numbers are big, this may take awhile...")
        print("Progress will be printed.")
    
    ### Library dict entry example
    ## library:{'stats':{'book_count':5, 'signup_days':2, 'shipping':2}
    ##          'books':[0,1,2,3,4]}
    
    not_signed_up_libs = {k for k in library_dict.keys()}
    signed_up_libs = set()
    
    ### Books ordered by highest book first
    library_dict_copy = library_dict.copy()
    for k,v in library_dict.items():
        library_dict_copy[k]['bookset'] = set(sorted(library_dict_copy[k]['bookset'],reverse=True,key=book_scores.get))
    # print(library_dict_copy)
    
    ### Determine order to sign up libraries
    # No/arbitrary order
    library_order = [x for x in range(total_library_count)]
    library_order.reverse()
    
    
    
    signup_full = False
    lib_being_signed_up = ""
    days_remain_for_sign_up = 0
    libraries_signed_up_count = 0
    books_received = []
    if PRINT_SELECT:
        print("\nThe scores of the books are:\n",book_scores)
        print("\nLibrary dictionary",library_dict)
    
    for day in range(total_day_count):
        if PRINT_SELECT:
            print("\nDay",day,"of",total_day_count,". ",round(day/total_day_count,2),"complete")
        if total_day_count > 5000 and day%500==0:
            print("\nDay",day,"of",total_day_count,"  ",round(day/total_day_count,3),"complete")
        libraries_to_remove = []
        for library in signed_up_libs:
            librarys_books = library_dict_copy[library]['bookset']
            if len(librarys_books) == 0:
                libraries_to_remove.append(library)
                continue
            if PRINT_SELECT:
                print("Library",library,"is signed up and active.")
            librarys_books = library_dict_copy[library]['bookset']
            num_book_to_ship = library_dict_copy[library]['stats']['shipping']
            for i in range(num_book_to_ship):
                try:
                    book_to_send = list(librarys_books)[i]
                    books_received.append(book_to_send)
                    if PRINT_SELECT:
                        print("Library",library,"sends book",book_to_send)
                except:
                    pass
            for book in books_received: # just say if book in, then remove
                if book in library_dict_copy[library]['bookset']:
                    library_dict_copy[library]['bookset'].remove(book)
        for lib in libraries_to_remove:
            signed_up_libs.remove(lib)
        
        if len(not_signed_up_libs) > 0:
            if signup_full == False:
                lib_being_signed_up = library_order[libraries_signed_up_count]
                signup_full = True
                days_remain_for_sign_up = library_dict[lib_being_signed_up]['stats']['signup_days']
                if PRINT_SELECT:
                    print("Library",lib_being_signed_up,"begins the sign process. It will take",
                          days_remain_for_sign_up,"days, finishing on day",day-1+days_remain_for_sign_up)
                days_remain_for_sign_up -= 1
            elif signup_full == True:
                days_remain_for_sign_up -= 1
                if days_remain_for_sign_up == 0:
                    signed_up_libs.add(lib_being_signed_up)
                    not_signed_up_libs.remove(lib_being_signed_up)
                    if PRINT_SELECT:
                        print("Library",lib_being_signed_up,"finished the signup process")
                    signup_full = False
                    lib_being_signed_up = ""
                    libraries_signed_up_count += 1
                    days_remain_for_sign_up = 0
    
    books_received = set(books_received)
    if PRINT_SELECT:
        print("\n\nBooks received set",books_received)
    score = 0
    for i in books_received:
        score += book_scores[i]
    if PRINT_SELECT:
        print("Total score is",score)
    return score