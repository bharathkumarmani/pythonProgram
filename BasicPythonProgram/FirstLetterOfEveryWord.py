def firstletterofeveryword(text):
    result=""
    v = True
    for i in range(len(text)):
        if(text[i]==" "):
            v = True
        elif(text[i] != " " and v==True):
            result += text[i]
            v=False
    return result 


print(firstletterofeveryword("Good To Learn Python"))