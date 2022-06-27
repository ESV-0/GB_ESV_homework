# Домашнеее задание, урок-5, задание-4

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

result = []

for i in range(len(src)):
   flag = 1
   for j in range(len(src)):
      if src[i] == src[j] and i != j:
         flag = 0
         break
   if flag:
       result.append(src[i])

print(result)

