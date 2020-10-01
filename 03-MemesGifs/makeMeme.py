from PIL import Image, ImageFont, ImageDraw

achtergrond = Image.open("meme_background.jpg")
lettertype = ImageFont.truetype("impact.ttf", 40)

breedte = str(achtergrond.width)
hoogte = str(achtergrond.height)

tekengebied = ImageDraw.Draw(achtergrond)

tekst_ark = "Ark                   Ik\n                                         School"
tekengebied.multiline_text((150,250), tekst_ark, font=lettertype, fill=(225,255,255))

achtergrond.show()
