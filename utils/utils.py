import random

adenine = 'A'
cytosine = 'C'
guanine = 'G'
thymine = 'T'
uracil = 'U'

dna_bases = (adenine, cytosine, guanine, thymine)
dna_compliments = (thymine, guanine, cytosine, adenine)
rna_bases = (uracil)


def get_compliment(base):
    return dna_compliments[dna_bases.index(base)]


def random_basepair():
    base = random.choice(dna_bases)
    return ''.join((base, get_compliment(base)))


def generate_basepairs(length):
    return tuple([random_basepair() for _ in range(length)])
