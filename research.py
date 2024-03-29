#!/usr/local/bin/python3

import argparse
import pyattck


def research(platform, verbose):
    platform = platform.lower()
    print('entered: ', platform)
    att = pyattck.Attck()
    # print(att.malwares[0].platforms[0].title())  // this works

    for x in att.malwares:
        if x.platforms is not None:
            arr_platforms = list(map(str.lower, x.platforms))
            if arr_platforms.count(platform) > 0:
                print('Malware Name: ', x.name)
                print('Platforms:', x.platforms)
                if verbose:
                    print('Description: ', x.description, '\n')


if __name__ == "__main__":
    # create parser
    parser = argparse.ArgumentParser(prog="research", description="")
    parser.add_argument("platform",
                        help="the platform that the malware attacks")
    parser.add_argument("--verbose", action="store_true", help="Show details")
    args = parser.parse_args()
    verbose = args.verbose
    if verbose:
        print('Running: {argv[0]}')

    research(args.platform, verbose)
