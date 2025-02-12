import hangman
from time import sleep

def main():
   play_again = True #initial
   win_streak = 0
   while play_again:
      hangman.clear_console()
      win_streak = hangman.play_hangman(win_streak)
      print(f"Current win-streak: {win_streak}")
      play_again = hangman.ask_play_again()
      if play_again == False:
         break
      hangman.clear_console()
   
   print("Thanks for playing our game, see you later..")
   sleep(1)



if __name__ == "__main__":
   main()