import os
import subprocess
from dotenv import load_dotenv
from Authentication.database_connection import DatabaseConnection
from Authentication.userService import UserService
from Authentication import authentification
from EncrpyptionDecryption import encode_decode, crypt_asym, crypt_sym
from Hash import crackhash, hash
import threading

load_dotenv(".env")


def start_server():
    subprocess.call('python chatroom/server.py 9999', creationflags=subprocess.CREATE_NEW_CONSOLE)


def start_client():
    subprocess.call('python chatroom/client.py 9999', creationflags=subprocess.CREATE_NEW_CONSOLE)


def encode():
    message = input(" Enter your message ")
    encode_decode.encode(message)


def decode():
    message = input(" Enter your message ")
    encode_decode.decode(message)


def aes():
    choice = int(input("1. Encryption \n" "2. Decryption \n"))
    if choice == 1:
        crypt_sym.aes256_crypt()
    if choice == 2:
        crypt_sym.aes256_decrypt()


def des():
    choice_crypt = int(input("1. Encryption \n" "2. Decryption \n"))
    if choice_crypt == 1:
        crypt_sym.des_crypt()
    if choice_crypt == 2:
        crypt_sym.des_decrypt()


def rsa():
    choice_crypt = int(input("1. Encryption \n" "2. Decryption \n"))
    if choice_crypt == 1:
        crypt_asym.encrypt_rsa()
    if choice_crypt == 2:
        crypt_asym.decrypt_rsa()


def gamal():
    choice_crypt = int(input("1. Encryption \n" "2. Decryption \n"))
    if choice_crypt == 1:
        crypt_asym.encrypt_elgamal()
    if choice_crypt == 2:
        crypt_asym.decrypt_elgamal()


def chat():
    print("--------------------------------------------------------------------\n"
          "------------------------------CHATROOM------------------------------\n"
          "--------------------------------------------------------------------")

    number = int(input("Give the number of users : \n"))
    t = []
    t1 = threading.Thread(target=start_server)
    t1.start()
    for i in range(number):
        t.append(threading.Thread(target=start_client))
        t[i].start()


if __name__ == "__main__":
    choice = None
    DB_HOSTNAME: str = os.environ.get("DB_HOSTNAME")
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD")
    DB_DATABASE: str = os.environ.get("DB_DATABASE")
    conn = DatabaseConnection(
        DB_HOSTNAME,
        DB_USER,
        DB_PASSWORD,
        DB_DATABASE,
    )
    userService = UserService(conn)
    while choice != 4:
        choice = int(
            input(
                "Tap your choice: \n"
                "1. Sign up.\n"
                "2. Login.\n"
                "3. Menu.\n"
                "4. Exit.\n"
            )
        )

        if choice == 1:
            authentification.sign_up(userService=userService)
        elif choice == 2:
            login_choice = None
            while login_choice != 1 and login_choice != 2:
                login_choice = int(input(
                    "Tap your choice: \n"
                    "1. 2-Factor Authentication \n"
                    "2. Kerberos \n"
                ))
                if login_choice == 1:
                    authentification.twoFactor(userService=userService)
                if login_choice == 2:
                    authentification.twoFactor(userService=userService)
                else:
                    print("Wrong choice! try again")


        elif choice == 3:
            choice_menu = int(input(
                "Tap your choice: \n"
                "1. Encoding and decoding\n"
                "   1- Encoding \n"
                "   2- Decoding \n"
                "2. Hash \n"
                "   1- MD5 \n"
                "   2- SHA1 \n"
                "   3- SHA256 \n"
                "3. Crack \n"
                "   1- MD5 \n"
                "   2- SHA1 \n"
                "   3- SHA256 \n"
                "4. Symmetric Encryption \n"
                "   1- DES \n"
                "   2- AES256 \n"
                "5. Asymmetric Encryption \n"
                "   1- RSA \n"
                "   2- elgamal \n"
                "6. Chatroom\n"
                "7. EXIT \n"
            ))

            switcher = {
                11: encode,
                12: decode,
                21: hash.md5,
                22: hash.sha1,
                23: hash.sha256,
                31: crackhash.md5,
                32: crackhash.sha1,
                33: crackhash.sha256,
                41: des,
                42: aes,
                51: rsa,
                52: gamal,
                6: chat,

            }
            switcher.get(choice_menu, lambda: "Invalid choice")()

        elif choice == 4:
            exit()
