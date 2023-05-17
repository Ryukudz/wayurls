import argparse
import requests
import json
from urllib.parse import urlparse, unquote
from rich import print

print('''[red]\t     _        _/ _
\t|/|//_|/_//_///_\ 
\t       _/         
\t [white]coded by [cyan] ryuku 🥷
''')

def decode_urls(urls):
    decoded_urls = []
    for url in urls:
        decoded_url = unquote(url)
        decoded_urls.append(decoded_url)
    return decoded_urls

def main():
    parser = argparse.ArgumentParser(description='extracts URLs from the Wayback Machine 📚')
    parser.add_argument('-u', '--url', type=str, required=True, help='target URL e.g https://example.com')
    parser.add_argument('-o', '--output', type=str, help='Output results to a file')
    parser.add_argument('-f', '--filter', type=str, choices=['js', 'param', 'txt', 'json'], help='Filter the output by file extension e.g js')
    parser.add_argument('-d', '--directory', type=str, help='Filter the output by directory e.g admin')
    parser.add_argument('--decode', action='store_true', help='URL decode the output.')
    args = parser.parse_args()

    if not args.url.startswith(('http://', 'https://')):
        print('[red] ⚠️  Invalid URL')
        exit()

    target = f'https://web.archive.org/web/timemap/json?url={args.url}&matchType=prefix&collapse=urlkey&output=json&fl=original'
    response = requests.get(target)

    if response.status_code != 200:
        print('[red] ⚠️  Something went wrong.')
        exit()

    data = json.loads(response.text)
    urls = [line[0].split()[0] for line in data if line[0].startswith('http')]

    if args.filter:
        if args.filter == 'js':
            urls = [url for url in urls if url.endswith('.js')]
        elif args.filter == 'param':
            urls = [url for url in urls if '?' in url]
        elif args.filter == 'txt':
            urls = [url for url in urls if url.endswith('.txt')]
        elif args.filter == 'json':
            urls = [url for url in urls if url.endswith('.json')]

    if args.directory:
        directory = args.directory.strip('/')
        urls = [url for url in urls if urlparse(url).path.strip('/').endswith(directory)]

    if args.decode:
        urls = decode_urls(urls)

    if args.output:
        with open(args.output, 'w') as f:
            f.write('\n'.join(urls))
    else:
        for i, url in enumerate(urls, 1):
            print(f'[green]{i}:[white] {url}')

    print(f'{len(urls)} 🔗 URLs found.')


if __name__ == '__main__':
    main()
