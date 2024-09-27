"""Get users enrolled in a Moodle course.

Usage:
    enrol_get_enrolled_users.py <courseid>

Options:
  <courseid>    numberic ID of the course in Moodle
  -h --help     Show this screen.
  --version     Show version.
"""

import json
import sys

from docopt import docopt
import requests

import config

# usage: python core_enrol_get_enrolled_users.py 3606
# 3606 is Eric's staging test course
# https://moodle.cca.edu/webservice/rest/server.php?wstoken=...&wsfunction=core_enrol_get_enrolled_users&moodlewsrestformat=json&courseid=...


def get_enrolled_users(courseid):
    """print enrolled users in a course"""
    url = config.url
    params = {
        "courseid": courseid,
        "moodlewsrestformat": "json",
        "wsfunction": "core_enrol_get_enrolled_users",
        # found at https://moodle.cca.edu/admin/settings.php?section=webservicetokens
        "wstoken": config.token,
    }

    response = requests.get(url, params=params)
    data = response.json()

    # pretty print full data
    return data


if __name__ == "__main__":
    args = docopt(__doc__, version="enrol_get_enrolled_users 1.0")
    print(json.dumps(get_enrolled_users(args["<courseid>"]), indent=4, sort_keys=True))
