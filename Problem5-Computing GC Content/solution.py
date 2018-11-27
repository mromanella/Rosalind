"""

Problem
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

Sample Dataset
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
Sample Output
Rosalind_0808
60.919540
"""


import sys
sys.path.append('../utils')


test_string = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""


def gc_content(dna_string):
    """Performs the gc ration on the str."""
    from utils import guanine, cytosine
    return (dna_string.count(guanine) + dna_string.count(cytosine)) / len(dna_string)


if __name__ == '__main__':
    rosalinds = test_string.split('>')
    rank = []
    for r in rosalinds:
        if r and not r.isspace():
            r = r.strip().replace('\n', '')
            name = r[:13]
            dna_string = r[13:]
            rank.append((name, gc_content(dna_string)))
    print(sorted(rank, key=lambda x: x[1], reverse=True))
    with open('rosalind_gc.txt') as infile:
        rosalinds = infile.read().split('>')
    rank = []
    for r in rosalinds:
        if r and not r.isspace():
            r = r.strip().replace('\n', '')
            name = r[:13]
            dna_string = r[13:]
            rank.append((name, gc_content(dna_string)))
    print(sorted(rank, key=lambda x: x[1], reverse=True))
