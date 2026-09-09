## Create a simple university course registration / timetable system using tuple
## We use tuple here because the information should not change, or change after a very long time. 
# Tuple is immutable, and so it is a good choice for this kind of data structure.


# Following are the valid teaching days on which a course can be held. 
valid_days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
)


# Write logic to first accept course code from the user, then course name, credits, and semester. 
# Store them in a tuple called course.





# Accept course schedule information like the day, start time, end time, and room. Store them in a tuple called schedule.




# Add the schedule tuple to the course tuple to create a nested tuple.




# Make sure the schedule is complete. Meaning, it doesn't have any empty values.


# Check if the day is valid. Meaning, it should be one of the valid days defined above.


# Print the course information to look like the following:


""" 
====================================
       COURSE INFORMATION
====================================

Course: CS205 - Software Engineering
Credits: 5
Semester: Autumn 2026

------------- SCHEDULE -------------
Day: Monday
Time: 10:00 - 12:00
Room: B204

Schedule Complete: YES
Class Day Valid: YES

==================================== """
