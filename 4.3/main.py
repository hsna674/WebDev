word_list = open('enable1.txt').read().splitlines()
six_letter_words = [x for x in word_list if len(x) == 6]
words_with_e = [x for x in word_list if 'e' in x]
words_without_e = [x for x in word_list if 'e' not in x]
five_letter_with_e_not_first = [x for x in word_list if len(x) == 5 and 'e' in x[1:]]