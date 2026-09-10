# Attendance record of a week (each lissst represents a day)
attendance_week = [
    ['alice', 'Bob', 'Charlie',"david"],  # dey1
    ['alice', 'charlie', 'david'],  # day2
    ['alice','Bob', 'Charlie'],  # day3
     ['alice', 'charlie','eve'],  # day4
    [ 'Bob', 'Charlie','David']  # day5
]

attendeance_set = [set(day) for day in attendance_week]
print(attendeance_set) 

persent_every_day = set.intersection(*attendeance_set)
print("persent_every_day:", persent_every_day)

all_students = set.union(*attendeance_set)
absent_at_least_one_dey = all_students - persent_every_day
print("absent_at_least_one_dey:", absent_at_least_one_dey)
