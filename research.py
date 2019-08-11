#!/usr/local/bin/python3

import argparse
import pyattck


def research(platform):
    att = pyattck.Attck()
    # print(att.malwares[0].platforms[0].title())

    for x in att.malwares:
        if x.platforms is not None and x.platforms.count(platform) > 0:
            print('Name: ', x.name)
            print('Platform:', x.platforms)
            print('Description: ', x.description, '\n')


if __name__ == "__main__":
    # create parser
    parser = argparse.ArgumentParser(prog="xxxx", description="")
    parser.add_argument("platform",
                        help="the platform that the malware attacks")
    parser.add_argument("--verbose", action="store_true", help="Show details")
    args = parser.parse_args()
    verbose = args.verbose
    if verbose:
        print('Running: {argv[0]}')

    research(args.platform)
