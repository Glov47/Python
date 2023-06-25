from random import *
def randomizer():
    return randrange(1,101)
def isint(number):
    try:
        int(number)
        return True
    except ValueError:
        return False
def is_valid(number):
    flag = True
    if isint(number) != True:
        flag = False
        return flag
    if int(number) > 100 or int(number) < 1:
        flag = False
    return flag
n = randomizer()
print('Добро пожаловать в числовую угадайку!', 
      'Я загадал вам целое число от 1 до 100, попробуйте его угадать;)', 
      'Введите число:', sep='\n')
guess = 0
count = 0
while guess != n:
    guess = input()
    count += 1
    if is_valid(guess) == False:
        print('Введите целое число от 1 до 100:')
    elif int(guess) < n:
        print(f'Я загадал число больше чем {guess}, попробуйте еще раз:')
    elif int(guess) > n:
        print(f'Я загадал число меньше чем {guess}, попробуйте еще раз:')    
    else:
        print('Это именно оно!', f'Ваше количество попыток: {count}.', 'Попробуете улучшить результат?', 
              'Напишите "да", если хотите попробовать еще раз или "нет", если не хотите.', sep='\n')
        restart = input().lower()
        while restart != 'нет' and restart != 'да':
            print('Я вас не понял:(, напишите "да" или "нет".')
            restart = input().lower()
        if restart == 'нет':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break;
        else:
            guess = 0
            count = 0
            print('Введите число:')