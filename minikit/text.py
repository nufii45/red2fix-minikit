import re


def slugify(text):
    """Turn a title into a URL slug: 'Hello World!' -> 'hello-world'."""
    text = re.sub(r"[^\x00-\x7f]", "", text)  # drop accents
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")
