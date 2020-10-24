# Vragen om telefoonnummer en opslaan in de invoer variabele
invoer = input("Voer je telefoonnummer in: ")

# Dit is de regular expression die we willen vinden
patroon = '^06-?[0-9]{8}'

# Hier vragen we de re module om het patroon op de invoer te matchen
matches = re.findall(patroon, invoer)

# matches bevat een list met de gevonden matches van het patroon
print(matches)
