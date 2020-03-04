def encrypt(message, key):
    message.upper()
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    crypted = []
    msg = ""
    translator = message.upper()
    for i in range(len(translator)):        
        if translator[i] in alphabet:
            value = alphabet.index(translator[i])
            if(value+key <= 25):
                crypted.append(alphabet[value+key])
            else:
                numb = ((value+key)-26)
                crypted.append(alphabet[(-26+numb)])
        else:
            crypted.append(translator[i])    
    msg =  ''.join(crypted)  
    return msg.lower()

def decrypt(message, key):
    message.upper()
    alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    crypted = []
    msg = ""
    translator = message.upper()
    for i in range(len(translator)):        
        if translator[i] in alphabet:
            value = alphabet.index(translator[i])
            if(value-key >= 0):
                crypted.append(alphabet[value-key])
            else:
                numb = (value-key)
                crypted.append(alphabet[numb])
        else:
            crypted.append(translator[i])    
    msg =  ''.join(crypted)  
    return msg.lower()

running = True

while(running):
    print("Would you like to encrypt(1) or decrypt(2) or exit(3)?")
    choice = input("Enter choice: ")

    if(choice == "1" or choice == "2" or choice == "3"):
        if(choice == "1"):
            message = str(input("Type your encryption message: "))
            key = int(input("Type your key: "))
            print(encrypt(message,key),"\n")

        if(choice == "2"):
            message = str(input("Type your decryption message: "))
            key = int(input("Type your key: "))
            print(decrypt(message,key),"\n")
        
        if(choice == "3"):
            running = False
    else:
        print("\nInvalid input\n")