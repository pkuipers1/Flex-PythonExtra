from PIL import Image

# Afbeelding openen en oplsaan in de variabele met de naam: afbeelding
afbeelding = Image.open("meme.jpg")

# De afbeelding tonen in de standaard image viewer van jouw systeem
afbeelding.show()

# De breedte en hoogte van de afbeelding lezen en tonen
breedte = afbeelding.width
hoogte = afbeelding.height

# Afmetingen op het scherm zetten
# Andere info uitlezen en tonen
print(afbeelding.format, afbeelding.size, afbeelding.mode)
