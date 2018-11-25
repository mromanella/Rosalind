

"""Problem
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.

Sample Dataset
AAAACCCGGT
Sample Output
ACCGGGTTTT."""

import sys
sys.path.append('../utils')


test_string = 'AAAACCCGGT'
expected = 'ACCGGGTTTT'


def reverse_compliment(dna_string):
    """reverse_compliment reverses the dna_string and switches each base to its compliment."""
    from utils import get_compliment
    dna_string = dna_string[::-1]
    bases = list(dna_string)
    return ''.join([get_compliment(base) for base in bases])


if __name__ == '__main__':
    assert reverse_compliment(test_string) == expected
    with open('rosalind_revc.txt') as infile:
        line = infile.read().strip()
        print(reverse_compliment(line))
