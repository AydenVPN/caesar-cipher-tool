FIRST_CHAR_CODE = ord("A") 
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1


def caesar_shift(message, shift):
# Go through each of the letters in the message.
    
    
    result = ""
    for char in message.upper():
        if char.isalpha():
            
            # Convert character to the ASCII code.
            char_code = ord(char) # <--- Characters ASCII code.
            new_char_code = (char_code + shift)
            if(new_char_code > LAST_CHAR_CODE):
                new_char_code -= CHAR_RANGE

            if new_char_code < FIRST_CHAR_CODE:
                new_char_code += CHAR_RANGE

            new_char = chr(new_char_code)
            result += new_char
        else:
            result += char

    return result

outc = ""
user_decision = input("Would you like to encrypt or decrypt a message? E/D:  ")
if user_decision.upper() == "E":
    user_message = input("Message to Encrypt:  ")
    user_shift_key = int(input("Shift key (Integer):  "))
    outc = (caesar_shift(user_message, user_shift_key))
    print(outc)
    
if user_decision.upper() == "D":
    user_message = input("Message to Decrypt:  ")
    user_shift_key = int(input("Shift key (Integer):  "))
    outc = (caesar_shift(user_message, user_shift_key))
    print(outc)
    
if user_decision.upper() != "E" and user_decision.upper() != "D":
    print("Invalid input. Please enter E for encrypt or D for decrypt.")
