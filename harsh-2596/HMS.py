# """
# -> 3 clients, 6 files ,one for diet and other for exercise.
# -> client name Harry, Rohan, Marsh
# -> create a function which takes client name as input, then ask for diet log or exercise log.
# ->
#
# """

def hlmng():
    n = input("Enter Whose Log You Wanna See (Harry, Rohan, or Marsh): ")
    if n == "harry":
        print("For Diet Log Enter 'hd'\n"
              "For Workout Log Enter 'he'")
    elif n == "rohan":
        print("For Diet Log Enter 'rd'\n"
              "For Workout Log Enter 're'")
    elif n == "marsh":
        print("For Diet Log Enter 'md'\n"
              "For Workout Log Enter 'me'")
    else:
        print("Invalid Input")
    k = input("Which Log You Wanna See: ")
    if k == "hd":
        hd = open("harryd.txt", "r+")
        a = hd.read()
        print(a)
    elif k == "rd":
        rd = open("rohand.txt", "r+")
        b = rd.read()
        print(b)
    elif k == "md":
        md = open("marshd.txt", "r+")
        c = md.read()
        print(c)
    elif k == "he":
        he = open("harrye.txt", "r+")
        d = he.read()
        print(d)
    elif k == "re":
        re = open("rohane.txt", "r+")
        e = re.read()
        print(e)
    elif k == "me":
        me = open("marshe.txt", "r+")
        f = me.read()
        print(f)
    else:
        print("Invalid Input")
hlmng()
