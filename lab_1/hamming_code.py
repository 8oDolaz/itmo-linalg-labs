import numpy as np

def main():
    alphabet_str = ''.join(
        chr(i) for i in range(ord('а'), ord('я') + 1)
    )
    alphabet_dict = {
        letter: ('0' * (5 - len(bin(i)[2:]))) + bin(i)[2:]
        for i, letter in enumerate(alphabet_str)
    }

    word = 'игра'
    word = ''.join(alphabet_dict[letter] for letter in word)
    word = [
        np.matrix([[int(word[i - 4:i][j])] for j in range(4)])
        for i in range(4, len(word) + 1, 4)
    ]

    encoded_word = [
        (generator_matrix.T * word_part) % 2
        for word_part in word
    ]

    encoded_word[0][2] = (encoded_word[0][2] + 1) % 2

    encoded_word[1][:2] = ([
        [(encoded_word[1].item(i) + 1) % 2]
        for i in range(2)
    ])

    encoded_word[2][1] = [(encoded_word[2].item(1) + 1) % 2]
    encoded_word[2][4] = [(encoded_word[2].item(4) + 1) % 2]
    encoded_word[2][6] = [(encoded_word[2].item(6) + 1) % 2]

    encoded_word[3][2:6] = ([
        [(encoded_word[3].item(i) + 1) % 2]
        for i in range(3, 7)
    ])

    parity_check = [
        (parity_check_matrix * part) % 2
        for part in encoded_word
    ]

    for i, parity in enumerate(parity_check):
        if parity.sum() == 1:
            row_index, _ = np.where(parity == 1)
            row_index += 4
            encoded_word[i][row_index] = (encoded_word[i][row_index] + 1) % 2
        elif parity.sum() == 2:
            parity_raw = parity.getA1()
            ones_indices = [i for i in range(len(parity_raw)) if parity_raw[i]]

            error_index = p[ones_indices[0]].intersection(p[ones_indices[1]])
            error_index.remove(3)
            error_index = error_index.pop()

            encoded_word[i][error_index] = (encoded_word[i][error_index] + 1) % 2
        elif parity.sum() == 3:
            encoded_word[i][3] = (encoded_word[i][3] + 1) % 2

    for encoded_part in encoded_word:
        print(encoded_part  )

    broken_word = [
        (reverse_matrix * encoded_part) % 2
        for encoded_part in encoded_word
    ]
    broken_word = [broken_part.getA1() for broken_part in broken_word]
    broken_word = [broken_word[i // 4][i % 4] for i in range(20)]
    broken_word = [broken_word[i - 5:i] for i in range(5, 20 + 1, 5)]
    broken_word = [int(''.join(str(p) for p in part), 2) for part in broken_word]
    broken_word = ''.join(alphabet_str[i] for i in broken_word)

    print(broken_word)

if __name__ == '__main__':
    generator_matrix = np.matrix([
        [1, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 1, 1],
    ])
    parity_check_matrix = np.matrix([
        [1, 1, 0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0, 0, 1]
    ])
    reverse_matrix = np.matrix([
        [1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
    ])

    p = [
        set([0, 1, 3]),
        set([0, 2, 3]),
        set([1, 2, 3]),
    ]

    main()
