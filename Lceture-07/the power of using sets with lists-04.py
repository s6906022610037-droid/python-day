# Attendance record of a week (each lissst represents a day)
attendance_week = [
    ['Alice', 'Bob', 'Charlie','David'],  # day1
    ['Alice', 'Charlie', 'David'],  # day2
    ['Alice','Bob', 'David'],  # day3
     ['Alice', 'David','Eve'],  # day4
    [ 'Bob', 'Charlie','David']  # day5
]

attendeance_set = [set(day) for day in attendance_week]
print(attendeance_set) 

persent_every_day = set.intersection(*attendeance_set)
print("persent_every_day:", persent_every_day)

all_students = set.union(*attendeance_set)
absent_at_least_one_dey = all_students - persent_every_day
print("absent_at_least_one_dey:", absent_at_least_one_dey)

first_day_present = attendeance_set[0]
last_day_present = attendeance_set[-1]
firt_day_but_not_last = list(first_day_present - last_day_present)
print("firt_day_but_not_last:", firt_day_but_not_last)

unique_student_count = len(all_students)
print(" Total unique student:", unique_student_count)

