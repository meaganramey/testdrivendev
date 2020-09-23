#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Meagan Ramey"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description="Transforms user's text based upon input commands.")
    parser.add_argument(
        'word', nargs=1,
        help='the word or phrase to be echoed in the terminal')
    parser.add_argument(
        '-u', '--upper', help='Change each letter to uppercase',
        action='store_true')
    parser.add_argument(
        '-l', '--lower', help='Change each letter to lowercase',
        action='store_true')
    parser.add_argument(
        '-t', '--title', help='''Tile case word or pharse.
                                Example: \n
                                example phrase --> Example Phrase''',
        action='store_true')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    name_space = parser.parse_args(args)
    print(name_space)
    return


if __name__ == '__main__':
    main(sys.argv[1:])
