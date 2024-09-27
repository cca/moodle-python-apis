import json
import sys

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
    print(json.dumps(get_enrolled_users(sys.argv[1]), indent=4, sort_keys=True))
