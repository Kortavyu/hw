"""
Напишите программу, выдающую скидку на эффект в зависимости от выбранных баллов.
Программа должна запросить количество набранных баллов и распечатать сообщение «Ваша скидка:» и скидка:
— от 0 до 49 баллов — «Скидка 10%»;
— от 50 до 99 баллов — «Скидка 15%»;
— от 100 баллов и выше — «Скидка 20%».
Примечание. Наличие функции является обязательным. Функция должна принимать количество набранных баллов.
"""

деф  set_discount ():
    mark  =  int ( input ( "Баллы (0-завершить): " ))
    пока  отметка  !=  0 :
        если  отметка  >=  1  и  отметка  <=  49 :
            вернуть  10
        elif  mark  >=  50  и  mark  <=  99 :
            вернуть  15
        Элиф  знак  ==  100 :
            вернуть  20
        еще :
            вернуть  0

print ( "Ваша скидка: " , set_discount (), "%" )