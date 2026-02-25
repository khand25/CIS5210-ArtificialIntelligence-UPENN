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
        # assign the best_q_value to negative infinity so that any q_value we calculate
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
        # iterate over the possible actions and calculate the q_value for each action
        # if the q_value is bigger than the current best_q_value, update the best_q_value
        # and the best_possible_action
        for action in possible_actions:
            q_value = self.get_q_value(state, action)
            if q_value > best_q_value:
                best_q_value = q_value
                best_possible_action = action
        return best_possible_action

    def iterate(self):
        """Run single value iteration using Bellman equation:
        V_{k+1}(s) = max_a Q*(s,a)
        Then update values: V*(s) = V_{k+1}(s)
        """
        ...  # TODO


# 2. Policy Iteration
class PolicyIterationAgent(ValueIterationAgent):
    """Implement Policy Iteration Agent.

    The only difference between policy iteration and value iteration is at
    their iteration method. However, if you need to implement helper function
    or override ValueIterationAgent's methods, you can add them as well.
    """

    def iterate(self):
        """Run single policy iteration.
        Fix current policy, iterate state values V(s) until
        |V_{k+1}(s) - V_k(s)| < ε
        """
        epsilon = 1e-6

        ...  # TODO


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
