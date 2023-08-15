from caesarcipher import CaesarCipher

message = input("Enter the message you want to process: ")
offset = int(input("Enter the desired offset: "))
action = input("Enter 'E' to encrypt or 'D' to decrypt: ")

if action == 'E':
    cipher = CaesarCipher(message, offset=offset)
    processed_message = cipher.encoded
elif action == 'D':
    cipher = CaesarCipher(message, offset=-offset)
    processed_message = cipher.decoded
else:
    print("Invalid action. Please enter 'E' to encrypt or 'D' to decrypt.")
    exit()

print("Processed message:", processed_message)
