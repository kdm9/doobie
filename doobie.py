#!/usr/bin/env python

from __future__ import print_function
import hashlib
import os
import sys


def human_size(num, exp=1024.0):
    exp = float(exp)
    for x in ['B','KB','MB','GB', 'TB', 'PB', 'EB']:
        if num < exp:
            return "{:3.1f}{}".format(num, x)
        num /= exp
    return "{:3.1f}{}".format(num, 'YB')

class Doobie(object):
    """Doobie: Hash in a pipe
    """
    hasher = None

    def __init__(self, verbosity=0):
        self.verbosity = verbosity

    def hash(self, input_fh=sys.stdin, output_fh=sys.stderr):
        # Never print messages to a file
        if not os.isatty(sys.stderr.fileno()):
            self.verbosity = 0
        # if we're supposed to print to stderr, don't print verbose stuff
        if output_fh is sys.stderr:
            self.verbosity = 0
        hasher_inst = self.hasher()
        bytes_proc = 0
        buf = input_fh.read(1024)
        while len(buf) > 0:
            bytes_proc += 1024
            hasher_inst.update(buf)
            sys.stdout.write(buf) # emit buffer again on stderr
            sys.stdout.flush()
            if self.verbosity > 0:
                if bytes_proc % (1024 * 1024) == 0:
                    print("Processed", human_size(bytes_proc).rjust(8),
                          end='\r', file=sys.stderr)
            buf = input_fh.read(1024)
        if self.verbosity > 0:
            print(file=sys.stderr)
        output_fh.write(hasher_inst.hexdigest())
        input_fh.close()
        output_fh.close()

class DoobieMD5(Doobie):
    hasher = hashlib.md5

class DoobieSHA1(Doobie):
    hasher = hashlib.sha1

class DoobieSHA224(Doobie):
    hasher = hashlib.sha224

class DoobieSHA256(Doobie):
    hasher = hashlib.sha256

class DoobieSHA384(Doobie):
    hasher = hashlib.sha384

class DoobieSHA512(Doobie):
    hasher = hashlib.sha512

HASH_CLASS_MAP = {
    "md5": DoobieMD5,
    "sha1": DoobieSHA1,
    "sha224": DoobieSHA224,
    "sha256": DoobieSHA256,
    "sha384": DoobieSHA384,
    "sha512": DoobieSHA512,
}

if __name__ == "__main__":
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
