"""Problem
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t."""

import sys
sys.path.append('../utils')

test_string = 'GATGGAACTTGACTACGTAAATT'
expected = 'GAUGGAACUUGACUACGUAAAUU'


def transcribe(dna_string):
    """Transcribes the dna_string into an rna_string, replacing thymine with uracil."""
    from utils import thymine, uracil
    return dna_string.replace(thymine, uracil)


if __name__ == '__main__':
    assert transcribe(test_string) == expected
    with open('rosalind_rna.txt') as infile:
        print(transcribe(infile.read().strip()))
