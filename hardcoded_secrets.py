import re
import csv
import os

def get_pattern():
    # Define the regex pattern to search for sensitive data
    regex_pattern = [
        re.compile(r'(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b)'|), # email
        re.compile(basic [a-zA-Z0-9_\\-:\\.=]+|bearer [a-zA-Z0-9_\\-\\.=]+) # Authorization
        re.compile(r'(\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b)'|"^4[0-9]{12}(?:[0-9]{3})?$"), # credit and debit card
        re.compile(r'(\b(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}\b)'|[p|P][a|A][s|S][s|S].*\=.*.|[p|P][a|A][s|S][s|S].*\:.*.|[p|P][a|A][s|S].*\:.*.), # password
        re.compile(.........\.[Dd][Bb][^=:]*[:=].*,) # hardcoded database
        re.compile(AIza[0-9A-Za-z\\-_]{35}|[0-9]+-[0-9A-Za-z_]{32}\.apps\.googleusercontent\.com|ya29\\.[0-9A-Za-z\\-_]+) # Google key
        re.compile(crypt_key.*=.*.\w|private.*key|ssh-rsa*.*,|.secret.*.|.*_rsa|.*_dsa|.*_ed25519|.*_ecdsa|.?ssh/config) # crypto key
        re.compile(.pem|.?mysql_history|.?s3cfg|.?htpasswd|.?htaccess) # secret files
        re.compile(.?aws/credentials|(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}|amzn\.mws\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}) #aws secrets and access keys
        re.compile(jenkins.plugins.publish_over_ssh.BapSshPublisherPlugin.xml|xox[baprs]-([0-9a-zA-Z]{10,48})?|hooks.slack.com|https://hooks.slack.com/services/T[a-zA-Z0-9_]{10}/B[a-zA-Z0-9_]{10}/[a-zA-Z0-9_]{24}) # jenkins and slack path
    ]
    return regex_pattern

def search_files(directory, pattern):
    result = []
    # Walk the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        # Loop through each file in the directory
        for file in files:
            file_path = os.path.join(root, file)
            # Try to open the file
            try:
                with open(file_path, 'r') as f:
                    # Read the contents of the file
                    file_contents = f.read()
                    # Use the re module to search for the pattern in the contents of the file
                    match = pattern.search(file_contents)
                    # If a match was found
                    if match:
                        result.append({'file_path': file_path, 'match': match.group()})
            except:
                pass
    return result

def save_to_csv(result, csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['file_path', 'match'])
        writer.writeheader()
        writer.writerows(result)

if __name__ == '__main__':
    # Define the directory containing the code base
    directory = '<DIRECTORY>'
    # Get the regex pattern
    pattern = get_pattern()
    # Search the code base for sensitive data
    result = search_files(directory, pattern)
    # Save the result to a CSV file
    save_to_csv(result, 'result.csv')


    
