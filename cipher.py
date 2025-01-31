def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr(start + (ord(char) - start + shift) % 26)
        else:
            result += char
    
    return result

if __name__ == "__main__":
    while True:
        mode = input("Do you want to encrypt or decrypt? (Type 'exit' to quit): ").strip().lower()
        if mode == 'exit':
            break
        elif mode not in ['encrypt', 'decrypt']:
            print("Invalid option. Please choose 'encrypt' or 'decrypt'.")
            continue
        
        text = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        
        result = caesar_cipher(text, shift, mode)
        print(f"Result: {result}\n")
