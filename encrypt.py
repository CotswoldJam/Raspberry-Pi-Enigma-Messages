from enigma.machine import EnigmaMachine

chosen_rotors = ''    # Type a space between each rotor e.g. V IV I
rotor_start = ''
message_key = ''
plaintext = 'RASPBERRYPI'   # The message you want to encrypt

print("You started with message key " + message_key + " and plaintext " + plaintext)

# Set up the Enigma machine
machine = EnigmaMachine.from_key_sheet(
   rotors=chosen_rotors,
   reflector='B',
   ring_settings='20 5 10',
   plugboard_settings='SX KU QP VN JG TC LA WM OB ZF')

# Set the initial position of the Enigma rotors
machine.set_display(rotor_start)

# Encrypt the message key (the three letters you chose)
encrypted_message_key = machine.process_text(message_key)
print("The encrypted message key is " + encrypted_message_key)

# Set the rotor start position to the UNENCRYPTED message key
machine.set_display(message_key)

# The result
ciphertext = machine.process_text(plaintext)

print("The cipher text is: " + ciphertext)
