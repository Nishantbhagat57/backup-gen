# backup-gen

**Backup Files Wordlist Generator** is a useful penetration testing tool that helps generate a comprehensive list of potential backup file Wordlist based on a given list of  URLs and associated backup file extensions or backup file wordlist.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Results](#results)
- [Generated Combinations](#generated-combinationspermutations)
- [Prompt Used For Making This Script](#prompt-used-for-making-this-script)
- [License](#license)

## Features

- Generates URL combinations for potential backup files.
- Handles large hostnames intelligently.
- Generates combinations based on TLD intelligently.
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

```
python gen.py <urls_file> <extensions_file> --full
```

```
python gen.py <urls_file> <backup_wordlist_file> --full
```

- ```<urls_file>:``` Path of text file containing live URLs, one per line.
- ```<extensions_file>:``` Path of text file containing backup file extensions, one per line.
- ```<backup_wordlist_file>:``` Path of text file containing backup file extensions, one per line.
- ```--full``` If used the output result will include full urls with http/https scheme.

# Examples
### Example of input files

- urls.txt
  ```
  https://app.example.com
  http://subdomain.example.org
  https://dev.app.anything.me.xyz.example.com.au
  ```

- extensions.txt
  ```
  .example
  .OLD
  .bak
  ```

- backup_wordlist.txt
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
example
xyz
```

# Results

Command Used : ```python3 gen.py urls.txt extensions.txt```

- urls.txt
   ```
   https://dev.app.anything.me.xyz.example.com.au
   ```

- extensions.txt
   ```
   .OLD
   .db
   .BAK
   ```

- Output result
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
   
Command Used : ```python3 gen.py urls.txt extensions.txt --full```

- urls.txt
   ```
   https://dev.app.anything.me.xyz.example.com.au
   ```

- extensions.txt
   ```
   .OLD
   ```

- Output result
   ```
   https://dev.app.anything.me.xyz.example.com.au/dev-app-anything-me-xyz-example-com-au.OLD
   https://dev.app.anything.me.xyz.example.com.au/dev-app-anything-me-xyz-example.OLD
   https://dev.app.anything.me.xyz.example.com.au/dev-app-anything-me-xyz.OLD
   https://dev.app.anything.me.xyz.example.com.au/dev-app-anything-me.OLD
   https://dev.app.anything.me.xyz.example.com.au/dev-app-anything.OLD
   https://dev.app.anything.me.xyz.example.com.au/dev-app.OLD
   https://dev.app.anything.me.xyz.example.com.au/dev.OLD
   https://dev.app.anything.me.xyz.example.com.au/dev.app.OLD
   https://dev.app.anything.me.xyz.example.com.au/dev.app.anything.OLD
   https://dev.app.anything.me.xyz.example.com.au/dev.app.anything.me.OLD
   https://dev.app.anything.me.xyz.example.com.au/dev.app.anything.me.xyz.OLD
   https://dev.app.anything.me.xyz.example.com.au/dev.app.anything.me.xyz.example.OLD
   https://dev.app.anything.me.xyz.example.com.au/dev.app.anything.me.xyz.example.com.au.OLD
   https://dev.app.anything.me.xyz.example.com.au/example.OLD
   https://dev.app.anything.me.xyz.example.com.au/xyz.OLD
   ```

# Prompt Used For Making This Script

This tool was made using the Power of GPT-4. The full Prompt I used to make this tool

```
I am a Pentester. I want to make a Python script takes a urls file and extensions file in txt and then use permutations and combinations to generate wordlist. But for that I have made a plan that we can use to understand the full process of doing this so we can use the whole process to make our perfect script.

The url file can contains urls like:
https://aireserve-preprod.example.com
https://stagehost-iad.openapi.example.com
https://rsp-core-eg-tst.example.com
and more.....

As a Python Programmer make a Python scrip that:

1. Let the user specify the input urls file in cli like: python3 script.py /path/to/urls.txt
2. Read URL text file and extensions file. From this point we will be talking for the current URL that is being read by our script. We will perform every step below for just this current URL one at a time.
3. Eliminate `www` prefix if present in the url.
4. Identify and preserve original URL's scheme (http/https).
5. Parse the URL to get the full tld like if the url is X then the tld is Y. These are all just examples:
URL(X): https://abc.xyz.example.com.au | TLD(Y): example.com.au
URL(X): https://abc-xyz-1ox-example.com.br | TLD(Y): example.com.br
URL(X): https://app.example.com | TLD(Y): example.com
URL(X): https://dev-history-app.example.in | TLD(Y): example.in

6. Remove the tld part (whether it's connected with - or .) along with http/https protocol so we are left with words(Z):
URL(X): https://abc.xyz.example.com.au | TLD(Y): example.com.au | Left With Word(Z): abc.xyz
URL(X): https://abc-xyz-1ox-example.com.br | TLD(Y): example.com.br | Left With Word(Z): abc-xyz-1ox
URL(X): https://app.example.com | TLD(Y): example.com | Left With Word(Z): app 
URL(X): https://dev-history-app.example.in | TLD(Y): example.in | Left With Word(Z): dev-history-app


7. Remove the tld part (whether it's connected with - or .) along with http/https protocol, but take the company name from the tld, Suppose TLD(X) is tld | CompanyName(Z) is company name:
TLD(X): example.com.au | CompanyName(Y): example
TLD(X): example.com.br | CompanyName(Y): example
TLD(X): example.com | CompanyName(Y): example
TLD(X): example.in | CompanyName(Y): example

Note: Save both TLD(X) as well as CompanyName(Y), we will be using them in later steps.


8. From step 6 take the word that we are "Left With Word(Z)" and from step 7 take the TLD(X) then:
a) IF there's any hyphen (-) in the the "Left With Word(Z)" then replace them with dot (.) AND IF there's any dot (.) in the the "Left With Word(Z)" then replace them with dot (.) and save the result for further usage. Let say that this result is RS1. Example Result of this step:

Result 1 without concating TLD(Y) to our Left With Word(Z)
URL(X): https://abc.xyz.example.com.au | TLD(Y): example.com.au | CompanyName(Z): example | Left With Word(Z): abc.xyz | RS1: abc.xyz
URL(X): https://abc-xyz-1ox-example.com.br | TLD(Y): example.com.br | CompanyName(Z): example | Left With Word(Z): abc-xyz-1ox | RS1: abc.xyz.1ox
URL(X): https://app.example.com | TLD(Y): example.com | CompanyName(Z): example | Left With Word(Z): app | RS1: app
URL(X): https://dev-history-app.example.in | TLD(Y): example.in | CompanyName(Z): example | Left With Word(Z): dev-history-app | RS1: dev.history.app

Result 2 by concating TLD(Y) to our Left With Word(Z) | This Result 2 is just for saving, we wil not perform any combinations on the Result 2.
URL(X): https://abc.xyz.example.com.au | TLD(Y): example.com.au | CompanyName(Z): example | Left With Word(Z): abc.xyz | RS1: abc.xyz.example.com.au
URL(X): https://abc-xyz-1ox-example.com.br | TLD(Y): example.com.br | CompanyName(Z): example | Left With Word(Z): abc-xyz-1ox | RS1: abc.xyz.1ox.example.com.br
URL(X): https://app.example.com | TLD(Y): example.com | CompanyName(Z): example | Left With Word(Z): app | RS1: app.example.com
URL(X): https://dev-history-app.example.in | TLD(Y): example.in | CompanyName(Z): example | Left With Word(Z): dev-history-app | RS1: dev.history.app.example.in

Result 3 by concating CompanyName(Z) to our Left With Word(Z) | This Result 3 is just for saving, we wil not perform any combinations on the Result 3.
URL(X): https://abc.xyz.example.com.au | TLD(Y): example.com.au | CompanyName(Z): example | Left With Word(Z): abc.xyz | RS1: abc.xyz.example
URL(X): https://abc-xyz-1ox-example.com.br | TLD(Y): example.com.br | CompanyName(Z): example | Left With Word(Z): abc-xyz-1ox | RS1: abc.xyz.1ox.example
URL(X): https://app.example.com | TLD(Y): example.com | CompanyName(Z): example | Left With Word(Z): app | RS1: app.example.com
URL(X): https://dev-history-app.example.in | TLD(Y): example.in | CompanyName(Z): example | Left With Word(Z): dev-history-app | RS1: dev.history.app.example

b) IF there's any dot (.) in the the "Left With Word(Z)" then replace them with hyphen (-) AND IF there's any hyphen (-) in the the "Left With Word(Z)" then replace them with hyphen (-) and save the result for further usage. Let say that this result is RS2. Example Result of this step:

Result 1 without concating TLD(Y) to our Left With Word(Z)
URL(X): https://abc.xyz.example.com.au | TLD(Y): example.com.au | CompanyName(Z): example | Left With Word(Z): abc.xyz | RS2: abc-xyz
URL(X): https://abc-xyz-1ox-example.com.br | TLD(Y): example.com.br | CompanyName(Z): example | Left With Word(Z): abc-xyz-1ox | RS2: abc-xyz-1ox
URL(X): https://app.example.com | TLD(Y): example.com | CompanyName(Z): example | Left With Word(Z): app | RS2: app
URL(X): https://dev-history-app.example.in | TLD(Y): example.in | CompanyName(Z): example | Left With Word(Z): dev-history-app | RS2: dev-history-app

Result 2 by concating TLD(Y) to our Left With Word(Z) | This Result 2 is just for saving, we wil not perform any combinations on the Result 2.
URL(X): https://abc.xyz.example.com.au | TLD(Y): example.com.au | CompanyName(Z): example | Left With Word(Z): abc.xyz | RS2: abc-xyz-example-com-au
URL(X): https://abc-xyz-1ox-example.com.br | TLD(Y): example.com.br | CompanyName(Z): example | Left With Word(Z): abc-xyz-1ox | RS2: abc-xyz-1ox-example-com-br
URL(X): https://app.example.com | TLD(Y): example.com | CompanyName(Z): example | Left With Word(Z): app | RS2: app-example-com
URL(X): https://dev-history-app.example.in | TLD(Y): example.in | CompanyName(Z): example | Left With Word(Z): dev-history-app | RS2: dev-history-app-example-in

Result 3 by concating CompanyName(Z) to our Left With Word(Z) | This Result 3 is just for saving, we wil not perform any combinations on the Result 3.
URL(X): https://abc.xyz.example.com.au | TLD(Y): example.com.au | CompanyName(Z): example | Left With Word(Z): abc.xyz | RS2: abc-xyz-example
URL(X): https://abc-xyz-1ox-example.com.br | TLD(Y): example.com.br | CompanyName(Z): example | Left With Word(Z): abc-xyz-1ox | RS2: abc-xyz-1ox-example
URL(X): https://app.example.com | TLD(Y): example.com | CompanyName(Z): example | Left With Word(Z): app | RS2: app-example-com
URL(X): https://dev-history-app.example.in | TLD(Y): example.in | CompanyName(Z): example | Left With Word(Z): dev-history-app | RS2: dev-history-app-example

9. Now, take just the Result 1 of RS1 and RS2 from step 8. We know that in RS1 we took dot (.) mechanism and in RS2 we took hyphen (-) mechanism. In this step we will form combinations on RS1 and RS2 and this combination list will be our basic foundation of our result wordlist. Steps to form combinations for both RS1 and RS2:

Note: For this we will take "dev.app" as example Result 1 of RS1:
a) If there is single word in RS1 or RS2 then keep it as it is. Like if the RS1 or RS2 is "dev" then the result is just "dev".
b) If there 2 words in RS1 or RS2 then:
    1. Just take the first word that is divided by hyphen (-) or dot (.) and keep it as it is. Example Result (for RS1 as dev.app): dev | Example Result (for RS2 as dev-app): dev
    2. Keep them as it is. Example Result (for RS1 as dev.app): dev.app | Example Result (for RS1 as dev-app): dev-app

c) If there are more than 2 words in RS1 or RS2 then we can make combinations but it should be made intelligently. How? For this we will take "dev-history-app" as example result RS2:
    1. Just take the first word that is divided by hyphen (-) or dot (.) and keep it as it is. Example Result (for RS1 as dev.app.anything.me.xyz): dev | Example Result (for RS2 as dev-app-anything-me-xyz): dev
    2. Take the first 2 words from RS1 or RS2 and keep them as it is. Example Result (for RS1 as dev.app.anything.me.xyz): dev.app | Example Result (for RS2 as dev-app-anything-me-xyz): dev-app
    3. Take the first 3 words from RS1 or RS2 and keep them as it is. Example Result (for RS1 as dev.app.anything.me.xyz): dev.app.anything | Example Result (for RS2 as dev-app-anything-me-xyz): dev-app-anything 
    3. Only If there are 4 or more words available in RS1 or RS2 then: Take the first 4 words from RS1 or RS2 and keep them as it is. Example Result (for RS1 as dev.app.anything.me.xyz): dev.app.anything.me | Example Result (for RS2 as dev-app-anything-me-xyz): dev-app-anything-me
    4. Take the whole RS1 and RS2 as they are. Example Result (for RS1 as dev.app.anything.me.xyz): dev.app.anything.me.xyz | Example Result (for RS2 as dev-app-anything-me-xyz): dev-app-anything-me-xyz
    5. Take the last word from RS1 or RS2 and keep it as it is. Example Result (for RS1 as dev.app.anything.me.xyz): xyz | Example Result (for RS2 as dev-app-anything-me-xyz): xyz

Note: By "Take the first/last/anything word" I am saying save the list that we are forming somewhere.

10. In this step we have to print the result on our CLI. But for better understanding let's take examples:
A) Suppose if our initial URL was https://dev-history-app.example.in then our overall result should be:
    Step 8 Result a) [Contains Result 1, Result 2, Result 3]: dev.history.app , dev.history.app.example.in , dev.history.app.example
    Step 8 Result b) [Contains Result 1, Result 2, Result 3]: dev-history-app , dev-history-app-example-in , dev-history-app-example
    Step 9 Result: dev , dev-history , dev-history-app ,  dev.history , dev.history.app , app

B) Suppose if our initial URL was https://dev.app.anything.me.xyz.example.com.au then our overall result should be:
    Step 8 Result a) [Contains Result 1, Result 2, Result 3]: dev.app.anything.me.xyz , dev.app.anything.me.xyz.example.com.au , dev.app.anything.me.xyz.example
    Step 8 Result b) [Contains Result 1, Result 2, Result 3]: dev-app-anything-me-xyz , dev-app-anything-me-xyz-example-com-au , dev-app-anything-me-xyz-example
    Step 9 Result: dev , dev-app , dev-app-anything , dev-app-anything-me , dev-app-anything-me-xyz , dev.app , dev.app.anything , dev.app.anything.me , dev.app.anything.me.xyz , app


So our Overall Results that will be print on the CLI will look like this:
A) Suppose if our initial URL was https://dev-history-app.example.in then our overall result that will be print on the cli should be:
dev.history.app
dev.history.app.example.in
dev.history.app.example
dev-history-app
dev-history-app-example-in
dev-history-app-example
dev
dev-history
dev-history-app
dev.history
dev.history.app
app

Note: I know there will be duplicates but that doesn't matter, we have to follow our process and according to that duplicates can occur.

B) Suppose if our initial URL was https://dev.app.anything.me.xyz.example.com.au then our overall result that will be print on the cli should be:
dev.app.anything.me.xyz
dev.app.anything.me.xyz.example.com.au
dev.app.anything.me.xyz.example
dev-app-anything-me-xyz
dev-app-anything-me-xyz-example-com-au
dev-app-anything-me-xyz-example
dev
dev-app
dev-app-anything
dev-app-anything-me
dev-app-anything-me-xyz
dev.app
dev.app.anything
dev.app.anything.me
dev.app.anything.me.xyz
xyz

So that was the whole process just for a single URL that we processed in step 2.
Now as a Python Programmer first understand the whole process thouroughly then make this full working script for me.
```

Prompt 2
```
Modify this script to:
1. Take extensions file in txt as cli like: python3 script.py /path/to/urls.txt /path/to/extensions.txt


And the extensions file data looks like
.zip
.PHP
.bz2
.cache
.jsp~
and more...

2. Concat all of them one by one in print("\n".join(results)) so that a single "results" there will be multiple one depending on overall extensions.
```

Prompt 3
```
Now the thing is, this script works great. But I want to add a feature that the user can use to also add the full hostname of the generated wordlist of that particular URL.

Like, generally if I use this script and the URL was https://dev.app.anything.me.xyz.example.com.au then the generated wordlist with extensions.txt file that contains single extension .OLD the result will be:

dev-app-anything-me-xyz-example-com-au.OLD
dev-app-anything-me-xyz-example.OLD
dev-app-anything-me-xyz.OLD
dev-app-anything-me.OLD
dev-app-anything.OLD
dev-app.OLD
dev.OLD
dev.app.OLD
dev.app.anything.OLD
dev.app.anything.me.OLD
dev.app.anything.me.xyz.OLD
dev.app.anything.me.xyz.example.OLD
dev.app.anything.me.xyz.example.com.au.OLD
example.OLD
xyz.OLD

But I want that if the user specifies the flag --full then it should also print the full hostname with http/https protocol like this:

https://dev.app.anything.me.xyz.example.com.au/dev-app-anything-me-xyz-example-com-au.OLD
https://dev.app.anything.me.xyz.example.com.au/dev-app-anything-me-xyz-example.OLD
https://dev.app.anything.me.xyz.example.com.au/dev-app-anything-me-xyz.OLD
https://dev.app.anything.me.xyz.example.com.au/dev-app-anything-me.OLD
https://dev.app.anything.me.xyz.example.com.au/dev-app-anything.OLD
https://dev.app.anything.me.xyz.example.com.au/dev-app.OLD
https://dev.app.anything.me.xyz.example.com.au/dev.OLD
https://dev.app.anything.me.xyz.example.com.au/dev.app.OLD
https://dev.app.anything.me.xyz.example.com.au/dev.app.anything.OLD
https://dev.app.anything.me.xyz.example.com.au/dev.app.anything.me.OLD
https://dev.app.anything.me.xyz.example.com.au/dev.app.anything.me.xyz.OLD
https://dev.app.anything.me.xyz.example.com.au/dev.app.anything.me.xyz.example.OLD
https://dev.app.anything.me.xyz.example.com.au/dev.app.anything.me.xyz.example.com.au.OLD
https://dev.app.anything.me.xyz.example.com.au/example.OLD
https://dev.app.anything.me.xyz.example.com.au/xyz.OLD
```
   
# License
Backup Files Wordlist Generator (backup-gen) is released under the [MIT License](LICENSE).
