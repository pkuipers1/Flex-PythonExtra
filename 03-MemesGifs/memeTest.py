from PIL import Image

# Afbeelding openen en opslaan in de variabele met de naam: afbeelding
afbeelding = Image.open("sunset.jpg")

# De afbeelding tonen in de standaard image viewer van jouw systeem
afbeelding.show()

# De breedte en hoogte van de afbeelding lezen en tonen
# Met str() zet je een getal naar een string om. Dan kan print() het gebruiken.
breedte = str(afbeelding.width)
hoogte = str(afbeelding.height)

# breedte en hoogte door twee delen (en afronden naar beneden)

helft_breedte = afbeelding.width // 2
helft_hoogte = afbeelding.height // 2
