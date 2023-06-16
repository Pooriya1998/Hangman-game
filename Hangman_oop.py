import random


class HangmanGame:
    player_list = list()
    player_name = list()
    wordlist = ['python', 'programming', 'hangman', 'function', 'functional']

    def __init__(self):
        self.masked_word = None
        self.name = input("Enter your name: ")
        print('........................................')
        self.__rand_word = random.choice(self.wordlist)
        self.__guessed_letters = set()
        self.__guess_left = 3
        self.__win_state = False
        self.player_list.append(self)
        self.player_name.append(self.name)

    def check_answer(self):
        while self.__guess_left > 0:
            self.masked_word = ''.join([c if c in self.__guessed_letters else '_' for c in self.__rand_word])
            print(self.masked_word)
            print('........................................')

            if '_' not in self.masked_word:
                print("Congratulations, you guessed the word!")
                print('........................................')
                print(f"{self.name} Won")
                print('........................................')
                self.__win_state = True
                return

            answer = input(f"\n{self.name}, please enter your guess: ")
            print('........................................')
            self.__guessed_letters.add(answer)

            if answer not in self.__rand_word:
                self.__minus_guess_left()
                print("Incorrect guess, try again.")
                print('........................................')

            print(f"{self.__guess_left} guesses left")
            print('........................................')

        print("You ran out of guesses")
        print('........................................')

    def __minus_guess_left(self):
        self.__guess_left -= 1

    def has_guess_left(self):
        if self.__guess_left > 0:
            return True
        elif self.__guess_left == 0:
            return False

    def has_won(self):
        return self.__win_state

    @classmethod
    def game_has_winner(cls):
        if any(player.has_won() is True for player in cls.player_list):
            return True
        else:
            return False


class GameController:
    checker = 0

    def __init__(self):
        while True:
            for player in HangmanGame.player_list:
                if not player.has_won():
                    player.check_answer()
                    self.checker = 0

                if not player.has_guess_left():
                    self.checker = 1
                    print(f"The game is over, {player.name}'s loss")
                    print('........................................')

            if self.checker == 1:
                break

            if HangmanGame.game_has_winner():
                break


if __name__ == "__main__":
    while True:
        order = input("What do you want to do? \norder(Start game, Add player, List of players, Exit the game): ")
        print('........................................')
        if order == "Add player":
            HangmanGame()
        elif order == "Start game":
            GameController()
        elif order == "List of players":
            for i in HangmanGame.player_name:
                print(i, end=', ')
            print('')
            print('........................................')
        elif order == "Exit the game":
            print("Goodbye")
            break
