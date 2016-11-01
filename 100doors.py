import math
doors = []
for i in range(1, 101):
    if math.sqrt(i) % 1:
        stan='c'
    else:
        stan='o'
        doors.append(i)
print("The following doors are open:", doors)
