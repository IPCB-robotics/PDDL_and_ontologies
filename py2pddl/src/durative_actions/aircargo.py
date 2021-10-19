from py2pddl import Domain, create_type
from py2pddl import predicate, action, goal, init


class AirCargoDomain(Domain):

    Plane = create_type("Plane")
    Cargo = create_type("Cargo")
    Airport = create_type("Airport")

    @predicate(Cargo, Airport)
    def cargo_at(self, c, a):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(Plane, Airport)
    def plane_at(self, p, a):
        """Complete the method signature and specify
        the respective types in the decorator"""

    @predicate(Cargo, Plane)
    def in_(self, c, p):
        """Complete the method signature and specify
        the respective types in the decorator"""


    @action(Cargo, Plane, Airport)
    def unload(self, c, p, a):
        durat = [">=", 3]
        precond = ["at start", self.in_(c, p), "at end", self.plane_at(p, a), "at end", self.plane_at(p, a)]
        effect = ["at start", self.cargo_at(c, a), "at end", ~self.in_(c, p)]
        return durat, precond, effect


class AirCargoProblem(AirCargoDomain):

    def __init__(self):
        super().__init__()
        self.cargos = AirCargoDomain.Cargo.create_objs([1, 2], prefix="c")
        self.planes = AirCargoDomain.Plane.create_objs([1, 2], prefix="p")
        self.airports = AirCargoDomain.Airport.create_objs(["sfo", "jfk"])

    @init
    def init(self):
        at = [self.cargo_at(self.cargos[1], self.airports["sfo"]),
              self.cargo_at(self.cargos[2], self.airports["jfk"]),
              self.plane_at(self.planes[1], self.airports["sfo"]),
              self.plane_at(self.planes[2], self.airports["jfk"]),]
        return at

    @goal
    def goal(self):
        return [self.cargo_at(self.cargos[1], self.airports["jfk"]),
                self.cargo_at(self.cargos[2], self.airports["sfo"])]