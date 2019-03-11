# Evaluation test for GSOC Project

## Convert UNIX timestamp

To run the code, type in the terminal:
```
python convert_time.py '/path/to/your/h5/file/1541962108935000000_167_838.h5'
```
It will print coverted UTC and CERN local time into your console.

![Add img](convert_time.png?raw=true "Title")


## Traverse directory tree

To run the code, type in the terminal:
```
python convert_time.py '/path/to/your/h5/file/1541962108935000000_167_838.h5' '/path/to/your/output/file/traverse_directory_tree.csv'
```
It will create .csv file listing all groups and datasets in it with size/shape/dtype information.

## Get image
