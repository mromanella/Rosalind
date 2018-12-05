package main

// Problem
// Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.

// Given two strings s
// and t of equal length, the Hamming distance between s and t, denoted dH(s,t),
// is the number of corresponding symbols that differ in s and t

// . See Figure 2.

// Given: Two DNA strings s
// and t

// of equal length (not exceeding 1 kbp).

// Return: The Hamming distance dH(s,t)

// .
// Sample Dataset

// GAGCCTACTAACGGGAT
// CATCGTAATGACGGCCT

// Sample Output

// 7

import (
	"fmt"
	"strings"

	"../utils"
)

var (
	test           = "GAGCCTACTAACGGGAT\nCATCGTAATGACGGCCT"
	testExpected   = 7
	infile         = "rosalind_hamm.txt"
	infileExpected = 498
)

func countPointMutations(sequence1, sequence2 string) int {
	mismatched := 0
	for i := range sequence1 {
		if sequence1[i] != sequence2[i] {
			mismatched++
		}
	}
	return mismatched
}

func main() {
	sequences := strings.Split(test, "\n")
	ans := countPointMutations(sequences[0], sequences[1])
	fmt.Println(ans)
	fmt.Println(ans == testExpected)
	sequences, _ = utils.ReadLines(infile, -1)
	ans = countPointMutations(sequences[0], sequences[1])
	fmt.Println(ans)
	fmt.Println(ans == infileExpected)
}
