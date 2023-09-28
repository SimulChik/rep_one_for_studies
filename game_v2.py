'''game "guess the number"
   computer's choice and guess '''

import numpy as np

def random_predict(number:int=1) -> int: #Обратите внимание, что в аргументах функции мы через 
    #двоеточие указываем тип данных для ввода (int), через равно — стандартное значение этого типа данных. 
    # Стрелка (->) указывает, какой тип данных мы должны получить на выходе. 
    # Это упростит заполнение документации (VS Code сможет автоматически генерировать её), 
    # а также позволит в дальнейшем эффективнее работать с ошибками.
    
    
    """random guessing 
        #Сгенерируем документацию для нашей функции. 
        # Для этого в теле функции прописываем тройные кавычки (символ docstring), и, 
        # если у вас установлено расширение Python Docstring Generator, 
        # шаблон документации будет создан автоматически. 
        # На месте [summary] прописываем описание функции, 
        # а вместо [description] указываем описание аргументов и возвращаемого значения:

    Args:
        number (int, optional): hidden number. Defaults to 1.

    Returns:
        int: qnty of iterations
    """
    count=0
    
    while True:
        count+=1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
    
    return(count)

def score_game(random_predict) -> int:
    """In how many iterations is needed to success (in avg for 1000 attempts)

    Args:
        random_predict (_type_): guessing function

    Returns:
        int: average qnty
    """
    count_ls = [] # список для сохранения кол-ва попыток
    np.random.seed(1) # фиксируем рэндом сид для воспроизводимости (чтобы был воспроизводимый результат. т.е. чтобы генерация рэндома была каждый раз постоянная. чтобы при перезапуске функции получали один и тот же результат)
    random_array = np.random.randint(1,101, size=(1000)) #Загадали список чисел
    
    for number in random_array:
       count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток
    print(f'Ваш алгоритм угадывает число в реднем за: {score} попыток')
    return(score)  

if __name__ == '__main__':
    #RUN
    score_game(random_predict)
    
#print(f'qnty of iterations: {random_predict(10)}') - из первого варианта задачи, 
# до необходимости рассчитывать среднее кол-во подходов

            #the end
    #=====

#ПОДВЕДЁМ ИТОГ ПО СОЗДАННОМУ КОДУ
# На самом деле мы с вами создали маленькую библиотеку game_v2.py. 
# Она содержит в себе две документированные функции: random_predict() и score_game(). 
# Мы можем импортировать их из других файлов и использовать в дальнейшем.

#Зачем нужно указывать передаваемые типы переменных в функции?
#Чтобы не ошибиться в типе переменной при передаче аргументов функции
#Для упрощения написания документации

#Для чего нужна документация к функции?
#Для объяснения назначение функции
#Для облегчения процесса вхождения новых участников в проект
