sent_message = 'Hey there! This is a secret message.'
unsent_message = 'This message has been unsent.'

with open('sent_message.txt','w') as file:
    file.write(sent_message)

with open('sent_message.txt', 'r+') as file:
    original_message = file.read()
    print("original message:", original_message)
    file.seek(0)
    file.write(unsent_message)
    file.truncate(len(unsent_message))
    file.seek(0)
    new_message = file.read()
    print('new message:', new_message)
