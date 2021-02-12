PLACEHOLDER = "[name]"


with open("Input/Names/invited_names.txt") as starting_names_file:
    names = starting_names_file.read().splitlines()
with open("Input/Letters/starting_letter.txt") as starting_letter_file:
    starting_letter = starting_letter_file.read()


for name in names:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as create_file:
        letter = starting_letter.replace(PLACEHOLDER, name)
        create_file.write(letter)
