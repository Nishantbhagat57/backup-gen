import sys
import tldextract

def combinations(words, symbol):
    words_split = words.split(symbol)
    results = [symbol.join(words_split[:i + 1]) for i in range(len(words_split))]
    return results

def concat_extensions(results, extensions):
    extended_results = [''.join([result, extension]) for result in results for extension in extensions]
    return extended_results

def parse_url(url, extensions):
    parsed_url = tldextract.extract(url)
    scheme = url.split(":")[0]

    left_with_word_Z = parsed_url.subdomain
    tld_Y = parsed_url.registered_domain
    company_name_Z = tld_Y.split(".")[0]

    words_Z_dot = combinations(left_with_word_Z.replace("-", "."), '.')
    words_Z_dash = combinations(left_with_word_Z.replace(".", "-"), '-')

    results = []
    results.extend(words_Z_dot)
    results.append(words_Z_dot[-1] + '.' + company_name_Z)
    results.append(words_Z_dot[-1] + '.' + tld_Y)
    results.extend(words_Z_dash)
    results.append(words_Z_dash[-1] + '-' + company_name_Z.replace(".", "-"))
    results.append(words_Z_dash[-1] + '-' + tld_Y.replace(".", "-"))
    results.append(words_Z_dot[-1])

    # Concate results with extensions
    results = concat_extensions(results, extensions)

    return results
  
def get_extensions(ext_filepath):
    with open(ext_filepath, 'r') as ext_file:
        extensions = ext_file.read().splitlines()
        # Check if extensions start with ".", else add one
        extensions = ['.' + ext if ext[0] != '.' else ext for ext in extensions]
        return extensions

def main(url_file_path, ext_filepath):
    extensions = get_extensions(ext_filepath)
    with open(url_file_path, 'r') as url_file:
        for url in url_file:
            url = url.strip()  # Removing leading/trailing whitespaces, if any
            if url:  # In case there are empty lines within file, just skip it
                results = sorted(list(set(parse_url(url, extensions))))
                print("\n".join(results))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
