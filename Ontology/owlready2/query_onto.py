#!/usr/bin/python3

from owlready2 import *
import os

file_location = "/Users/rodrigobernardo/Documents/VS/Ontology/Home_Lab.owl"
onto = get_ontology(file_location).load()

# Extract name of the file .owl
file_name = os.path.basename(file_location)
file_name = file_name.replace(".owl","")


def remove_mainclass(list,file_name):
    clear_list = []
    for x in list:
        clear_list.append(str.replace(str(x),file_name+".", ''))
    return (clear_list)

def save_ontology(file_location):
    onto.save(file = file_location)

## Search instances of Class
def instances_class(Class):    
    return getattr(onto, Class).instances()

## Search properties of different instances
def properties_instance(instance):    
    return (getattr(onto, instance).get_properties())

## Information of instance based on property
def information_instance(instance,property):    
    return (getattr(getattr(onto, instance), property))

## Create an instance of a given class
def create_instance(instance,Class):
    new_instance = getattr(onto, Class)(instance)
    save_ontology(file_location)
    return (new_instance)

create_instance("Prof_Paulo","Clock")


with onto:
        class has_for_cost(DataProperty): # Each drug has a single cost
                domain    = [onto.Rooms]
                range     = [float]

my_drug = onto.Rooms("my_drug")

my_drug.has_for_cost = 100

print(my_drug.has_for_cost)


## Destroy instance
def destroy_instance(instance):
    return destroy_entity(getattr(onto,instance))

## Create a object property
'''
In addition, the following subclasses of Property are available: FunctionalProperty, InverseFunctionalProperty, TransitiveProperty, SymmetricProperty, 
 AsymmetricProperty, ReflexiveProperty, IrreflexiveProperty.
'''
def funtion():
    input = (TransitiveProperty, SymmetricProperty)
    with onto:
        class is_ingredient(FunctionalProperty):
            domain  = [onto.Environment]
            range  = [onto.Robot]

    def write_rule():
        with onto:
            class Drug(Thing): pass
            class number_of_tablets(Drug >> int, FunctionalProperty): pass
            class price(Drug >> float, FunctionalProperty): pass
            class price_per_tablet(Drug >> float, FunctionalProperty): pass

            rule = Imp()
            rule.set_as_rule("""Drug(?d), price(?d, ?p), number_of_tablets(?d, ?n), divide(?r, ?p, ?n) -> price_per_tablet(?d, ?r)""")
        save_ontology(file_location)
  
drug = onto.Drug(number_of_tablets = 15, price = 40.0)
print(drug)

sync_reasoner_pellet(infer_property_values = True, infer_data_property_values = True)
print(drug.price_per_tablet)

## Create relations of instance
def create_relations_instance(instance,property,relat_instance):
    return None
