import random
import time

playAnswer = "yes"






def gameFunc():
  clock = 0



  list = []

  for i in range(0 , 2):
    a = int(input(f"Enter round {i + 1} st number : "))
    list.append(a)

  randomNumber = random.randint(list[0], list[1])

  isGuessing = True

  b = int
  start = time.time()

  while isGuessing:

    b = int(input("Enter your guess : "))
    if(randomNumber < b):
      print("Your guess bigger then mein!")
    elif(randomNumber > b):  
      print("Your guess smaller then mein!")
    elif(randomNumber == b):
      print("Congratulations ! You find my number which I keept my mind" , randomNumber)
      done = time.time()
      clock = done - start

      print("Elapsed Time :  ", int(clock))
      playAnswer = str(input("For play another type 'yes' :  "))
      youWantToPlay(playAnswer)
      isGuessing = False
def youWantToPlay(isPlayingAnswer):
  if(isPlayingAnswer == "yes"):
    gameFunc()
  else:
    print("Thanks for playing :D , Hope you come again :p ")
youWantToPlay(playAnswer)

  





