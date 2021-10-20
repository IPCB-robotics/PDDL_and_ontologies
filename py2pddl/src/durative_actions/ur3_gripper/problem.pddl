(define
	(problem ur3_gripper)
	(:domain ur3_gripper)
	(:objects
		robotiq - gripper
		obj0 obj1 obj2 obj3 - obj
		p0 p1 p2 p3 - p_goal
	)
	(:init (at-arm p0) (free robotiq) (at obj1 p3) (at obj2 p3))
	(:goal (and (at obj1 p0) (at obj2 p2)))
)
