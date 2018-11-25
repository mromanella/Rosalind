// Package utils includes utility functions to help with Rosalind problems
package utils

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strings"
	"time"
)

var (
	// Adenine = "A"
	Adenine = "A"
	// Cytosine = "C"
	Cytosine = "C"
	// Guanine  = "G"
	Guanine = "G"
	// Thymine  = "T"
	Thymine = "T"
	// Uracil = "U"
	Uracil = "U"

	// DNABases is a slice of available bases Adenine, Cytosine, Guanine, Thymine
	DNABases = []string{Adenine, Cytosine, Guanine, Thymine}
	// DNACompliments are the compliments of the bases
	DNACompliments = []string{Thymine, Guanine, Cytosine, Adenine}
	// RNABases are the rna bases (uracil)
	RNABases = []string{Uracil}
)

// ReadLines reads the numLines provided from the given filename and returns a
// list of lines as text with the lines not including "\n" or "\r\n."
// If numLines < 0 return all lines in filename. If numLines = 0, return only 1st line.
func ReadLines(filename string, numLines int) ([]string, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var lines []string
	count := 0
	for scanner.Scan() && count >= numLines {
		line := scanner.Text()
		line = strings.TrimSpace(line)
		lines = append(lines, line)
		count++
	}
	return lines, nil
}

func randomChoice(from []string) string {
	rand.Seed(time.Now().Unix())
	return from[rand.Intn(len(from))]
}

// GetCompliment returns the compliment of the base provided
func GetCompliment(base string) string {
	return DNACompliments[GetStringIndex(DNABases, base)]
}

// RandomBasepair returns a random basepair
func RandomBasepair() string {
	base := randomChoice(DNABases)
	return fmt.Sprintf("%s%s", base, GetCompliment(base))
}

// GenerateBasepairs generates a DNA sequence of length provided
func GenerateBasepairs(length int) []string {
	var basepairs []string
	for i := 0; i < length; i++ {
		basepairs = append(basepairs, RandomBasepair())
	}
	return basepairs
}

// GetStringIndex returns the index of the target in the string slice if found.
// Returns -1 if not found.
func GetStringIndex(slice []string, target string) int {
	for i := range slice {
		if slice[i] == target {
			return i
		}
	}
	return -1
}
