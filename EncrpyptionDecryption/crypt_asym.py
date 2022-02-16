import rsa
from EncrpyptionDecryption import elgamal_algo

publicKeyRsa, privateKeyRsa = rsa.newkeys(512)
elgamal_keys = elgamal_algo.generate_keys()

publicKeyElGamal = elgamal_keys["publicKey"]
privateKeyElGamal = elgamal_keys["privateKey"]


def encrypt_rsa():
    message = input("Enter your Message (RSA encryption) : ")
    crypted_message: bytes = rsa.encrypt(message.encode(), publicKeyRsa)
    print(crypted_message.hex())


def decrypt_rsa():
    message = input("Enter your Message (RSA decryption): ")
    decrypted_message: bytes = rsa.decrypt(bytes.fromhex(message), privateKeyRsa)
    print(decrypted_message.decode("utf-8").strip())


def encrypt_elgamal():
    message = input("Enter your Message (Elgamal encryption)")
    encrypted_message = elgamal_algo.encrypt(publicKeyElGamal, message)
    print(encrypted_message)


def decrypt_elgamal():
    message = input("Enter your Message (Elgamal decryption)")
    decrypted_message = elgamal_algo.decrypt(privateKeyElGamal, message)
    print(decrypted_message)
