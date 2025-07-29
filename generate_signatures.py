from PIL import Image, ImageDraw, ImageFont
import unicodedata
import os

# =============== Configuration : Edit this section to change the signatures ============

# List of people with their details
people = [
    { "name": "Nacer DIOURI", "role": "Directeur Général", "phone": "+212 6 66 13 95 81", "fax": "+212 5 22 31 04 04", "website": "www.eni.ma"},
    { "name": "Mohamed FARI", "role": "Responsable Marketing", "phone": "+212 6 60 29 20 20", "fax": "+212 5 22 31 04 04", "website": "www.eni.ma"},
    { "name": "Fatima Zahra EL FASSI", "role": "Déléguée Marketing", "phone": "+212 6 00 39 39 39", "fax": "+212 5 22 31 04 04", "website": "www.eni.ma"},
    { "name": "Youssef EL KHALFI", "role": "Responsable Commercial", "phone": "+212 6 66 13 95 81", "fax": "+212 5 22 31 04 04", "website": "www.eni.ma"},
    { "name": "Hicham EL KHALFI", "role": "Téléconseiller", "phone": "+212 6 66 13 95 81", "fax": "+212 5 22 31 04 04", "website": "www.eni.ma"},
    { "name": "Salma BENALI", "role": "UI/UX Designer", "phone": "+212 6 66 13 95 81", "fax": "+212 5 22 31 04 04", "website": "www.eni.ma"},
    { "name": "Yassine EL KHALFI", "role": "Développeur Web", "phone": "+212 6 66 13 95 81", "fax": "+212 5 22 31 04 04", "website": "www.eni.ma"},
    { "name": "Hicham EL KHALFI", "role": "Développeur Mobile", "phone": "+212 6 66 13 95 81", "fax": "+212 5 22 31 04 04", "website": "www.eni.ma"},
]

# Coordinates in the base image
coords = {
    "title": (996, 210),
    "role": (996, 320),
    "info": (996, 420),
    "website": (996, 493),
}

# font sizes
font_sizes = {
    "title": 85,
    "role": 70,
    "info": 50,
    "website": 53,
}

# Element Colors
color = {
    "title": (31, 54, 89),
    "role": (192, 48, 36),
    "info": (112, 112, 111),
    "website": (31, 54, 89),
} 



# =============== Signature Generator : Do not edit below this line =====================

# Load base image
base_img_path = "./templates/eni_signature.png"
output_dir = "signatures"
os.makedirs(output_dir, exist_ok=True)

# normalize names and roles to NFC
for person in people:
    person["name"] = unicodedata.normalize("NFC", person["name"])
    person["role"] = unicodedata.normalize("NFC", person["role"])
    person["phone"] = unicodedata.normalize("NFC", person["phone"])
    person["fax"] = unicodedata.normalize("NFC", person["fax"])
    person["website"] = unicodedata.normalize("NFC", person["website"])

# Font paths (you may need to adjust)
font_Sansation_Regular = "./fonts/sansation/Sansation_Regular.ttf"
font_Sansation_Bold = "./fonts/sansation/Sansation_Bold.ttf"
font_lgSmart_Regular = "./fonts/lgSmart/LgSmartRegular.ttf"
font_lgSmart_Bold = "./fonts/lgSmart/LgSmartBold.ttf"
font_lgSmart_semiBold = "./fonts/lgSmart/LgSmartSemiBold.ttf"

for person in people:
    img = Image.open(base_img_path).convert("RGB")
    draw = ImageDraw.Draw(img)

    # Draw text on the image:
    draw.text(
        coords["title"],
        person["name"],
        font=ImageFont.truetype(font_Sansation_Bold, font_sizes["title"]),
        fill=color["title"]
    )

    draw.text(
        coords["role"],
        person["role"],
        font=ImageFont.truetype(font_lgSmart_Bold, font_sizes["role"]),
        fill=color["role"]
    )

    draw.text(
        coords["info"],
        f"T : {person['phone']} |  F : {person['fax']}",
        font=ImageFont.truetype(font_lgSmart_Regular, font_sizes["info"]),
        fill= color["info"]
    )

    draw.text(
        coords["website"],
        person["website"],
        font=ImageFont.truetype(font_lgSmart_semiBold, font_sizes["website"]),
        fill=color["website"]
    )

    # Save the output
    output_path = os.path.join(output_dir, f"{person['name'].replace(' ', '_')}.png")
    img.save(output_path)

print("✅ Signatures generated.")
