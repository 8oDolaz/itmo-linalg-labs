import numpy as np

def encrypt(message: str, key: np.matrix, alphabet: str) -> str:
    encrypted_message = ''
    for i in range(len(key), len(message) + 1, len(key)):
        message_part = message[i - len(key):i]
        part_vector = np.matrix([
            [alphabet.find(symbol)]
            for symbol in message_part
        ])

        encrypted_part = (key * part_vector) % len(alphabet)
        encrypted_part = ''.join(alphabet[i] for i in encrypted_part.getA1())

        encrypted_message += encrypted_part

    return encrypted_message

def decrypt(enc_message: str, inverted_key: np.matrix, alphabet: str) -> str:
    decrypted_message = ''

    for i in range(len(inverted_key), len(enc_message) + 1, len(inverted_key)):
        message_part = enc_message[i - len(inverted_key):i]
        part_vector = np.matrix([
            [alphabet.find(symbol)]
            for symbol in message_part
        ])

        decrypted_part = (inverted_key * part_vector) % len(alphabet)
        decrypted_part = ''.join(alphabet[i] for i in decrypted_part.getA1())

        decrypted_message += decrypted_part

    return decrypted_message

def main():
    encrypted_message = [
        encrypt(message, m_key, alphabet)
        for m_key in matrix_keys
    ]

    print('Зашифрованное сообщение: ')
    print(*encrypted_message, sep='\n')

    encrypted_message[0] = encrypted_message[0][:2] + alphabet[:2] + encrypted_message[0][4:]
    encrypted_message[1] = encrypted_message[1][:4] + alphabet[2:4] + encrypted_message[1][6:]
    encrypted_message[2] = encrypted_message[2][:5] + alphabet[5:7] + encrypted_message[2][7:]

    print('\nВредоностное вмешательнство:')
    print(*encrypted_message, sep='\n')

    decrypted_messages = [
        decrypt(encrypted_message[i], inverted_matrix_keys[i], alphabet)
        for i in range(3)
    ]

    print('\nРезультат:')
    print(*decrypted_messages, sep='\n')


if __name__ == '__main__':
    message = 'люблю линал!'
    alphabet = ''.join(sorted(set(message)))

    print(alphabet)

    matrix_keys = [
        np.matrix([[7, 10], [3, 5]]),
        np.matrix([[1, 8, 8], [3, 3, 10], [11, 3, 7]]),
        np.matrix([[0, 5, 6, 2], [8, 6, 1, 4], [7, 1, 2, 8], [5, 6, 9, 7]]),
    ]

    inverted_matrix_keys = [
        np.matrix([[1, 6], [1, 3]]),
        np.matrix([[1, 0, 0], [7, 1, 2], [0, 3, 5]]),
        np.matrix([[7, 6, 5, 6], [3, 4, 6, 6], [2, 5, 0, 0], [7, 3, 5, 1]])
    ]

    main()
