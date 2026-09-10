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