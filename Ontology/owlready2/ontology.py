#!/usr/bin/python

from owlready2 import *

#  Loading an ontology from OWL files
#
# Owlready2 currently reads the following file format: RDF/XML, OWL/XML, NTriples. The file format is automatically detected.
# RDF/XML is the most common format;

onto = get_ontology("file:///home/ist-linux/Desktop/Ontology/Ontologia.owl").load()



# .classes() : returns a generator for the Classes defined in the ontology (see Classes and Individuals (Instances))
# .individuals() : returns a generator for the individuals (or instances) defined in the ontology (see Classes and Individuals (Instances))
# .object_properties() : returns a generator for ObjectProperties defined in the ontology (see Properties)
# .data_properties() : returns a generator for DataProperties defined in the ontology (see Properties)
# .annotation_properties() : returns a generator for AnnotationProperties defined in the ontology (see Annotations)
# .properties() : returns a generator for all Properties (object-, data- and annotation-) defined in the ontology
# .disjoint_classes() : returns a generator for AllDisjoint constructs for Classes defined in the ontology (see Disjointness, open and local closed world reasoning)
# .disjoint_properties() : returns a generator for AllDisjoint constructs for Properties defined in the ontology (see Disjointness, open and local closed world reasoning)
# .disjoints() : returns a generator for AllDisjoint constructs (for Classes and Properties) defined in the ontology
# .different_individuals() : returns a generator for AllDifferent constructs for individuals defined in the ontology (see Disjointness, open and local closed world reasoning)
# .get_namepace(base_iri) : returns a namespace for the ontology and the given base IRI (see namespaces below, in the next section)

#Print number of classes 

n_classes = len(list(onto.classes()))
print(n_classes)

# Print list of individuals

print(list(onto.individuals()))

## Print a ancestors of Indoor_environment
print(onto.Indoor_environment.ancestors())

## Simple queries


# Warning

# .search() does not perform any kind of reasoning, it just searches in asserted facts. In addition, it cannot find Classes through SOME or ONLY restrictions.

# Simple queries can be performed with the .search() method of the ontology. It expects one or several keyword arguments. The supported keywords are:

#     iri, for searching entities by its full IRI
#     type, for searching Individuals of a given Class
#     subclass_of, for searching subclasses of a given Class
#     is_a, for searching both Individuals and subclasses of a given Class
#     subproperty_of, for searching subproperty of a given Property
#     any object, data or annotation property name

# Special arguments are:

#     _use_str_as_loc_str: whether to treats plain Python strings as strings in any language (default is True)
#     _case_sensitive: whether to take lower/upper case into consideration (default is True)
#     _bm25: if True, returns a list of (entity, relevance) pairs instead of just the entities (default is False)


 print(onto.search(is_a = onto.Environment))

# Saving an ontology to an OWL file

onto.save(file = "filename", format = "rdfxml")

# Creating Individuals

# Creação de um individuo de uma determinada classe

my_individual = onto.Arm_robot("my_individual")

# or
unamed_individual = onto.Arm_robot()

# Destroying entities

# The destroy_entity() global function can be used to destroy an entity, i.e. to remove it from the ontology and the quad store.

destroy_entity(onto.arm_robot1)
destroy_entity(onto.my_individual)


# The .instances() class method can be used to iterate through all Instances of a Class (including its subclasses). It returns a generator.

for i in onto.Chair.instances(): print(i)

# Introspecting Individuals

#The list of properties that exist for a given individual can be obtained by the .get_properties() method. It returns a generator that yields the properties (without dupplicates).

onto.Chair_1.get_properties()

#### Properties
#### Creating a new class of property

# A new property can be created by sublcassing the ObjectProperty or DataProperty class. The ‘domain’ and ‘range’ properties can be used to specify the domain and the range of the property. Domain and range must be given in list, since OWL allows to specify several domains or ranges for a given property (if multiple domains or ranges are specified, the domain or range is the intersection of them, i.e. the items in the list are combined with an AND logical operator).

# The following example creates two Classes, Drug and Ingredient, and then an ObjectProperty that relates them.

# >>> from owlready2 import *

# >>> onto = get_ontology("http://test.org/onto.owl")

# >>> with onto:
# ...     class Drug(Thing):
# ...         pass
# ...     class Ingredient(Thing):
# ...         pass
# ...     class has_for_ingredient(ObjectProperty):
# ...         domain    = [Drug]
# ...         range     = [Ingredient]

# In addition, the following subclasses of Property are available: FunctionalProperty, InverseFunctionalProperty, TransitiveProperty, SymmetricProperty, 
# AsymmetricProperty, ReflexiveProperty, IrreflexiveProperty. They should be used in addition to ObjectProperty or DataProperty (or the ‘domain >> range’ syntax).

with onto:
        class has_for_ingredient(onto.Rooms >> onto.Environment, TransitiveProperty):
                pass

# Getting domain and range

has_for_ingredient.domain

# Data Property

# A functional property is a property that has a single value for a given instance. Functional properties are created by inheriting the FunctionalProperty class.

with onto:
        class has_for_cost(DataProperty): # Each drug has a single cost
                domain    = [onto.Rooms]
                range     = [float]

my_drug = onto.Rooms("my_drug")

my_drug.has_for_cost = 4.2

print(my_drug.has_for_cost)


# Creating a subproperty

# A subproperty can be created by subclassing a Property class.

# >>> with onto:
# ...     class ActivePrinciple(Ingredient):
# ...         pass
# ...     class has_for_active_principle(has_for_ingredient):
# ...         domain    = [Drug]
# ...         range     = [ActivePrinciple]

## Saber onde está localizada uma instancia usando uma property

print(onto.Chair_1.LocatedAt)

## Getting relation instances

print(list(onto.LocatedAt.get_relations()))


## Reasnoner 

#Hermit

sync_reasoner()

# Pellet

sync_reasoner_pellet()

## Querying inferred classification

# The .get_parents_of(), .get_instances_of() and .get_children_of() methods of an ontology can be used to query the hierarchical relations, limited to those defined in the given ontology. This is commonly used after reasoning, to obtain the inferred hierarchical relations.

#         .get_parents_of(entity) accepts any entity (Class, property or individual), and returns the superclasses (for a class), the superproperties (for a property), or the classes (for an individual). (NB for obtaining all parents, independently of the ontology they are asserted in, use entity.is_a).
#         .get_instances_of(Class) returns the individuals that are asserted as belonging to the given Class in the ontology. (NB for obtaining all instances, independently of the ontology they are asserted in, use Class.instances()).
#         .get_children_of(entity) returns the subclasses (or subproperties) that are asserted for the given Class or property in the ontology. (NB for obtaining all children, independently of the ontology they are asserted in, use entity.subclasses()).



onto.get_instances_of(onto.Bedroom) 
#[Ontologia.BedRoom_1]

onto.get_children_of(onto.Environment)
#[Ontologia.Indoor_environment, Ontologia.Outdoor_environment]
