from __future__ import print_function
from doobie import (
    HASH_CLASS_MAP,
)

import sys
import argparse

parse = argparse.ArgumentParser(description="Doobie: Hash in a pipe")
parse.add_argument('--hash', '-H', metavar="HASH", type=str, dest="hash",
                   default="sha256", help="The hash to use")
parse.add_argument('--in', '-i', metavar="FILE", type=str, dest="input",
                   default=None, help="Input file, default STDIN")
parse.add_argument('--out', '-o', metavar="FILE", type=str, dest="output",
                   default=None, help="Output file, default STDERR")
parse.add_argument('--verbose', '-v', action='count', dest="verbose",
                   help="Print a progress meter")
args = parse.parse_args()
if args.hash not in HASH_CLASS_MAP:
    print("ERROR: bad hash name", args.hash, file=sys.stderr)
    print("Supported hashes are:", file=sys.stderr)
    for hash in HASH_CLASS_MAP.keys():
        print(" - {}".format(hash), file=sys.stderr)
    exit(1)
# default I/O files
ifh = sys.stdin
ofh = sys.stderr
if args.input is not None:
    ifh = open(args.input)
if args.output is not None:
    ofh = open(args.output, "w")
hasher = HASH_CLASS_MAP[args.hash](verbosity=args.verbose)
hasher.hash(ifh, ofh)
