import argparse
from GHtool import GHtools
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-s","--site")
parser.add_argument("-q","--query_file")
parser.add_argument("-o","--output")
args = parser.parse_args()

if args.query_file==None:
    print("\n\terror!!! you need to input query file")
    sys.exit()

GHtools(args.query_file,args.site,args.output)

sys.exit()
