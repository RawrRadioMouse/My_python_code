a = []

while True:

    if not a:
        print("empty")
        a.append("now not empty")
        print(a)
        break
a.clear()
while True:

    if len(a)==0:
        print("empty again!")
        a.append("now not empty(again...)")
        print(a)
