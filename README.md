# PRODIGY_CS_01
Implementing Caesar Cipher
Imagine you have a secret message that you want to send to your friend, but you don't want anyone else to understand it if they happen to see it. The Caesar Cipher is a simple way to encrypt your message so that only you and your friend can understand it.

Here's how it works:

Encryption: When you want to send a secret message, you take each letter of your message and shift it a certain number of positions down the alphabet. For example, if you choose a shift of 3, the letter 'A' becomes 'D', 'B' becomes 'E', and so on. If you reach the end of the alphabet, you wrap around to the beginning. So, 'X' becomes 'A', 'Y' becomes 'B', and 'Z' becomes 'C'.
Decryption: When your friend receives the encrypted message, they need to decrypt it to read the original message. To do this, they simply shift each letter in the encrypted message back by the same number of positions you used for encryption. So, if you used a shift of 3 to encrypt, they would shift each letter in the encrypted message back by 3 positions to reveal the original message.
Now, let's look at the code:

The encrypt function takes a text and a shift value as input. It goes through each character in the text. If the character is a letter, it shifts it down the alphabet by the specified shift value. If it's not a letter (like a number or a punctuation mark), it leaves it unchanged. Finally, it returns the encrypted text.
The decrypt function does the opposite of encryption. It takes the encrypted text and shifts each letter back up the alphabet by the same shift value to reveal the original message.
The main function is where the magic happens. It asks the user whether they want to encrypt or decrypt a message, takes the input text, and the shift value. Then it either encrypts or decrypts the text based on the user's choice and prints the result.
It also asks if the user wants to perform another operation. If they say no, the program ends.
So, with this code, you can encrypt your secret messages using the Caesar Cipher and share them securely with your friends!
