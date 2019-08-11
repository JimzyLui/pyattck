#!/usr/local/bin/python3

import argparse
import sys
import pyattck


def run():
    global platformTally
    platformTally = {}
    att = pyattck.Attck()

    for malware in att.malwares:
        arrPlatforms = malware.platforms
        if arrPlatforms is None:
            arrPlatforms = ['None']
        tallyPlatformList(arrPlatforms)
    # print(platformTally)
    printStats(platformTally)

# print out the stats


def printStats(platformTally):
    print(f'               NUMBER OF')
    print(f'PLATFORM    MALWARE THREATS')
    print(f'________    _______________')
    for keys, values in platformTally.items():
        print(f"{keys:<12}  {values:>6}")


def tallyPlatformList(arrPlatforms):
    global platformTally
    # arrPlatforms = ['a', 'b', 'c', 'b', 'd', 'c']
    # keep track of the number of potential threats to each platform
    # platformTally = {}
    for p in arrPlatforms:
        if p not in platformTally:
            platformTally[p] = 1
        else:
            platformTally[p] += 1
