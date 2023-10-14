# backup-gen

**Backup URL Wordlist Generator** is a useful penetration testing tool that helps generate a comprehensive list of potential backup file URLs based on a given list of live URLs and associated backup file extensions or backup file wordlist.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [FAQ](#faq)
- [License](#license)

## Features

- Generates URL combinations for potential backup files.
- Handles large hostnames intelligently.
- Supports multi-threading for faster processing.
- Accepts input files for live URLs and backup file extensions.

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
   pip3 install cytoolz
   ```


# Usage
```
python gen1.py <urls_file> <extensions_file>
python gen2.py <urls_file> <backup_wordlist_file>
```

- ```<urls_file>:``` A text file containing live URLs, one per line.
- ```<extensions_file>:``` A text file containing backup file extensions, one per line.
- ```<backup_wordlist_file>:``` A text file containing backup file extensions, one per line.


# Examples

Example of input files:

urls.txt
  ```
  https://app.example.com
  http://subdomain.example.org
  ```

extensions.txt (for gen1.py)
  ```
  .example
  .OLD
  .bak
  ```


backup_wordlist.txt (for gen2.py)
  ```
  administration.sql
  admin.old
  admin.rar
  wordpress.sql.zip
  wordpress.tar.gz
  ```


# Run gen1.py script:

  ```python gen1.py urls.txt extensions.txt```

Output:
  ```
  https://app.example.com/app.zip
  https://app.example.com/example.zip
  https://app.example.com/app.example.zip
  https://app.example.com/example.app.zip
  https://app.example.com/app-example.zip
  https://app.example.com/example-app.zip
  https://app.example.com/app_example.zip
  https://app.example.com/example_app.zip
  https://app.example.com/app.OLD
  https://app.example.com/example.OLD
  https://app.example.com/app.example.OLD
  https://app.example.com/example.app.OLD
  https://app.example.com/app-example.OLD
  https://app.example.com/example-app.OLD
  https://app.example.com/app_example.OLD
  https://app.example.com/example_app.OLD
  ```

# Run gen2.py script:

python gen2.py urls.txt wordlist.txt

Output:
  ```
  https://app.example.com/app.wordpress.sql.zip
  https://app.example.com/example.wordpress.sql.zip
  https://app.example.com/app.example.wordpress.sql.zip
  https://app.example.com/example.app.wordpress.sql.zip
  https://app.example.com/app-example.wordpress.sql.zip
  https://app.example.com/example-app.wordpress.sql.zip
  https://app.example.com/app_example.wordpress.sql.zip
  https://app.example.com/example_app.wordpress.sql.zip
  https://app.example.com/app.wp-config.bk
  https://app.example.com/example.wp-config.bk
  https://app.example.com/app.example.wp-config.bk
  https://app.example.com/example.app.wp-config.bk
  https://app.example.com/app.example.wp-config.bk
  https://app.example.com/example.app.wp-config.bk
  https://app.example.com/app-example.wp-config.bk
  https://app.example.com/example-app.wp-config.bk
  https://app.example.com/app_example.wp-config.bk
  https://app.example.com/example_app.wp-config.bk
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
