import random

student_name = "Danyal Razaa Khan"


# 1. Q-Learning
class QLearningAgent:
    """Implement Q Reinforcement Learning Agent using Q-table."""

    def __init__(self, game, discount, learning_rate, explore_prob):
        """Store any needed parameters into the agent object.
        Initialize Q-table.
        """
        self.game = game
        self.discount = discount
        self.learning_rate = learning_rate
        self.explore_prob = explore_prob
        # store a table of possible q values that can be
        # later updated as needed
        self.possible_q_values = dict()

    def get_q_value(self, state, action):
        """Retrieve Q-value from Q-table.
        For an never seen (s,a) pair, the Q-value is by default 0.
        """
        result = self.possible_q_values.get((state, action), 0)
        return result

    def get_value(self, state):
        """Compute state value from Q-values using Bellman Equation.
        V(s) = max_a Q(s,a)
        """
        # grab the possible actions from the game object as a set
        # for later examaniation
        possible_actions = self.game.get_actions(state)
        # if the action set is empty, then there are no possible
        # actions available so return 0
        if not possible_actions:
            return 0
        # build an empty list to store q values in to later return the
        # max q value from easier
        list_of_qs = []
        # iterate through the set of possible actions and on each iteration
        # call the get_q_value function from above and append the resultant
        # q value to our list
        for current_action in possible_actions:
            list_of_qs.append(self.get_q_value(state, current_action))
        # Use Python's built in max function to return maximum q value from our
        # list
        return max(list_of_qs)

    def get_best_policy(self, state):
        """Compute the best action to take in the
        state using Policy Extraction.
        π(s) = argmax_a Q(s,a)

        If there are ties, return a random one for better performance.
        Hint: use random.choice().
        """
        # grab the possible actions from the game object as a set
        # for later examaniation
        possible_actions = self.game.get_actions(state)
        # if there action set is empty signifying no
        # actions, return 0
        if not possible_actions:
            return None
        # call our previous get_value function to retreive the
        # highest q value from the table
        best_possible_value = self.get_value(state)
        best_possible_actions = []
        # iterate through the set of possible actions and on each iteration
        # call the get_q_value function from above and append the resultant
        # q value to our best_possible_actions list
        for current_action in possible_actions:
            # if the current q value is equivalent to the best possible q value
            # then add it's action to our best_possible_actions list to return
            # later actions from
            if self.get_q_value(state, current_action) == best_possible_value:
                best_possible_actions.append(current_action)
        # return a random policy from mutiple best policies if there
        # are ties
        result = random.choice(best_possible_actions)
        return result

    def update(self, state, action, next_state, reward):
        """Update Q-values using running average.
        Q(s,a) = (1 - α) Q(s,a) + α (R + γ V(s'))
        Where α is the learning rate, and γ is the discount.

        Note: You should not call this function in your code.
        """
        # Q(s,a) == get_q_value(state, action)
        # first half of the equation
        # grab our current q value
        current_q = self.get_q_value(state, action)
        # using our current q value multiply it by
        # the 1 - the learning rate defined by our
        # internal instance variable
        current_q *= (1 - self.learning_rate)
        # RHS of the equation where we take the product
        # of the learning rate with the reward summed with the
        # product of the discount and current value
        updated_reward = self.learning_rate * (reward +
                                               (self.discount *
                                                self.get_value(next_state)))
        # the new q value we get after fully applying the formula above
        new_q = current_q + updated_reward
        # update our current q table with the new next q value we just
        # calculated!
        self.possible_q_values[(state, action)] = new_q

    # 2. Epsilon Greedy
    def get_action(self, state):
        """Compute the action to take for the agent, incorporating exploration.
        That is, with probability ε, act randomly.
        Otherwise, act according to the best policy.

        Hint: use random.random() < ε to check if exploration is needed.
        """
        return None  # TODO


# 3. Bridge Crossing Revisited
def question3():
    epsilon = ...
    learning_rate = ...
    return epsilon, learning_rate
    # If not possible, return 'NOT POSSIBLE'


# 5. Approximate Q-Learning
class ApproximateQAgent(QLearningAgent):
    """Implement Approximate Q Learning Agent using weights."""

    def __init__(self, *args, extractor):
        """Initialize parameters and store the feature extractor.
        Initialize weights table."""

        super().__init__(*args)
        ...  # TODO

    def get_weight(self, feature):
        """Get weight of a feature.
        Never seen feature should have a weight of 0.
        """
        return 0  # TODO

    def get_q_value(self, state, action):
        """Compute Q value based on the dot
        product of feature components and weights.
        Q(s,a) = w_1 * f_1(s,a) + w_2 * f_2(s,a)
        + ... + w_n * f_n(s,a)
        """
        return 0  # TODO

    def update(self, state, action, next_state, reward):
        """Update weights using least-squares approximation.
        Δ = R + γ V(s') - Q(s,a)
        Then update weights: w_i = w_i + α * Δ * f_i(s, a)
        """
        ...  # TODO


# 6. Feedback
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
