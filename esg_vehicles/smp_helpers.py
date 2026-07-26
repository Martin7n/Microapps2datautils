
# data = {}
#
# while True:
#
#     z = str(input())
#     if z == 'q':
#         break
#     x = z.split("zz")
#     dd = x[0].replace("\t", "")
#     if dd not in data:
#         data[dd] = x[1].replace("\t", "")
#
#
# print(data)

dtt = []
while True:
    z = str(input()).lower().strip()
    f = z.split(" ")
    if z=='q':
        break
    dtt += f

print(set(dtt))