import socket
import pickle
from Crypto.Cipher import AES
from fake_encryption import fake_cbc_encryption, fake_cfb_encryption
from fake_decryprion import fake_cbc_decryption, fake_cfb_decryption

k3 = "1234564212345642"
iv3 = "4560987652646442"


def client_program():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 50000))


    while True:

        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)


        if data != None:
            message = "Encryption Mode Received"
            client_socket.send(message.encode())

        if data.upper() == "CBC":

            # Receive CBC Encrypted Key and decrypt it
            data = client_socket.recv(1024)
            enc_k2 = pickle.loads(data)
            k2 = fake_cbc_decryption(k3, iv3, enc_k2)
            print("K2 : " + k2)

            # Receive CBC Encrypted IV and decrypt it
            data = client_socket.recv(1024)
            enc_iv2 = pickle.loads(data)
            iv2 = fake_cbc_decryption(k3, iv3, enc_iv2)
            print("IV2 : " + iv2)

            enc_message = fake_cbc_encryption(k2, iv2, "Client B is done")
            data = pickle.dumps(enc_message)
            client_socket.send(data)

            data = client_socket.recv(1024).decode()
            print(data)

            # Receive number of blocks
            data = client_socket.recv(1024)
            aux_length = str(data, 'utf8')
            length = int(aux_length)

            enc_message = []
            index = 0

            # Receive encrypted blocks
            while length > index:
                data = client_socket.recv(1024)
                enc_message.append(pickle.loads(data))
                index += 1

            # Decrypt blocks
            message = fake_cbc_decryption(k2, iv2, enc_message)
            print(message)

        elif data.upper() == "CFB":

            # Receive CFB Encrypted Key and decrypt it
            data = client_socket.recv(1024)
            enc_k2 = pickle.loads(data)
            k2 = fake_cfb_decryption(k3, iv3, enc_k2)
            print("K2 : " + k2)

            # Receive CFB Encrypted IV and decrypt it
            data = client_socket.recv(1024)
            enc_iv2 = pickle.loads(data)
            iv2 = fake_cfb_decryption(k3, iv3, enc_iv2)
            print("IV2 : " + iv2)

            enc_message = fake_cfb_encryption(k2, iv2, "Client B is done")
            data = pickle.dumps(enc_message)
            client_socket.send(data)

            data = client_socket.recv(1024).decode()
            print(data)

            # Receive number of blocks
            data = client_socket.recv(1024)
            aux_length = str(data, 'utf8')
            length = int(aux_length)

            enc_message = []
            index = 0

            # Receive encrypted blocks
            while length > index:
                data = client_socket.recv(1024)
                enc_message.append(pickle.loads(data))
                index += 1

            # Decrypt blocks
            message = fake_cbc_decryption(k2, iv2, enc_message)
            print(message)

        message = input()

    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
