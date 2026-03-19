############################################################
# CIS 521: Homework 8
############################################################

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import string
import random

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
    result_list = []
    # padding used for adding the START and END token characters
    appended_tokens = ["<START>"] * (n - 1) + tokens + ["<END>"]
    # iterate through the start and end character lists and for each
    # element create a context value that is slice of the appended tokens
    # from i - (n - 1) to i value (n-1 tuple value) to the end of the token
    # Use this context value with the current token value which is grabbed
    # from the appended_tokens list above and return it as a tuple like element
    # in the result list
    for i in range(n - 1, len(appended_tokens), 1):
        start_val = i - (n - 1)
        end_val = i
        context = tuple(appended_tokens[start_val:end_val])
        current_token = appended_tokens[i]
        result_list.append((context, current_token))
    # return the result list as needed
    return result_list


print(ngrams(1, ["a", "b", "c"]))
print(ngrams(2, ["a", "b", "c"]))
print(ngrams(3, ["a", "b", "c"]))
print(ngrams(2, []))


class NgramModel(object):

    def __init__(self, n):
        self.n = n
        # keep track of number of tokens
        # as an dictionary map
        self.num_of_tokens = dict()
        # keep track of number of context count
        # as an dictionary map
        self.num_of_context = dict()

    def update(self, sentence):
        # retreive the tokenized sentence from the input sentence
        # using our tokenize function from above
        list_of_tokens = tokenize(sentence)
        # convert our tokenized sentence into a valid
        # ngrams to be used later
        ngrams_sentence = ngrams(self.n, list_of_tokens)
        # iterate through the ngrams and check wheter both the
        # context and token values of each ngram is already part of
        # the two dictionaries we defined in the init function
        for value in ngrams_sentence:
            current_context = value[0]
            current_token = value[1]
            # if the context is not the num_of_tokens map
            # then add it as a new entire dictionary to be used
            # later
            if current_context not in self.num_of_tokens:
                self.num_of_tokens[current_context] = dict()
            # if the context is not int the num_of_context map
            # then add it as a new key value pair of the key being
            # the context and value being 0. Increment this new key value
            # pair regardless if value was added or not
            if current_context not in self.num_of_context:
                self.num_of_context[current_context] = 0
            self.num_of_context[current_context] += 1
            # if the context is not int the num_of_tokens map
            # then add it as a new key value pair of the key being
            # the context and the current token and the value being 0.
            # Increment this new key value
            # pair regardless if value was added or not by 1
            if current_token not in self.num_of_tokens[current_context]:
                self.num_of_tokens[current_context][current_token] = 0
            self.num_of_tokens[current_context][current_token] += 1

    def prob(self, context, token):
        # if the context is not present in our num_of_context
        # map, then update function before may have not seen the
        # specific context
        # value passed into this function so return 0.0
        if context not in self.num_of_context:
            return 0.0
        # if the token is not present in our num_of_tokens
        # map, then update function before may have not seen the specific token
        # value passed into this function so return 0.0
        if token not in self.num_of_tokens[context]:
            return 0.0
        # Otherwise if both token and context were already presented in the two
        # maps, then calculate the P(token | context) as per the assignment
        # instructions and return this conditional probabiltiy value
        # accordingly
        val = self.num_of_tokens[context][token] / self.num_of_context[context]
        return (val)

    def random_token(self, context):
        # grab all the tokens context's and convert them into a list
        # and sort that list soon after.
        likely_tokens = list(self.num_of_tokens[context].keys())
        likely_tokens.sort()
        # generate some random value to dictate the token value
        # later
        random_val = random.random()
        # keep track of the total accumalted problabiltiy to this point
        total_prob = 0.0
        # iterate through our tokens list, use our prob function from above
        # to get the probabilitly of the token and append its
        # result to the total_prob variable. If our random val is indeed
        # less than our total accumalted prob so far, then return the current
        # token as is
        for i in range(0, len(likely_tokens), 1):
            total_prob += self.prob(context, likely_tokens[i])
            if random_val < total_prob:
                return likely_tokens[i]
        # Otherwise return the last token from the list
        return likely_tokens[len(likely_tokens) - 1]

    def random_text(self, token_count):
        pass

    def perplexity(self, sentence):
        pass


# Test cases for NgramModel Class:
m = NgramModel(1)
m.update("a b c d")
m.update("a b a b")
print(m.prob((), "a"))
print(m.prob((), "c"))
print(m.prob((), "<END>"))
m = NgramModel(2)
m.update("a b c d")
m.update("a b a b")
print(m.prob(("<START>", ), "a"))
print(m.prob(("b",), "c"))
print(m.prob(("a",), "x"))
m = NgramModel(1)
m.update("a b c d")
m.update("a b a b")
random.seed(1)
val = [m.random_token(()) for i in range(25)]
print(val)


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
