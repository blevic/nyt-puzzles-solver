import os

INNER_LETTER = 'i'
OUTER_LETTERS = 'abodlr'


def words():
    lst = []
    curr_directory = os.path.dirname(os.path.realpath('__file__'))
    dictionary_path = os.path.join(curr_directory, '../dict/words.txt')
    dictionary_path = os.path.abspath(os.path.realpath(dictionary_path))
    with open(dictionary_path, 'r') as file:
        for row in file:
            lst.append(row.strip())
    return lst


def is_valid(w, m, opts):
    return m in w and set(w).issubset(opts) and len(w) > 3


def main():
    mandatory_letter = INNER_LETTER.lower()
    optional_letters = set(OUTER_LETTERS.lower() + mandatory_letter)
    results = []

    for word in words():
        if is_valid(word, mandatory_letter, optional_letters):
            results.append(word)

    for w in sorted(results, key=len):
        print(w)


if __name__ == '__main__':
    main()
