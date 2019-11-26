t = input("Введите слово:").replace(' ','')
c=len(t)
d=1
r=1
s=1
for x in t:
    if (x>='A' and x<='Z') or (x>='А' and x<='Я'):
        b=round(d*100/c)
        result = str(b) + '% заглавные буквы'
        d+=1
    elif (x>='a'and x<='z') or (x>='а' and x<='я'):
        e=round(r*100/c)
        result1 = str(e) +'% прописные буквы'
        r+=1
    elif (x>=chr(0) and x<=chr(64) or (x>=chr(91) and x<=chr(96)) or (x>=chr(123) and chr(124))):
        f=round(s*100/c)
        result2 = str(f) +'% другие символы'
        s+=1
try:
    print(result,result1,result2)  
except:
    print('Есть символы вне ASCII')
    