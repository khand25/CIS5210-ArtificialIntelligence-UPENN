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
# train = [({"x1": 1}, True), ({"x2": 1}, True),
# ({"x1": -1}, False), ({"x2": -1}, False)]

# test = [{"x1": 1}, {"x1": 1, "x2": 1}, {"x1": -1, "x2": 1.5},
# {"x1": -0.5, "x2": -2}]

# p = BinaryPerceptron(train, 1)
# print([p.predict(x) for x in test])


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
# train = [({"x1": 1}, 1), ({"x1": 1, "x2": 1}, 2), ({"x2": 1}, 3),
# ({"x1": -1, "x2": 1}, 4), ({"x1": -1}, 5), ({"x1": -1, "x2": -1}, 6),
# ({"x2": -1}, 7), ({"x1": 1, "x2": -1}, 8)]
# p = MulticlassPerceptron(train, 10)
# print([p.predict(x) for x, y in train])
############################################################
# Section 2: Applications
############################################################


class IrisClassifier(object):

    def __init__(self, data):
        # store each of the columns from the iris dataset
        iris_rows = []
        # iterate through each of the rows in the iris dataset
        for value in data:
            # x_val is a tuple of 4 elements containing
            # each iris plants measurements for their attributes
            x_val = value[0]
            # y_val is the classification of the iris plant based
            # on its feature value
            y_val = value[1]
            attributes = dict()
            # add all 4 features from each row in the iris dataset
            # to the attributes dictionary as a valid feature name to value
            # key value pair
            attributes["sepal_length"] = x_val[0]
            attributes["sepal_width"] = x_val[1]
            attributes["petal_length"] = x_val[2]
            attributes["petal_width"] = x_val[3]
            # fully convert each row in the iris dataset into
            # a clear valid tuple to add to our iris_rows list
            row_to_add = (attributes, y_val)
            iris_rows.append(row_to_add)
        # create a mutliclassperception instance from our class above
        # to be used as their machine learning model to later classify
        # the iris dataset values
        self.model = MulticlassPerceptron(iris_rows, 25)

    def classify(self, instance):
        # store the feature values as a mapping scheme
        attributes = dict()
        # add all 4 features from each row in the iris dataset
        # to the attributes dictionary as a valid feature name to value
        # key value pair
        attributes["sepal_length"] = instance[0]
        attributes["sepal_width"] = instance[1]
        attributes["petal_length"] = instance[2]
        attributes["petal_width"] = instance[3]
        # return the proper predicted iris plant classification
        # using our MulticlassPerceptron model from above
        return self.model.predict(attributes)


# Test cases for IrisClassifier
# c = IrisClassifier(data.iris)
# print(c.classify((5.1, 3.5, 1.4, 0.2)))
# c = IrisClassifier(data.iris)
# print(c.classify((7.0, 3.2, 4.7, 1.4)))


class DigitClassifier(object):

    def __init__(self, data):
        rows_with_digits = []
        # iterate through the rows in the digit pixel dataset
        for value in data:
            # x_val is a tuple of 64 elements containing
            # pixel counts between digits 0 -16 inclusively
            x_val = value[0]
            # y_val is digit represented by the image in te dataset
            y_val = value[1]
            # store the feature values as a mapping scheme
            attributes = dict()
            # for every digit in the x tuple,
            # conctenate with the "pixel_" string
            # literal and add it as a new key value pair
            # with the digit as a value
            # to our feature dict
            for i in range(0, len(x_val), 1):
                temp = "pixel_" + str(i)
                attributes[temp] = x_val[i]
            # fully convert each row in the pixel dataset into
            # a clear valid tuple to add to our rows_with_digits list
            row_val = (attributes, y_val)
            rows_with_digits.append(row_val)
        # create a mutliclassperception instance from our class above
        # to be used as their machine learning model to later classify
        # the pixel dataset values
        self.model = MulticlassPerceptron(rows_with_digits, 20)

    def classify(self, instance):
        # store the feature values as a mapping scheme
        attributes = dict()
        # for every digit in the instance tuple,
        # concatenate with the "pixel_" string
        # literal and add it as a new key value
        # pair with the digit as a value
        # to our feature dict
        for i in range(0, len(instance), 1):
            temp = "pixel_" + str(i)
            attributes[temp] = instance[i]
        # return the proper predicted digit pixel classification
        # using our MulticlassPerceptron model from above
        return self.model.predict(attributes)


# Test case
# c = DigitClassifier(data.digits)
# print(c.classify((0, 0,5, 13, 9, 1, 0, 0,0,0,13,15,10,15,5,0,0,3,
# 15,2,0,11,8,0,0,4,12,0,0,8,8,0,0,5,8,0,0,9,8,0,0,4,11,
# 0,1,12,7,0,0,2,14,5,10,12,0,0,0,0,6,13,10,0,0,0)))


class BiasClassifier(object):

    def __init__(self, data):
        example_list = []
        # iterate through the rows in the data.bias
        # dataset and for each row, add it to our attributes
        # dictionary mapping scheme to use our BinaryPerception
        # class model
        for value in data:
            x_val = value[0]
            y_val = value[1]
            attributes = dict()
            attributes["x"] = x_val
            # add a bais feature to each of the rows in the
            # dataset
            attributes["bias"] = 1
            # fully convert each row in the bias dataset into
            # a clear valid tuple to add to our examples list
            row_val = (attributes, y_val)
            example_list.append(row_val)
        # Use our BinaryPerceptron model from above as compling
        # with the assingment instructions
        self.model = BinaryPerceptron(example_list, 15)

    def classify(self, instance):
        # dictionary mapping scheme to
        # store the rows in he bias dataset properly
        attributes = dict()
        attributes["x"] = instance
        # add a bias feature to each of the rows in the
        # dataset
        attributes["bias"] = 1
        # return the proper predicted bias classifier classification
        # using our BinaryPerceptron model from above
        result = self.model.predict(attributes)
        return result


# Test case for BiasClassifierClass
# c = BiasClassifier(data.bias)
# print([c.classify(x) for x in (-1, 0, 0.5, 1.5, 2)])


class MysteryClassifier1(object):

    def __init__(self, data):
        example_list = []
        # iterate through the rows in the data.mystery1
        # dataset and for each row, add it to our attributes
        # dictionary mapping scheme to use our BinaryPerception
        # class model
        for value in data:
            x_val = value[0]
            y_val = value[1]

            # each x value is a 2 item tuple
            # consisting of a coordinate pair for a point
            # y value is the binary classification label of
            # the feature point
            attributes = dict()
            # ensure linear seperation is possible by squaring both x value
            # tuple values to gether and summing their results
            higher_dimension = (x_val[0] ** 2) + (x_val[1] ** 2)
            attributes["higher_dimension"] = higher_dimension
            # add a bias feature to each of the rows in the
            # dataset
            attributes["bias"] = 1
            # fully convert each row in the mystery1 dataset into
            # a clear valid tuple to add to our examples list
            row_val = (attributes, y_val)
            example_list.append(row_val)
        # Use our BinaryPerceptron model from above as compling
        # with the assingment instructions
        self.model = BinaryPerceptron(example_list, 20)

    def classify(self, instance):
        # x_val1 = instance[0]
        # x_val2 = instance[1]
        # dictionary mapping scheme to
        # store the rows in the mystery1 dataset properly
        attributes = dict()
        # ensure linear seperation is possible by squaring both x value
        # tuple values to gether and summing their results
        higher_dimension = (instance[0] ** 2) + (instance[1] ** 2)
        attributes["higher_dimension"] = higher_dimension
        # add a bias feature to each of the rows in the
        # dataset
        attributes["bias"] = 1
        # return the proper predicted mystery 1 classifier classification
        # using our BinaryPerceptron model from above
        result = self.model.predict(attributes)
        return result


# Test case for MysteryClassifier1 code
# c = MysteryClassifier1(data.mystery1)
# print([c.classify(x) for x in ((0, 0), (0, 1),
# (-1, 0), (1, 2), (-3, -4))])


class MysteryClassifier2(object):

    def __init__(self, data):
        example_list = []
        # iterate through the rows in the data.mystery2
        # dataset and for each row, add it to our attributes
        # dictionary mapping scheme to use our BinaryPerception
        # class model
        for value in data:
            x_val = value[0]
            y_val = value[1]
            # each x value is a 3 item tuple
            # consisting of a coordinate pair for a point
            # y value is the binary classification label of
            # the feature point
            attributes = dict()
            x_val1 = x_val[0]
            x_val2 = x_val[1]
            x_val3 = x_val[2]
            # ensure linear seperation is possible by
            # taking the product of all three
            # x values
            # tuple values to gather their commulative results
            three_dimensional = x_val1 * x_val2 * x_val3
            attributes["three_dimensional"] = three_dimensional
            # add a bias feature to each of the rows in the
            # dataset
            attributes["bias"] = 1
            # fully convert each row in the mystery2 dataset into
            # a clear valid tuple to add to our examples list
            row_val = (attributes, y_val)
            example_list.append(row_val)
        # Use our BinaryPerceptron model from above compliing
        # with the assignment instructions
        self.model = BinaryPerceptron(example_list, 20)

    def classify(self, instance):
        # dictionary mapping scheme to
        # store the rows in the mystery2 dataset properly
        attributes = dict()
        # ensure linear seperation is
        # possible by taking the product of all three
        # x values
        # tuple values to gather their results
        three_dimensional = instance[0] * instance[1] * instance[2]
        attributes["three_dimensional"] = three_dimensional
        # add a bias feature to each of the rows in the
        # dataset
        attributes["bias"] = 1
        # return the proper predicted mystery2 classifier classification
        # using our BinaryPerceptron model from above
        result = self.model.predict(attributes)
        return result


# Test case for MysteryClassifier2 class
# c = MysteryClassifier2(data.mystery2)
# print([c.classify(x) for x in ((1, 1, 1), (-1, -1, -1),
# (1, 2, -3), (-1, -2, 3))])


############################################################
# Section 3: Feedback
############################################################


# Just an approximation is fine.
feedback_question_1 = """
I spent anywhere around 13 - 14 hours working
on this homework assignment
spread out during this week
"""

feedback_question_2 = """
I found the creation of the multiclass
perceptron to be the toughest part of this
assingment as it had requried be to fully
understand how basic perceptrons worked
with the help of outside Youtube videos.
I had to try to visulize on pen and paper
how a multiclass perceptron can be drawn
and applied to a specific dataset which was
challenging but also very engaging
"""

feedback_question_3 = """
I liked working through the datasets
from the data file as it gave hands
on exprience with working on the two models I was able to
create above. Specifically revisiting the famous iris dataset was fun
as in my prior Data Mining class, I had applied the KNN algorithm to this
dataset and comparing and contrasting it with a multiclass Perceptron was
quite surprising.
"""
