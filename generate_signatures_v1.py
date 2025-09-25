# filename: app.py
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os
import unicodedata

# Config
base_img_path = "./templates/eni_signature.png"
output_dir = "signatures"
os.makedirs(output_dir, exist_ok=True)

coords = {
    "title": (996, 210),
    "role": (996, 320),
    "info": (996, 420),
    "website": (996, 493),
}

font_sizes = {
    "title": 85,
    "role": 70,
    "info": 50,
    "website": 53,
}

color = {
    "title": (31, 54, 89),
    "role": (192, 48, 36),
    "info": (112, 112, 111),
    "website": (31, 54, 89),
}

# Fonts
font_Sansation_Bold = "./fonts/sansation/Sansation_Bold.ttf"
font_lgSmart_Bold = "./fonts/lgSmart/LgSmartBold.ttf"
font_lgSmart_Regular = "./fonts/lgSmart/LgSmartRegular.ttf"
font_lgSmart_semiBold = "./fonts/lgSmart/LgSmartSemiBold.ttf"

# Streamlit Form
st.title("Signature Generator")

name = st.text_input("Name")
role = st.text_input("Role")
phone = st.text_input("Phone")
fax = st.text_input("Fax")
website = st.text_input("Website")

if st.button("Generate Signature"):
    # Normalize
    name = unicodedata.normalize("NFC", name)
    role = unicodedata.normalize("NFC", role)
    phone = unicodedata.normalize("NFC", phone)
    fax = unicodedata.normalize("NFC", fax)
    website = unicodedata.normalize("NFC", website)

    # Create image
    img = Image.open(base_img_path).convert("RGB")
    draw = ImageDraw.Draw(img)
    draw.text(coords["title"], name, font=ImageFont.truetype(font_Sansation_Bold, font_sizes["title"]), fill=color["title"])
    draw.text(coords["role"], role, font=ImageFont.truetype(font_lgSmart_Bold, font_sizes["role"]), fill=color["role"])
    draw.text(coords["info"], f"T : {phone} | F : {fax}", font=ImageFont.truetype(font_lgSmart_Regular, font_sizes["info"]), fill=color["info"])
    draw.text(coords["website"], website, font=ImageFont.truetype(font_lgSmart_semiBold, font_sizes["website"]), fill=color["website"])

    # Save output
    output_path = os.path.join(output_dir, f"{name.replace(' ', '_')}.png")
    img.save(output_path)
    st.success(f"Signature saved: {output_path}")
    st.image(img)

