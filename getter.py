import urllib.parse
import requests

# ANSI escape codes for text color
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

# Function to extract URLs with GET parameters and check HTTP status codes
def extract_urls_with_get_params(input_file, output_file, success_file):
    urls_with_get_params = []
    success_urls = []

    try:
        with open(input_file, 'r') as infile:
            for line in infile:
                line = line.strip()
                try:
                    # Parse the URL
                    parsed_url = urllib.parse.urlparse(line)
                    
                    # Check if the URL has GET parameters
                    if parsed_url.query:
                        urls_with_get_params.append(line)
                except ValueError as e:
                    # Handle invalid URLs gracefully
                    print(f"Invalid URL: {line} - {str(e)}")

        # Save the results to the output file and check HTTP status codes
        with open(output_file, 'w') as outfile:
            outfile.write("URLs with GET parameters and their HTTP status codes:\n")
            for url in urls_with_get_params:
                response = requests.get(url)
                status_code = response.status_code
                if status_code == 200:
                    success_urls.append(url)
                    colored_url = GREEN + url + RESET
                else:
                    colored_url = RED + url + RESET
                outfile.write(f"{colored_url} - HTTP Status Code: {status_code}\n")

        # Save the success URLs to a separate file
        with open(success_file, 'w') as successfile:
            successfile.write("URLs with HTTP status code 200 (OK):\n")
            for url in success_urls:
                successfile.write(url + '\n')

        print(f"Results saved to {output_file}")
        print(f"Success URLs saved to {success_file}")

        # Display the results in the terminal
        print("URLs with GET parameters and their HTTP status codes:")
        for url in urls_with_get_params:
            response = requests.get(url)
            status_code = response.status_code
            if status_code == 200:
                colored_url = GREEN + url + RESET
            else:
                colored_url = RED + url + RESET
            print(f"{colored_url} - HTTP Status Code: {status_code}")

    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
        return []

# Prompt the user to enter the input and output file paths
input_file = input("Enter the path to the input file containing URLs: ")
output_file = input("Enter the path to the output file to save all results: ")
success_file = input("Enter the path to the output file to save success URLs (HTTP 200): ")

# Extract URLs with GET parameters, save results, and display in the terminal with colors
extract_urls_with_get_params(input_file, output_file, success_file)
