# Шифр Цезаря на стероидах
# Логика работы: Каждое слово строки шифруется с помощью шифра Цезаря
# (циклического сдвига на длину этого слова)

# The_Caesar-Cipher_On-Steroids_CCOS
# Logic of operation: Each word of the string is encrypted using a Caesar cipher
# (cyclic shift by the length of this word)

word_en = str(input())
word_en = word_en.split()
mirror_list = []

en_alpha_up = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
en_alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(0, len(word_en)):
	# Счётчик букв в слове
  # Letter counter in a word
	count = 0

	# Создаём массив для обработки слова и добавляем туда слово
  # Create an array to process the word and add the word there
	mirror_list = []
	mirror_list.extend(word_en[i])

	# Обрабатываем слово (считаем буквы в массиве mirror_list)
  # Processing the word (counting letters in the mirror_list array)
	for letter in mirror_list:
		if letter.isalpha():
			count += 1

	for j in range(0, len(mirror_list)):
		if mirror_list[j].isupper():
			index = en_alpha_up.index(mirror_list[j])
			mirror_list[j] = en_alpha_up[index + count]
		elif mirror_list[j].islower():
			index = en_alpha_lower.index(mirror_list[j])
			mirror_list[j] = en_alpha_lower[index + count]

	''.join(mirror_list)
	# После добавляем в оригинальный массив
  # Then we add it to the original array
	word_en[i] = ''.join(mirror_list)

print(*word_en)
