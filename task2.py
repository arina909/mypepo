s1 = [input()]
s2 = [input()]
i = ["dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
   "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"]
b = i[0].split('-')
c = []
for n in range(1, len(i)):
    k=i[n].split('-')
    if k[0] in b or k[1] in b:
        b+=k
    else:
        c+=k
# create certain list for certain group
if set(s1).issubset(b) and set(s2).issubset(b) or set(s1).issubset(c) and set(s2).issubset(c):
    print('True')
else:
    print('False')