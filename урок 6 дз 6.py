summa  =  int ( input ( 'Введите сумму к случаю:' ))
пока  Истина :
    cost  =  float ( input ( 'Введите стоимость покупки: ' ))
    если  стоимость  %  2  ==  0 :
        стоимость  =  стоимость  /  2
        print ( 'К случаю:' , стоимость )
    еще :
        стоимость  = ( стоимость  /  100 ) *  15
        print ( 'К случаям:' , стоимость )

    print ( 'Спасибо за покупку!' )