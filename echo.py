#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Meagan Ramey"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument(
        'text', nargs=1,
        help='text to be manipulated')
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase',
        action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase',
        action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase',
        action='store_true')
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    name_space = parser.parse_args(args)
    if not name_space:
        parser.print_usage()
        sys.exit(1)
    word = name_space.text[0]
    up = name_space.upper
    lw = name_space.lower
    title = name_space.title
    if up:
        word = word.upper()
    if lw:
        word = word.lower()
    if title:
        word = word.title()

    print(word)


if __name__ == '__main__':
    main(sys.argv[1:])
