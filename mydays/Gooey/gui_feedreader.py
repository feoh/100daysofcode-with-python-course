import feedparser
import argparse
from gooey import Gooey, GooeyParser

@Gooey
def parse_args():
    parser = GooeyParser(description="RSS Feed Parser!")
    parser.add_argument('feed_file', widget="FileChooser")
    return parser.parse_args()


def parse_rss(feed_file):
    return feedparser.parse(feed_file)


def parse_tags(taglist):
    return [tag['term'] for tag in taglist]


def main():
    args = parse_args()
    feed = parse_rss(args.feed_file)

    for entry in feed['entries']:
        print(f"Title: {entry.title}")
        taglist = entry.tags
        tags = parse_tags(taglist)
        print(f"Tags: {tags}")


if __name__ == "__main__":
    main()
