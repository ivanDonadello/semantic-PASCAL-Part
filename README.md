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


## Structure of LTN folder

- `pascalpart_dataset`: it contains the refined images and annotations (e.g., small specific parts are merged into bigger parts) of pascalpart dataset in pascalvoc style. This folder is necessary if you want to train Fast-RCNN (https://github.com/rbgirshick/fast-rcnn) on this dataset for computing the grounding/features vector of each bounding box.
    - `Annotations`: the annotations in `.xml` format. To see bounding boxes in the images use the pascalvoc devkit http://host.robots.ox.ac.uk/pascal/VOC/index.html.
    - `ImageSets`: the split of the dataset into train and test set according to every unary predicate/class. For further information See pascalvoc format at devkit http://host.robots.ox.ac.uk/pascal/VOC/index.html.
    - `JPEGImages`: the images in `.jpg` format.
