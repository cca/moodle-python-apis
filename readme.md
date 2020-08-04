# Moodle API Tools

These are example scripts for accessing different portions of the Moodle REST APIs. The Moodle APIs are very comprehensive but sometimes a bit tricky to use. These scripts are both examples and not intended for production use, though similar code is running in other CCA apps. The easiest way to run them is to obtain a Web Services token at https://moodle.cca.edu/admin/settings.php?section=webservicetokens for a Service with the appropriate API permissions, then save that token in a config.py file (see example.config.py for details) in the root of this project.

**get_mdl_course_id**

This script was an example provided to the Portal team during Learning Hub development so that links to Moodle course sites could be established. The Portal has moved away from having direct access to the Moodle database but Moodle course links require knowledge of Moodle's internal IDs; this script returns those IDs when given a course "shortname" of form `ANIMA-1000-1-2019FA`.

**get_mdl_categories**

This script was an example provided to the Integration Engineer so that a Moodle course database could be built which includes structured enrollment data with knowledge of Moodle course category IDs. This makes it so courses are added under the appropriate categories when they appear in the database. It takes a "filter" dict of course properties (e.g. `{"name": "2019SU"}`) and returns an array of all categories that match and their children.

**get_mdl_courses**

Get all the Moodle courses using the `core_course_get_courses` wsfunction. This is currently (as of August 2020) the method that the Portal uses to pull Moodle data, which it matches to its course data. So we need to make sure this function works with whatever web services user/token that Portal is going to use.
