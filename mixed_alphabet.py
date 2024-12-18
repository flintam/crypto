class MixedAlphabet:
    encrypt_dict = {}
    decrypt_dict = {}
    def __init__(self, key: str):
        self.key = self.process_key(key)
        print('MixedAlphabet [{}] inited: {}'.format(self.key, key))
        ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alphabet = ALPHABET.lower()
        P_LIST = list(ALPHABET)
        p_list = list(alphabet)
        C_LIST = P_LIST.copy()
        c_list = p_list.copy()
        keyListRev = list(self.key)
        keyListRev.reverse()
        for each in keyListRev:
            C_LIST.remove(each)
            C_LIST.insert(0, each)
            c_list.remove(each.lower())
            c_list.insert(0, each.lower())
        for i in range(len(P_LIST)):
            self.encrypt_dict[P_LIST[i]] = C_LIST[i]
            self.encrypt_dict[p_list[i]] = c_list[i]
            self.decrypt_dict[C_LIST[i]] = P_LIST[i]
            self.decrypt_dict[c_list[i]] = p_list[i]

    def process_key(self, string):
        string = string.upper().replace(" ", "")
        return "".join(dict.fromkeys(string))

    def encrypt(self, text):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                encrypted_text += self.encrypt_dict[char]
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, text):
        decrypted_text = ""
        for char in text:
            if char.isalpha():
                decrypted_text += self.decrypt_dict[char]
            else:
                decrypted_text += char
        return decrypted_text

def main():
    instance = None
    while True:
        print("\nMenu:")
        if (instance == None):
            print("0. Init")
        else:
            print("1. Encrypt")
            print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '0' and instance == None:
            text = input("Enter secret key: ")
            instance = MixedAlphabet(text)
        elif choice == '1' and instance != None:
            text = input("Enter text to encrypt: ")
            print("--> :", instance.encrypt(text))
        elif choice == '2' and instance != None:
            text = input("Enter text to decrypt: ")
            print("==> :", instance.decrypt(text))
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
