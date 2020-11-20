import socket
import random
from Crypto.Cipher import AES


def generate_random():

    random_string = ""
    for _ in range(16):
        random_string += str(random.randint(0, 9))

    return random_string


def padding(string_to_encode):

    number_of_spaces = 0
    length = len(string_to_encode)
    for _ in range(16 - (length % 16)):
        string_to_encode += " "
        number_of_spaces += 1

    return [string_to_encode, number_of_spaces]


def fake_cbc_encryption(k, iv, string_to_encode):
    # Padding
    if len(string_to_encode) % 16 != 0:
        aux_list = padding(string_to_encode)
        string_to_encode = aux_list[0]
        number_of_spaces = aux_list[1]
    else:
        number_of_spaces = 0
    string_to_encode = string_to_encode.encode()
    index_lower = 0
    index_upper = 16
    aux_iv = generate_random()
    k = k.encode()
    aux_iv = aux_iv.encode()
    iv = iv.encode()

    encoded_string = [number_of_spaces, aux_iv]
    while index_lower < len(string_to_encode):

        if index_lower == 0:
            # Encrypt the result of (Plaintext XOR IV)
            aes = AES.new(k, AES.MODE_CBC, aux_iv)
            actual_encoded_string = aes.encrypt(
                bytes([_a ^ _b for _a, _b in zip(string_to_encode[index_lower:index_upper], iv)]))
            encoded_string.append(actual_encoded_string)

            index_lower += 16
            index_upper += 16
            prev_encoded_string = actual_encoded_string

        else:
            # Encrypt the result of (Cyphertext XOR IV)
            aes = AES.new(k, AES.MODE_CBC, aux_iv)
            actual_encoded_string = aes.encrypt(
                bytes([_a ^ _b for _a, _b in zip(string_to_encode[index_lower:index_upper], prev_encoded_string)]))
            encoded_string.append(actual_encoded_string)

            index_lower += 16
            index_upper += 16
            prev_encoded_string = actual_encoded_string

    return encoded_string


def fake_cfb_encryption(k, iv, string_to_encode):

    # Padding
    if len(string_to_encode) % 16 != 0:
        aux_list = padding(string_to_encode)
        string_to_encode = aux_list[0]
        number_of_spaces = aux_list[1]
    else:
        number_of_spaces = 0

    string_to_encode = string_to_encode.encode()
    index_lower = 0
    index_upper = 16
    aux_iv = generate_random()
    k = k.encode()
    aux_iv = aux_iv.encode()
    iv = iv.encode()
    encoded_string = [number_of_spaces, aux_iv]

    # Looping through the blocks of plaintext
    while index_lower < len(string_to_encode):

        if index_lower == 0:
            # IV Encryption
            aes = AES.new(k, AES.MODE_CFB, aux_iv)
            encrypted_iv = aes.encrypt(iv)

            # Plain Text XOR Encrypted IV
            actual_encoded_string = (
                bytes([_a ^ _b for _a, _b in zip(string_to_encode[index_lower:index_upper], encrypted_iv)]))
            encoded_string.append(actual_encoded_string)

            index_lower += 16
            index_upper += 16
            prev_encoded_string = actual_encoded_string

        else:
            # Cypher Text Encryption
            aes = AES.new(k, AES.MODE_CFB, aux_iv)
            prev_encoded_string = aes.encrypt(prev_encoded_string)

            # Plain Text XOR Encrypted Cypher Text
            actual_encoded_string = (
                bytes([_a ^ _b for _a, _b in zip(string_to_encode[index_lower:index_upper], prev_encoded_string)]))
            encoded_string.append(actual_encoded_string)
            index_lower += 16
            index_upper += 16
            prev_encoded_string = actual_encoded_string

    return encoded_string

