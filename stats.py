def word_count(book_txt):
    book_words = book_txt.split()
    return len(book_words)

def charachter_count(book_txt):
    counter = {}
    book_txt_l = book_txt.lower()
    book_words = book_txt_l.split()
    for word in book_words:
        for l in word:
            if l not in counter:
                counter[l] = 1
            else:
                counter[l] += 1
    return counter

def sort_dict(count_dict):
    sorted_by_value = dict(sorted(count_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_by_value