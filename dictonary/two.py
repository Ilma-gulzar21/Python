
info = [
    ("alice,math"),
    ("Bob,Science"),
    ("alice,Science"),
    ("charlie,math"),
    ("Bob,math"),
    ("Alice,english"),
    ("charlie,english"),
]
dict={}

for item in info:
    name, subject=item.split(",")
    if dict.get(name)==None:
        dict.update({name:set()})     
        dict[name].add(subject)
    else:
         dict[name].add(subject)
print(dict)

