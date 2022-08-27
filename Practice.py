import random


#some variables with weird name
yourcode = input('enter a code : ')
codenum = len(yourcode)
codeedchars = ["y","d",'f',"t","h",'é']
codeinstulist = range(0 , codenum)
codedcode = yourcode[random.randrange(codenum)]
finalecode = ''
#The function that will hash the input randomly
while True:
    if codenum:

        codedcode = codeinstulist[random.randrange(len(codeinstulist))]
        codenum -=1
        codedcode2 = codeedchars[random.randrange(len(codeedchars))]
        #Mix between random letters and number
        finalecode = finalecode + str(codedcode) + str(codedcode2)
        
    else:
        print('Code regenerated')
        break
print("Your encoded code is : " +finalecode)