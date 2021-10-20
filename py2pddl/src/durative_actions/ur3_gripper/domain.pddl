(define
	(domain ur3_gripper)
	(:requirements :strips :typing :fluents :disjunctive-preconditions :durative-actions)
	(:types
		gripper
		obj
		p_goal
	)
	(:predicates
		(at ?b - obj ?r - p_goal)
		(at-arm ?r - p_goal)
		(carry ?o - obj ?g - gripper)
		(free ?g - gripper)
		(opened ?g - gripper)
	)
	(:durative-action drop
		:parameters (?obj - obj ?p-goal - p-goal ?gripper - gripper)
		:duration ( = ?duration 2)
		:condition (and (at start (carry ?obj ?gripper)) (over all (at-arm ?p-goal)))
		:effect (and (at start (at ?obj ?p-goal)) (at end (free ?gripper)) (at end (not (carry ?obj ?gripper))) (at end (not (opened ?gripper))))
	)
	(:durative-action move-ur3
		:parameters (?loc-from - p-goal ?to - p-goal)
		:duration ( = ?duration 5)
		:condition (at start (at-arm ?loc-from))
		:effect (and (at end (at-arm ?to)) (at start (not (at-arm ?loc-from))))
	)
	(:durative-action open
		:parameters (?gripper - gripper)
		:duration ( = ?duration 2)
		:condition (over all (free ?gripper))
		:effect (over end (opened ?gripper))
	)
	(:durative-action pick
		:parameters (?obj - obj ?p-goal - p-goal ?gripper - gripper)
		:duration ( = ?duration 2)
		:condition (and (at start (at ?obj ?p-goal)) (over all (at-arm ?p-goal)) (at start (free ?gripper)) (at start (opened ?gripper)))
		:effect (and (at end (carry ?obj ?gripper)) (at end (not (at ?obj ?p-goal))) (at start (not (free ?gripper))) (at start (not (opened ?gripper))))
	)
)