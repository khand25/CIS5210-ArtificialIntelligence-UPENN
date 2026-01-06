import numpy
import nltk

############################################################
# CIS 521: Homework 1
############################################################

student_name = "Danyal Razaa Khan"

# This is where your grade report will be sent.
student_email = "danyalkh@seas.upenn.edu"

############################################################
# Section 1: Python Concepts
############################################################

python_concepts_question_1 = """Python is a strongly typed language meaning
that the Python interpreter throws a "TypeError" at runtime
when two values are incompatible with each other when doing operations.
An example of this is trying to add a String value to an integer value.
x = "Hello" + 7.
This will result in a TypeError as the two types are different
and incompatible with each other for the additon operator here.
Python is also a dynamically typed language
meaning you don't have to predefine a varaible's data type on declaration.
It is assumed by the python interpreter at runtime
when a variable's value is assigned.
Also the data type of a variable can automatically change when a new value
is assigned to that varaible of a different data type.
An example of this is decalaring a variable z
and assigning it an integer value of 4.
And then later assigning z to a string value of "Danyal".
"""

python_concepts_question_2 = """In Python, you cannot use a
"mutable data type" like
a list as a key in a dictionary.
This is because mutable data types can be modified
after they are created. Since dictionary keys must be hashable
and their hash value
never changes for fast lookups, using a mutable data type like a list
would violate this requirement. Instead you can use an immutable data type
like a tuple as a dictionary key
since tuples cannot be modified after creation.
resulting in a constant hash value to map a set of coordinates to a value."""

python_concepts_question_3 = """Using the "join" function in Python
is more effiecient
than using string concatenation in a loop for larger strings.
This is because the join function is optimized for combining
multiple strings or other
iterables into a single string separated by a specified separtor.
The underlying implementation of join preallocates memory for the final string
based on the total length of all the strings being joined."""

############################################################
# Section 2: Working with Lists
############################################################


def extract_and_apply(lst, p, f):
    return [f(x) for x in lst if p(x)]


def concatenate(seqs):
    # this nested list comprehension will iterate thorugh a
    # list argument and each
    # element in the list arugment will be assigned to element1 using a for
    # each loop. There is a possibility that element1
    # could be another iterable
    # so we will iterate through element1
    # and assign each element to element2 in another
    # nested for each loop. We will finally append each element2 to a new list
    # and return that new list.
    return [element2 for element1 in seqs for element2 in element1]


def transpose(matrix):
    result_list = []
    # a single dimensional row list to temporarily hold the
    # transposed column values
    temp_list = []
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            temp_list.append(matrix[i][j])
        result_list.append(temp_list)
        temp_list = []
    return result_list
# print(transpose([[1,2,3]]))
# print(transpose([[1,2],[3,4],[5,6]]))

############################################################
# Section 3: Sequence Slicing
############################################################


def copy(seq):
    # Using slicing to copy the entire sequence from index 0 to the end
    # inclusively and return the copied sequence.
    result = seq[0:]
    return result
# print(copy((1,2,3)))
# print(copy("abc"))
# x = [0,0,0]
# y = copy(x)
# print(x,y)
# x[0] = 1
# print(x,y)


def all_but_last(seq):
    result = seq[0:len(seq)-1]
    return result
# print(all_but_last("abc"))
# print(all_but_last((1,2,3)))
# print(all_but_last(""))
# print(all_but_last([]))


def every_other(seq):
    result = seq[0:len(seq):2]
    return result
# print(every_other([1,2,3,4,5]))
# print(every_other("abcde"))
# print(every_other([]))
# print(every_other([1,2,3,4,5,6]))
# print(every_other("abcdef"))

############################################################
# Section 4: Combinatorial Algorithms
############################################################


def prefixes(seq):
    # Input parameter is some sort of iterable sequence (like a list)
    # Loop through the sequence
    # of the i values indicies
    # being 0 to the length
    # of the sequence (inclusively)
    # and on each iteration yield the slice of the
    # sequence from index 0 to index i (not inclusively).
    # When we use the 'yeild' keyword,
    # we will essentially
    # pause the for loop and greater prefixes function, return
    # the sliced iterable outside of this prefixes
    # functions (as an iterable sequence) and then resume the for loop
    # inside the function again to continue doing
    # this same process until the for loop is done.
    for i in range(0, len(seq) + 1, 1):
        yield seq[0:i]
# print(list(prefixes([1,2,3])))
# print(list(prefixes("abc")))
# print(list(prefixes([])))
# print(list(prefixes([1,2])))


def suffixes(seq):
    for i in range(0, len(seq)+1, 1):
        yield seq[i:len(seq)]
# print(list(suffixes([1,2,3])))
# print(list(suffixes("abc")))
# print(list(suffixes([])))
# print(list(suffixes([1,2])))


def slices(seq):
    for i in range(0, len(seq), 1):
        for j in range(i+1, len(seq)+1, 1):
            yield seq[i:j]
# print(list(slices([1,2,3])))
# print(list(slices("abc")))
# print(list(slices([])))
# print(list(slices([1,2])))

############################################################
# Section 5: Text Processing
############################################################


def normalize(text):
    pass


def no_vowels(text):
    pass


def digits_to_words(text):
    pass


def to_mixed_case(name):
    pass

############################################################
# Section 6: Polynomials
############################################################


class Polynomial(object):

    def __init__(self, polynomial):
        pass

    def get_polynomial(self):
        pass

    def __neg__(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __call__(self, x):
        pass

    def simplify(self):
        pass

    def __str__(self):
        pass

############################################################
# Section 7: Python Packages
############################################################


def sort_array(list_of_matrices):
    pass


def POS_tag(sentence):
    pass

############################################################
# Section 8: Feedback
############################################################


# Just an approximation is fine.
feedback_question_1 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
