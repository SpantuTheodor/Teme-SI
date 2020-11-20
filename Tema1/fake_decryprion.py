from Crypto.Cipher import AES

def fake_cbc_decryption(k, iv, string_to_decode):

    aux_iv = string_to_decode[1]
    iv = iv.encode()
    k = k.encode()

    for index in range(2, len(string_to_decode)):
        if index == 2:
            aes = AES.new(k, AES.MODE_CBC, aux_iv)
            dec_index = aes.decrypt(string_to_decode[index])
            decoded_string = bytes([_a ^ _b for _a, _b in zip(dec_index, iv)])
            prev_dec_index = string_to_decode[index]
        else:
            aes = AES.new(k, AES.MODE_CBC, aux_iv)
            dec_index = aes.decrypt(string_to_decode[index])
            actual_decoded_string = bytes([_a ^ _b for _a, _b in zip(prev_dec_index, dec_index)])
            decoded_string += actual_decoded_string
            prev_dec_index = string_to_decode[index]
    return str(decoded_string)[2: - string_to_decode[0] - 1]


def fake_cfb_decryption(k, iv, string_to_decode):
    aux_iv = string_to_decode[1]
    iv = iv.encode()
    k = k.encode()
    for index in range(2, len(string_to_decode)):
        if index == 2:
            aes = AES.new(k, AES.MODE_CFB, aux_iv)  # IV Encryption
            dec_iv = aes.encrypt(iv)

            decoded_string = bytes([_a ^ _b for _a, _b in zip(string_to_decode[index], dec_iv)])
            prev_index = string_to_decode[index]
            # Ciphertext XOR Encrypted IV

        else:
            aes = AES.new(k, AES.MODE_CFB, aux_iv)
            prev_dec_index = aes.encrypt(prev_index)  # Previous Ciphertext Encryption

            actual_decoded_string = bytes([_a ^ _b for _a, _b in zip(string_to_decode[index], prev_dec_index)])
            decoded_string += actual_decoded_string
            prev_index = string_to_decode[index]
            # Ciphertext XOR Encrypted Previous Ciphertext

    return str(decoded_string)[2: - string_to_decode[0] - 1]

