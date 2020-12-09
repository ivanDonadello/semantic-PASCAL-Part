# semantic-PASCAL-Part
This is a curated semantic version of the PASCAL-Part dataset for part-based object detection. Objects are aligned with a provided ontology.




One such a dataset is the PASCAL-P ART dataset
[5]. Image segments of this dataset are labelled with
classes of animals, vehicles, indoor objects and their
parts. However, labels for parts in PASCAL-P ART are
very specific, e.g., “left lower leg” and “right hand”.
Since we are not interested in such a fine-grained dis-
tinction, we merged the segments of the images that
refers to the same part in a unique segment, e.g. two
segments labelled with “left lower leg” and “left front
leg” of the same leg have been merged in a seg-
ment labelled with “leg”.


## Structure of the semanticPascalPartDataset foldr
Download from here and unzip the semantic PASCAL-Part Dataset.

- `semanticPascalPart`: it contains the refined images and annotations (e.g., small specific parts are merged into bigger parts) of the PASCAL-Part dataset in Pascal-voc style.
    - `Annotations_set`: the test set annotations in `.xml` format. For further information See pascalvoc format at devkit http://host.robots.ox.ac.uk/pascal/VOC/index.html.
    - `Annotations_trainval`: the train and validation set annotations in `.xml` format. For further information See pascalvoc format at devkit http://host.robots.ox.ac.uk/pascal/VOC/index.html.
    - `JPEGImages_test`: the test set images in `.jpg` format.
    - `JPEGImages_trainval`: the train and validation set images in `.jpg` format.
    - `test.txt`:
    - `trainval.txt`:
