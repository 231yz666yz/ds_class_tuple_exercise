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
course_code = input("Enter your course code: ")
course_name = input("Enter your course name: ")
course_credits = int(input("Enter your course credits: "))
course_semester = input("Enter your course semester: ")
course = (course_code, course_name, course_credits, course_semester)

# Accept course schedule information like the day, start time, end time, and room. Store them in a tuple called schedule.
day = input("Enter the day: ")
start_time = input("Enter the start time: ")
end_time = input("Enter the end time: ")
room = input("Enter the room: ")
schedule = (day, start_time, end_time, room)

# Add the schedule tuple to the course tuple to create a nested tuple.
nested = course + schedule

# Make sure the schedule is complete. Meaning, it doesn't have any empty values.
if '' in schedule:
    schedule_check = "NO"
    print("The schedule is not completed")
else:
    schedule_check = "YES"

# Check if the day is valid. Meaning, it should be one of the valid days defined above.
if day not in valid_days:
    day_check = "NO"
    print("The day is invalid")
else:
    day_check = "YES"

# Print the course information to look like the following:
print(f"""====================================
COURSE INFORMATION
====================================

Course: {course_name}
Credits: {course_credits}
Semester: {course_semester}

------------- SCHEDULE -------------
Day: {day}
Time: {start_time} - {end_time}
Room: {room}

Schedule Complete: {schedule_check}
Class Day Valid: {day_check}

==================================== 
""")

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
