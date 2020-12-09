# semantic-PASCAL-Part
This is a curated semantic version of the PASCAL-Part dataset for part-based object detection. Objects are concepts in the provided ontology and are aligned with the synsets of [WordNet](https://wordnet.princeton.edu/) and with the concepts of [Yago](https://yago-knowledge.org/) where possible.

[PASCAL-Part dataset](https://www.cs.stanford.edu/~roozbeh/pascal-parts/pascal-parts.html) contains objects labelled with classes of animals, vehicles, indoor objects and their parts. However, labels for parts are very specific, e.g., “left lower leg” and “right hand” and in many applications of semantic image interpretation such a fine-grained distinction is not necessary. Therefore, we merged the segments of the images that refers to the same part in a unique segment, e.g. two segments labelled with “left lower leg” and “left front leg” of the same leg have been merged in a segment labelled with “leg”. Then, we converted the segments into bounding boxes.

We also provide a semantics to the labels of objects by aligning them with a corresponding synset of WordNet and a corresponding concept of Yago if possible.

## Citing semantic PASCAL-Part

If you use semantic PASCAL-Part in your research, please use the following BibTeX entry.

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

## The PASCAL-Part Ontology
The ontologies can be browsed with many Semantic Web tools such as:

- [Protégé](https://protege.stanford.edu/): a graphical tool for ongology modelling;
- [OWLAPI](http://owlapi.sourceforge.net/): Java API for manipulating OWL ontologies;
- [rdflib](https://rdflib.readthedocs.io/en/stable/): Python API for working wwith the RDF format.
- RDF stores: databases for storing and semantically retrieve RDF triples. See [here](https://www.w3.org/wiki/LargeTripleStores) for some examples.

## Structure of the semantic PASCAL-Part Dataset folder
Download the data [here](https://drive.google.com/file/d/1m1YHlisEFvlQa52zdab6Q7qqhHQP9Vtl/view?usp=sharing) and unzip the semantic PASCAL-Part Dataset:

- `semanticPascalPart`: it contains the refined images and annotations (e.g., small specific parts are merged into bigger parts) of the PASCAL-Part dataset in Pascal-voc style.
    - `Annotations_set`: the test set annotations in `.xml` format. For further information See pascalvoc format at devkit http://host.robots.ox.ac.uk/pascal/VOC/index.html.
    - `Annotations_trainval`: the train and validation set annotations in `.xml` format. For further information See pascalvoc format at devkit http://host.robots.ox.ac.uk/pascal/VOC/index.html.
    - `JPEGImages_test`: the test set images in `.jpg` format.
    - `JPEGImages_trainval`: the train and validation set images in `.jpg` format.
    - `test.txt`: the 2416 image filenames in the test set.
    - `trainval.txt`: the 7687 image filenames in the train and validation set.

## Provided code
We provide the code for parsing the dataset. 
