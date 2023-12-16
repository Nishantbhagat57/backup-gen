import sys
import tldextract
import argparse

def combinations(words, symbol):
    words_split = words.split(symbol)
    # exclude the first combination when split words length is equal to 1
    results = [symbol.join(words_split[:i + 1]) for i in range(len(words_split)) if not(i == 0 and len(words_split) == 1)]
    return [result for result in results if result]

def concat_extensions(results, extensions):
    # filtering out any results that start with "." or "-" or are empty strings
    results = [result for result in results if not result.startswith(("-",".")) and result] 
    extended_results = [''.join([result, extension]) for result in results for extension in extensions]
    return extended_results

def parse_url(url, extensions, full_url=False):
    parsed_url = tldextract.extract(url)
    scheme = url.split(":")[0] if ":" in url else ""

    subdomain_Z = parsed_url.subdomain
    domain_Y = parsed_url.registered_domain

    results_dot = combinations(subdomain_Z.replace("-", "."), '.')
    results_dash = combinations(subdomain_Z.replace(".", "-"), '-')
    results_Y = [domain_Y.split(".")[0], domain_Y, domain_Y.replace(".", "-")]

    results = []
    results.extend(results_dot)
    results.extend(results_dash)
    results.extend(results_Y)

    if full_url and scheme:
        results = [f'{url}/{i}' for i in results]

    results = concat_extensions(results, extensions)

    return results
  
def get_extensions(ext_filepath):
    with open(ext_filepath, 'r') as ext_file:
        extensions = ext_file.read().splitlines()
        # Check if extensions start with ".", else add one
        extensions = ['.' + ext if ext[0] != '.' else ext for ext in extensions]
        return extensions

def main():
    # Using argparse to handle CLI arguments
    parser = argparse.ArgumentParser(description='URL Wordlist Generator')
    parser.add_argument('url_file', type=str, help='The file path for the URLs')
    parser.add_argument('ext_file', type=str, help='The file path for the extensions')
    parser.add_argument('--full', action='store_true', help='Include full urls with http/https scheme')

    args = parser.parse_args()

    extensions = get_extensions(args.ext_file)

    with open(args.url_file, 'r') as url_file:
        for url in url_file:
            url = url.strip()  # Removing leading/trailing whitespaces, if any
            if url:  # In case there are empty lines within file, just skip it
                results = sorted(list(set(parse_url(url, extensions, args.full))))
                print("\n".join(results))

if __name__ == "__main__":
    main()
