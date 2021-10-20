(define
	(problem robot_base)
	(:domain robot_base)
	(:objects
		kenny - robot
		wp0 wp1 wp2 wp3 wp4 - waypoint
	)
	(:init (robot-at kenny wp1) (docked kenny) (dock-at wp1))
	(:goal (and (visited wp1) (visited wp2) (visited wp3) (docked kenny)))
)
