from pathlib import Path
from urllib.parse import quote
import html
import base64
import re
import streamlit as st

st.set_page_config(
    page_title="A fábrica das ideas",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE = Path(__file__).parent
ASSETS = BASE / "assets"
CONTACTO = ASSETS / "contacto"

BUSINESS = {
    "instagram_user": "afabricadasideas",
    "instagram_url": "https://instagram.com/afabricadasideas",
    "phone_display": "673 67 57 06",
    "phone_raw": "34673675706",
    "email": "afabricadasideas23@gmail.com",
}

COLORS = {
    "bg": "#FFFFFF",
    "text": "#222222",
    "muted": "#5F6063",
    "line": "#EEE6E0",
    "blue_baby": "#EAF4FF",
    "soft_box": "#FFFCFB",
}

SECTION_COLORS = {
    "impresion": "#FFF8EA",
    "bordado": "#F2FBF7",
    "grabado": "#FFF5F8",
}

LOGO = ASSETS / "logo" / "logo_principal.png"
HERO = ASSETS / "portada" / "portada_manuel.png"
EVENT = ASSETS / "eventos" / "evento_camisetas_01.png"


SECTIONS = {
    "impresion": {
        "name": "Impresión",
        "emoji": "🎨",
        "intro": (
            "🎨 **Vinilo, DTF y sublimación** para dar vida a ideas bonitas y súper especiales.\n\n"
            "👕 Personalizamos camisetas, sudaderas, bodies, bolsas, tazas, termos y botellas.\n"
            "🎁 Ideal para regalos con nombre, detalles de bebé, fiestas, eventos y recuerdos únicos."
        ),
        "products": [
            ("Camiseta personalizada", "Desde 12€", "👕 Niños 12€ · Adultos 15€", "impresion_nenes_camiseta_04.png"),
            ("Taza personalizada", "9€", "☕ Con foto, nombre o diseño especial", "impresion_objeto_taza_01.png"),
            ("Termo personalizado", "13,90€", "🥤 Acero inox 500 ml", "impresion_objeto_botella_04.png"),
            ("Botella", "8,50€", "🧒 Aluminio 550 ml", "impresion_nenes_botella_01.png"),
            ("Body bebé personalizado", "12€", "👶 Dulce y muy especial", "impresion_bebe_body_06.png"),
            ("Tote bag personalizada", "8€", "🎀 Ideal para para ti o para regalar", "impresion_objeto_totebag_01.png"),
            ("Sudadera personalizada", "22€", "❤️ A tu gusto", "impresion_zadultos_sudadera_02.png"),
            ("Bolsa merienda", "4,90€", "🍪 Medida 20 x 25 cm", "impresion_bebe_bolsa_merienda_01.png"),
            ("Tote bag bebé", "8€", "👶 Medida 33x40cm", "impresion_bebe_totebag_03.png"),
        ],
        "gallery": [
            "Camisetas fiesta tematica.jpeg", "IMG-20250906-WA0010.jpg", "IMG-20250906-WA0021.jpg",
            "IMG-20250906-WA0030.jpg", "IMG-20250906-WA0031.jpg", "casco Carla fg.jpg",
            "WhatsApp Image 2026-03-27 at 22.02.25 (3).jpeg"
        ],
    },
    "bordado": {
        "name": "Bordado",
        "emoji": "🧵",
        "intro": (
            "🧵 **Bordado en hilo** con un acabado bonito, elegante y duradero.\n\n"
            "👚 Perfecto para nombres, iniciales y detalles especiales en prendas o complementos.\n"
            "✨ El precio depende del tamaño del bordado, la complejidad y de si traes la prenda o la ponemos nosotras."
        ),
        "products": [
            ("Bordado pequeño", "Desde 5€", "🪡 Nombre o detalle sencillo", "bordado_objeto_bolsa_merienda_02.png"),
            ("Bordado pequeño", "Desde 5€", "👕 Nombre bordado neceser", "bordado_objeto_bolsa_merienda_04.png"),
            ("Camiseta nombre bordado", "Consultar", "🎁 Ideal para regalo", "bordado_objeto_camiseta_mascota_01.png"),
            ("Pack padre e hija", "Consultar", "💞 Conjunto personalizado", "bordado_objeto_camiseta_padre_hija_01.png"),
        ],
        "gallery": [
            "WhatsApp Image 2026-03-29 at 14.13.54.jpeg", "WhatsApp Image 2026-03-27 at 22.02.25.jpeg", "Camiseta padre e hija.jpeg"
        ],
    },
    "grabado": {
        "name": "Grabado y corte",
        "emoji": "🔥",
        "intro": (
            "🔥 **Grabado y corte láser** para crear detalles únicos con mucho sentimiento.\n\n"
            "🌳 Trabajamos madera, vidrio, espejo, piedra y otros materiales.\n"
            "💝 Ideal para placas, recuerdos especiales, carteles, llaveros y regalos personalizados."
        ),
        "products": [
            ("Grabado en madera 12 cm", "12€", "🪵 Circular con soporte", "grabado_objeto_circulo_03.png"),
            ("Grabado en madera 16 cm", "16€", "🪵 Circular con soporte", "grabado_objeto_circulo_02.png"),
            ("Grabado en madera 18 cm", "18€", "🪵 Circular con soporte", "grabado_objeto_circulo_01.png"),
            ("Placa rectangular", "16€", "📏 Tamaño 13 x 17 cm", "grabado_objeto_rectangulo_01.png"),
        ],
        "gallery": ["Padre e hijo.jpeg", "Caballo.jpeg", "Dia del padre.jpeg", "WhatsApp Image 2026-03-29 at 14.13.55.jpeg"],
    },
}


IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".webp"}


def is_image_file(path: Path) -> bool:
    return path.is_file() and path.suffix.lower() in IMAGE_EXTS


def normalize_name(name: str) -> str:
    stem = Path(name).stem.lower()
    return re.sub(r"[^a-z0-9]+", "", stem)


def list_section_images(group: str, section: str) -> list[Path]:
    folder = ASSETS / group / section
    if not folder.exists():
        return []
    return sorted([p for p in folder.rglob("*") if is_image_file(p)], key=lambda p: p.name.lower())


def resolve_section_image(group: str, section: str, requested_name: str, fallback_index: int | None = None) -> Path | None:
    candidates = list_section_images(group, section)
    if candidates:
        requested_lower = requested_name.lower()
        requested_norm = normalize_name(requested_name)
        for path in candidates:
            if path.name.lower() == requested_lower:
                return path
        for path in candidates:
            if normalize_name(path.name) == requested_norm:
                return path
        if fallback_index is not None:
            return candidates[fallback_index % len(candidates)]
        return candidates[0]

    all_assets = sorted([p for p in ASSETS.rglob("*") if is_image_file(p)], key=lambda p: p.name.lower())
    if not all_assets:
        return None
    requested_lower = requested_name.lower()
    requested_norm = normalize_name(requested_name)
    for path in all_assets:
        if path.name.lower() == requested_lower:
            return path
    for path in all_assets:
        if normalize_name(path.name) == requested_norm:
            return path
    if fallback_index is not None:
        return all_assets[fallback_index % len(all_assets)]
    return all_assets[0]


def wa_url(message: str) -> str:
    return f"https://wa.me/{BUSINESS['phone_raw']}?text={quote(message)}"


def section_badge(text: str, color: str) -> None:
    st.markdown(
        f"<div class='section-badge' style='background:{color}'>{html.escape(text)}</div>",
        unsafe_allow_html=True,
    )


def safe_image(path: Path | None, missing_text: str = "Imagen no disponible") -> None:
    if path and path.exists():
        st.image(str(path), use_container_width=True)
    else:
        st.warning(missing_text)


def product_card(section: str, item, index: int) -> None:
    name, price, desc, image = item
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    safe_image(
        resolve_section_image("Cátalogo", section, image, fallback_index=index),
        missing_text=f"No encuentro imagen para {name}",
    )
    st.markdown(
        f"<div class='product-line'><div class='product-name'>{html.escape(name)}</div><div class='product-price'>{html.escape(price)}</div></div>"
        f"<div class='product-desc'>{html.escape(desc)}</div>",
        unsafe_allow_html=True,
    )
    st.link_button(
        "Pedir por WhatsApp",
        wa_url(f"Hola 😊 Me interesa {name} ({price}). ¿Me das más información?"),
        use_container_width=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)


def gallery_grid(section: str) -> None:
    images = list_section_images("galeria", section)
    if not images:
        st.info("Todavía no hay imágenes en esta galería.")
        return
    cols = st.columns(3, gap="medium")
    for i, path in enumerate(images):
        with cols[i % 3]:
            st.image(str(path), use_container_width=True)


def contact_icon_uri(kind: str) -> str | None:
    candidates = [
        CONTACTO / f"{kind}.png",
        CONTACTO / f"{kind}.jpg",
        CONTACTO / f"{kind}.jpeg",
        CONTACTO / f"{kind}.webp",
        CONTACTO / f"{kind}.svg",
    ]

    mime_map = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".svg": "image/svg+xml",
    }

    for path in candidates:
        if path.exists():
            data = base64.b64encode(path.read_bytes()).decode("utf-8")
            mime = mime_map[path.suffix.lower()]
            return f"data:{mime};base64,{data}"

    return None

def contact_item(kind: str, label: str, href: str) -> None:
    icons = {
        "whatsapp": "💬",
        "instagram": "📸",
        "phone": "📞",
        "mail": "✉️",
    }

    st.markdown(
        f"<a class='contact-item' href='{href}' target='_blank'>"
        f"<span class='cicon {kind}'>{icons[kind]}</span>"
        f"<span class='contact-label'>{html.escape(label)}</span>"
        f"</a>",
        unsafe_allow_html=True,
    )

def set_page(page: str):
    st.session_state["page"] = page


def render_products(key: str):
    data = SECTIONS[key]
    color = SECTION_COLORS[key]
    section_badge(f"{data['emoji']} {data['name']}", color)
    st.markdown(f"<div class='section-text'>{data['intro']}</div>", unsafe_allow_html=True)
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    rows = [data['products'][i:i+3] for i in range(0, len(data['products']), 3)]
    for row in rows:
        cols = st.columns(3, gap="medium")
        start_index = data['products'].index(row[0])
        for offset, (col, item) in enumerate(zip(cols, row)):
            with col:
                product_card(key, item, start_index + offset)


def render_gallery(key: str):
    data = SECTIONS[key]
    color = SECTION_COLORS[key]
    section_badge(f"📸 Galería · {data['name']}", color)
    gallery_grid(key)


st.markdown(
    f"""
<style>
html, body, [class*="css"] {{ font-family: 'Segoe UI', sans-serif; }}
.stApp {{ background: {COLORS['bg']}; }}
.main .block-container {{ max-width: 1180px; padding-top: .15rem; padding-bottom: 4rem; }}
#MainMenu, footer, [data-testid="stStatusWidget"], [data-testid="stDecoration"], [data-testid="stSidebarNav"] {{ display:none !important; }}
.logo-wrap {{ text-align:center; margin: .1rem 0 .45rem 0; }}
.topbar {{ width:100%; margin:.35rem 0 1rem 0; height:42px; border-radius:999px; border:1px solid {COLORS['line']}; background:linear-gradient(180deg, rgba(242,153,181,.18) 0%, rgba(245,220,158,.18) 18%, rgba(189,231,220,.18) 36%, rgba(201,192,202,.16) 50%, rgba(255,255,255,0) 50%, rgba(255,255,255,0) 100%), #fff; }}
.panelbar {{ width:100%; margin: 1.25rem 0 1rem 0; height:42px; border-radius:999px; border:1px solid {COLORS['line']}; background:linear-gradient(180deg, rgba(242,153,181,.18) 0%, rgba(245,220,158,.18) 18%, rgba(189,231,220,.18) 36%, rgba(201,192,202,.16) 50%, rgba(255,255,255,0) 50%, rgba(255,255,255,0) 100%), #fff; }}
.hero, .events, .contact-box, .page-box {{ background:{COLORS['soft_box']}; border:1px solid {COLORS['line']}; border-radius:28px; padding:1.3rem; box-shadow:0 10px 24px rgba(0,0,0,.035); }}
.hero-text, .events-text, .section-text {{ color:{COLORS['muted']}; font-size:1.04rem; line-height:1.85; }}
.section-badge {{ display:inline-block; padding:.68rem 1rem; border-radius:18px; font-weight:800; color:#6b6b6b; margin: .2rem 0 1rem 0; }}
.product-card {{ background:#fff; border:1px solid {COLORS['line']}; border-radius:22px; padding:1rem; box-shadow:0 8px 18px rgba(0,0,0,.035); height:100%; }}
.product-line {{ display:flex; justify-content:space-between; gap:1rem; align-items:flex-start; margin-top:.7rem; }}
.product-name {{ font-weight:800; color:{COLORS['text']}; line-height:1.35; }}
.product-price {{ font-weight:800; color:#000; white-space:nowrap; text-align:right; }}
.product-desc {{ color:{COLORS['muted']}; font-size:.95rem; margin-top:.35rem; min-height:42px; }}
.stLinkButton > a {{ background:{COLORS['blue_baby']} !important; color:#16314b !important; border:1px solid #c7ddf7 !important; border-radius:16px !important; font-weight:700 !important; }}
.stLinkButton > a:hover {{ background:#dcedff !important; }}
.contact-item {{ display:flex; align-items:center; gap:.8rem; text-decoration:none; color:{COLORS['text']} !important; border:1px solid {COLORS['line']}; border-radius:18px; background:#fff; padding:.95rem 1rem; margin-bottom:.8rem; }}
.cicon {{ width:42px; height:42px; display:inline-flex; align-items:center; justify-content:center; border-radius:50%; font-size:20px; flex:0 0 42px; }}
.cicon img {{ width:24px; height:24px; object-fit:contain; display:block; }}
.cicon.whatsapp {{ background:#EAF9F0; }}
.cicon.instagram {{ background:#FCEAF4; }}
.cicon.phone {{ background:#EEF3FF; }}
.cicon.mail {{ background:#FFF6E2; }}
[data-testid="stSidebar"] {{ background:#fff; border-right:1px solid {COLORS['line']}; }}
[data-testid="collapsedControl"] {{ display:block !important; position:fixed !important; top:14px; left:14px; z-index:1001; }}
[data-testid="collapsedControl"] button {{
    background:#fff7ea !important;
    border:2px solid #e7cfa8 !important;
    border-radius:18px !important;
    width:58px !important;
    height:58px !important;
    box-shadow:0 10px 24px rgba(0,0,0,.14) !important;
    transition:all .18s ease !important;
}}
[data-testid="collapsedControl"] button:hover {{
    background:#ffeecf !important;
    border-color:#dcb677 !important;
    transform:scale(1.04);
}}
[data-testid="collapsedControl"] svg {{ width:28px !important; height:28px !important; }}
[data-testid="collapsedControl"] svg path {{
    fill:#8f6b2d !important;
}}
.sidebar-title {{ font-weight:800; margin:.25rem 0 .75rem 0; color:#4e4e4e; }}
.sidebar-group {{ font-size:.92rem; font-weight:800; color:#7b7b7b; margin:1rem 0 .35rem 0; text-transform:uppercase; letter-spacing:.04em; }}
.stButton > button {{ width:100%; border-radius:14px; border:1px solid {COLORS['line']}; background:#fff; color:{COLORS['text']}; text-align:left; font-weight:600; }}
.stButton > button:hover {{ border-color:#dacfc8; color:#111; }}
@media (max-width: 820px) {{ .panelbar {{height:36px;}} }}
</style>
""",
    unsafe_allow_html=True,
)

if "page" not in st.session_state:
    st.session_state["page"] = "Inicio"

with st.sidebar:
    st.markdown("<div class='sidebar-title'>Menú</div>", unsafe_allow_html=True)
    if st.button("🏠 Inicio", use_container_width=True):
        set_page("Inicio")
    if st.button("🎉 Eventos", use_container_width=True):
        set_page("Eventos")
    st.markdown("<div class='sidebar-group'>Cátalogo</div>", unsafe_allow_html=True)
    if st.button("👕 Impresión", use_container_width=True):
        set_page("Cátalogo · Impresión")
    if st.button("🧵 Bordado", use_container_width=True):
        set_page("Cátalogo · Bordado")
    if st.button("🔥 Grabado / Corte", use_container_width=True):
        set_page("Cátalogo · Grabado")
    st.markdown("<div class='sidebar-group'>Galería</div>", unsafe_allow_html=True)
    if st.button("📒 Impresión", use_container_width=True):
        set_page("Galería · Impresión")
    if st.button("📒 Bordado", use_container_width=True):
        set_page("Galería · Bordado")
    if st.button("📒 Grabado", use_container_width=True):
        set_page("Galería · Grabado")
    st.markdown("<div class='sidebar-group'>Contacto</div>", unsafe_allow_html=True)
    if st.button("📲 Contáctanos", use_container_width=True):
        set_page("Contacto")

logo_c1, logo_c2, logo_c3 = st.columns([0.18, 0.64, 0.18])
with logo_c2:
    st.image(str(LOGO), width=760)

st.markdown("<div class='topbar'></div>", unsafe_allow_html=True)

page = st.session_state["page"]

if page == "Inicio":
    c1, c2 = st.columns([1.02, .98], gap="large")
    with c1:
        st.markdown("<div class='hero'>", unsafe_allow_html=True)
        st.markdown(
            "<div class='hero-text'>💛 <b>Diseño e impresión</b> donde las ideas se convierten en detalles únicos. Creamos regalos y personalizaciones con mimo para bebés, familias, eventos, recuerdos especiales y pequeños caprichos bonitos. ✨</div>",
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:.8rem'></div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='hero-text'>🎁 Cada pedido se prepara con cariño, cuidando la imagen, el acabado y ese toque especial que hace que el regalo emocione de verdad.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.image(str(HERO), use_container_width=True)

    st.markdown("<div class='panelbar'></div>", unsafe_allow_html=True)

    col_text, col_img = st.columns([1.05, .95], gap="large")
    with col_text:
        st.markdown("<div class='events'>", unsafe_allow_html=True)
        st.markdown("<div class='section-text'><b>🎉 ¿Buscas algo único para tu evento?</b> ✨</div>", unsafe_allow_html=True)
        st.markdown("<div style='height:.6rem'></div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='events-text'>Realizamos impresiones personalizadas para todo tipo de ocasiones: 🎊 fiestas temáticas, 🎂 cumpleaños, 🥳 eventos especiales y 👕 celebraciones en grupo.</div>",
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:.8rem'></div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='events-text'>Trabajamos con prendas, objetos y materiales distintos, adaptándonos a lo que necesites para que tu idea cobre vida 💫</div>",
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:.8rem'></div>", unsafe_allow_html=True)
        st.markdown(
            "<div class='events-text'>Además, ofrecemos precios especiales para pedidos grandes, perfectos para grupos, asociaciones o eventos 🎁</div>",
            unsafe_allow_html=True,
        )
        st.markdown("</div>", unsafe_allow_html=True)
    with col_img:
        st.image(str(EVENT), use_container_width=True)

elif page == "Eventos":
    st.markdown("<div class='page-box'>", unsafe_allow_html=True)
    st.markdown("### 🎉 Eventos y pedidos especiales")
    st.markdown(
        "<div class='events-text'>Realizamos impresiones personalizadas para todo tipo de ocasiones: 🎊 fiestas temáticas, 🎂 cumpleaños, 🥳 eventos especiales y 👕 celebraciones en grupo.<br><br>Trabajamos con prendas, objetos y materiales distintos, adaptándonos a lo que necesites para que tu idea cobre vida 💫<br><br>Además, ofrecemos precios especiales para pedidos grandes, perfectos para grupos, asociaciones o eventos 🎁</div>",
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)
    st.image(str(EVENT), use_container_width=True)

elif page == "Cátalogo · Impresión":
    render_products("impresion")
elif page == "Cátalogo · Bordado":
    render_products("bordado")
elif page == "Cátalogo · Grabado":
    render_products("grabado")
elif page == "Galería · Impresión":
    render_gallery("impresion")
elif page == "Galería · Bordado":
    render_gallery("bordado")
elif page == "Galería · Grabado":
    render_gallery("grabado")
elif page == "Contacto":
    st.markdown("<div class='contact-box'>", unsafe_allow_html=True)
    st.markdown("### 📲 Contacto")
    contact_item("whatsapp", BUSINESS["phone_display"], wa_url("Hola 😊 Quiero información sobre vuestras personalizaciones."))
    contact_item("phone", BUSINESS["phone_display"], f"tel:+{BUSINESS['phone_raw']}")
    contact_item("instagram", f"@{BUSINESS['instagram_user']}", BUSINESS["instagram_url"])
    contact_item("mail", BUSINESS["email"], f"mailto:{BUSINESS['email']}")
    st.markdown("</div>", unsafe_allow_html=True)
