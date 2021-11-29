
class RobotProblem(RobotDomain):

    def __init__(self):
        super().__init__()
        self.waypoint = RobotDomain.waypoint.create_objs([1,2,3,4,5,6], prefix='wp')
		self.robot = RobotDomain.robot.create_objs(['Kenny'])
		
        

    @init
    def init(self) -> list:
        return [self.robot_at(self.robots['Kenny'], self.waypoints[1]), self.docked(self.robots['Kenny']), self.docked_at(self.waypoints[1])]
        

    @goal
    def goal(self) -> list:
        return [self.visited(self.waypoints[1]), self.visited(self.waypoints[2]), self.visited(self.waypoints[3]), self.docked(self.robots['Kenny'])]
