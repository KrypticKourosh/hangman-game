import hangman
from time import sleep

def main():
   play_again = True #initial
   while play_again:
      hangman.play_hangman()
      play_again = hangman.ask_play_again()
      if not play_again:
         break
   print("Thanks for playing our game, see you later..")
   sleep(1)



if __name__ == "__main__":
   main()