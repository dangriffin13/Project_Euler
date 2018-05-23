n = int(input())

names = []
for i in range(n):
    names.append(input())
    
names.sort()

q = int(input())

for j in range(q):
    name = input()
    location = names.index(name) + 1
    letter_score = sum([ord(char) - 96 for char in name.lower()])
    print(location*letter_score)