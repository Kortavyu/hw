"""
Напишите ожидаемую допуску ученика к зачету.
Программа должна запросить число учеников, у каждого ученика запросить баллы за окончательный тест
и в ответ печатать, допущен ли он (Верно или Неверно) к зачету (необходимо набрать больше 50 баллов).
Ученикам без допуска следует рассчитаться "Вы отчислены".
Выдача допуска реализуй как функцию.
"""

def  mark_test ( отметка ):
     знак  возврата >  50

сумма  =  int ( input ( "Число записан: " ))
для  i  в  диапазоне ( сумма ):
    mark1  =  int ( input ( "Введите балл за тест: " ))
    результат  =  метка_тест ( метка1 )
    если  результат :
        print ( "Вы молодец!" )
    еще :
        print ( "Вы отчислены :(" )