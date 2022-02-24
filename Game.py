print("Игра крестики-нолики")

pole = list(range(1,10))

def risunok_pole(pole):
   print("-" * 13) # черточки сверху
   for i in range(3): # в одной строке будет три клетки
      print("|", pole[0+i*3], "|", pole[1+i*3], "|", pole[2+i*3], "|") # составление поля из 3 строк с разделителем
      print("-" * 13) # черточки в поле

def take_input(nomer_igroka): # ввод нужного игрока
   valid = False
   while not valid: # проверяет истинно или ложно
      player_answer = input(nomer_igroka + " ставим в клетку...")  # Спрашиваю, куда ходит игрок
      try:
         player_answer = int(player_answer)
      except:
         print("Это не число. Введите нужное число от 1 до 9") # Проверка, что ввели именно число
         continue
      if player_answer >= 1 and player_answer <= 9: # Проверка, что вводят числа от 1 до 9 включительно
         if(str(pole[player_answer-1]) not in "XO"): # Проверка, что введено подходящее число и это цифра
            pole[player_answer-1] = nomer_igroka
            valid = True # проверка, что клетка свободна
         else:
            print("Эта клетка занята, используйте пустую клетку")
      else:
        print("Нужно ввести число от 1 до 9.") # Проверка, что введено число от 1 до 9

def check_win(pole):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)) # Выигрышные комбинации
   for each in win_coord:
       if pole[each[0]] == pole[each[1]] == pole[each[2]]:
          return pole[each[0]]
   return False

def main(pole):
    counter = 0
    win = False
    while not win:
        risunok_pole(pole)
        if counter % 2 == 0:
           take_input("X") # Игру начинает X
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(pole)
           if tmp:
              print(tmp, "выигрывает эту партию")
              win = True
              break
        if counter == 9:
            print("ничья в игре")
            break
    risunok_pole(pole)
main(pole)



git remote add origin https://github.com/logoshisha/Game-1.git