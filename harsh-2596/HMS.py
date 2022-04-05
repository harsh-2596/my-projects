# """
# -> 3 clients, 6 files ,one for diet and other for exercise.
# -> client name Harry, Rohan, Marsh
# -> create a function which takes client name as input, then ask for diet log or exercise log.
# ->
#
# """
#
#
# def getdate():
#     import datetime
#     return datetime.datetime.now()
#
#
#
#
#
# # Diet log OF Harry
# hd = open("harryd.txt", "w")
# hd.write("DATE AND TIME                             DIET\n")
# hd.write(str(getdate()))
# hd.write("               Sprouts\n")
# hd.write(str(getdate()))
# hd.write("               2 Chapati and Dal\n")
# hd.write(str(getdate()))
# hd.write("               150g Cottage Cheese with Salt\n")
# hd.write(str(getdate()))
# hd.write("               1 Chapati, 1 Bowl Rice, Sauted Veggies\n")
# hd.close()
#
#
# # Diet log of Rohan
# rd = open("rohand.txt", "w")
# rd.write("DATE AND TIME                             DIET\n")
# rd.write(str(getdate()))
# rd.write("               Bread Butter\n")
# rd.write(str(getdate()))
# rd.write("               2 Chapati and Sabzi\n")
# rd.write(str(getdate()))
# rd.write("               Sauted Broccoli\n")
# rd.write(str(getdate()))
# rd.write("               1 Chapati, 1 Bowl Rice, Curd\n")
# rd.close()
#
#
# # Diet log of Marsh
# md = open("marshd.txt", "w")
# md.write("DATE AND TIME                             DIET\n")
# md.write(str(getdate()))
# md.write("               Oats with Milk\n")
# md.write(str(getdate()))
# md.write("               4 Chapati and Potato Sabzi\n")
# md.write(str(getdate()))
# md.write("               1 glass Milk, Bread Butter\n")
# md.write(str(getdate()))
# md.write("               3 Chapati, 1 bowl rice, Soy Bean Chunks  \n")
# md.close()
#
# # Workout log of Marsh
# he = open("harrye.txt", "w")
# he.write("DATE AND TIME                           EXERCISES\n")
# he.write(str(getdate()))
# he.write("               Running\n")
# he.write(str(getdate()))
# he.write("               Cardio\n")
# he.write(str(getdate()))
# he.write("               Crunches\n")
# he.write(str(getdate()))
# he.write("               Leg Raise\n")
# he.write(str(getdate()))
# he.write("               Burpees\n")
# he.close()
#
#
# # Workout log of Marsh
# re = open("rohane.txt", "w")
# re.write("DATE AND TIME                           EXERCISES\n")
# re.write(str(getdate()))
# re.write("               Running\n")
# re.write(str(getdate()))
# re.write("               Cardio\n")
# re.write(str(getdate()))
# re.write("               Crunches\n")
# re.write(str(getdate()))
# re.write("               Leg Raise\n")
# re.write(str(getdate()))
# re.write("               Burpees\n")
# re.write(str(getdate()))
# re.write("               Planks\n")
# re.close()
#
#
# # Workout log of Marsh
# me = open("marshe.txt", "w")
# me.write("DATE AND TIME                           EXERCISES\n")
# me.write(str(getdate()))
# me.write("               Push Ups\n")
# me.write(str(getdate()))
# me.write("               Pull Ups\n")
# me.write(str(getdate()))
# me.write("               Barbell Chest Press\n")
# me.write(str(getdate()))
# me.write("               Seated Cable Row \n")
# me.write(str(getdate()))
# me.write("               Barbell Curls\n")
# me.write(str(getdate()))
# me.write("               Downward Cable Extension\n")
# me.close()
#
#
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
