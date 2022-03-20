target_word = "PARTY"

used_word = "START"

user_word = "STARY"
correct_positions = "000T0"
new_correct_positions = ""
for uw_index, uw_char in enumerate(user_word):
    if uw_char in target_word:
        pass
    if uw_char == target_word[uw_index] and correct_positions[uw_index] == "0":
        new_correct_positions += uw_char
    else:
        new_correct_positions += correct_positions[uw_index]

correct_positions = new_correct_positions

print(correct_positions)
