############################################################
# CIS 521: Homework 8
############################################################

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import string

############################################################

student_name = "Danyal Razaa Khan"

############################################################
# Section 1: Ngram Models
############################################################


def tokenize(text):
    # store the list of token substrings
    list_of_tokens = []
    # keep track of the current token for easy appending later
    token = []
    # iterate through the input String
    for i in range(0, len(text), 1):
        # if the current character in the string is a space
        # then skip that character in the
        # the token list
        if text[i].isspace():
            if token:
                temp = ''.join(token)
                list_of_tokens.append(temp)
                token = []
        # handle punctuation to be treated as separate
        # token characters using the string module
        # punctuation function
        elif text[i] in string.punctuation:
            # if the current token is not empty
            # add the curent punctuation character
            # to the token list
            if token:
                temp = ''.join(token)
                list_of_tokens.append(temp)
                token = []
            list_of_tokens.append(text[i])
        # treat any regular character as part of its own
        # token like sequence to add to the list
        else:
            token.append(text[i])
    # if the last character is a token, then add it to the
    # list if possible
    if token:
        temp = ''.join(token)
        list_of_tokens.append(temp)
    return list_of_tokens


# test cases for tokenize function above
print(tokenize("  This is an example.  "))
print(tokenize(" 'Medium-rare,' she said."))


def ngrams(n, tokens):
    pass


class NgramModel(object):

    def __init__(self, n):
        pass

    def update(self, sentence):
        pass

    def prob(self, context, token):
        pass

    def random_token(self, context):
        pass

    def random_text(self, token_count):
        pass

    def perplexity(self, sentence):
        pass


def create_ngram_model(n, path):
    pass

############################################################
# Section 2: Feedback
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
