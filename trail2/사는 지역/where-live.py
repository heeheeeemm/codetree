class Information:
    def __init__(self, iname, iaddress, iregion):
        self.iname = iname
        self.iaddress = iaddress
        self.iregion = iregion


n = int(input())

people = []

for _ in range(n):
    name, address, region = input().split()
    people.append(Information(name, address, region))


people.sort(key=lambda x: x.iname)

answer = people[-1]

print("name", answer.iname)
print("addr", answer.iaddress)
print("city", answer.iregion)