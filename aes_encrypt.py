alphabet = "abcdefghijklmnopqrstuvwxyz"
def encrypt():
    newMessage = ''

    message = raw_input('Please enter a message: ')
    key = raw_input('Enter key: ')

    for character in message:
            position = alphabet.find(character)
            newPosition = (position + int(key)) % 26
            newCharacter = alphabet[newPosition]
            # print 'The new character is: ', newCharacter
            newMessage += newCharacter

    print 'Your message is: ', newMessage

def decrypt():
    decrypt_message = raw_input('What is the message')
    decrypt_key = raw_input('What is the key')

    for character in decrypt_message:

        position = alphabet.find(character)
        newPosition = (position + int(key)) % 26
        newCharacter = alphabet[newPosition]
        # print 'The new character is: ', newCharacter
        newMessage += newCharacter


encrypt()
