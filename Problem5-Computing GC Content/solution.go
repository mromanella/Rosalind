package main

// Problem
// The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

// DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

// In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

// Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

// Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

// Sample Dataset
// >Rosalind_6404
// CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
// TCCCACTAATAATTCTGAGG
// >Rosalind_5959
// CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
// ATATCCATTTGTCAGCAGACACGC
// >Rosalind_0808
// CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
// TGGGAACCTGCGGGCAGTAGGTGGAAT
// Sample Output
// Rosalind_0808
// 60.919540

import (
	"fmt"
	"sort"
	"strings"

	"../utils"
)

var (
	testString = `>Rosalind_6404
	CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
	TCCCACTAATAATTCTGAGG
	>Rosalind_5959
	CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
	ATATCCATTTGTCAGCAGACACGC
	>Rosalind_0808
	CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
	TGGGAACCTGCGGGCAGTAGGTGGAAT`
	expected  = "Rosalind_0808"
	expected2 = "Rosalind_4710"
)

type rank struct {
	name       string
	percentage float64
}

type ranks []rank

func (r ranks) Len() int {
	return len(r)
}
func (r ranks) Swap(i, j int) {
	r[i], r[j] = r[j], r[i]
}
func (r ranks) Less(i, j int) bool {
	return r[i].percentage > r[j].percentage
}

func (r rank) String() string {
	return fmt.Sprintf("(%s, %f)", r.name, r.percentage)
}

// GCContent performs the gc ration on the str.
func GCContent(DNAString string) float64 {
	return float64(strings.Count(DNAString, utils.Guanine)+strings.Count(DNAString, utils.Cytosine)) / float64(len(DNAString))
}

func main() {
	rosalinds := strings.Split(testString, ">")
	ranking := make(ranks, 0)
	for _, r := range rosalinds {
		if r != "" && len(strings.TrimSpace(r)) != 0 {
			r = strings.TrimSpace(r)
			r = strings.Replace(r, "\n", "", -1)
			r = strings.Replace(r, "\t", "", -1)
			name := r[:13]
			DNAString := r[13:]
			ranking = append(ranking, rank{name, GCContent(DNAString)})
		}
	}
	// fmt.Println(ranking)
	sort.Slice(ranking, func(i, j int) bool { return ranking[i].percentage > ranking[j].percentage })
	fmt.Println(ranking[0].name == expected)

	ros, err := utils.ReadLines("rosalind_gc.txt", -1)
	rosalinds = strings.Split(strings.Join(ros, ""), ">")
	if err != nil {
		panic(err)
	}
	ranking = make(ranks, 0)
	for _, r := range rosalinds {
		if r != "" && len(strings.TrimSpace(r)) != 0 {
			r = strings.TrimSpace(r)
			r = strings.Replace(r, "\n", "", -1)
			r = strings.Replace(r, "\t", "", -1)
			name := r[:13]
			DNAString := r[13:]
			ranking = append(ranking, rank{name, GCContent(DNAString)})
		}
	}
	sort.Slice(ranking, func(i, j int) bool { return ranking[i].percentage > ranking[j].percentage })
	fmt.Println(ranking[0].name == expected2)
}
