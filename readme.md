# Moodle API Tools

Example scripts for accessing different portions of the Moodle REST APIs. The Moodle APIs are comprehensive but tricky to use. These scripts are illustrative and not intended for production use, though similar code is running in other CCA apps. To run them, obtain a [Web Services token](https://moodle.cca.edu/admin/webservice/tokens.php) for a Service with the appropriate API permissions, then save that token in a config.py file (see example.config.py for details) in the root of this project.

## get_mdl_categories

This script was an example provided to the Integration Engineer so that a Moodle course database could be built which includes structured enrollment data with knowledge of Moodle course category IDs. This makes it so courses are added under the appropriate categories when they appear in the database. It takes a "filter" dict of category properties (e.g. `{"name": "2021SU"}`) and returns an array of all categories that match the filter and their children.

## get_mdl_course

This script was an example provided to the Portal team during Learning Hub development so that links to Moodle course sites could be established. The Portal has moved away from having direct access to the Moodle database but Moodle course links require knowledge of Moodle's internal IDs; this script returns course information, including ID, when given a "shortname" of form `ANIMA-1000-1-2021FA`.

## get_mdl_courses

Returns _all_ the Moodle courses using the `core_course_get_courses` wsfunction. This is currently (as of August 2020) the method that the Portal uses to pull Moodle data, which it matches to its course data. So we need to ensure this function works with whatever web services user/token Portal uses.

## enrol_get_enrolled_users

Given a course ID, returns a list of users enrolled in that course using the `core_enrol_get_enrolled_users` function.
