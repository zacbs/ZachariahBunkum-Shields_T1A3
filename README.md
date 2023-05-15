# T1A3 Terminal app
Third assessment for term 1

Table of Coentents:

- [R4: Source control repository](#r4-source-control-repository)
- [R5: Style guide](#r5-style-guide)
- [R6: Project features](#r6-project-features)
- [R7: Project managment](#r7-project-management)
- [R8: How to use the application](#r8-how-to-use-the-application)
- [Presentation](#presentation)



## R4: Source control repository
[Link to the project](https://github.com/zacbs/ZachariahBunkum-Shields_T1A3)
## R5: Style guide
When building this project I will attempt to follow the [PEP8](https://peps.python.org/pep-0008/) style guide. I will acheive this by using the [autopep8](https://pypi.org/project/autopep8/) package.
## R6: Project features
Features of the project:
1. Be able to set an alarm for a certain time
2. Save alarms that are set, to allow user to quickly set alarms in the future
3. Allow the user to set alarms to reoccur
4. Allow user to set a sound to play when the alarm sounds or pick their own sound
## R7: Project management
[Link to trello board](https://trello.com/invite/b/zl1x8zTX/ATTI3c74f83553dd8ff3e5dd1870716d6ed3A9496EF0/application)

### Feature 1: Set Alarm
Task 1: Get current time

Task 2: Take user input and save it to a file

Task 3: When alarm time is equal to current time send an alert to the terminal

Task 4: When alarm sends alert to terminal change alarm on to false in the save file

Task 5: Show current active alarms vs current time

### Feature 2: Manage saved alarms
Task 1: Create a save file and ensure it is setup correctly

Task 2: Ability to toggle alarms on and off

Task 3: Display a list of alarms to the user

Task 4: Ability to delete an alarm

Task 5: Integrate saved alarm feature with setting alarms feature

### Feature 3: Reoccuring alarms

Task 1: Allow user to toggle alarm reoccuring

Task 2: Alarms that have a reoccuring flag dont turn off after triggering

Task 3: Buid menu for alarm reoccuring

Task 4: 

Task 5: 

### Feature 4: Sound

Task 1: Play sound when alarm is triggered

Task 2: Allow user to edit which sound plays


## R8: How to use the application

Download the application and run the run.sh script. 

Python is required to run the program and the dependencies are available in the requirements.txt file

If you get a permission error run chmod +x run.sh before running the script

### Program use
After running the script the program will run and can be used, follow the instructions laid out within the program. Any times entered will need to be entered as 00-23:00-59
### Hardware requirements
The program will need a sound device to play sound to or the alarm will only print a statement and warning that the program has no sound device available.

# Presentation
[Link](https://www.youtube.com/watch?v=9i9z8m2RWgI)