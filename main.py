import hangman
from time import sleep

def main():
   play_again = True #initial
   win_streak = 3
   while play_again:
      win_streak = hangman.play_hangman(win_streak)
      print(f"Current win-streak: {win_streak}")
      play_again = hangman.ask_play_again()
      if not play_again:
         break
   print("Thanks for playing our game, see you later..")
   sleep(1)



if __name__ == "__main__":
   main()