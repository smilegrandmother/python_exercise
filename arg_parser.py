#!/usr/bin/python3

import argparse
import os

parser = argparse.ArgumentParser()

#parser.add_mutually_exclusive_group()
parser.add_argument('-t', '--triangle', help='Triangle to file.', type = int)
parser.add_argument('-d', '--delete', action='store_true', help='delete file.')
parser.add_argument('filename')

# print(parser.parse_args())
args = parser.parse_args()
if args.delete:
    if os.path.isfile(args.filename):
        os.remove(args.filename)

elif args.triangle:    
    print(os.path.isfile(args.filename))
    with open(args.filename, 'w') as f:
        for i in range(args.triangle):
            print('*' * (i + 1), file=f)
    """
    f = open(args.filename, 'w')
    for i in range(0, args.triangle):
        f.write( '*' * (i+1) + '\n')
    f.close()
    """

else:
    if os.path.isfile(args.filename):
        with open(args.filename, 'r') as f:
            print(f.read(), end='')
    else:
        print('File not exists.')
    
    
#if argparse.