# Evaluation test for GSOC Project

Firstly, install requirements.txt:
```
pip install -r requirements.txt
```

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
To run the code, type in the terminal:
```
python get_image.py '/path/to/your/h5/file/1541962108935000000_167_838.h5'
```
It will show you an image and save it as .png file.

![Add img](streak_image.png?raw=true "Title")
