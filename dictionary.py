dictionary = {"Voiture":"Car", "Maison":"House", "Ordinateur":"Computer", "Moniteur":"Monitor", "Clavier":"Keyboard"}

def new_word():
    new_key = input("Insert a new word to the dictionary: ")
    new_value = input("Insert It's translation: ")

    for i in dictionary.keys():
        if (i == new_key):
            return "The word is already in the dictionary!"

    dictionary.update({str(new_key): str(new_value)})
    return dictionary

def all_translations():
    for i in dictionary.values():
        print(i)

def remove(c, d):
    death_list = []
    for i in d.keys():
        if (i.startswith(c)):
            death_list.append(i)
    
    for i in death_list:
        d.pop(i)

print(dictionary)

remove("V", dictionary)

print(dictionary)