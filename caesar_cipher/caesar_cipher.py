alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
len_alphabet = len(alphabet)

def cipher(text, shift, operation):
  final_text = ""
  
  for one_letter in text:
    if one_letter != " ":
      text_index = alphabet.index(one_letter)
      if operation == "encode":
        new_index = text_index + shift
        if new_index > len_alphabet:
          final_text += alphabet[new_index - len_alphabet]
        else:
          final_text += alphabet[new_index]
      
      elif operation == "decode":
        new_index = text_index - shift
        final_text += alphabet[new_index] 

      else:
        print("Wrong operation")
        again
    else:
      final_text += one_letter
  
  print(final_text)

again = True
while again:

  operation_input = input("Type 'encode' to encrypt or 'decode' for decrypt the message: ").lower()
  text_input = input("Type your message: ").lower()
  shift_input = int(input("Type the shift number: "))

  cipher(text_input, shift_input, operation_input)

  continue_input = input("Type 'yes' to go again, otherwise 'no': ")
  
  if continue_input == "no":
    again = False
    quit()
