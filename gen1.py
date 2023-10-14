import sys
import itertools
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import lru_cache
import cytoolz as ct

@lru_cache(maxsize=None)
def generate_combinations(parts):
    return list(itertools.permutations(parts))

def process_url(url, extensions):
    protocol = re.search(r'^https?://', url.strip()).group(0)
    url = re.sub(r'^https?://', '', url.strip())
    parts = tuple(url.split('.'))
    if len(parts) > 4:
        combinations = [parts]
    else:
        combinations = generate_combinations(parts)

    def generate_permutations():
        for p in combinations:
            yield '-'.join(p)
            yield '_'.join(p)
            yield '.'.join(p)

    def generate_backup_permutations():
        for c in generate_permutations():
            for ext in extensions:
                yield f'{c}{ext}'

    base_url = f'{protocol}{url}'

    for c in ct.concatv(generate_permutations(), generate_backup_permutations()):
        yield f'{base_url}/{c}'

def main(urls_file, extensions_file):
    with open(urls_file, 'r') as f:
        urls = f.readlines()

    with open(extensions_file, 'r') as f:
        extensions = [line.strip() for line in f.readlines()]

    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(process_url, url, extensions): url for url in urls}
        for future in as_completed(futures):
            for url in future.result():
                print(url)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python url_wordlist_generator.py <urls_file> <extensions_file>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
