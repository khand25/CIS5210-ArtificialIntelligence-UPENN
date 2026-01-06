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
    # Convert the input String to lowercase format
    temp_string = text.lower()
    # Now remove leading and trailing whitespace
    temp_string2 = temp_string.strip()
    # Create a list of string words here by splitting the temp_string2
    # by any spaces as an element in the list
    temp_list = temp_string2.split()
    # Rejoin the list of words into a single string value where each previous
    # list element is separated by a single space character.
    result_string = " ".join(temp_list)
    return result_string
# print(normalize("This is an example."))
# print(normalize("  Extra  SPACE     "))
# print(normalize("This is\nan\texample."))
# print(normalize(" hellO,    WoRLD!"))


def no_vowels(text):
    # Vowels: 'a', 'e', 'i', 'o', 'u' (both uppercase and lowercase)
    result = text.replace("a", "")
    result = result.replace("e", "")
    result = result.replace("i", "")
    result = result.replace("o", "")
    result = result.replace("u", "")
    result = result.replace("A", "")
    result = result.replace("E", "")
    result = result.replace("I", "")
    result = result.replace("O", "")
    result = result.replace("U", "")
    return result
# print(no_vowels("This Is An Example."))
# print(no_vowels("HELLO world!"))
# print(no_vowels("We love Python!"))
# print(no_vowels(""))


def digits_to_words(text):
    # dictionary to map digits characters in input text to their
    # corresponding English word representation
    dictionary_digit_map = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three',
                            '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
                            '8': 'eight', '9': 'nine'}
    # Initialize an empty result string to later return
    result_string = ""
    # Loop thorugh each character in the input text
    for character in text:
        # On each iteration check if the current character
        # is a digit found as a key from the dictionary,
        # if so grab the value of the key and
        # concatenate it to the result string with an space character.
        if character in dictionary_digit_map.keys():
            result_string = result_string + dictionary_digit_map[character]
            result_string = result_string + " "
    # Remove trailing spaces
    result_string = result_string.strip()
    return result_string
# print(digits_to_words("Zip Code: 19104"))
# print(digits_to_words("Pi is 3.14156..."))
# print(digits_to_words("Yello!"))
# print(digits_to_words(""))


def to_mixed_case(name):
    # Handle the edge case where the input parameter only consists
    # of underscores
    all_underscores = True
    for element in name:
        if element != '_':
            all_underscores = False
    if all_underscores:
        return ""
    if '_' not in name:
        return name
    # Remove all leading and trailing underscores first
    name = name.strip('_')
    # Split the input string by underscores to get a list of words
    # where each element is a word
    # list_words = name.split('_')
    # Used to store the final result string
    result = ""
    # Boolean varaible used to decide when to capitalize the next letter
    capitalize_next_letter = False
    # iterate through the string name iterable and on each character
    # check if it is an underscore, if so then set the boolean variable
    # to True to capitlize the next character afterwards
    # Otherwise skip to next iteration of a character that is not an underscore
    for character in name:
        if character == '_':
            capitalize_next_letter = True
        else:
            if result == "":
                # Identify that we are at the first character
                # of the result string and must
                # make it lowercase
                result = result + character.lower()
            elif capitalize_next_letter:
                result = result + character.upper()
                capitalize_next_letter = False
            else:
                result = result + character.lower()
    return result


# print(to_mixed_case("to_mixed_case"))
# print(to_mixed_case("__EXAMPLE__NAME__"))
# print(to_mixed_case("alreadyMixedCase"))
# print(to_mixed_case("___"))
# print(to_mixed_case(""))
############################################################
# Section 6: Polynomials
############################################################


class Polynomial(object):

    def __init__(self, polynomial):
        # Constructor method to initialize
        # the calling object as a polynomial object
        # with its polynomial instance variable
        # being assigned to the input parameter polynomial.
        # Which is assumed to be a list of tuples coordinate pairs
        # Convert the list of tuples for the calling
        # object's polynomial instance variable value
        # to a tuple of tuples (using tuple init function) and return it
        self.polynomial = tuple(polynomial)

    def get_polynomial(self):
        # Getter method to return the calling object's polynomial
        # instance variable value
        return self.polynomial

    def __neg__(self):
        # Grab the calling object's polynomial instance variable
        # memory address using the getter method
        poly = self.get_polynomial()
        # Create a new result list to hold the negated coefficient
        result = []
        # Remember that a poly is a refrence to a tuple of tuples
        # 2d tuple structure
        # iterate through each element in the outer tuple (rows)
        # and on each iteration grab the coefficient and power values
        # from the inner tuple (columns) and append a new tuple
        # with the negated coefficient and original power value
        # to the result list. Finally return a new Polynomial object
        # initialized with the result list 
        # converted to a tuple of tuples
        for i in range(len(poly)):
            coef, power = poly[i]
            result.append((-coef, power))
        return Polynomial(tuple(result))
        

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
p = Polynomial([(2,1), (1,0)])
print(p.get_polynomial())
q = -(-p )
print(q.get_polynomial())
q = Polynomial([])
print(q.get_polynomial())
q = -q
print(q.get_polynomial())
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
