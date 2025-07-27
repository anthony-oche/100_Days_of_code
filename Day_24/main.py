#TODO: Create a letter using starting_letter.txt
with open("Input/Letters/starting_letter.txt") as letter:
    content_letter = letter.read()

#for each name in invited_names.txt
with open("Input/Names/invited_names.txt") as names:
    content_name = names.readlines()


#Replace the [name] placeholder with the actual name.
mail_list = []
for num in range(len(content_name)):
    new_letter = content_letter.replace("[name]", content_name[num].strip())
    mail_list.append(new_letter)


#Save the letters in the folder "ReadyToSend".
for num in range(len(content_name)):
    with open(f"Output/ReadyToSend/{content_name[num].strip()}_letter.txt", mode="w") as content:
        content.write(mail_list[num])
