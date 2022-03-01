import os
from random import choice

WORD_SIZE = 5
NUMBER_OF_ROUNDS = 6


def initial_words():
    lst = []
    curr_directory = os.path.dirname(os.path.realpath('__file__'))
    dictionary_path = os.path.join(curr_directory, '../dict/words.txt')
    dictionary_path = os.path.abspath(os.path.realpath(dictionary_path))
    with open(dictionary_path, 'r') as file:
        for row in file:
            word = row.strip()
            if len(word) == WORD_SIZE:
                lst.append(row.strip())
    return lst


def enter_result():
    done = False
    result = ""
    print("What was the result? [G]reen, [Y]ellow, [B]lack")
    while not done:
        result = input("[G/Y/B]: ").lower()
        if len(result) == WORD_SIZE and (set(result)).issubset({'g', 'y', 'b'}):
            done = True
        else:
            print("Invalid entry. Type the 5 colors you obtained (example: GBBBY)")
    return result


def update_words(lst, word, rst):
    updated_words, green_idx, green_letters, yellow_idx, yellow_letters, black_letters = [], [], [], [], [], []
    for idx in range(WORD_SIZE):
        color = rst[idx]
        letter = word[idx]
        if color == 'g':
            green_idx.append(idx)
            green_letters.append(letter)
        elif color == 'y':
            yellow_idx.append(idx)
            yellow_letters.append(letter)
        elif color != 'b':
            raise Exception("Result not in g/y/b")

    for idx in range(WORD_SIZE):
        color = rst[idx]
        letter = word[idx]
        if color == 'b' and letter not in green_letters + yellow_letters:
            black_letters.append(letter)

    def possible_word(candidate, actual_word):
        # black
        for i in range(WORD_SIZE):
            if candidate[i] in black_letters:
                return False

        # green
        for i in range(WORD_SIZE):
            if i in green_idx and candidate[i] != actual_word[i]:
                return False

        # yellow
        for i in range(WORD_SIZE):
            if i in yellow_idx:
                if candidate[i] == actual_word[i] or actual_word[i] not in candidate:
                    return False

        return True

    for w_candidate in lst:
        if possible_word(w_candidate, word):
            updated_words.append(w_candidate)

    return updated_words


def get_word(words_lst):
    guess_word = ""
    print("Do you want a [R]andom word or to [T]ype your own guess?")
    while guess_word == "":
        letter = input("R/T: ").lower()
        if letter == 'r':
            done = False
            while not done:
                guess_word = choice(words_lst)
                print("Try the word: " + guess_word.upper())
                accepted = input("Was it accepted? Y/N: ").lower()
                done = True if accepted == 'y' else False
        elif letter == 't':
            done = False
            while not done:
                guess_word = input("Type the word you wrote: ").lower()
                if len(guess_word) == WORD_SIZE:
                    done = True
                else:
                    print("Invalid word length.")
        else:
            print("Type R or T ([R]andom word or [T]ype your own guess")

    return guess_word


def main():
    words = initial_words()
    current_round = 1

    while current_round <= NUMBER_OF_ROUNDS:
        print("\nRound " + str(current_round) + ". There are " + str(len(words)) + " possible words.")
        chosen_word = get_word(words)
        result = enter_result()
        words = update_words(words, chosen_word, result)
        if result == "ggggg":
            print("Congrats!")
            break
        if len(words) == 0:
            print("No more possible words!")
            break
        current_round += 1


if __name__ == '__main__':
    main()
