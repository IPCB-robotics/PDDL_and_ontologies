#!/usr/bin/python

from owlready2 import *

#  Loading an ontology from OWL files
#
# Owlready2 currently reads the following file format: RDF/XML, OWL/XML, NTriples. The file format is automatically detected.
# RDF/XML is the most common format;

onto = get_ontology("file:///home/ist-linux/Desktop/Ontology/Home_Lab.owl").load()

print(onto.Rooms)


