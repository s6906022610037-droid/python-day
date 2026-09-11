# 1. กำหนดข้อมูลคะแนนสอบ (List of scores)
scores = [85, 92, 78, 90, 65]

# 2. คำนวณหาค่าเฉลี่ย
total_sum = sum(scores)
count = len(scores)
average = total_sum / count

# 3. แสดงผลลัพธ์
print(f"คะแนนทั้งหมด: {scores}")
print(f"ผลรวมของคะแนน (sum): {total_sum}")
print(f"จำนวนนักเรียนทั้งหมด (len): {count}")
print(f"ค่าเฉลี่ยที่ได้ (average): {average}")


