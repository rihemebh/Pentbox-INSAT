import os
import subprocess
from dotenv import load_dotenv
from Authentication.database_connection import DatabaseConnection
from Authentication.userService import UserService
from Authentication import authentification
from Encryption import encode_decode
from Hash import hash
from Encryption import crypt_sym
from Encryption import crypt_asym
from Hash import crackhash
import threading

load_dotenv(".env")


def start_server():
    subprocess.call('python chatroom/server.py 9999', creationflags=subprocess.CREATE_NEW_CONSOLE)

def start_client():
    subprocess.call('python chatroom/client.py 9999', creationflags=subprocess.CREATE_NEW_CONSOLE)


if __name__ == "__main__":
    choice = None
    DB_HOSTNAME: str = os.environ.get("DB_HOSTNAME")
    DB_USER: str = os.environ.get("DB_USER")
    DB_PASSWORD: str = os.environ.get("DB_PASSWORD")
    DB_DATABASE: str = os.environ.get("DB_DATABASE")
    conn = DatabaseConnection(
        hostname=DB_HOSTNAME,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE,
    )
    userService = UserService(databaseConnection=conn)
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
            authentification.login(userService=userService)
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
                "5. Asymmectric Encryption \n"
                "   1- RSA \n"
                "   2- elgamal \n"
                "6. Chatroom\n"
                "7. Quitter \n"
            ))
            
             if choice_menu == 11:
                 message = input(" entrer votre message ")
                 encode_decode.encode(message)
             if choice_menu == 12:
                 message = input(" entrer votre message ")
                 encode_decode.decode(message)
             if choice_menu == 21:
                 hash.md5()
             if choice_menu == 22:
                 hash.sha1()
             if choice_menu == 23:
                 hash.sha256()
             if choice_menu == 31:
                 crackhash.md5()
             if choice_menu == 32:
                 crackhash.sha1()
             if choice_menu == 33:
                 crackhash.sha256()
             if choice_menu == 41:
                 choice_crypt = int(input("1. Encryption \n" "2. Decryption \n"))
                 if choice_crypt == 1:
                     crypt.des_crypt()
                 if choice_crypt == 2:
                     crypt.des_decrypt()
             if choice_menu == 42:
                 choice_crypt = int(input("1. Encryption \n" "2. Decryption \n"))
                 if choice_crypt == 1:
                     crypt.aes256_crypt()
                 if choice_crypt == 2:
                     crypt.aes256_decrypt()
             if choice_menu == 51:
                 choice_crypt = int(input("1. Encryption \n" "2. Decryption \n"))
                 if choice_crypt == 1:
                     crypt_asym.encrypt_rsa()
                 if choice_crypt == 2:
                     crypt_asym.decrypt_rsa()
             if choice_menu == 52:
                 choice_crypt = int(input("1. Encryption \n" "2. Decryption \n"))
                 if choice_crypt == 1:
                     crypt_asym.encrypt_elgamal()
                 if choice_crypt == 2:
                     crypt_asym.decrypt_elgamal()
            if choice_menu == 6:
                print("------------------------------CHATROOM------------------------------")
                number = int(input("Give the number of users : \n"))
                t = []
                t1 = threading.Thread(target=start_server)
                t1.start()
                for i in range(number):
                    t.append(threading.Thread(target=start_client))
                    t[i].start()

        elif choice == 4:
            exit()
