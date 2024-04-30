print ("                                                                       ")
print ("                                                                       ")
print ("            #####################################################" )       
print ("            #                                                   #" )        
print ("            #                   Caesar Cipher tool              #" ) 
print ("            #                                                   #" )                          
print ("            #                   Cryptography Tool               #" )        
print ("            #                                                   #" )            
print ("            #                                                   #" )       
print ("            #                Author : Raghul Kannan A         #" )       
print ("            #                                                   #" )       
print ("            #####################################################" )       

print("                                                                   ")


print("                                           ")

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - ord('a' if char.islower() else 'A') - shift) % 26 + ord('a' if char.islower() else 'A'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (encrypt/decrypt): ").lower()
        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")
            continue
        text = input("Enter the text: ")
        shift = int(input("Enter the shift value: "))
        if choice == 'encrypt':
            encrypted_text = encrypt(text, shift)
            print("Encrypted text:", encrypted_text)
        else:
            decrypted_text = decrypt(text, shift)
            print("Decrypted text:", decrypted_text)

        another = input("Do you want to perform another operation? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
