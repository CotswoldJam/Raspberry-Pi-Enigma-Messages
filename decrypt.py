from enigma.machine import EnigmaMachine

chosen_rotors = ''    # Type a space between each rotor e.g. V IV I
rotor_start = ''
message_key = ''
plaintext = ''   # The message you want to decrypt

print("You started with message key " + message_key + " and plaintext " + plaintext)

# Set up the Enigma machine
machine = EnigmaMachine.from_key_sheet(
   rotors=chosen_rotors,
   reflector='B',
   ring_settings='20 5 10',
   plugboard_settings='SX KU QP VN JG TC LA WM OB ZF')

# Set the initial position of the Enigma rotors
machine.set_display(rotor_start)

# Decrypt the message key
decrypted_message_key = machine.process_text(message_key)
print("The decrypted message key is " + decrypted_message_key)

# Set the rotor start position to the DECRYPTED message key
machine.set_display(decrypted_message_key)

# The result
ciphertext = machine.process_text(plaintext)

print("The cipher text is: " + ciphertext)
