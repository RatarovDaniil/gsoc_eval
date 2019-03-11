import h5py
import pandas as pd
import argparse
import os, sys

# parse arguments
parser = argparse.ArgumentParser(description='Create .csv file with all of the groups and datasets.')
parser.add_argument('input', help='path to the input file')
parser.add_argument('output', help='path to the output file')

args = parser.parse_args()

class Queue():
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def pushBack(self, item):
        self.items.append(item)

    def popFront(self):
        if self.empty():
            raise Exception("Queue: 'popFront' applied to empty container")
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def BFS(file):
    q = Queue()
    q.pushBack(file)
    data = {}

    while not q.empty():
        current = q.popFront()

        if isinstance(current, h5py.Dataset):
            try:
                data[current.name] = ['dataset', current.size, current.shape, current.dtype]
            # TypeError: No NumPy equivalent for TypeBitfieldID exists
            except TypeError:
                data[current.name] = ['dataset', current.size, current.shape, None]
        else:
            data[current.name] = ['group', None, None, None]
            if isinstance(current, h5py.Group):
                [q.pushBack(current[key]) for key in list(current)]
            # Datatype object
            else:
                data[current.name] = ['group', None, None, current.dtype]

    return data

with h5py.File(args.input, 'r') as file:
    data = BFS(file)
    
    df = pd.DataFrame.from_dict(data, orient='index', columns=['class','size','shape','dtype'])
    if '.csv' in args.output:
        df.to_csv(args.output)
    else:
        df.to_csv(str(args.output) + '.csv')