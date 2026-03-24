############################################################
# CIS 521: Homework 9
############################################################

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import homework9_data as data

############################################################

student_name = "Danyal Razaa Khan"

############################################################
# Section 1: Perceptrons
############################################################


class BinaryPerceptron(object):

    def __init__(self, examples, iterations):
        self.possible_weights = dict()

        # iterate through the number of iterations iterations number
        # of times
        for i in range(0, iterations, 1):
            for values in examples:
                x_val = values[0]
                y_val = values[1]
                new_predication = self.predict(x_val)

                if new_predication != y_val:
                    if y_val:
                        for feature, val in x_val.items():
                            self.possible_weights[feature] = (
                                self.possible_weights.get(feature, 0) + val
                            )
                    else:
                        for feature, val in x_val.items():
                            self.possible_weights[feature] = (
                                self.possible_weights.get(feature, 0) - val
                            )

    def predict(self, x):
        dot_product_sum = 0

        for feature, val in x.items():
            dot_product_sum += self.possible_weights.get(feature, 0) * val

        greater_than_zero = dot_product_sum > 0
        return greater_than_zero
# Test case for BinaryPerceptron class
train = [({"x1": 1}, True), ({"x2": 1}, True), 
         ({"x1": -1}, False), ({"x2": -1}, False)]

test = [{"x1": 1}, {"x1": 1, "x2": 1}, {"x1": -1, "x2": 1.5},
        {"x1": -0.5, "x2": -2}]

p = BinaryPerceptron(train, 1)
print([p.predict(x) for x in test])
class MulticlassPerceptron(object):

    def __init__(self, examples, iterations):
        pass

    def predict(self, x):
        pass

############################################################
# Section 2: Applications
############################################################


class IrisClassifier(object):

    def __init__(self, data):
        pass

    def classify(self, instance):
        pass


class DigitClassifier(object):

    def __init__(self, data):
        pass

    def classify(self, instance):
        pass


class BiasClassifier(object):

    def __init__(self, data):
        pass

    def classify(self, instance):
        pass


class MysteryClassifier1(object):

    def __init__(self, data):
        pass

    def classify(self, instance):
        pass


class MysteryClassifier2(object):

    def __init__(self, data):
        pass

    def classify(self, instance):
        pass

############################################################
# Section 3: Feedback
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
