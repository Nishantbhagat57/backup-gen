import sys
import tldextract
import argparse

def combinations(words, symbol):
    words_split = words.split(symbol)
    results = [symbol.join(words_split[:i + 1]) for i in range(len(words_split))]
    return results

def concat_extensions(results, extensions):
    extended_results = [''.join([result, extension]) for result in results for extension in extensions]
    return extended_results

def parse_url(url, extensions, full_url=False):
    parsed_url = tldextract.extract(url)
    scheme = url.split(":")[0]

    left_with_word_Z = parsed_url.subdomain
    tld_Y = parsed_url.registered_domain
    company_name_Z = tld_Y.split(".")[0]

    words_Z_dot = left_with_word_Z.replace("-", ".").split(".")
    words_Z_dash = left_with_word_Z.split("-")

    results_dot = combinations(left_with_word_Z.replace("-", "."), '.')
    results_dash = combinations(left_with_word_Z.replace(".", "-"), '-')

    results = []
    results.extend(results_dot)
    results.append(results_dot[-1] + '.' + company_name_Z)
    results.append(results_dot[-1] + '.' + tld_Y)

    results.extend(results_dash)
    results.append(results_dash[-1] + '-' + company_name_Z.replace('.', '-'))
    results.append(results_dash[-1] + '-' + tld_Y.replace('.', '-'))

    results.append(words_Z_dot[-1])
    results.append(company_name_Z)

    # Check if the full_url flag is true then append the scheme to results
    if full_url:
        results = [scheme + '://' + url + '/' + i for i in results]
    # Concate results with extensions
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
