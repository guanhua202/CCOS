# ——————————————————— 🔐 Caesar Cipher on steroids
# ✅ Скрестить два кода для расширения функционала до расшифрования
# ✅ Шифровать цифры в сообщении
# o Посмотреть почему цифры в сообщении не расшифровываются

import string

msg = input("Message: ").split()
mode = input("Encode/Decode (1, 2): ")

en_up = [letter for letter in string.ascii_uppercase]
en_lower = [letter for letter in string.ascii_lowercase]

digits = [digit for digit in string.digits]

def find_next_letter(letter, len_word, letters, mode):
	if mode == '1':
		index = letters.index(letter) + len_word
		
		if index >= len(letters):
			while index >= len(letters):
				index -= len(letters)
			return letters[index]
		else:
			return letters[index]
		
	elif mode == '2':
		return letters[letters.index(letter) - len_word]

for i in range(0, len(msg)):
	
	len_word = 0

	new_msg = []
	new_msg.extend(msg[i])

	for letter in new_msg:
		if letter.isalnum():
			len_word += 1

	for j in range(0, len(new_msg)):
		if new_msg[j].isupper():
			new_msg[j] = find_next_letter(new_msg[j], len_word, en_up, mode)
			
		elif new_msg[j].islower():
			new_msg[j] = find_next_letter(new_msg[j], len_word, en_lower, mode)
			
		elif new_msg[j].isdigit():
			new_msg[j] = find_next_letter(new_msg[j], len_word, digits, mode)

	msg[i] = ''.join(new_msg)

print(*msg)