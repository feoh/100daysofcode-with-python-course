import requests
import argparse

def download_feed(feed_file, feed_url):
    resp = requests.get(feed_url)

    with open(feed_file,'wb') as feed:
        feed.write(resp.content)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--feed-file', help='RSS feed filename')
    parser.add_argument('-u', '--feed-url', help='RSS feed URL')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    download_feed(args.feed_file, args.feed_url)
