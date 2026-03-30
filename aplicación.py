from pathlib import Path
import base64
import streamlit as st

st.set_page_config(
    page_title="A fábrica das ideas",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE = Path(__file__).parent
ASSETS = BASE / "assets"

BUSINESS = {
    "name": "A fábrica das ideas",
    "tagline": "Personalizaciones",
    "instagram_user": "afabricadasideas",
    "phone_display": "673 67 57 06",
    "phone_plain": "673675706",
    "phone_raw": "34673675706",
    "email": "afabricadasideas23@gmail.com",
}

COLORS = {
    "white": "#FFFFFF",
    "text": "#153F8E",      # azul dominante de tu web/capturas
    "muted": "#4D628C",
    "soft_blue": "#DDE7F7", # fondo azul suave de capturas
    "soft_yellow": "#F3DEAE",
    "orange": "#FF7E24",
    "green": "#8FD65D",
    "pink": "#F5B1C8",
    "mint": "#BFE7D6",
    "sand": "#F6E2BF",
    "border": "#C7D4EE",
    "dark": "#18243A",
}

LOGO = ASSETS / "Logo Instagram.png"

IMPRESSION_PRODUCTS = [
    {"title": "Bolsa merienda personalizada", "price": "4.90€", "details": "20x25 cm", "image": "IMG-20250906-WA0031.jpg"},
    {"title": "Termo de acero inox 500ml", "price": "13.90€", "details": "Personalizado", "image": "WhatsApp Image 2026-03-28 at 06.55.47.jpeg"},
    {"title": "Botella de aluminio 550ml", "price": "8.50€", "details": "Personalizada", "image": "IMG-20250906-WA0030.jpg"},
    {"title": "Camiseta personalizada", "price": "Desde 12€", "details": "Niños 12€ · Adultos 15€", "image": "IMG-20250906-WA0022.jpg"},
    {"title": "Tote bag personalizada", "price": "8€", "details": "33x40 cm", "image": "IMG-20250906-WA0025.jpg"},
    {"title": "Sudadera personalizada", "price": "22€", "details": "Diseño personalizado", "image": "IMG-20250906-WA0010.jpg"},
    {"title": "Taza personalizada", "price": "9€", "details": "Con foto o diseño", "image": "IMG-20250906-WA0021.jpg"},
    {"title": "Camiseta + termo", "price": "21.90€", "details": "Pack personalizado", "image": "IMG-20250906-WA0022.jpg"},
    {"title": "Calcetines personalizados", "price": "6€", "details": "Con imagen o personaje", "image": "Calcetines.jpeg"},
    {"title": "Body bebé personalizado", "price": "12€", "details": "Con nombre o frase", "image": "WhatsApp Image 2026-02-05 at 23.02.23 (1).jpeg"},
    {"title": "Neceser personalizado", "price": "5€", "details": "Ideal para regalo", "image": "WhatsApp Image 2026-02-05 at 23.02.23.jpeg"},
    {"title": "Camisetas fiesta temática", "price": "A consultar", "details": "Para grupos y eventos", "image": "Camisetas fiesta tematica.jpeg"},
    {"title": "Bodies regalo", "price": "A consultar", "details": "Presentación lista para regalar", "image": "WhatsApp Image 2026-02-05 at 23.02.23 (4).jpeg"},
    {"title": "Casco personalizado", "price": "A consultar", "details": "Nombre o diseño", "image": "casco Carla fg.jpg"},
]

EMBROIDERY_PRODUCTS = [
    {"title": "Camiseta bordada", "price": "Desde 5€", "details": "Bordado pequeño", "image": "WhatsApp Image 2026-03-27 at 22.02.25 (3).jpeg"},
    {"title": "Saquito bordado", "price": "Desde 5€", "details": "Nombre o dibujo", "image": "WhatsApp Image 2026-03-27 at 22.02.25.jpeg"},
    {"title": "Pack bordado", "price": "Desde 5€", "details": "Prenda o artículo", "image": "Camiseta padre e hija.jpeg"},
    {"title": "Camiseta nombre bordado", "price": "Desde 5€", "details": "Diseño sencillo", "image": "WhatsApp Image 2026-03-27 at 22.02.25 (2).jpeg"},
]

LASER_PRODUCTS = [
    {"title": "Grabado en madera 12 cm", "price": "12€", "details": "Hasta 12 cm", "image": "WhatsApp Image 2026-03-29 at 14.13.55.jpeg"},
    {"title": "Grabado en madera 16 cm", "price": "16€", "details": "Circular con soporte", "image": "Padre e hijo.jpeg"},
    {"title": "Grabado en madera 18 cm", "price": "18€", "details": "Circular con soporte", "image": "Caballo.jpeg"},
    {"title": "Placa 13x17 cm", "price": "16€", "details": "Personalizada", "image": "WhatsApp Image 2026-03-29 at 14.13.55.jpeg"},
    {"title": "Grabado memorial mascota", "price": "A consultar", "details": "Con foto y texto", "image": "Dia del padre.jpeg"},
]

GALLERY_BY_CATEGORY = {
    "Impresión": [
        "IMG-20250906-WA0022.jpg",
        "IMG-20250906-WA0025.jpg",
        "IMG-20250906-WA0010.jpg",
        "IMG-20250906-WA0021.jpg",
        "IMG-20250906-WA0030.jpg",
        "IMG-20250906-WA0031.jpg",
        "Calcetines.jpeg",
        "WhatsApp Image 2026-02-05 at 23.02.23 (1).jpeg",
        "WhatsApp Image 2026-02-05 at 23.02.23 (3).jpeg",
        "WhatsApp Image 2026-02-05 at 23.02.23 (4).jpeg",
        "WhatsApp Image 2026-02-05 at 23.02.23.jpeg",
        "Camisetas fiesta tematica.jpeg",
        "casco Carla fg.jpg",
    ],
    "Bordados": [
        "WhatsApp Image 2026-03-27 at 22.02.25 (3).jpeg",
        "WhatsApp Image 2026-03-27 at 22.02.25.jpeg",
        "Camiseta padre e hija.jpeg",
        "WhatsApp Image 2026-03-27 at 22.02.25 (2).jpeg",
    ],
    "Grabado y corte": [
        "Padre e hijo.jpeg",
        "Caballo.jpeg",
        "WhatsApp Image 2026-03-29 at 14.13.55.jpeg",
        "Dia del padre.jpeg",
    ],
}


def img_path(name: str) -> str:
    return str(ASSETS / name)


def image_to_base64(path: Path) -> str:
    data = path.read_bytes()
    encoded = base64.b64encode(data).decode("utf-8")
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{encoded}"


def contact_card(icon: str, label: str, value: str, href: str, accent: str, prominent: bool = False):
    cls = "contact-card prominent" if prominent else "contact-card"
    st.markdown(
        f"""
        <a class="{cls}" href="{href}" target="_blank">
            <span class="contact-icon" style="background:{accent};">{icon}</span>
            <span class="contact-copy">
                <strong>{label}</strong>
                <small>{value}</small>
            </span>
        </a>
        """,
        unsafe_allow_html=True,
    )


def product_card(product: dict):
    st.markdown('<div class="product-card">', unsafe_allow_html=True)
    st.image(img_path(product["image"]), use_container_width=True)
    st.markdown(f'<div class="price-badge">{product["price"]}</div>', unsafe_allow_html=True)
    st.markdown(f"<h4>{product['title']}</h4>", unsafe_allow_html=True)
    st.markdown(f"<p>{product['details']}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


logo_tag = ""
if LOGO.exists():
    logo_tag = f'<img class="logo-img" src="{image_to_base64(LOGO)}" alt="Logo">'

st.markdown(
    f"""
    <style>
    .stApp {{ background: {COLORS['white']}; }}
    .main .block-container {{ max-width: 1180px; padding-top: 1rem; padding-bottom: 4rem; }}
    [data-testid="stHeader"] {{ background: rgba(255,255,255,.92); }}
    h1,h2,h3,h4,p,li,span,div {{ color: {COLORS['text']}; }}
    .section {{ border-radius: 28px; padding: 2.1rem 1.5rem; margin: 1rem 0 1.4rem; border: 1px solid {COLORS['border']}; }}
    .blue {{ background: {COLORS['soft_blue']}; }}
    .yellow {{ background: {COLORS['soft_yellow']}; }}
    .white-card {{ background: white; border: 1px solid {COLORS['border']}; border-radius: 24px; padding: 1.25rem; box-shadow: 0 8px 24px rgba(21,63,142,.08); }}
    .hero-grid {{ display:grid; grid-template-columns: 1.1fr .9fr; gap: 1.4rem; align-items:center; }}
    .hero-text h1 {{ font-size: 3rem; margin: 0 0 .4rem; color: {COLORS['dark']}; }}
    .hero-text p {{ font-size: 1.16rem; line-height: 1.7; color: {COLORS['text']}; margin-bottom: 0; }}
    .logo-box {{ display:flex; align-items:center; gap:1rem; margin-bottom: 1rem; flex-wrap:wrap; }}
    .logo-img {{ max-width: 360px; width: 100%; height: auto; object-fit: contain; }}
    .section-title {{ text-align:center; font-size: 2.2rem; font-weight: 900; margin: 0 0 1rem; color: {COLORS['text']}; }}
    .section-title.green {{ color: {COLORS['green']}; }}
    .section-title.orange {{ color: {COLORS['orange']}; }}
    .section-title.dark {{ color: {COLORS['dark']}; }}
    .big-copy {{ font-size: 1.15rem; line-height: 1.8; font-weight: 700; }}
    .accent-orange {{ color: {COLORS['orange']}; font-weight: 800; }}
    .accent-green {{ color: {COLORS['green']}; font-weight: 800; }}
    .tiny-note {{ color: {COLORS['muted']}; font-size: .98rem; line-height:1.6; }}
    .contact-grid {{ display:grid; grid-template-columns: repeat(2,minmax(0,1fr)); gap: 1rem; }}
    .contact-card {{ display:flex; align-items:center; gap:1rem; text-decoration:none; background:white; border:1px solid {COLORS['border']}; padding:1rem 1.1rem; border-radius:20px; box-shadow:0 8px 18px rgba(21,63,142,.08); }}
    .contact-card.prominent {{ border:2px solid #7ad96a; box-shadow:0 12px 28px rgba(87,201,84,.18); }}
    .contact-icon {{ width:58px; height:58px; border-radius:18px; display:flex; align-items:center; justify-content:center; font-size:1.8rem; flex:0 0 58px; }}
    .contact-copy strong {{ display:block; font-size:1.05rem; color:{COLORS['dark']}; }}
    .contact-copy small {{ display:block; font-size:1rem; color:{COLORS['text']}; }}
    .bullet-list {{ font-size: 1.1rem; line-height: 1.8; font-weight: 700; }}
    .bullet-list .line {{ margin-bottom: .45rem; }}
    .center-note {{ text-align:center; font-size:1.08rem; line-height:1.8; font-weight:700; }}
    .product-card {{ position:relative; background:white; border-radius:22px; border:1px solid {COLORS['border']}; padding: .9rem .9rem 1rem; box-shadow: 0 8px 20px rgba(21,63,142,.08); height:100%; }}
    .product-card h4 {{ font-size: 1rem; line-height:1.35; text-align:center; min-height: 48px; margin: .7rem 0 .25rem; color:{COLORS['text']}; }}
    .product-card p {{ font-size: .95rem; text-align:center; margin:0; color:{COLORS['muted']}; font-weight:700; }}
    .price-badge {{ position:absolute; top:10px; right:10px; background: {COLORS['soft_yellow']}; color:{COLORS['orange']}; font-weight:900; padding:.4rem .7rem; border-radius:999px; border: 1px dashed {COLORS['orange']}; }}
    .subhead {{ text-align:center; font-size: 1.95rem; font-weight: 900; margin: 1rem 0 1rem; color: {COLORS['green']}; }}
    .mini-head {{ text-align:center; font-size: 1.8rem; font-weight:900; margin:.5rem 0 1rem; color:{COLORS['orange']}; }}
    .gallery-title {{ font-size:1.55rem; font-weight:900; color:{COLORS['dark']}; margin:.4rem 0 1rem; text-align:center; }}
    .footer-help {{ text-align:center; font-size: 2rem; line-height:1.5; font-weight:900; color:{COLORS['text']}; margin-top:1rem; }}
    @media (max-width: 900px) {{
        .hero-grid {{ grid-template-columns: 1fr; }}
        .contact-grid {{ grid-template-columns: 1fr; }}
        .hero-text h1 {{ font-size: 2.2rem; }}
        .section-title {{ font-size: 1.8rem; }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# HERO
st.markdown('<div class="section blue">', unsafe_allow_html=True)
col1, col2 = st.columns([1.15, 0.85], gap="large")
with col1:
    st.markdown('<div class="hero-text">', unsafe_allow_html=True)
    st.markdown(f'<div class="logo-box">{logo_tag}</div>', unsafe_allow_html=True)
    st.markdown("<h1>Diseño e impresión</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p>Donde la creatividad cobra vida: personalizamos tus ideas y las hacemos realidad.</p>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)
with col2:
    st.image(img_path("IMG-20250906-WA0022.jpg"), use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# TEXTO GENERAL IMPRESION / BORDADO
st.markdown('<div class="section yellow">', unsafe_allow_html=True)
st.markdown('<div class="section-title dark">Impresión y bordado</div>', unsafe_allow_html=True)
st.markdown(
    f"""
    <div class="bullet-list">
      <div class="line"><span class="accent-orange">IMPRESIÓN:</span> vinilo, DTF y sublimación aplicados sobre textil y otros soportes.</div>
      <div class="line">👉 Camisetas, sudaderas, gorras, bolsas de tela, ropa laboral, tazas, cojines, puzzles y artículos promocionales, etc...</div>
      <div class="line" style="margin-top:.8rem;"><span class="accent-orange">BORDADO:</span> personalización mediante hilo sobre prendas textiles.</div>
      <div class="line">👉 Polos, camisetas, gorras, sudaderas, chaquetas, uniformes, ropa laboral y textil corporativo, etc...</div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# BUSCAS ALGO UNICO
st.markdown('<div class="section yellow">', unsafe_allow_html=True)
left, right = st.columns([1.15, 0.85], gap="large")
with left:
    st.markdown('<div class="section-title dark" style="text-align:left;font-size:1.9rem;">¿Buscas algo único para tu evento? ✨</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="big-copy">
        Realizamos impresiones personalizadas para todo tipo de ocasiones:<br><br>
        🎉 Fiestas temáticas<br>
        🎂 Cumpleaños<br>
        🎊 Eventos especiales<br>
        👕 Celebraciones en grupo<br><br>
        Trabajamos con todo tipo de prendas, objetos y materiales, adaptándonos a lo que necesites para que tu idea cobre vida.<br><br>
        Además, ofrecemos precios especiales para pedidos grandes, ideales para grupos, asociaciones o eventos.<br><br>
        📩 Solicita tu presupuesto sin compromiso y te ayudamos a crear algo totalmente personalizado.
        </div>
        """,
        unsafe_allow_html=True,
    )
with right:
    st.image(img_path("Camisetas fiesta tematica.jpeg"), use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# IMPRESION PRODUCTOS
st.markdown('<div class="section blue">', unsafe_allow_html=True)
st.markdown('<div class="section-title green">Impresión</div>', unsafe_allow_html=True)
for row_start in range(0, len(IMPRESSION_PRODUCTS), 3):
    cols = st.columns(3, gap="large")
    for col, product in zip(cols, IMPRESSION_PRODUCTS[row_start: row_start + 3]):
        with col:
            product_card(product)
st.markdown("</div>", unsafe_allow_html=True)

# BORDADO
st.markdown('<div class="section blue">', unsafe_allow_html=True)
st.markdown('<div class="section-title green">Bordado</div>', unsafe_allow_html=True)
cols = st.columns(4, gap="large")
for col, product in zip(cols, EMBROIDERY_PRODUCTS):
    with col:
        product_card(product)
st.markdown(
    """
    <div class="center-note" style="margin-top:1.1rem;">
    El precio varía según el tamaño del diseño, la complejidad y si la prenda la aportas tú o la ponemos nosotros.<br><br>
    💰 Desde 5€ (bordado pequeño)<br>
    📩 Presupuesto sin compromiso
    </div>
    <div class="footer-help">Trae tu prenda o artículo y lo personalizamos mediante impresión o bordado ✨<br><br>¡Pide tu presupuesto!</div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# LASER EXPLAINER
st.markdown('<div class="section yellow">', unsafe_allow_html=True)
st.markdown('<div class="section-title dark">Grabado y corte (trabajo con láser)</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="bullet-list">
      <div class="line">🌳 <strong>Madera</strong><br>Perfecta para carteles, nombres decorativos, llaveros, placas, detalles personalizados, etc...</div>
      <div class="line">🧁 <strong>Metacrilato (acrílico)</strong><br>Ideal para topper de tartas, nombres, letras, logotipos, señalización, decoración, etc...</div>
      <div class="line">🧵 <strong>Tela y cuero</strong><br>Perfectos para parches, etiquetas, detalles en ropa y complementos personalizados. El cuero, además, aporta un acabado prémium y muy duradero.</div>
      <div class="line">📦 <strong>Cartón y papel</strong><br>Ideales para invitaciones, packaging, cajas personalizadas, etiquetas y trabajos creativos, etc...</div>
      <div class="line">🫙 <strong>Vidrio</strong><br>Perfecto para personalizar copas, vasos, botellas o espejos, creando un efecto grabado elegante y sofisticado.</div>
      <div class="line">🧱 <strong>Piedra (pizarra, mármol o granito)</strong><br>Ideal para placas, posavasos, decoración y regalos personalizados con un acabado duradero y exclusivo.</div>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# LASER PRICES AND DETAIL
st.markdown('<div class="section blue">', unsafe_allow_html=True)
price_cols = st.columns(4, gap="large")
for col, product in zip(price_cols, LASER_PRODUCTS[:4]):
    with col:
        product_card(product)

st.markdown('<div class="mini-head">12 cm · 12€ <span style="font-size:1rem;">(hasta 12cm)</span></div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="center-note">
    Fotografía grabada en madera con láser (3 mm) 🪵✨<br>
    Envíanos tu imagen y la convertimos en un regalo original 🎁 para decorar cualquier espacio 🏡<br><br>
    Opcional: grabado trasero con texto 📝 (mensaje, fecha, canción, etc.), indicando la fuente 🔤<br><br>
    Recomendación: usa imágenes nítidas y de alta calidad 📸; evita fotos reenviadas por WhatsApp ❌📲<br><br>
    <span class="accent-orange">Cada pieza se realiza a medida, por lo que el precio varía según el tamaño que necesites.</span><br>
    <span class="accent-orange">Cuéntanos qué quieres y te preparamos un presupuesto personalizado sin compromiso.</span><br><br>
    👉 <span class="accent-orange">Solicita presupuesto</span>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown("</div>", unsafe_allow_html=True)

# GALLERY WITH TABS
st.markdown('<div class="section white-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title dark">Galería de trabajos</div>', unsafe_allow_html=True)
tabs = st.tabs(list(GALLERY_BY_CATEGORY.keys()))
for tab, (name, images) in zip(tabs, GALLERY_BY_CATEGORY.items()):
    with tab:
        st.markdown(f'<div class="gallery-title">{name}</div>', unsafe_allow_html=True)
        for i in range(0, len(images), 3):
            cols = st.columns(3, gap="medium")
            for col, image in zip(cols, images[i:i+3]):
                with col:
                    st.image(img_path(image), use_container_width=True)
st.markdown("</div>", unsafe_allow_html=True)

# CONTACTO
st.markdown('<div class="section blue">', unsafe_allow_html=True)
st.markdown('<div class="section-title green">Contacto</div>', unsafe_allow_html=True)
contact_card("📞", "Llamar", BUSINESS["phone_plain"], f"tel:+{BUSINESS['phone_raw']}", "#E8EEF9")
st.markdown("<div style='height:.7rem'></div>", unsafe_allow_html=True)
contact_card("🟢", "WhatsApp", BUSINESS["phone_plain"], f"https://wa.me/{BUSINESS['phone_raw']}", "#CFF3C8", prominent=True)
st.markdown("<div style='height:.7rem'></div>", unsafe_allow_html=True)
cols = st.columns(2, gap="large")
with cols[0]:
    contact_card("📷", "Instagram", f"@{BUSINESS['instagram_user']}", f"https://instagram.com/{BUSINESS['instagram_user']}", "#F7D3E6")
with cols[1]:
    contact_card("✉️", "Email", BUSINESS["email"], f"mailto:{BUSINESS['email']}", "#FFE0C3")
st.markdown("</div>", unsafe_allow_html=True)

st.caption("Puedes cambiar el logo después sustituyendo el archivo assets/Logo Instagram.png por el bueno.")
