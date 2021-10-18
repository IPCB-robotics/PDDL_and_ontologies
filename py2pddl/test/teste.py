from py2pddl import Domain, create_type
from py2pddl import predicate, action, goal, init


class 232 232 232Domain(Domain):

    23 = create_type("23")

    @predicate(...)
    def 23(self):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @action(...)
    def 23(self):
        precond: list = None  # to fill in
        effect: list = None  # to fill in
        return precond, effect


class 232 232 232Problem(232 232 232Domain):

    def __init__(self):
        super().__init__()
        """To fill in"""

    @init
    def init(self) -> list:
        # To fill in
        # Return type is a list
        return None

    @goal
    def goal(self) -> list:
        # To fill in
        # Return type is a list
        return None
