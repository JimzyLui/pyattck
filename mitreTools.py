#!/usr/local/bin/python3

import argparse
import sys
# import pyattck
import platformstats
import malwareByPlatform
import actorByMalware
import malwareSearch

'''
def run(platform, verbose):
    platform = platform.lower()
    print('entered: ', platform)
    att = pyattck.Attck()

    for malware in att.malwares:
        if platform == 'all':
            printData(platform, malware, verbose)
        elif platform == 'none':
            if malware.platforms is None:
                printData(platform, malware, verbose)
        else:
            if malware.platforms is not None:
                arr_platforms = list(map(str.lower, malware.platforms))
                if arr_platforms.count(platform) > 0:
                    printData(platform, malware, verbose)


def printData(platform, malware, verbose):
    print('Malware Name: ', malware.name)
    if verbose:
        print('Platforms:', malware.platforms)
        print('Description: ', malware.description, '\n')
'''

'''
        This is the single entrypoint to run all tools using Python's pyattck module to utilize the Mitre Network.
  '''
if __name__ == "__main__":
    # create parser
    parser = argparse.ArgumentParser(
        prog='mitreTools',
        description="A centralized location to run python tools that access the Mitre ATT&CK Framework.",
        add_help=True)
    arrToolChoices = ['pso', 'malwareByPlatform',
                      'linux', 'macos', 'none', 'android']
    parser.add_argument('tool',
                        default='pso', const='pso',
                        nargs='?', choices=arrToolChoices,
                        type=str.lower)
    # subparsers = parser.add_subparsers()

    parser_malwareByPlatform = parser.add_argument_group(
        'malewarByPlatform', 'List malware by platform')
    arrPlatformChoices = ['all', 'windows',
                          'linux', 'macos', 'none', 'android']
    parser_malwareByPlatform.add_argument('-p', '--platform',
                                          default='all', const='all',
                                          nargs='?', choices=arrPlatformChoices,
                                          type=str.lower)

    # parser.add_argument("platform", help = "the platform that the malware attacks (case insensitive)")
    parser_malwareByPlatform.add_argument(
        "-ps", "--platform_stats",
        action='store_true',
        help="Show the count of malware per platform")
    parser_malwareByPlatform.add_argument(
        "-pso", "--platform_statsonly",
        action='store_true',
        help="Show the count of malware per platform. Nothing else.")
    parser_malwareByPlatform.add_argument("-v", "--verbose",
                                          action="store_true",
                                          help="Show details (applicable platforms and descriptions)")
    parser.print_help()

    # parser_malwareByPlatform.set_defaults(func=malwareByPlatform)

    args = parser.parse_args()
    verbose = args.verbose
    if verbose:
        print(f'Running: {sys.argv[0]}')

    # if(not args.platform_statsonly):
    if args.tool == 'platform':
        malwareByPlatform.run(args.platform, verbose)

    if args.platform_stats or args.platform_statsonly:
        platformstats.run()
