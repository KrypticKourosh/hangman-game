import hangman

def main():
   print("--------Welcome to hangman game--------")
   word_len = hangman.get_word_len()
   random_word = hangman.fetch_random_word(word_len)
   hint = ["_"] * len(random_word)
   wrong_guess_count = 0
   guessed_letters = []

   is_running = True
   while is_running:
      hangman.display_art(wrong_guess_count)
      hangman.display_hint(hint)

      while True:
         guess = input("Enter letter: ")
         flag = hangman.check_guess(guessed_letters, guess=guess)
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
         hint = hangman.update_hint(random_word, hint, guess)
      else:
         wrong_guess_count += 1
      guessed_letters.append(guess)

      flag = hangman.check_win_condition(wrong_guess_count, hint)
      if flag == "won":
         print(f"You won, total incorrect guesses: {wrong_guess_count}")
         is_running = False
      elif flag == "lost":
         hangman.display_art(6) #full hangman
         print(f"You lost, the word was: {random_word}")
         is_running = False


if __name__ == "__main__":
   main()