#!/usr/bin/python

from py2pddl import Domain, create_type
from py2pddl import predicate, action, goal, init

class Robot_baseDomain(Domain):

    waypoint = create_type("waypoint")
    robot = create_type("robot")

    @predicate(robot, waypoint)
    def robot_at(self, v, wp):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(waypoint)
    def visited(self, wp):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(robot)
    def undocked(self, v):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(robot)
    def docked(self, v):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(robot)
    def localised(self, v):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(waypoint)
    def dock_at(self, wp):
        """Complete the method signature and specify
        the respective types in the decorator"""


    @action(robot, waypoint, waypoint)
    def goto_waypoint(self, v, loc_from, to):
        duration = ["=", 10]
        precond= ["at start", self.robot_at(v,loc_from), "at start", self.localised(v), "over all", self.undocked(v)]
        effect = ["at end", self.visited(to), "at end", self.robot_at(v,to), "at start", ~self.robot_at(v,loc_from)]
        return duration, precond, effect
    #
    @action(robot)
    def localise(self, v):
        duration = ["=", 60]
        precond = ["over all", self.undocked(v)]
        effect = ["at end", self.localised(v)]
        return duration, precond, effect

    @action(robot, waypoint)
    def dock(self, v, wp):
        duration = ["=", 30]
        precond = ["over all", self.dock_at(wp), "at start", self.robot_at(v,wp), "at start", self.undocked(v)]
        effect = ["at end", self.docked(v), "at start", ~self.undocked(v)]
        return duration, precond, effect

    @action(robot, waypoint)
    def undock(self, v, wp):
        duration = ["=", 5]
        precond = ["over all", self.dock_at(wp), "at start", self.docked(v)]
        effect = ["at start", ~self.docked(v), "at end", self.undocked(v)]
        return duration, precond, effect





class RobotProblem(RobotDomain):

    def __init__(self):
        super().__init__()
        self.waypoint = Robot_baseDomain.waypoint.create_objs([1,2,3,4,5,6], prefix='wp')
		self.robot = Robot_baseDomain.robot.create_objs(['Kenny'])
	        

    @init
    def init(self) -> list:
        return [self.robot_at(self.robots['Kenny'], self.waypoints[1]), self.docked(self.robots['Kenny']), self.docked_at(self.waypoints[1])]
        

    @goal
    def goal(self) -> list:
        return [self.visited(self.waypoints[1]), self.visited(self.waypoints[2]), self.visited(self.waypoints[3]), self.docked(self.robots['Kenny'])]
