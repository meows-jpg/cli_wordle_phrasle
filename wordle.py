from random import randint
from time import sleep #only used for testing - no requirement



class Wordle:
    def __init__(self, mode=None, language=None, phases=None, difficulty=None, word_char_count=None):
        #game settings
        self.mode = mode or "classic"
        self.language = language or "en"
        self.phases = phases or 6
        self.difficulty = difficulty or "hard"
        self.word_char_count = word_char_count or 5
        #backend
        self.target = None
        self.words = None
        #hints
        self.correct_positions = None or self.word_char_count*"0"
        self.correct_chars = ""
        self.incorrect_chars = ""


    def start(self):

        def get_word_list(filename):
            with open(filename+".txt", "r", encoding="UTF8") as words:
                self.words = words.read().split()


        def pick_target_word():
            self.target = self.words[randint(0, len(self.words)+1)]


        file_name = self.language + str(self.word_char_count) + self.difficulty
        get_word_list(file_name)
        pick_target_word()


    #maybe make a class out of it and call it Playerinteraction or so
    def loop_phases(self):
        def player_input():
            while True:
                user_word = input(f"enter your word for turn {self.phases}: ").upper()
                try:
                    if len(user_word) == self.word_char_count and user_word in self.words:
                        return user_word
                except:
                    print(f"\nwrong formation or {user_word} does not exist - try again.")
                    print(f"type in a word with exactly {self.word_char_count} characters\n")


        def validate_word(user_word):
            if self.target == user_word:
                return True
            else:
                cached_user_word = user_word
                correct_positions = ""
                correct_chars = ""
                for index, target_char in enumerate(self.target):
                    if target_char in user_word:
                        user_word = user_word.replace(target_char, "", 1)
                        correct_chars += target_char
                    if target_char == cached_user_word[index] and self.correct_positions[index] == "0":
                        correct_positions += target_char
                    else:
                        correct_positions += self.correct_positions[index]


                #update char hints
                for cc_char in correct_chars:
                    if cc_char not in self.correct_chars:
                        self.correct_chars += cc_char
                self.correct_positions = correct_positions

                for uw_char in user_word:
                    if uw_char not in self.incorrect_chars:
                        self.incorrect_chars += uw_char


        #I think this should be in a gui class or file/function collection
        def hints():
            print(f"correct positions   - {self.correct_positions}")
            print(f"correct chars       - {self.correct_chars}")
            print(f"incorrect chars     - {self.incorrect_chars}\n")


        #interact with player going through the in self.phases defined phases
        #prints will be taken off later once i got the gui
        #for now its here for testing
        while self.phases > 0:
            if validate_word(player_input()) is True:
                print("You won!")
                break
            else:
                hints()
            self.phases -= 1
            if self.phases == 0:
                print(f"Das it, {self.phases} turns left")
                print(f"You lost! {self.target} was the word")


        # collecting stats maybe a new class for this
        def result(self):
            ...


if __name__ == "__main__":
    print("this is not the file you should try to run")
