
# # find_in_list function defined here but not called
# def find_in_list(query, mainlist):
# # this function is used to find the position of the "query" in the "mainlist". If "query" is in the list then it returns its position, otherwise it returns None
#     mainlist_len = len(mainlist)
#     range_for_loop = range(mainlist_len)
#     index = None
#     for i in range_for_loop:
#         element = mainlist[i]
#         if element == query:
#             index = i
#     return index
# # this should return the position of the "query" in the "mainlist"


# chars =         ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# shifted_chars = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']

# # encrypt_message function defined here but not called
# def encrypt_message(plain_msg):
# # this fucnction takes "plain_msg" as an argument and print/return the encrypted message. The "plain_msg" is tranfered into "encrypted_msg" using "shifted_chars" list. Example, if plain_msg = "ng" then n => p, g => i  and hence encrypted_msg = "pi"
#     encrypted_msg = ""
#     for character in plain_msg:
#       # for character in msg
#         if character in chars:
#             char_index = find_in_list(character, chars)
#             new_char = shifted_chars[char_index]
#             encrypted_msg = encrypted_msg + new_char
#         else:
#             encrypted_msg = encrypted_msg + character
#     return encrypted_msg


# # decrypt_message function defined here but not called
# def decrypt_message(encrypted_msg):
# # this fucnction takes "encrypted_msg" as an argument and print/return the encrypted message. The "encrypted_msg" is tranfered into "decrypted_msg" using "shifted_chars" list. Example, if encrypted_msg = "pi" then p => n, i => g  and hence decrypted_msg = "ng"
#     decrypted_msg = ""
#     for character in encrypted_msg:
#         if character in shifted_chars:
#             char_index = find_in_list(character, shifted_chars)
#             new_char = chars[char_index]
#             decrypted_msg = decrypted_msg + new_char
#         else:
#             decrypted_msg = decrypted_msg + character
#     return decrypted_msg


# # methods should return or print the new messages.
# ############################################### Code starts from here ##################################################
# flag = True
# while flag == True:
#     choice = raw_input("What do you want to do? 1. Encrypt a message 2. Decrypt a message  Enter `e` or `d` respectively!")
#     if choice == 'e':
#         plain_message = raw_input("Enter message to encrypt??")
#         print encrypt_message(plain_message)
#     elif choice == 'd':
#         encrypted_msg = raw_input("Enter message to decrypt?")
#         print decrypt_message(encrypted_msg)
    
#     play_again = raw_input("Do you want to try agian or Do you want to exit? (Y/N)")
#     if play_again == 'Y':
#         continue
#     elif play_again == 'N':
#         break




#cipher.2#


def encrypt():
  message = raw_input("Enter the message you want to encrypt")
  ascii_message = [ord(char)+3 for char in message]
  encrypt_message = [ chr(char) for char in ascii_message]  
  print ''.join(encrypt_message)


def decrypt():
  message = raw_input("Enter the message you want to decrypt")
  ascii_message = [ord(char) for char in message]
  decrypt_message = [ chr(char) for char in ascii_message]  
  print ''.join(decrypt_message)

flag = True
while flag == True:
    choice = raw_input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter 'e' or 'd' respectively!")
    if choice =='e':
        print encrypt()
    elif choice == 'd':
        print decrypt()    

    play_again = raw_input("Do you want to try agian or Do you want to exit? (Y/N)")
    if play_again == 'Y':
        continue
    elif play_again == 'N':
        break