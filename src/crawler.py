#!/usr/bin/python3


# pip install --user requests beautifulsoup4
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import sys


def crawl(url, maxDepth, depth, visited):
    """
    Given an absolute URL, print each hyperlink found within the document.

    Your task is to make this into a recursive function that follows hyperlinks
    until one of two base cases are reached:

    0) No new, unvisited links are found
    1) The maximum depth of recursion is reached

    You will need to change this function's signature to fulfill this
    assignment.
    """

    if depth >= maxDepth:
        return
    try:
        response = requests.get(url)
        if not response.ok:
            print(f"crawl({url}): {response.status_code} {response.reason}")
            return

        html = BeautifulSoup(response.text, 'html.parser')
        links = html.find_all('a')
        for a in links:
            link = a.get('href')
            if link:
                # Create an absolute address from a (possibly) relative URL
                absoluteURL = urljoin(url, link)
                
                # Only deal with resources accessible over HTTP or HTTPS
                if absoluteURL.startswith('http'):
                    url = absoluteURL.split('#')[0]
                    if url not in visited:
                        visited.add(url)
                        for i in range(depth + 1):
                            print("    ", end='')
                        print(url)
                        crawl(url, maxDepth, depth + 1, visited)

    except Exception as e:
        print(f"crawl(): {e}")
    return


## An absolute URL is required to begin
if len(sys.argv) < 2:
    print("Error: no Absolute URL supplied")
    sys.exit(1)
else:
    url = sys.argv[1]

parsed = urlparse(url)
if parsed.scheme == '' or parsed.netloc == '':
    print("Error: Invalid URL supplied\nPlease supply an absolute URL to this program")
    sys.exit(1)

maxDepth = 3
if len(sys.argv) > 2:
    if sys.argv[2].isnumeric() and int(sys.argv[2]) >= 0:
        maxDepth = int(sys.argv[2])
    else:
        print("Error: Invalid crawl depth\nPlease enter a positive integer.")
        sys.exit(1)

plural = 's'
if maxDepth == 1:
    plural = ''


depth = 0
print(f"Crawling from {url} to a maximum depth of {maxDepth} link{plural}")
print(url)
visited = {url}
crawl(url, maxDepth, depth, visited)

