import csv
import packj

def sca_scan(code_dir):
    # Initialize the PackJ library
    packj.init()

    # Scan the code directory
    warnings = packj.scan(code_dir)

    # Close the PackJ library
    packj.close()

    return warnings

def store_results_in_csv(results, file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Library', 'Version', 'Vulnerability', 'Severity'])
        for result in results:
            writer.writerow([result['library'], result['version'], result['vulnerability'], result['severity']])

results = sca_scan('code')
store_results_in_csv(results, 'sca_results.csv')
