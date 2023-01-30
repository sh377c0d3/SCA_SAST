<?php

$codeDir = "code";

// Run the SAST scan using the RIPS tool
exec("rips.phar -f csv -d $codeDir", $output);

// Store the results in a CSV file
$fileName = "sast_results.csv";
$file = fopen($fileName, "w");
foreach ($output as $line) {
  fputcsv($file, explode(",", $line));
}
fclose($file);

?>
