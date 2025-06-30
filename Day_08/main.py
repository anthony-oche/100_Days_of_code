import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(art.logo)

# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# def encrypt(original_text, shift_amount):
#     # Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#     #  by the shift amount and print the encrypted text.
#
#     """Takes the users text and shift number and encrypts the message"""
#     encoded_text = ""
#
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         #this ensures we are within the length of the alphabet
#         shifted_position %= len(alphabet)
#         encoded_text += alphabet[shifted_position]
#     print(f"Here is your encoded result: {encoded_text}")
#
# # Call the 'encrypt()' function and pass in the user inputs.
#encrypt(text, shift)
#
# # TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
# #  by the shift amount and print the decrypted text.
#
# def decrypt(original_text, shift_amount):
#     """Takes the users text and shift number and decrypts the message"""
#     decoded_text = ""
#
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         decoded_text += alphabet[shifted_position]
#     print(f"Here is your decoded result: {encoded_text}")
#
# decrypt(text, shift)

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caesar(original_text, shift_amount, encode_or_encode):
    """Takes the users text and shift number and encrypts the message"""

    output_text = ""

    if encode_or_encode == "decode":
        shift_amount *= -1

    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            # this ensures we are within the length of the alphabet
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is your {encode_or_encode}d result: {output_text}")



should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")

