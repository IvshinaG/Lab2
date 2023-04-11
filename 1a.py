a=input("Введите пароль: ")
b=input("Повторите пароль: ")
num = 0
up = 0
lo = 0
sp = 0
s="Ненадёжный пароль, добавьте"
k=len(s)
if a==b:
    if len(a)<6:
        print("Слишком короткий пароль")
    else:
        for i in a:
            if i.isnumeric():
                num=1
            elif i.islower():
                lo=1
            elif i.isupper():
                up=1
            elif i in "@#*&!":
                sp=1
        if num and lo and up and sp:
            print("Пароль сохранён")
        else:
            if num==0:
                s += " цифры"
            elif lo==0:
                s+=" буквы нижнего регистра"
            elif up==0:
                s+=" буквы верхнего регистра"
            elif sp==0:
                s += " специальные символы"
            print(s) #добавила вывод нехватающих символов для сложного пароля.
else:
    print("Пароль не совпадает")



