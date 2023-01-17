from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
            shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            char_index = alphabet.index(char)
            new_index = (char_index + shift_amount) % len(alphabet)
            end_text += alphabet[new_index]
        else:
            end_text+= char
    print(f"The {cipher_direction}d text is {end_text}.")

repeat = "yes"
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    user_input = input('Type "yes" if you want to go again.').lower()
    if user_input != repeat:
        print("Thank you. Goodbye!")
        break