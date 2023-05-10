# wayurls 🔗
It's 2023, I came to the realization that I'm still manually browsing to https://archive.org/web/ typing and clicking through several pages x) so i wrote this tool in few minutes.

# Features
- filter by extension
- filter by directory
# Installation 🤓
```sh
git clone https://github.com/Ryukudz/wayurls.git
cd wayurls
pip install -r requirements.txt
```
# Usage 🪄
```sh
python3 wayurls.py -h
```
This will display help for the tool, Here are all the switches it supports.
```yaml
usage: wayurls.py [-h] -u URL [-o OUTPUT] [-f {js,param,txt,json}] [-d DIRECTORY]

extracts URLs from the Wayback Machine 📚

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     target URL e.g https://example.com
  -o OUTPUT, --output OUTPUT
                        Output results to a file
  -f {js,param,txt,json}, --filter {js,param,txt,json}
                        Filter the output by file extension e.g js
  -d DIRECTORY, --directory DIRECTORY
                        Filter the output by directory e.g admin
```
