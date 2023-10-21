# Corporate-App

IoT application in progress.

### Current Status

This does not represent a finished product and is meant to act as a test application to practice integrating scalable data storage/access features. Currently the program:
- demonstrates a basic GUI using python kivy framework
- connects to a local sql server
- handles user signups/logins sucessfully with some consideration made to prevent sql injections
- all passwords are encrypted in the local sql data base and hashed on gui screen
- When a signup is successful (ie username didnt exist already in database) JSON file is created with user details and stored in cloudant database for user. No passwords are saved on cloud.
- ibm cloud services used: IBM cloudant, db2, IBM cloud.
- Usage: IBM cloud used uniquely for image storage, IBM cloudnat used for JSON files in pertitioned document format
- images displyed on app are downloaded first from cloud if they do not already exist locally when login is successful. They are used as button backgrounds
- JSON file is updated when user training for specific part is complete so that competencies are recorded and saved permanently.
