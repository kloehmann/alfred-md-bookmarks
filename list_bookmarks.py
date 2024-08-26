#!/usr/bin/env python3
import json
import re
import os

BOOKMARKS_FILE = os.getenv("bookmarksfile")
LINK_PATTERN = re.compile(".*\\[(.*)\\]\\((.*)\\)")
# We ignore heading level 1
HEADING_PATTERN = re.compile("\\#(\\#+) (.*)")


if __name__ == "__main__":
    json_data = {"items": []}
    bookmarksfile = open(BOOKMARKS_FILE, "r")
    previous_headings = []

    for line in bookmarksfile:
        link = LINK_PATTERN.match(line)
        heading = HEADING_PATTERN.match(line)
        if link:
            path = "/".join(previous_headings)
            json_data["items"].append({
                        "title": "%s/%s" % (path, link.group(1)),
                        "arg": link.group(2)
                        })
        elif heading:
            current_heading_level = len(heading.group(1))-1
            if current_heading_level <= len(previous_headings):
                while current_heading_level < len(previous_headings):
                    previous_headings.pop()
            previous_headings.append(heading.group(2))
    print(json.dumps(json_data))
