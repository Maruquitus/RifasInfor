from PIL import ImageFont, ImageDraw, Image
font = ImageFont.truetype("Montserrat-Bold.ttf", 72)

print("~ Gerador de cartelas da rifa de infor 2")
n = 0
for c in range(1, 46):
    print(f"Gerando cartela Nº{c}...") 
    im = Image.open("Modelo.jpg")
    draw = ImageDraw.Draw(im)
    for y in range(10):
        for x in range(10):
            n += 1
            draw.text((438 + x*288, 2008 + y*211), str(n).zfill(4), font=font, fill=(0, 0, 0), anchor="mm")
    im.save(f"Resultados/Cartela do Nº{c}.jpg")