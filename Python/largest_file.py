import os

print("Enter full pathname to find the largest file: ", end=' ')
path = input()
highest = 0
filename = 0
totalsize = 0


for filename in os.listdir(path):
    totalsize = totalsize + os.path.getsize(os.path.join(path, filename))

    if totalsize > highest:
        highest = os.path.getsize(os.path.join(path, filename))


highest_name = os.path.relpath(filename)
print("Largest file: " + os.path.relpath(highest_name))
print(str(highest / 8) + ' B.')
print(str(highest / 8 / 1000) + ' KB.')
print(str(highest / 8 / 1000 / 1000) + ' MB.')
print(str(highest / 8 / 1000 / 1000 / 1000) + ' GB.')
