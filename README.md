# backup-gen

**Backup Files URLs Generator** is a useful penetration testing tool that helps generate a comprehensive list of potential backup file URLs based on a given list of live URLs and associated backup file extensions or backup file wordlist.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Results](#results)
- [FAQ](#faq)
- [License](#license)

## Features

- Generates URL combinations for potential backup files.
- Handles large hostnames intelligently.
- Accepts input files for live URLs and backup file extensions or backup file wordlist and generates potential backup files wordlist.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Nishantbhagat57/backup-gen.git
   ```

2. Change to the project directory:
  
   ```bash
   cd backup-gen
   ```

3. Install required packages:

   ```bash
   pip3 install tldextract
   ```


# Usage
```
python gen.py <urls_file> <extensions_file>
```

```
python gen.py <urls_file> <backup_wordlist_file>
```

- ```<urls_file>:``` A text file containing live URLs, one per line.
- ```<extensions_file>:``` A text file containing backup file extensions, one per line.
- ```<backup_wordlist_file>:``` A text file containing backup file extensions, one per line.


# Examples

### Example of input files

urls.txt
  ```
  https://app.example.com
  http://subdomain.example.org
  https://dev.app.anything.me.xyz.example.com.au
  ```

extensions.txt
  ```
  .example
  .OLD
  .bak
  ```

backup_wordlist.txt
  ```
  .administration.sql
  .admin.old
  .admin.rar
  .wordpress.sql.zip
  .wordpress.tar.gz
  ```

# Generated Combinations/Permutations

Combinations Generated for URL https://dev.app.anything.me.xyz.example.com.au
```
dev
dev-app
dev-app-anything
dev-app-anything-me
dev-app-anything-me-xyz
dev-app-anything-me-xyz-example
dev-app-anything-me-xyz-example-com-au
dev.app
dev.app.anything
dev.app.anything.me
dev.app.anything.me.xyz
dev.app.anything.me.xyz.example
dev.app.anything.me.xyz.example.com.au
xyz
```

# Results

Command Used : ```python3 gen.py urls.txt extensions.txt```

urls.txt:
```https://dev.app.anything.me.xyz.example.com.au```

extensions.txt
```
.OLD
.db
.BAK
```

Output result
```
dev-app-anything-me-xyz-example-com-au.BAK
dev-app-anything-me-xyz-example-com-au.OLD
dev-app-anything-me-xyz-example-com-au.db
dev-app-anything-me-xyz-example.BAK
dev-app-anything-me-xyz-example.OLD
dev-app-anything-me-xyz-example.db
dev-app-anything-me-xyz.BAK
dev-app-anything-me-xyz.OLD
dev-app-anything-me-xyz.db
dev-app-anything-me.BAK
dev-app-anything-me.OLD
dev-app-anything-me.db
dev-app-anything.BAK
dev-app-anything.OLD
dev-app-anything.db
dev-app.BAK
dev-app.OLD
dev-app.db
dev.BAK
dev.OLD
dev.app.BAK
dev.app.OLD
dev.app.anything.BAK
dev.app.anything.OLD
dev.app.anything.db
dev.app.anything.me.BAK
dev.app.anything.me.OLD
dev.app.anything.me.db
dev.app.anything.me.xyz.BAK
dev.app.anything.me.xyz.OLD
dev.app.anything.me.xyz.db
dev.app.anything.me.xyz.example.BAK
dev.app.anything.me.xyz.example.OLD
dev.app.anything.me.xyz.example.com.au.BAK
dev.app.anything.me.xyz.example.com.au.OLD
dev.app.anything.me.xyz.example.com.au.db
dev.app.anything.me.xyz.example.db
dev.app.db
dev.db
```

## FAQ

### How many URL combinations will it form for a single URL?

The number of URL combinations generated for a single URL depends on the number of parts in the hostname and the number of extensions provided (in gen1.py).

- For hostnames with 4 or fewer distinct parts and a list of m extensions:

    ```Total combinations: 6 * m + 6```

- For hostnames with more than 4 distinct parts and a list of m extensions:

    ```Total combinations: 3 * m + 3```

# License
Backup URL Wordlist Generator is released under the [MIT License](LICENSE).
