package main

import (
	"fmt"
	"strings"

	"../utils"
)

// Problem
// A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

// An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

// Given: A DNA string s of length at most 1000 nt.

// Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

// Sample Dataset
// AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
// Sample Output
// 20 12 17 21

var (
	testString = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
	adenine    = "A"
	cytosine   = "C"
	guanine    = "G"
	thymine    = "T"
	expected   = "20 12 17 21"
)

// countNucleobases counts the amount of nucleobases:
// adenine(A), cytosine(C), guanine(G) and thymine(T).
// Returns four integers seperated by spaces of frequency of occurrence of like (A, C, G, T).
func countNucleobases(DNAString string) string {
	return fmt.Sprintf("%d %d %d %d", strings.Count(DNAString, adenine),
		strings.Count(DNAString, cytosine),
		strings.Count(DNAString, guanine),
		strings.Count(DNAString, thymine))
}

func main() {
	fmt.Println(countNucleobases(testString) == expected)
	lines, err := utils.ReadLines("rosalind_dna.txt", 0)
	if err != nil {
		panic(err)
	}
	fmt.Println(countNucleobases(lines[0]))
}
