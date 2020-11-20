import time
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

    message = input(" Choose between CBC and CFB  -> ")

    while True:

        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)

        if data.upper() == "CBC":

            # Receive CBC Encrypted Key and decrypt it
            data = client_socket.recv(1024)
            enc_k1 = pickle.loads(data)
            k1 = fake_cbc_decryption(k3, iv3, enc_k1)
            print("K1 : " + k1)

            # Receive CBC Encrypted IV and decrypt it
            data = client_socket.recv(1024)
            enc_iv1 = pickle.loads(data)
            iv1 = fake_cbc_decryption(k3, iv3, enc_iv1)
            print("IV1 : " + iv1)

            enc_message = fake_cbc_encryption(k1, iv1, "Client A is done")
            data = pickle.dumps(enc_message)
            client_socket.send(data)

            data = client_socket.recv(1024).decode()
            print(data)

            message = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.     "

            # Encrypt and send length
            enc_message = fake_cbc_encryption(k1,iv1,message)
            length = len(enc_message)
            client_socket.send(bytes(str(length), 'utf8'))

            # Send Encrypted Blocks
            index = 0
            while len(enc_message) > index:

                data = pickle.dumps(enc_message[index])
                client_socket.send(data)
                index += 1
                time.sleep(.1)


        elif data.upper() == "CFB":

            # Receive CFB Encrypted Key and decrypt it
            data = client_socket.recv(1024)
            enc_k1 = pickle.loads(data)
            k1 = fake_cfb_decryption(k3, iv3, enc_k1)
            print("K1 : " + k1)

            # Receive CFB Encrypted IV and decrypt it
            data = client_socket.recv(1024)
            enc_iv1 = pickle.loads(data)
            iv1 = fake_cfb_decryption(k3, iv3, enc_iv1)
            print("IV1 : " + iv1)

            enc_message = fake_cfb_encryption(k1, iv1, "Client A is done")
            data = pickle.dumps(enc_message)
            client_socket.send(data)

            data = client_socket.recv(1024).decode()
            print(data)

            message = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s.     "


            # Encrypt and send length
            enc_message = fake_cfb_encryption(k1, iv1, message)
            length = len(enc_message)
            client_socket.send(bytes(str(length), 'utf8'))

            # Send Encrypted Blocks
            index = 0
            while len(enc_message) > index:
                data = pickle.dumps(enc_message[index])
                client_socket.send(data)
                index += 1
                time.sleep(.1)

        message = input()

    client_socket.close()


if __name__ == '__main__':
    client_program()
