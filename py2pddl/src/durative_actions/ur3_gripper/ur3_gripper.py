from py2pddl import Domain, create_type
from py2pddl import predicate, action, goal, init
class UR3_GripperDomain(Domain):

    p_goal = create_type("p_goal")
    obj = create_type("obj")
    gripper = create_type("gripper")

    @predicate(p_goal)
    def at_arm(self, r):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(obj, p_goal)
    def at(self, b, r):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(gripper)
    def free(self, g):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(obj, gripper)
    def carry(self, o, g):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(gripper)
    def opened(self, g):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @action(p_goal, p_goal)
    def move_ur3(self, loc_from, to):
        duration = ["=", 5]
        precond = ["at start", self.at_arm(loc_from)]
        effect = ["at end", self.at_arm(to), "at start", ~self.at_arm(loc_from)]
        return duration, precond, effect

    @action(obj, p_goal, gripper)
    def pick(self, obj, p_goal, gripper):
        duration = ["=", 2]
        precond = ["at start", self.at(obj,p_goal), "over all", self.at_arm(p_goal), "at start", self.free(gripper), "at start", self.opened(gripper)]
        effect  = ["at end", self.carry(obj,gripper), "at end", ~self.at(obj,p_goal), "at start", ~self.free(gripper), "at start", ~self.opened(gripper)]
        return duration, precond, effect

    @action(gripper)
    def open(self, gripper):
        duration = ["=", 2]
        precond = ["over all", self.free(gripper)]
        effect = ["over end", self.opened(gripper)]
        return duration, precond, effect

    @action(obj, p_goal, gripper)
    def drop(self, obj, p_goal, gripper):
        duration = ["=", 2]
        precond = ["at start", self.carry(obj,gripper), "over all", self.at_arm(p_goal)]
        effect = ["at start", self.at(obj,p_goal), "at end", self.free(gripper), "at end", ~self.carry(obj, gripper), "at end", ~self.opened(gripper)]
        return duration, precond, effect


class UR3_GripperProblem(UR3_GripperDomain):

    def __init__(self):
        super().__init__()
        self.p_goals = UR3_GripperDomain.p_goal.create_objs([0,1,2,3], prefix="p")
        self.objects = UR3_GripperDomain.obj.create_objs([0,1,2,3], prefix="obj")
        self.grippers = UR3_GripperDomain.gripper.create_objs(["robotiq"])

    @init
    def init(self) -> list:
        at = [self.at_arm(self.p_goals[0]),
              self.free(self.grippers["robotiq"]),
              self.at(self.objects[1], self.p_goals[3]),
              self.at(self.objects[2], self.p_goals[3])]
        return at
        

    @goal
    def goal(self) -> list:
        return [self.at(self.objects[1], self.p_goals[0]),
                self.at(self.objects[2], self.p_goals[2])]
