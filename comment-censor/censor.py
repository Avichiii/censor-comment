input = input("enter comment: ")



#this list store the strings that will be replaced wih the input
word = ["donkey", "looser", "shit", "fuck","trash"] #you can enter words of your likes that you want to change
#word = []

with open("comment.txt", "r") as f: #enter the .txt file name where you want to make a change
            a = f.read()
            
#with open("YOUR_FILE_NAME.txt", "r") as f:
#            a = f.read()
#if any of the input string contains word variable value that will be replaced

if input == word[0]:
        for i in word[0]:
            c = a.replace(word[0],"#$%@$&*") #you can choose any word you want to replace with 
        with open("comment.txt", "w") as g:
            g.write(c)
    
# if input == word[0]:
#         for i in word[0]:
#             c = a.replace(word[0],"ENTER_THE_WORD_YOU_WANT_TO_REPLACE_WITH") #
#         with open("comment.txt", "w") as g:
#             g.write(c)

elif input == word[1]:
    for i in word:
        d = a.replace(word[1],"#$%@$&*") #HERE
    with open("comment.txt", "w") as g:
        g.write(d)

elif input == word[2]:
    for i in word:
        e = a.replace(word[2],"#$%@$&*") #HERE
    with open("comment.txt", "w") as g:
        g.write(e)

elif input == word[3]: 
    for i in word:
        p = a.replace(word[3],"#$%@$&*") #HERE
    with open("comment.txt", "w") as g:
        g.write(p)

elif input == word[4]:
    for i in word:
        z = a.replace(word[4],"#$%@$&*") #HERE
    with open("comment.txt", "w") as g:
        g.write(z)
            
#THIS ONE WILL APPEND IF THE WORD YOU ENTER ISN'T PRESENT

elif input != word:
    with open("comment.txt", "a") as g:
        append = g.write(f"\n{input}")


else:
    print("you are good!")
