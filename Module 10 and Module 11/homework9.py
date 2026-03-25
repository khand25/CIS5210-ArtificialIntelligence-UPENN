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
        # follow iven psuedocode specification very closely
        # initialize the weight vector mapping scheme
        self.possible_weights = dict()

        # iterate through the number of iterations iterations number
        # of times
        for i in range(0, iterations, 1):
            # for each x and y value in the examples
            # iterable
            for values in examples:
                x_val = values[0]
                y_val = values[1]
                # compute the predicted class as yi^ = sign(w * xi)
                new_predication = self.predict(x_val)
                # if the predicated value is not eqaul to the actual
                # y value
                if new_predication != y_val:
                    if y_val:
                        # set the current weight to the current weight
                        # plus the xi -> value is the y_value is True
                        # positive
                        for feature, val in x_val.items():
                            self.possible_weights[feature] = (
                                self.possible_weights.get(feature, 0) + val
                            )
                    else:
                        # set the current weight to the current weight
                        # minus the xi -> value is the y_value is False
                        # (negative)
                        for feature, val in x_val.items():
                            self.possible_weights[feature] = (
                                self.possible_weights.get(feature, 0) - val
                            )

    def predict(self, x):
        # accumalate the dot product as needed
        dot_product_sum = 0
        # iterate through the given x value map
        # and for every feature value found, try to retreive that same
        # feature value from the weights vectore and mutiply that value by the
        # current x map value and add it to the dot product sum
        for feature, val in x.items():
            dot_product_sum += self.possible_weights.get(feature, 0) * val
        # if the dot product is greater than 0, then its a positive
        # predication to be used accordingly to the loop in the
        # init function.
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
        # follow iven psuedocode specification very closely
        # initialize the weight vector mapping scheme and list
        # for labels
        self.new_labels = []
        self.possible_weights = dict()
        # for each x and y value in the examples
        # iterable
        for value in examples:
            x_val = value[0]
            y_val = value[1]
            # Initialize the weight vectors as wlk to
            # 0 for k = 1, ... m. Append current y value
            # to the label list
            if y_val not in self.possible_weights:
                self.new_labels.append(y_val)
                self.possible_weights[y_val] = dict()
        # iterate through the number of iterations iterations number
        # of times for exact iterations passes over the training set
        for i in range(0, iterations, 1):
            # for each x and y value in the examples
            # iterable
            for value in examples:
                x_val = value[0]
                y_val = value[1]
                # Compute the predicted label as yi hat = argmax(wlk * xi)
                new_predication = self.predict(x_val)
                # if y hat is not eqaul to yi
                if new_predication != y_val:
                    # then for each weight from the weight table,
                    # grab the current score from the preidciation and set
                    # wyi to wyi + xi increasing the value overall
                    for feature, val in x_val.items():
                        self.possible_weights[y_val][feature] = (
                            self.possible_weights[y_val].get(feature, 0) + val
                        )
                    # then for each weight from the weight table,
                    # grab the current score from the preidciation and set
                    # wyi to wyi - xi decrasing the value overall
                    for feature, val in x_val.items():
                        self.possible_weights[new_predication][feature] = (
                            self.possible_weights[new_predication].get(
                                feature, 0) - val
                        )

    def predict(self, x):
        # compute th dot product for each label and return the label
        # with the highest score goal
        # capture both the new score and improved
        # labels as seperate logical variables
        improved_label = None
        improved_score = None
        # iterate through the list of labels and keep track of the current
        # score
        for current_label in self.new_labels:
            current_score = 0
            # iterate through the given x value map
            # and for every feature value found, try to retreive that same
            # feature value from the weights vectors
            # and mutiply that value by the
            # current x map value and add it to the current score
            for feature, val in x.items():
                tl = self.possible_weights[current_label].get(feature, 0) * val
                current_score += tl
            # if there is no current value for the improved score or
            # current score is bigger than the improved score, assign improved
            # score to the current score and new label to the current label
            if improved_score is None or current_score > improved_score:
                improved_score = current_score
                improved_label = current_label
        return improved_label


# Test cases
train = [({"x1": 1}, 1), ({"x1": 1, "x2": 1}, 2), ({"x2": 1}, 3),
         ({"x1": -1, "x2": 1}, 4), ({"x1": -1}, 5), ({"x1": -1, "x2": -1}, 6),
         ({"x2": -1}, 7), ({"x1": 1, "x2": -1}, 8)]
p = MulticlassPerceptron(train, 10)
print([p.predict(x) for x, y in train])
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
