import string

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        word_count = file_contents.split()
        count = len(word_count)
        return count, file_contents
    
def count_the_characters(file_contents):
    new_word_list = file_contents.lower()
    dict_word = {}
    for i in (new_word_list):  
        if i in dict_word:
            dict_word[i] += 1
        else:
            dict_word[i] = 1 
    return dict_word

def sorted_dict(dict):
    return dict["num"]
