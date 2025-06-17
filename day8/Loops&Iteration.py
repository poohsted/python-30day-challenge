# for loop

for i in range(5):
    print(f"Counting: {i}")

# while loop

count = 0
while count < 5:
    print(f"Looping: {count}")
    count += 1

# break and continue

for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)

# else with loop

for i in range(3):
    print(i)
else:
    print("Loop ended normally!")
