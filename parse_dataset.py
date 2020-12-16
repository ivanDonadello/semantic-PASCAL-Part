from rdflib import Graph, Literal, RDF, URIRef
# rdflib knows about some namespaces, like FOAF
from rdflib.namespace import FOAF , XSD, RDF, OWL
import pdb
import csv
from rdflib import Namespace


class PASCALPArt_annotations:
  def __init__(self):
    self.annotations = {
      "00001": {
        "1": {
          "class": "Person",
          "x_1": 1,
          "y_1": 1,
          "x_2": 123,
          "y_2": 124,
          "isPartOf": ""
        },
        "2": {
          "class": "Leg",
          "x_1": 23,
          "y_1": 23,
          "x_2": 44,
          "y_2": 44,
          "isPartOf": "1"
        },
        "3": {
          "class": "Body",
          "x_1": 28,
          "y_1": 321,
          "x_2": 312,
          "y_2": 932,
          "isPartOf": "1"
        }
      },
      "00002": {
        "1": {
          "class": "Horse",
          "x_1": 1,
          "y_1": 1,
          "x_2": 123,
          "y_2": 124,
          "isPartOf": ""
        },
        "2": {
          "class": "Muzzle",
          "x_1": 23,
          "y_1": 23,
          "x_2": 44,
          "y_2": 44,
          "isPartOf": "1"
        },
        "3": {
          "class": "Tail",
          "x_1": 28,
          "y_1": 321,
          "x_2": 312,
          "y_2": 932,
          "isPartOf": "1"
        }
      }
    }

  def get_isPartOf_id(self, filename, obj_id):
    try:
      part_id = self.annotations[filename][obj_id]["isPartOf"]
      if part_id == "":
        print(f"Object {obj_id} in image {filename} is a whole object.")
        return None
      else:
        return part_id
    except KeyError:
      print(f"Annotation file {filename} or object id {obj_id} do not exist.")

  def get_objects(self, filename):
    try:
      return self.annotations[filename]
    except KeyError:
      print(f"Annotation file {filename} does not exist.")  

  def get_obj_class(self, filename, obj_id):
    try:
      return self.annotations[filename][obj_id]["class"]
    except KeyError:
      print(f"Annotation file {filename} or object id {obj_id} do not exist.")

  def get_BB(self, filename, obj_id):
    try:
      x_1 = self.annotations[filename][obj_id]["x_1"]
      y_1 = self.annotations[filename][obj_id]["y_1"]
      x_2 = self.annotations[filename][obj_id]["x_2"]
      y_2 = self.annotations[filename][obj_id]["y_2"]
      return [x_1, y_1, x_2, y_2]
    except KeyError:
      print(f"Annotation file {filename} or object id {obj_id} do not exist.")

  def load_data(self, filename):
    self.annotations = {}

  def toRDF(self):
    pasPart_namespace = Namespace("http://example.org/pasPart/")
    wordnet_yago_alignment = {}
    with open('WordNet_Yago_alignment.tsv') as f:
      reader = csv.DictReader(f, delimiter='\t')
      for row in reader:
        wordnet_yago_alignment[row['PASCAL-Part_class']] = [row['WDsynset'], row['YagoConcept']]

    g = Graph()
    pas_part_IRI = "https://dkm.fbk.eu/ontologies/PASCALPart/"
    g.add((pasPart_namespace.x_1, RDF.type, OWL.DatatypeProperty))
    g.add((pasPart_namespace.y_1, RDF.type, OWL.DatatypeProperty))
    g.add((pasPart_namespace.x_2, RDF.type, OWL.DatatypeProperty))
    g.add((pasPart_namespace.y_2, RDF.type, OWL.DatatypeProperty))
    g.add((pasPart_namespace.partOf, RDF.type, OWL.ObjectProperty))
    for filename in self.annotations.keys():
      for obj_id in self.annotations[filename].keys():
        obj_class = self.get_obj_class(filename, obj_id)
        bb = self.get_BB(filename, obj_id)
        obj_URI = URIRef(f"{pas_part_IRI}{filename}_{obj_class}_{obj_id}")
        class_URI = URIRef(f"{pas_part_IRI}{obj_class}")

        part_id = self.get_isPartOf_id(filename, obj_id)
        if part_id is not None:
          part_class = self.get_obj_class(filename, part_id)
          part_URI = URIRef(f"{pas_part_IRI}{filename}_{part_class}_{part_id}")
          g.add((obj_URI, pasPart_namespace.isPartOf, part_URI))

        g.add((obj_URI, RDF.type, class_URI))
        g.add((obj_URI, pasPart_namespace.x_1, Literal(bb[0])))
        g.add((obj_URI, pasPart_namespace.y_1, Literal(bb[1])))
        g.add((obj_URI, pasPart_namespace.x_2, Literal(bb[2])))
        g.add((obj_URI, pasPart_namespace.y_2, Literal(bb[3])))
        g.add((obj_URI, pasPart_namespace.hasWordnetId, Literal(wordnet_yago_alignment[obj_class][0])))
        g.add((obj_URI, pasPart_namespace.hasYagoConcept, URIRef(wordnet_yago_alignment[obj_class][1])))
    g.serialize(destination='semantic-PASCAL-Part.RDF')
 
ann = PASCALPArt_annotations()
#ee=ann.get_isPartOf_id("00002", "1")
#print(ee)
ee= ann.toRDF()
#print(ee)
