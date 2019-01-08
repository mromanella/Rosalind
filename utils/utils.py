import random

adenine = 'A'
cytosine = 'C'
guanine = 'G'
thymine = 'T'
uracil = 'U'

dna_bases = (adenine, cytosine, guanine, thymine)
dna_compliments = (thymine, guanine, cytosine, adenine)
rna_bases = (uracil)

rna_codon_table = {
    'UUU': 'F',        'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
'UUC': 'F',   'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
'UUA': 'L',   'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
'UUG': 'L',   'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
'UCU': 'S',   'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
'UCC': 'S',   'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
'UCA': 'S',   'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
'UCG': 'S',   'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
'UAU': 'Y',   'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
'UAC': 'Y',   'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
'UAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
'UAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
'UGU': 'C',   'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
'UGC': 'C',   'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
'UGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
'UGG': 'W',   'CGG': 'R',      'AGG': 'R',      'GGG': 'G' 
}


def get_compliment(base):
    return dna_compliments[dna_bases.index(base)]


def random_basepair():
    base = random.choice(dna_bases)
    return ''.join((base, get_compliment(base)))


def generate_basepairs(length):
    return tuple([random_basepair() for _ in range(length)])
