package main

import (
	"encoding/csv"
	"fmt"
	"os"
	"os/exec"
	"strings"
)

func runCommand(command string) string {
	out, err := exec.Command("sh", "-c", command).Output()
	if err != nil {
		fmt.Printf("error running command: %v\n", err)
		return ""
	}
	return string(out)
}

func sastScan(codeDir string) string {
	command := "gosec -fmt=csv -quiet " + codeDir
	output := runCommand(command)
	return output
}

func storeResultsInCSV(results string, fileName string) {
	file, err := os.Create(fileName)
	if err != nil {
		fmt.Printf("error creating file: %v\n", err)
		return
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	rows := strings.Split(results, "\n")
	for _, row := range rows {
		columns := strings.Split(row, ",")
		if len(columns) == 5 {
			err := writer.Write(columns)
			if err != nil {
				fmt.Printf("error writing row: %v\n", err)
				return
			}
		}
	}
}

func main() {
	codeDir := "code"
	output := sastScan(codeDir)
	fileName := "sast_go-lang_results.csv"
	storeResultsInCSV(output, fileName)
}
