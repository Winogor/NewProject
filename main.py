import random

def rock_paper_scissors():
  choise = ['камень', 'ножницы', 'бумага']
  while True:
    comp_choice = random.choice(choise)
    user_choice = input('Выберите и введите камень, ножницы или бумагу: ').lower()
    if user_choice not in choise:
      print('Вы ввели некорректное слово, введите еще раз: ')
      continue
    if user_choice == comp_choice:
      print('Выбор фигур одинаковый. Это ничья!)')
    elif user_choice == 'камень' and comp_choice == 'ножницы' or user_choice == 'ножницы' and comp_choice == 'камень' or user_choice == 'бумага' and comp_choice == 'камень':
      print(f"Вы крут! Противник выбрал {comp_choice} и вы победили!))")
    else:
      print(f"Вы проиграли(( противник выбрал {comp_choice}" )
    next_game = input('Хотите сыграть еще раз? Введите да или нет))?  ').lower()
    if next_game == 'нет':
      break

def guess_the_number():
  comp_num = random.randint(1,10)
  while True:
    user_num = int(input('Введите число от 1 до 10: '))
    if user_num != comp_num:
      print('Вы не угадали попробуйте еще раз: ')
    else:
      print(f"Вы угадали!)) Противник загадал {comp_num}")
      next_play = input('Хотите еще раз сыграть? Напишите да или нет: ').lower()
      if next_play == 'нет':
        break

def mainMenu():
  print('Есть 2 игры на выбор: \n1. Камень ножницы бумага \n2. Угадай число.')
  game = int(input('Выберите игру: '))
  if game == 1:
    rock_paper_scissors()
  elif game == 2:
    guess_the_number()

mainMenu()
