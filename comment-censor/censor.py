input = input("enter comment: ")



#this list store the strings that will be replaced wih the input
word = ["donkey", "looser", "shit", "fuck","trash"]


with open("comment.txt", "r") as f:
            a = f.read()
            
#if any of the input string contains word variable value that will be replaced

if input == word[0]:
        for i in word[0]:
            c = a.replace(word[0],"#$%@$&*")
        with open("comment.txt", "w") as g:
            g.write(c)
    


elif input == word[1]:
    for i in word:
        d = a.replace(word[1],"#$%@$&*")
    with open("comment.txt", "w") as g:
        g.write(d)

elif input == word[2]:
    for i in word:
        e = a.replace(word[2],"#$%@$&*")
    with open("comment.txt", "w") as g:
        g.write(e)

elif input == word[3]:
    for i in word:
        p = a.replace(word[3],"#$%@$&*")
    with open("comment.txt", "w") as g:
        g.write(p)

elif input == word[4]:
    for i in word:
        z = a.replace(word[4],"#$%@$&*")
    with open("comment.txt", "w") as g:
        g.write(z)


elif input != word:
    with open("comment.txt", "a") as g:
        append = g.write(f"\n{input}")


else:
    print("you are good!")