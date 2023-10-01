from hill_cipher import encrypt, decrypt

import math
import numpy as np
from random import randint

def generate_matirx_key(alphabet_length: int) -> np.matrix:
    while True:
        matrix = [[-1, -1], [-1, -1]]
        for elem in range(4):
            matrix[elem // 2][elem % 2] = randint(0, alphabet_length)
        matrix = np.matrix(matrix)

        det = int(np.linalg.det(matrix))
        if det > 0 and math.gcd(det, alphabet_length) == 1:
            return matrix

def main():
    matrix_key = generate_matirx_key(len(alphabet))

    enc_message_1 = encrypt(message_1, matrix_key, alphabet)
    enc_message_2 = encrypt(message_2, matrix_key, alphabet)

    print(f'Алфавит: "{alphabet}"')
    print(f'Исходник первого сообщения: "{message_1}"')
    print('Зашифрованные сообщения:')
    print(enc_message_1, enc_message_2, sep='\n')

    print('\n'.join(f'{symbol}, {i}' for i, symbol in enumerate(alphabet)))
    print(f'Исходник 1: {"_".join(str(alphabet.find(letter)) for letter in message_1)}')
    print(f'Исходник 2: {"_".join(str(alphabet.find(letter)) for letter in message_2)}')
    print(f'enc_message_1: {"_".join(str(alphabet.find(letter)) for letter in enc_message_1)}')
    print(f'enc_message_2: {"_".join(str(alphabet.find(letter)) for letter in enc_message_2)}')

if __name__ == '__main__':
    message_1 = 'я исходник!)'
    message_2 = 'не взломаешь'
    alphabet = ''.join(sorted(set(message_1 + message_2)))

    main()
