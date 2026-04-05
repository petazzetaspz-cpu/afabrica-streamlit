from pathlib import Path
from urllib.parse import quote
import html
import streamlit as st

st.set_page_config(
    page_title="A fábrica das ideas",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE = Path(__file__).parent
ASSETS = BASE / "assets"

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

LOGO = ASSETS / "logo_principal.png"
HERO = ASSETS / "IMG-20250906-WA0010.jpg"
EVENT = ASSETS / "Camisetas fiesta tematica.jpeg"

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
            ("Camiseta personalizada", "Desde 12€", "👕 Niños 12€ · Adultos 15€", "IMG-20250906-WA0021.jpg"),
            ("Taza personalizada", "9€", "☕ Con foto, nombre o diseño especial", "IMG-20250906-WA0010.jpg"),
            ("Termo personalizado", "13,90€", "🥤 Acero inox 500 ml", "IMG-20250906-WA0030.jpg"),
            ("Botella infantil", "8,50€", "🧒 Aluminio 550 ml", "IMG-20250906-WA0031.jpg"),
            ("Body bebé personalizado", "12€", "👶 Dulce y muy especial", "WhatsApp Image 2026-02-05 at 23.02.23 (1).jpeg"),
            ("Neceser personalizado", "5€", "🎀 Ideal para regalar", "WhatsApp Image 2026-02-05 at 23.02.23.jpeg"),
            ("Calcetines personalizados", "6€", "🧦 Originales y divertidos", "Calcetines.jpeg"),
            ("Bolsa merienda", "4,90€", "🍪 Medida 20 x 25 cm", "IMG-20250906-WA0025.jpg"),
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
            ("Bordado pequeño", "Desde 5€", "🪡 Nombre o detalle sencillo", "WhatsApp Image 2026-03-29 at 14.13.54.jpeg"),
            ("Camiseta bordada", "Desde 15€", "👕 Nombre bordado en pecho", "WhatsApp Image 2026-03-27 at 22.02.25.jpeg"),
            ("Saquito bordado", "Consultar", "🎁 Ideal para regalo", "WhatsApp Image 2026-03-29 at 14.13.54.jpeg"),
            ("Pack padre e hija", "Consultar", "💞 Conjunto personalizado", "Camiseta padre e hija.jpeg"),
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
            ("Grabado en madera 12 cm", "12€", "🪵 Circular con soporte", "WhatsApp Image 2026-03-29 at 14.13.55.jpeg"),
            ("Grabado en madera 16 cm", "16€", "🪵 Circular con soporte", "Padre e hijo.jpeg"),
            ("Grabado en madera 18 cm", "18€", "🪵 Circular con soporte", "Caballo.jpeg"),
            ("Placa rectangular", "16€", "📏 Tamaño 13 x 17 cm", "Dia del padre.jpeg"),
        ],
        "gallery": ["Padre e hijo.jpeg", "Caballo.jpeg", "Dia del padre.jpeg", "WhatsApp Image 2026-03-29 at 14.13.55.jpeg"],
    },
}


def asset(name: str) -> str:
    return str(ASSETS / name)


def wa_url(message: str) -> str:
    return f"https://wa.me/{BUSINESS['phone_raw']}?text={quote(message)}"


def section_badge(text: str, color: str) -> None:
    st.markdown(
        f"<div class='section-badge' style='background:{color}'>{html.escape(text)}</div>",
        unsafe_allow_html=True,
    )


def product_card(item) -> None:
    name, price, desc, image = item
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    st.image(asset(image), use_container_width=True)
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


def gallery_grid(images) -> None:
    cols = st.columns(3, gap="medium")
    for i, name in enumerate(images):
        with cols[i % 3]:
            st.image(asset(name), use_container_width=True)


def contact_item(kind: str, label: str, href: str) -> None:
    icons = {
        "whatsapp": "💬",
        "instagram": "📸",
        "phone": "📞",
        "mail": "✉️",
    }
    st.markdown(
        f"<a class='contact-item' href='{href}' target='_blank'>"
        f"<span class='cicon {kind}'>{icons[kind]}</span><span>{html.escape(label)}</span></a>",
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
        for col, item in zip(cols, row):
            with col:
                product_card(item)


def render_gallery(key: str):
    data = SECTIONS[key]
    color = SECTION_COLORS[key]
    section_badge(f"📸 Galería · {data['name']}", color)
    gallery_grid(data['gallery'])


st.markdown(
    f"""
<style>
html, body, [class*="css"] {{ font-family: 'Segoe UI', sans-serif; }}
.stApp {{ background: {COLORS['bg']}; }}
.main .block-container {{ max-width: 1180px; padding-top: .6rem; padding-bottom: 4rem; }}
#MainMenu, footer, [data-testid="stStatusWidget"], [data-testid="stDecoration"], [data-testid="stSidebarNav"] {{ display:none !important; }}
.logo-wrap {{ text-align:center; margin: .1rem 0 .45rem 0; }}
.topbar {{ width:min(960px, 94%); margin:.15rem auto .75rem auto; height:15px; border-radius:999px; background:linear-gradient(90deg, rgba(242,153,181,.42) 0%, rgba(245,220,158,.40) 18%, rgba(189,231,220,.38) 36%, rgba(201,192,202,.36) 50%, rgba(255,255,255,0) 50%, rgba(255,255,255,0) 100%); }}
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
.cicon.whatsapp {{ background:#EAF9F0; }}
.cicon.instagram {{ background:#FCEAF4; }}
.cicon.phone {{ background:#EEF3FF; }}
.cicon.mail {{ background:#FFF6E2; }}
[data-testid="stSidebar"] {{ background:#fff; border-right:1px solid {COLORS['line']}; }}
[data-testid="collapsedControl"] {{ display:block !important; position:fixed !important; top:12px; left:12px; z-index:1001; }}
[data-testid="collapsedControl"] button {{ background:#fff !important; border:1px solid {COLORS['line']} !important; border-radius:16px !important; width:46px !important; height:46px !important; box-shadow:0 8px 18px rgba(0,0,0,.08) !important; }}
[data-testid="collapsedControl"] svg {{ width:22px !important; height:22px !important; }}
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
    st.markdown("<div class='sidebar-group'>Productos</div>", unsafe_allow_html=True)
    if st.button("🎨 Impresión", use_container_width=True):
        set_page("Productos · Impresión")
    if st.button("🧵 Bordado", use_container_width=True):
        set_page("Productos · Bordado")
    if st.button("🔥 Grabado y corte", use_container_width=True):
        set_page("Productos · Grabado")
    st.markdown("<div class='sidebar-group'>Galería</div>", unsafe_allow_html=True)
    if st.button("📸 Impresión", use_container_width=True):
        set_page("Galería · Impresión")
    if st.button("📸 Bordado", use_container_width=True):
        set_page("Galería · Bordado")
    if st.button("📸 Grabado y corte", use_container_width=True):
        set_page("Galería · Grabado")
    st.markdown("<div class='sidebar-group'>Contacto</div>", unsafe_allow_html=True)
    if st.button("💬 Formas de contactar", use_container_width=True):
        set_page("Contacto")

st.image(str(LOGO), use_container_width=True)
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

elif page == "Productos · Impresión":
    render_products("impresion")
elif page == "Productos · Bordado":
    render_products("bordado")
elif page == "Productos · Grabado":
    render_products("grabado")
elif page == "Galería · Impresión":
    render_gallery("impresion")
elif page == "Galería · Bordado":
    render_gallery("bordado")
elif page == "Galería · Grabado":
    render_gallery("grabado")
elif page == "Contacto":
    st.markdown("<div class='contact-box'>", unsafe_allow_html=True)
    st.markdown("### 💬 Contacto")
    contact_item("whatsapp", BUSINESS["phone_display"], wa_url("Hola 😊 Quiero información sobre vuestras personalizaciones."))
    contact_item("phone", BUSINESS["phone_display"], f"tel:+{BUSINESS['phone_raw']}")
    contact_item("instagram", f"@{BUSINESS['instagram_user']}", BUSINESS["instagram_url"])
    contact_item("mail", BUSINESS["email"], f"mailto:{BUSINESS['email']}")
    st.markdown("</div>", unsafe_allow_html=True)
