"""
Problem
Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.

Given two strings s
and t of equal length, the Hamming distance between s and t, denoted dH(s,t), 
is the number of corresponding symbols that differ in s and t

. See Figure 2.

Given: Two DNA strings s
and t

of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)

.
Sample Dataset

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output

7
"""

test = """GAGCCTACTAACGGGAT\nCATCGTAATGACGGCCT"""


def count_point_mutations(sequence_1, sequence_2):
    mismatched = 0
    for i in range(len(sequence_1)):
        if sequence_1[i] != sequence_2[i]:
            mismatched += 1
    return mismatched


if __name__ == '__main__':
    sequences = test.split('\n')
    ans = count_point_mutations(*sequences)
    print(ans)
    with open('rosalind_hamm.txt') as infile:
        sequences = [line.strip('\n') for line in infile]
    ans = count_point_mutations(*sequences)
    print(ans)