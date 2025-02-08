import requests

def play_hangman():
   print("--------Welcome to hangman game--------")
   word_len = get_word_len()
   random_word = fetch_random_word(word_len)
   hint = ["_"] * len(random_word)
   wrong_guess_count = 0
   guessed_letters = []

   is_running = True
   while is_running:
      display_art(wrong_guess_count)
      display_hint(hint)

      while True:
         guess = input("Enter letter: ")
         flag = check_guess(guessed_letters, guess=guess)
         if flag == "length_error":
            print("letter should be 1 character long, try again..")
            continue
         elif flag == "alphabetic_error":
            print("letter should be alphabetic, try again..")
            continue
         elif flag == "repeated_error":
            print("you have already guessed that letter, try another one..")
            continue
         else:
            break

      if guess in random_word:
         hint = update_hint(random_word, hint, guess)
      else:
         wrong_guess_count += 1
      guessed_letters.append(guess)

      flag = check_win_condition(wrong_guess_count, hint)
      if flag == "won":
         print(f"You won, total incorrect guesses: {wrong_guess_count}")
         is_running = False
      elif flag == "lost":
         display_art(6) #full hangman
         print(f"You lost, the word was: {random_word}")
         is_running = False

def display_art(wrong_guess_count):
   hangman_art = {0:("   ",
                     "   ",
                     "   "),
                  1:(" o ",
                     "   ",
                     "   "),
                  2:(" o ",
                     " | ",
                     "   "),
                  3:(" o ",
                     "/| ",
                     "   "),
                  4:(" o ",
                     "/|\\",
                     "   "),
                  5:(" o ",
                     "/|\\",
                     "/  "),
                  6:(" o ",
                     "/|\\",
                     "/ \\"),}
   print("----------------")
   for art in hangman_art[wrong_guess_count]:
      print(art)
   print("----------------")

def display_hint(hint):
   print("word:", end=" ")
   print(" ".join(hint))
   print()

def update_hint(random_word, hint, guess):
   for index, letter in enumerate(random_word):
      if guess == letter:
         hint[index] = letter
   return hint

def check_guess(guessed_letters, guess=""):
   if len(guess) != 1:
      return "length_error"
   elif not guess.isalpha():
      return "alphabetic_error"
   elif guess in guessed_letters:
      return "repeated_error"
   else:
      return "no_error"

def check_win_condition(wrong_guess_count, hint):
   if wrong_guess_count == 6:
      return "lost"
   elif not "_" in hint:
      return "won"
   else:
      return "still_going"

def fetch_random_word(word_len):
   url = f"https://random-word-api.vercel.app/api?words=1&length={word_len}" 
   try:
      response = requests.get(url)
      response.raise_for_status()
      data = response.json() #list of single string
      data = "".join(data) #turns list into string
      return data
   except requests.HTTPError as http_error:
      print(f"HTTP error occurred: {http_error}")
   except requests.ConnectionError:
      print("Connection error, check your connection")
   exit()

def get_word_len():
   class WordLengthError(Exception):
      pass

   while True:
      try:
         word_len = int(input("Enter word length(3-9): "))
         if word_len < 3 or word_len > 9:
            raise WordLengthError
      except ValueError:
         print("invalid number, try again..")
         continue
      except WordLengthError:
         print("word length out of range, try again..")
         continue
      else:
         return word_len
      
def ask_play_again():
   yes_answers = ["YES", "Y", "YA", "YEA", "YEAH", "1"]
   no_answers = ["NO", "N", "NOT", "NA", "NOPE", "0"]
   while True:
      flag = input("Do you want to play again(Y/N): ").upper()
      if flag in yes_answers:
         return True
      elif flag in no_answers:
         return False
      else:
         print("Invalid input, try again..")
         continue