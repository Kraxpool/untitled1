def str():
    try:
        text = input('str - ')
        counter = 0
        counter2 = 0
        for i in text:
            if i.isalpha():
                counter += 1
            if i.isnumeric():
                counter2 += 1
        print(f'Num of letters -{counter}\nNum of digits - {counter2}')



    except Exception as ex:
        print(f'Eror information: {ex}')
