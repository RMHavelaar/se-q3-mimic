#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

__author__ = "Robert Havelaar, got some help from Group C study group."


import random
import sys


def create_mimic_dict(filename):
    mimic_dict = dict()
    with open(filename) as f:
        words = f.read().split()
    previous_word = ''
    for word in words:
        if previous_word in mimic_dict:
            mimic_dict[previous_word].append(word)
        else:
            mimic_dict[previous_word] = [word]
        previous_word = word
    return mimic_dict


def print_mimic_random(mimic_dict, num_words):
    start_word = ''
    for i in range(num_words):
        random_word = random.choice(mimic_dict[start_word])
        print(random_word, end=' ')
        if random_word not in mimic_dict:
            start_word = ''
        else:
            start_word = random.choice(mimic_dict[random_word])


def main(args):
    # Get input filename from command line args
    filename = args[0]

    # Create and print the jumbled (mimic) version of the input file
    print(f'Using {filename} as input:\n')
    d = create_mimic_dict(filename)
    print_mimic_random(d, 200)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
    else:
        main(sys.argv[1:])
    print('\n\nCompleted.')
