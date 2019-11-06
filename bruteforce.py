cribtext = ""
ciphertext = ""

# All possible combinations of rotors
rotors = [ "I II III", "I II IV", "I II V", "I III II",
"I III IV", "I III V", "I IV II", "I IV III",
"I IV V", "I V II", "I V III", "I V IV",
"II I III", "II I IV", "II I V", "II III I",
"II III IV", "II III V", "II IV I", "II IV III",
"II IV V", "II V I", "II V III", "II V IV",
"III I II", "III I IV", "III I V", "III II I",
"III II IV", "III II V", "III IV I", "III IV II",
"III IV V", "IV I II", "IV I III", "IV I V",
"IV II I", "IV II III", "IV I V", "IV II I",
"IV II III", "IV II V", "IV III I", "IV III II",
"IV III V", "IV V I", "IV V II", "IV V III",
"V I II", "V I III", "V I IV", "V II I",
"V II III", "V II IV", "V III I", "V III II",
"V III IV", "V IV I", "V IV II", "V IV III" ]

def find_rotor_start( rotor_choice, ciphertext, cribtext ):

    from enigma.machine import EnigmaMachine

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    machine = EnigmaMachine.from_key_sheet(
       rotors=rotor_choice,
       reflector='B',
       ring_settings='21 15 16',					
       plugboard_settings='KL IT PQ MY XC NF VZ JB SH OG')	


    # Search over all possible rotor starting positions
    for i in range(len(alphabet)):            # search for rotor 1 start position
        for j in range(len(alphabet)):        # search for rotor 2 start position
            for k in range(len(alphabet)):    # search for rotor 3 start position

                # Generate a possible rotor start position
                start_pos = alphabet[i] + alphabet[j] + alphabet[k]

                # Set machine initial starting position and attempt to decrypt
                machine.set_display(start_pos)
                plaintext = machine.process_text(ciphertext)

                #print("Plain: " + plaintext + ", Crib: " + cribtext)

                # Check if decrypted text is the same as the crib text
                if (plaintext == cribtext):
                    return( rotor_choice, start_pos )

    return( rotor_choice, "null" )



print("Brute force crypt attack on Enigma message " + ciphertext)
print("Crib text " + cribtext )

# Try all rotor settings 
for rotor_setting in rotors:
    print("Trying rotors " + rotor_setting)
    rotor_choice, start_pos = find_rotor_start( rotor_setting, ciphertext, cribtext )
    if (start_pos != "null"):
        print("Machine setting found!")
        print("Rotors: " + rotor_choice)
        print("Message key: " + start_pos)
        print("Using crib " + cribtext)
        exit(0)






        
