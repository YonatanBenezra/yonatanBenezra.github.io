import os
import json
import frontmatter
from datetime import datetime

POST_DIR = "./posts/"
POST_JSON_DIR = POST_DIR + "json/"

dict = {}

if not os.path.exists(POST_JSON_DIR):
    os.makedirs(POST_JSON_DIR)

for file in os.listdir(POST_DIR):
    if file.endswith(".md"):
        post = frontmatter.load(POST_DIR + file)
        metadata = post.metadata
        date_published = metadata["published"].strftime("%b %d, %Y")
        timestamp = datetime.timestamp(metadata["published"])
        obj = {
            **metadata,
            "published": date_published,
            "timestamp": int(timestamp),
            "location": file + ".json",
        }
        content = post.content

        with open(POST_JSON_DIR + file + ".json", "w") as file_descriptor:
            json.dump({**obj, "content": content}, file_descriptor)

        dict = {**dict, file: obj}

with open(POST_JSON_DIR + "index.json", "w") as file_descriptor:
    json.dump(dict, file_descriptor)
