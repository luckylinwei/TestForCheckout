__author__ = 'Lin'

import ngram

def string_similarity_ngram(str1, str2, param_N):
    n = ngram.NGram([str1], N = param_N)
    number_of_shared_ngrams = n.items_sharing_ngrams(str2)
    len_of_str1 = len(list(n._split(str1)))
    len_of_str2 = len(list(n._split(str2)))
    nagram_similarity = 2 * number_of_shared_ngrams / (len_of_str1 + len_of_str2)
    return nagram_similarity

str1 = "verticalDrawAction"
str2 = "drawVerticalAction"
print(string_similarity_ngram(str1, str2, 2))
#This is the first commit
def f():
	print("This is the second commit")
	
def ff():
	print("Add this function for the third commit")