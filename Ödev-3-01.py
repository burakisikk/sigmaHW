f = open("data", "w")

f.write("Name: Burak\nSurname: Isık\nGender: Male\nUsername: burakisikk\nJob: Engineer")
f.close()

f = open("data", "r")

lines = f.read().split("\n")

dictionary = {}
for line in lines:
    key, value = line.split(": ")
    dictionary[key] = value

print(dictionary)