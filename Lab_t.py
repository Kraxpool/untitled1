def str():
    try:
        text = input('str - ')
        word = input('find word - ')
        word2 = input('change word - ')
        edited_text = text.replace(word, word2)
        print(f'{ edited_text}')
    except Exception as ex:
        print(f'Eror information: {ex}')


str()