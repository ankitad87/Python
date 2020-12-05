string1 = input('Input your string:\n')

new = list(string1)


for i in new:
    if i.isdigit():
        fp1 = open('num.txt', "a")
        fp1.write(i)
        fp1.close()
    elif(i in (',', '.', '!','*')):
        fp2 = open('char.txt', "a")
        fp2.write(i)
        fp2.close()
    elif(i == " "):
        continue
    else:
        fp3 = open('texts.txt', "a")
        fp3.write(i)
        fp3.close()
