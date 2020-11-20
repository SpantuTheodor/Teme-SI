import socket
import time
from Crypto.Cipher import AES
from fake_encryption import fake_cbc_encryption, fake_cfb_encryption, generate_random
from fake_decryprion import fake_cbc_decryption, fake_cfb_decryption
import pickle

k1 = "8765345687653456"
k2 = "4742397547423975"
k3 = "1234564212345642"

iv1 = generate_random()
iv2 = generate_random()
iv3 = "4560987652646442"

print("K1: ", k1)
print("K2: ", k2)
print("IV1: ", iv1)
print("IV2: ", iv2)


def server_program():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 50000))
    server_socket.listen(2)
    conn_a, address = server_socket.accept()
    conn_b, address = server_socket.accept()

    while True:

        data = conn_a.recv(1024).decode()
        print("from connected user: " + str(data))
        if data.upper() == "CBC":

            conn_a.send("CBC".encode("utf-8"))

            # Send CBC Encrypted Key to client A
            enc_k1 = fake_cbc_encryption(k3, iv3, k1)
            data = pickle.dumps(enc_k1)
            conn_a.send(data)

            # Send CBC Encrypted IV to client A
            enc_iv1 = fake_cbc_encryption(k3, iv3, iv1)
            data = pickle.dumps(enc_iv1)
            conn_a.send(data)

            conn_b.send("CFB".encode())

            data = conn_b.recv(1024).decode()
            print("from connected user: " + str(data))

            # Send CFB Encrypted Key to client B
            enc_k2 = fake_cfb_encryption(k3, iv3, k2)
            data = pickle.dumps(enc_k2)
            conn_b.send(data)

            # Send CFB Encrypted IV to client B
            enc_iv2 = fake_cfb_encryption(k3, iv3, iv2)
            data = pickle.dumps(enc_iv2)
            conn_b.send(data)

            # Receive CBC Encrypted Message and decrypt it
            data = conn_a.recv(1024)
            enc_message = pickle.loads(data)
            message = fake_cbc_decryption(k1, iv1, enc_message)
            print(message)

            # Receive CBC Encrypted Message and decrypt it
            data = conn_b.recv(1024)
            enc_message = pickle.loads(data)
            message = fake_cfb_decryption(k2, iv2, enc_message)
            print(message)

            conn_a.send("Starting the communication with Client B".encode())
            conn_b.send("Starting the communication with Client A".encode())

            # Receive number of blocks
            data = conn_a.recv(1024)
            aux_length = str(data, 'utf8')
            length = int(aux_length)

            enc_message = []
            index = 0

            # Receive encrypted blocks
            while length > index:

                data = conn_a.recv(1024)
                enc_message.append(pickle.loads(data))
                index += 1

            # Decrypt blocks
            message = fake_cbc_decryption(k1, iv1, enc_message)
            print(message)

            # Encrypt and send length
            enc_message = fake_cbc_encryption(k2, iv2, message)
            length = len(enc_message)
            conn_b.send(bytes(str(length), 'utf8'))

            index = 0

            while length > index:
                data = pickle.dumps(enc_message[index])
                conn_b.send(data)
                index += 1
                time.sleep(.1)

        elif data.upper() == "CFB":
            conn_a.send("CFB".encode("utf-8"))

            # Send CFB Encrypted Key to client A
            enc_k1 = fake_cfb_encryption(k3, iv3, k1)
            data = pickle.dumps(enc_k1)
            conn_a.send(data)

            # Send CFB Encrypted IV to client A
            enc_iv1 = fake_cfb_encryption(k3, iv3, iv1)
            data = pickle.dumps(enc_iv1)
            conn_a.send(data)

            conn_b.send("CBC".encode())

            data = conn_b.recv(1024).decode()
            print("from connected user: " + str(data))

            # Send CBC Encrypted Key to client B
            enc_k2 = fake_cbc_encryption(k3, iv3, k2)
            data = pickle.dumps(enc_k2)
            conn_b.send(data)

            # Send CBC Encrypted IV to client B
            enc_iv2 = fake_cbc_encryption(k3, iv3, iv2)
            data = pickle.dumps(enc_iv2)
            conn_b.send(data)

            # Receive CFB Encrypted Message and decrypt it
            data = conn_a.recv(1024)
            enc_message = pickle.loads(data)
            message = fake_cfb_decryption(k1, iv1, enc_message)
            print(message)

            # Receive CBC Encrypted Message and decrypt it
            data = conn_b.recv(1024)
            enc_message = pickle.loads(data)
            message = fake_cbc_decryption(k2, iv2, enc_message)
            print(message)

            conn_a.send("Starting the communication with Client B".encode())
            conn_b.send("Starting the communication with Client A".encode())

            # Receive number of blocks
            data = conn_a.recv(1024)
            aux_length = str(data, 'utf8')
            length = int(aux_length)

            enc_message = []
            index = 0

            # Receive encrypted blocks
            while length > index:

                data = conn_a.recv(1024)
                enc_message.append(pickle.loads(data))
                index += 1

            # Decrypt blocks
            message = fake_cfb_decryption(k1, iv1, enc_message)
            print(message)

            # Encrypt and send length
            enc_message = fake_cbc_encryption(k2, iv2, message)
            length = len(enc_message)
            conn_b.send(bytes(str(length), 'utf8'))

            index = 0

            while length > index:
                data = pickle.dumps(enc_message[index])
                conn_b.send(data)
                index += 1
                time.sleep(.1)

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
