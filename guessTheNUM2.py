
import random



def compGuess(x):
    low = 1
    high = x
    feedback = '' # initializing an empty string just like guess 
    while feedback != 'c' :
        if low !=high: #c = correct
         guess = random.randint(low,high)
        else:
             guess = low   #can be high as well.
        feedback = input(f'Is {guess} too high(H), too low(L) or correct(C)??'.lower())
        if feedback =='h':
            high = guess -1
        elif feedback == 'l':
            low =guess+1

    print("Yayy! The computer guessed your number correctly. ")    

compGuess(10)        
