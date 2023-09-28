'''game "guess the number" '''

import numpy as np

number = np.random.randint(1,101)   #choosing a number

#qnty of attempt
count=0

while True:
    count +=1
    predict_number = int(input('Input your version: '))
    
    if predict_number > number:
        print('you are looking for a smaller number')
    elif predict_number < number:
        print('you are looking for a bigger number')
    else:
        print(f'your guess is correct, you succeed in {count} iterations. The number is {number}')
        break #the game is over
    #jflsdlblefblif;ubgv;uf