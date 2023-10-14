import sys
import itertools
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
import cytoolz as ct

def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def remove_http(url):
    return re.sub(r'^https?://', '', url)

def split_hostname(url):
    hostname = remove_http(url)
    return re.split(r'[.-]', hostname)

def create_combinations(words):
    for comb in ['.'.join(words), '-'.join(words)]:
        yield comb

def create_url_combinations(url, backup_files):
    words = split_hostname(url)
    hostname_combinations = list(create_combinations(words))
    file_combinations = []

    for backup_file in backup_files:
        for hostname in hostname_combinations:
            file_combinations.append(f'{hostname}.{backup_file}')

    file_combinations = ct.unique(file_combinations)

    return [f'{url}/{file_combination}' for file_combination in file_combinations]

def process_url(url, backup_files):
    file_combinations = create_url_combinations(url,tuple(backup_files))
    for file_combination in file_combinations:
        print(file_combination)

def main(urls_file, backup_files_file):
    urls = read_file(urls_file)
    backup_files = read_file(backup_files_file)

    with ThreadPoolExecutor() as executor:
        executor.map(process_url, urls, itertools.repeat(tuple(backup_files), len(urls)))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} urls_file backup_files_file')
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
