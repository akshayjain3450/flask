#F: Friendship L: Love A: Affair M: Marriage E: Enemy S: Sex

def input_details():
    name1 = input("Enter the first name:")
    name2 = input("Enter the second name:")
    name1 = name1.strip()
    name2 = name2.strip()
    name1 = name1.lower()
    name2 = name2.lower()
    final = name1 + name2
    return final

def remove_duplicates(parameter):
    sec_list = list()
    i = 1
    for character in parameter:
        if parameter[i:].find(character) == -1:
            sec_list.append(character)
        i = i + 1
    return sec_list

def flames(parameter1):
    word = "flames".split()
    while(True):
        if len(word) is not 1:
            index = parameter1 % len(word)
            if index == 0:
                word.pop(len(word)-1)
            else:
                word.pop(index-1)
        else:
            break
    if word == 'f':
        return "Friendship"
    if word == 'l':
        return "Love"
    if word == 'a':
        return "Affair"
    if word == 'm':
        return "Marriage"
    if word == 'e':
        return "Enemy"
    if word == 's':
        return "Sex"

final = input_details()
print(final)

letters = remove_duplicates(final)
print(letters)

count = len(letters)
print(count)

answer = flames(count)
print(answer)
