(define
	(domain robot_base)
	(:requirements :strips :typing :fluents :disjunctive-preconditions :durative-actions)
	(:types
		robot
		waypoint
	)
	(:predicates
		(dock-at ?wp - waypoint)
		(docked ?v - robot)
		(localised ?v - robot)
		(robot-at ?v - robot ?wp - waypoint)
		(undocked ?v - robot)
		(visited ?wp - waypoint)
	)
	(:durative-action dock
		:parameters (?v - robot ?wp - waypoint)
		:duration ( = ?duration 30)
		:condition (and (over all (dock-at ?wp)) (at start (robot-at ?v ?wp)) (at start (undocked ?v)))
		:effect (and (at end (docked ?v)) (at start (not (undocked ?v))))
	)
	(:durative-action goto-waypoint
		:parameters (?v - robot ?loc-from - waypoint ?to - waypoint)
		:duration ( = ?duration 10)
		:condition (and (at start (robot-at ?v ?loc-from)) (at start (localised ?v)) (over all (undocked ?v)))
		:effect (and (at end (visited ?to)) (at end (robot-at ?v ?to)) (at start (not (robot-at ?v ?loc-from))))
	)
	(:durative-action localise
		:parameters (?v - robot)
		:duration ( = ?duration 60)
		:condition (over all (undocked ?v))
		:effect (at end (localised ?v))
	)
	(:durative-action undock
		:parameters (?v - robot ?wp - waypoint)
		:duration ( = ?duration 5)
		:condition (and (over all (dock-at ?wp)) (at start (docked ?v)))
		:effect (and (at start (not (docked ?v))) (at end (undocked ?v)))
	)
)