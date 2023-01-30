import re
import csv
import os

def get_pattern():
    # Define the regex pattern to search for sensitive data
    regex_pattern = [
        re.compile(r'(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b)'|), # email
        re.compile(r'(\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b)'), # credit card
        re.compile(r'(\b(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}\b)'|[p|P][a|A][s|S][s|S].*\=.*.|[p|P][a|A][s|S][s|S].*\:.*.|[p|P][a|A][s|S].*\:.*.), # password
        re.compile(.........\.[Dd][Bb][^=:]*[:=].*,) # hardcoded database
        re.compile(crypt_key.*=.*.\w|ssh-rsa*.*,|.secret.*.|.*_rsa|.*_dsa|.*_ed25519|.*_ecdsa|.?ssh/config) # crypto key
        re.compile(.pem|.?mysql_history|.?s3cfg|.?htpasswd) # secret files
        re.compile(.?aws/credentials|private.*key|AKIA[0-9A-Z]|AGPA[0-9A-Z]|AIDA[0-9A-Z]|AIPA[0-9A-Z]|ANPA[0-9A-Z]|ANVA[0-9A-Z]|ASIA[0-9A-Z]|AIza[0-9A-Za-z\\-_]) #aws secrets keys
        re.compile(jenkins.plugins.publish_over_ssh.BapSshPublisherPlugin.xml|hooks.slack.com) # jenkins and slack path
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


    
