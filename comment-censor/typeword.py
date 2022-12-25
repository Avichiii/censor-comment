
with open("comment.txt", "w") as f:
    b = f.write("comment")

#this will loop the string for 100 times
#first a will print all the strings in the commnet.txt (in this case 11 times)
#second time a will again print 11 strings in the commnet.txt .... this will loop for 100 times
#at last we will have 100 * 11 = 1100 lines in the commnet.txt

for i in range(1,101):
    with open("comment.txt", "a") as f:
        a = f.write("fuck this bitch\n")
        a = f.write("donkey this bitch\n")
        a = f.write("shit this bitch\n")
        a = f.write("fuck this bitch\n")
        a = f.write("looser this bitch\n")
        a = f.write("trash this bitch\n")
        a = f.write("fuck this bitch\n")
        a = f.write("fuck this bitch\n")
        a = f.write("fuck this bitch\n")
        a = f.write("fuck this bitch\n")
        a = f.write("fuck this bitch\n")

#a will increment with i
        a * i