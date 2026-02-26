# Include your imports here, if any are used.
from collections import defaultdict

student_name = "Danyal Razaa Khan"


# 1. Value Iteration
class ValueIterationAgent:
    """Implement Value Iteration Agent using Bellman Equations."""

    def __init__(self, game, discount):
        """Store game object and discount value into the agent object,
        initialize values if needed.
        """
        self.game = game
        # make sure to keep the discount value between 0 and 1
        # floating point number
        self.discount = float(discount)
        # Intialize all the state values 0
        # V0(s) = 0
        # end of the line, not going to count
        # anymore future rewards.
        self.values = defaultdict(float)

    def get_value(self, state):
        """Return value V*(s) correspond to state.
        State values should be stored directly for quick retrieval.
        """
        # retun the value of the state from the values dictionary
        value = self.values.get(state, 0.0)
        value = float(value)
        return value

    def get_q_value(self, state, action):
        """Return Q*(s,a) correspond to state and action.
        Q-state values should be computed using Bellman equation:
        Q*(s,a) = Σ_s' T(s,a,s') [R(s,a,s') + γ V*(s')]
        """
        q_value = 0.0
        # get the transistion probabilities and rewards for the given state
        # state and action from the game object
        transition_function = self.game.get_transitions(state, action)
        # iterate over the possible new states and their probabilities
        # for each new state, calculate the reward and the value of the new
        # state and add it to the q_value
        for new_state, probability in transition_function.items():
            reward = self.game.get_reward(state, action, new_state)
            q_value += float(probability) * (float(reward) + self.discount *
                                             self.get_value(new_state))
        return q_value

    def get_best_policy(self, state):
        """Return policy π*(s) correspond to state.
        Policy should be extracted from Q-state values using policy extraction:
        π*(s) = argmax_a Q*(s,a)
        """
        best_possible_action = None
        # assign the best_q_value to negative
        # infinity so that any q_value we calculate
        # will be greater than it and we can update the best_q_value and the
        # best_possible_action accordingly
        best_q_value = float('-inf')
        # grab the possible actions for the given state from the generic
        # game object as a set object
        possible_actions = self.game.get_actions(state)
        # if we are in a terminal state, there are no possible actions,
        # so return None
        if not possible_actions:
            return None
        # iterate over the possible actions and
        # calculate the q_value for each action
        # if the q_value is bigger than
        # the current best_q_value, update the best_q_value
        # and the best_possible_action
        for action in possible_actions:
            q_value = self.get_q_value(state, action)
            if q_value > best_q_value:
                best_q_value = q_value
                best_possible_action = action
        return best_possible_action

    def iterate_helper(self, state, previous_values):
        # helper funtion to get the value of the previous state
        result = float(previous_values.get(state, 0.0))
        return result

    def iterate(self):
        """Run single value iteration using Bellman equation:
        V_{k+1}(s) = max_a Q*(s,a)
        Then update values: V*(s) = V_{k+1}(s)
        """
        # grab the instantanious values for all the states in the game object
        previous_values = dict(self.values)
        new_values = defaultdict(float)
        # iterate over all the states in the game object and
        # calculate the new value for each state
        # using the iterate_helper function
        for current_state in self.game.states:
            possible_actions = self.game.get_actions(current_state)

            # if we are in a terminal state, there are no possible actions,
            # so the value of the state is 0
            if not possible_actions:
                new_values[current_state] = 0.0
            else:
                # othewise, we are not in a terminal state, so we need
                # to calculate the new value for the state using the Bellman
                # equation and the iterate_helper function
                # assign the best_q_value to
                # negative infinity so that any q_value
                # we calculate will be greater than it
                best_q_value = float('-inf')
                # iterate over the possible actions and
                # calculate the q_value for
                # each action
                for action in possible_actions:
                    q_value = 0.0
                    # grab the possible new states and
                    # their probabilities for the
                    # given state and action from the game object
                    list_of_transitions = self.game.get_transitions(
                        current_state, action)
                    for new_state, prob in list_of_transitions.items():
                        # calculate the reward
                        # for the given state and new state
                        given_reward = self.game.get_reward(current_state,
                                                            action,
                                                            new_state)
                        # calculate the new q_value using
                        # the Bellman equation and the iterate
                        # helper function
                        q_value += float(prob) * (
                            float(given_reward) + self.discount *
                            self.iterate_helper(new_state, previous_values)
                        )
                    # if the q_value is now bigger
                    # than the current best_q_value, update
                    # it accordingly
                    if q_value > best_q_value:
                        best_q_value = q_value
                new_values[current_state] = best_q_value
        # update the values with the new values
        # for all the states
        self.values = new_values


# 2. Policy Iteration
class PolicyIterationAgent(ValueIterationAgent):
    """Implement Policy Iteration Agent.

    The only difference between policy iteration and value iteration is at
    their iteration method. However, if you need to implement helper function
    or override ValueIterationAgent's methods, you can add them as well.
    """

    def __init__(self, game, discount):
        # You can call the parent class constructor to initialize
        # the game and discount value
        super().__init__(game, discount)
        # initialize the policy for each state to be an empty
        # dictionary, which will be updated in the iterate function
        self.current_policy = dict()

    def iterate(self):
        """Run single policy iteration.
        Fix current policy, iterate state values V(s) until
        |V_{k+1}(s) - V_k(s)| < ε
        """
        # epsilon value already given
        epsilon = 1e-6
        # create the original policy
        unchanged_policy = dict()
        # iterate over all the states in the game object and
        # calculate the new value for each state
        for current_state in self.game.states:
            possible_actions = self.game.get_actions(current_state)
            # if we are in a terminal state, then there are no
            # possible actions, so the value of the state is 0
            if not possible_actions:
                unchanged_policy[current_state] = None
            else:
                # otherwise, we are not in a terminal state
                # capture the old policy action for
                # the state as from the current policy
                # dictionary
                old_policy_act = self.current_policy.get(current_state, None)
                # if the old policy action is not None and
                # it is in the possible actions, then we can
                # keep the same policy for the state
                if old_policy_act in possible_actions:
                    unchanged_policy[current_state] = old_policy_act
                else:
                    # otherwise, we need to update the policy for the state
                    # to be the first possible action for the state
                    for cur_action in possible_actions:
                        unchanged_policy[current_state] = cur_action
                        break
        # start of the policy iteration loop algorithm
        possible_values = dict(self.values)
        # boolean variable to keep track to
        # control the while loop for iterating
        # the values until convergence
        continue_iteration = True
        while continue_iteration:
            # discount coefficient
            discount_value = 0.0
            new_values = defaultdict(float)
            # iterate over all the states in the game object
            for current_state in self.game.states:
                action_to_take = unchanged_policy.get(current_state, None)
                # if the action to take is None, then we are in a terminal
                # state, so the value of the state is 0
                if action_to_take is None:
                    new_values[current_state] = 0.0
                else:
                    # otherwise, we are not in a terminal state, so we
                    # need to calculate the new value for the state using
                    # the Bellman equation
                    value_variable = 0.0
                    list_of_transitions = self.game.get_transitions(
                        current_state,
                        action_to_take)
                    # iterate over the possible new states
                    # and their probabilities
                    # for each new state,
                    # calculate the reward and the value of the
                    # new state and add it to the value variable
                    for new_state, probability in list_of_transitions.items():
                        given_reward = self.game.get_reward(current_state,
                                                            action_to_take,
                                                            new_state)
                        value_variable += float(probability) * (
                            float(given_reward) + self.discount *
                            possible_values.get(new_state, 0.0)
                        )
                    # update the new value for the
                    # current state in the new values
                    # dictionary and update the discount
                    # value to be the maximum
                    # of the current discount value
                    # and the absolute value of the
                    # difference between old and new values
                    new_values[current_state] = value_variable
                    discount_value = max(discount_value,
                                         abs(value_variable -
                                             float(possible_values.get(
                                                 current_state, 0.0))
                                             ))
            possible_values = dict(new_values)

            # if the discount value smaller than epsilon, then we can stop
            # iterating and update the policy
            if discount_value < epsilon:
                continue_iteration = False
        # update the policy
        # convergence has been reached, so we can update
        # the policy
        self.values = defaultdict(float, possible_values)

        # improvement of the policy
        # Step 2 of the algorithm
        better_policy = dict()
        # iterate over all the states in the game object and
        # calculate te best action for each state using the get
        # q_value function and update the better policy accordingly
        for current_state in self.game.states:
            possible_actions = self.game.get_actions(current_state)
            # if we are in a terminal state, then there are no
            # possible actions, so the policy is None
            if not possible_actions:
                better_policy[current_state] = None
            else:
                best_q_value = float('-inf')
                best_possible_action = None
                # iterate over the possible actions
                # and calculate the q_value for each
                # action using the get_q_value function
                for action in possible_actions:
                    q_value = self.get_q_value(current_state, action)
                    # if the q_value is now bigger
                    # than the current best_q_value, update
                    # it accordingly
                    if q_value > best_q_value:
                        best_q_value = q_value
                        best_possible_action = action
                better_policy[current_state] = best_possible_action
        # update the current policy with the better policy
        # we have just found!
        self.current_policy = better_policy


# 3. Bridge Crossing Analysis
def question_3():
    discount = ...
    noise = ...
    return discount, noise


# 4. Policies
def question_4a():
    discount = ...
    noise = ...
    living_reward = ...
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4b():
    discount = ...
    noise = ...
    living_reward = ...
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4c():
    discount = ...
    noise = ...
    living_reward = ...
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4d():
    discount = ...
    noise = ...
    living_reward = ...
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4e():
    discount = ...
    noise = ...
    living_reward = ...
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


# 5. Feedback
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
