from itertools import count


answer = 0
count = 1

while count <= 100:
  answer += count
  count += 1

print(answer)