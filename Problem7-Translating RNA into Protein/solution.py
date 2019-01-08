"""
Problem

The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet 
(all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. Henceforth, 
the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.

Given: An RNA string s

corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s

.
Sample Dataset

AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output

MAMAPRTEINSTRING
"""

import sys
sys.path.append('../utils')

test1 = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
output1 = 'MAMAPRTEINSTRING'


def get_protein(rna):
    from utils import rna_codon_table
    protein = ''
    i = 0
    while i < len(rna):
        n = rna_codon_table[rna[i:i+3]]
        if n == 'Stop':
            break
        protein += n
        i += 3
    return protein



if __name__ == '__main__':
    # get_protein(test1)
    assert get_protein(test1) == output1, get_protein(test1)
    with open('rosalind_prot.txt') as infile:
        rna = infile.read().strip()
    print(get_protein(rna))