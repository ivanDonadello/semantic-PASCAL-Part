# semantic-PASCAL-Part
This is a curated semantic version of the PASCAL-Part dataset for part-based object detection. Objects are concepts in the provided ontology and are aligned with the synsets of [WordNet](https://wordnet.princeton.edu/) and with the concepts of [Yago](https://yago-knowledge.org/) where possible.

The original [PASCAL-Part dataset](https://www.cs.stanford.edu/~roozbeh/pascal-parts/pascal-parts.html) contains objects labelled with classes of animals, vehicles, indoor objects and their parts. However, labels for parts are very specific, e.g., “left lower leg” and “right hand” and in many applications of semantic image interpretation such a fine-grained distinction is not necessary. Therefore, we merged the segments of the images that refer to the same part in a unique segment, e.g. two segments labelled with “left lower leg” and “left front leg” of the same leg have been merged in a segment labelled with “leg”. Then, we converted the segments into bounding boxes.

We also provide a semantics to these labels by aligning them with a corresponding synset of WordNet and a corresponding concept of Yago if possible.

## Structure of the semantic PASCAL-Part Dataset
Download the data [here](https://drive.google.com/file/d/1m1YHlisEFvlQa52zdab6Q7qqhHQP9Vtl/view?usp=sharing) and unzip the semantic PASCAL-Part Dataset:

- `semanticPascalPart`: it contains the refined images and annotations (e.g., small specific parts are merged into bigger parts) of the PASCAL-Part dataset in Pascal-voc style.
    - `Annotations_set`: the test set annotations in `.xml` format. For further information See the PASCAL VOC format [here](http://host.robots.ox.ac.uk/pascal/VOC/index.html).
    - `Annotations_trainval`: the train and validation set annotations in `.xml` format. For further information See the PASCAL VOC format [here](http://host.robots.ox.ac.uk/pascal/VOC/index.html).
    - `JPEGImages_test`: the test set images in `.jpg` format.
    - `JPEGImages_trainval`: the train and validation set images in `.jpg` format.
    - `test.txt`: the 2416 image filenames in the test set.
    - `trainval.txt`: the 7687 image filenames in the train and validation set.

## The PASCAL-Part Ontology
The PASCAL-Part OWL ontology formalizes, through logical axioms, the part-of relationship between whole objects (22 classes) and their parts (39 classes). The ontology contains 85 logical axiomns in Description Logic in (for example) the following form:
```
Every potted_plant has exactly 1 plant AND
                   has exactly 1 pot
```
We provide two versions of the ontology: with and without cardinality constraints in order to allow users to experiment with or without them. The WordNet alignment is encoded in the ontology as annotations. We further provide the `WordNet_Yago_alignment.csv` file with both WordNet and Yago alignments.

The ontology can be browsed with many Semantic Web tools such as:

- [Protégé](https://protege.stanford.edu/): a graphical tool for ongology modelling;
- [OWLAPI](http://owlapi.sourceforge.net/): Java API for manipulating OWL ontologies;
- [rdflib](https://rdflib.readthedocs.io/en/stable/): Python API for working with the RDF format.
- RDF stores: databases for storing and semantically retrieve RDF triples. See [here](https://www.w3.org/wiki/LargeTripleStores) for some examples.


## Provided code
We provide some Python 3 functions for parsing the dataset. Before loading the dataset create an empty annotation object with:
```python
ann = PASCALPArt_annotations()
```
Then, you need to load one of the test or trainval set with:
```python
ann.load_data(split="trainval")
```
You can browse the annotation object with dedicated functions:
- `get_objects(filename)` : given a `filename` of an image, it returns a dictionary containing the objects in the image.
- `get_BB(filename, obj_id)` : given a `filename` of an image, it returns the bounding box coordinates of `obj_id`.
- `get_obj_class(filename, obj_id)` : given a `filename` of an image, it returns the ontology string class of `obj_id`.
- `get_isPartOf_id(filename, obj_id)` : given a `filename` of an image, it returns the id the whole object of `obj_id`.
- `get_whole_ids(filename, obj_id)` : given a `filename` of an image, it returns the list if ids of the part objects of `obj_id`.

Last, you convert the annotation object into an RDF ontology:
```python
ann_rdf = ann.toRDF("trainval")
```
The function `toRDF` is built by using the previous browsing functions. It is possible to create a whole RDF file with both trainval and test set by instantiating the annotation object only one time:
```python
ann = PASCALPArt_annotations()
ann.load_data(split="trainval")
ann.load_data(split="test")
ann_rdf = ann.toRDF()
```

## Citing semantic PASCAL-Part

If you use semantic PASCAL-Part in your research, please use the following BibTeX entry

```
@article{DBLP:journals/ia/DonadelloS16,
  author    = {Ivan Donadello and
               Luciano Serafini},
  title     = {Integration of numeric and symbolic information for semantic image
               interpretation},
  journal   = {Intelligenza Artificiale},
  volume    = {10},
  number    = {1},
  pages     = {33--47},
  year      = {2016}
}
```
