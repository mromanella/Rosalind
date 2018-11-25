"""Problem
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
Sample Output
20 12 17 21"""


import sys
sys.path.append('../utils')

test_string = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
expected = '20 12 17 21'


def count_nucleobases(dna_string):
    """Counts the amount of nucleobases:
    adenine(A), cytosine(C), guanine(G) and thymine(T).
    Returns four integers seperated by spaces of frequency of occurrence of like (A, C, G, T)."""
    from utils import adenine, cytosine, guanine, thymine
    return ' '.join(map(str,
                        (dna_string.count(adenine),
                         dna_string.count(cytosine),
                         dna_string.count(guanine),
                         dna_string.count(thymine))
                        ))


if __name__ == '__main__':
    assert count_nucleobases(test_string) == expected
    with open('rosalind_dna.txt') as infile:
        print(count_nucleobases(infile.read()))
