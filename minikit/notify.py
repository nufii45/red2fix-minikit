import requests

from minikit.duration import parse_duration


def notify_timeout(url, text):
    """Post a job's timeout, in seconds, to the deploy webhook at url."""
    response = requests.post(url, json={"timeout_seconds": parse_duration(text)}, timeout=10)
    response.raise_for_status()
    return response
