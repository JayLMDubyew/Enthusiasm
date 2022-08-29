## JayLMDubyew (JLMW) - 2022
import random
import pprint
pp = pprint.PrettyPrinter(width=41, compact=True)

# useful for cesar, I guess
def rot(rotation_factor, message):
    ciphertext = ""
    for c in message:
        # rotate by rotation_factor
        if c.isupper():
            ciphertext += chr((ord(c) + rotation_factor - 65) % 26 + 65)
        else:
            ciphertext += chr((ord(c) + rotation_factor - 97) % 26 + 97)
    return ciphertext

#bruteforce rotation
def brute_rot(ciphertext):
    for i in range(26):
        print(f"Attempt {i+1} (Shift by {26-i}): {rot(i,ciphertext)}")


# monoalphabetic cipher
def monoalpha(message):
    alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    cipher = list(alphabet)
    random.shuffle(cipher)
    dictionary = dict(zip(list(alphabet), cipher))
    print("Your Cipher:")
    pp.pprint(dictionary)

    ciphertext=""
    for c in message:
        ciphertext += dictionary.get(c, c)
    print(ciphertext)

print(rot(4,"Hello"))
brute_rot("Lipps")

monoalpha("Let's go to the park")