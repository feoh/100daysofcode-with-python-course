import feedparser
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--feed-file', help='Filename of RSS feed to parse')
    return parser.parse_args()


def parse_rss(feed_file):
    return feedparser.parse(feed_file)


def parse_tags(taglist):
    return [tag['term'] for tag in taglist]


if __name__ == "__main__":
    args = parse_args()
    feed = parse_rss(args.feed_file)

    for entry in feed['entries']:
        print(f"Title: {entry.title}")
        taglist = entry.tags
        tags = parse_tags(taglist)
        print(f"Tags: {tags}")
