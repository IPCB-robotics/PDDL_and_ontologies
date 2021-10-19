(define
	(domain aircargo)
	(:requirements :strips :typing :fluents :disjunctive-preconditions :durative-actions)
	(:types
		airport
		cargo
		plane
	)
	(:predicates
		(cargo-at ?c - cargo ?a - airport)
		(in ?c - cargo ?p - plane)
		(plane-at ?p - plane ?a - airport)
	)
	(:durative-action unload
		:parameters (?c - cargo ?p - plane ?a - airport)
		:duration ( >= ?duration 3)
		:condition (and (at start (in ?c ?p)) (at end (plane-at ?p ?a)) (at end (plane-at ?p ?a)))
		:effect (and (at start (cargo-at ?c ?a)) (at end (not (in ?c ?p))))
	)
)