# User enter input
message = input('type any...')

# Greeting and print user input
print('Hello')
print('You entered: '+message)

# Demonstrate word retrieval and to lower or upper case using if else statement
length = len(message)-1
pointer = input('Enter any integer to retrieve the word in the message range (0 to '+str(length)+'): ')
print('Result: ' +message[int(pointer)])
if(message.isupper()):
    print('Result in Lower case: ' + message[int(pointer)].lower())
else:
    print('Result in Upper case: ' + message[int(pointer)].upper())

# Demonstrate contain function
searching_one = input('Enter any word to check words contain')
if searching_one in message:
    print('It exists')
else:
    print('Not found')

# Demonstrate changing
messageChanger = input('Enter new text for replacement')
new_message = message.replace(message,messageChanger)
print('New message is '+new_message)