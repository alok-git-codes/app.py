import streamlit as st
from streamlit_option_menu import option_menu

# Page Config
st.set_page_config(page_title="Local Store", page_icon="🏪", layout="centered", initial_sidebar_state="collapsed")

# Complete App Styling for Modern App UI
st.markdown("""
<style>
    /* Hide Streamlit Default UI */
    #MainMenu, header, footer {visibility: hidden;}
    
    .block-container {
        padding-top: 1rem;
        padding-bottom: 5rem;
        max-width: 420px;
    }
    
    /* Input Box */
    div[data-baseweb="input"] {
        border-radius: 12px !important;
        background-color: #f1f5f9 !important;
        border: none !important;
    }
    
    /* Hero Banner */
    .banner-card {
        background: linear-gradient(135deg, #2563eb 0%, #3b82f6 100%);
        border-radius: 16px;
        padding: 18px;
        color: white;
        margin: 15px 0;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
    }
    
    /* Shop Card */
    .shop-card {
        background: white;
        border-radius: 14px;
        padding: 14px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        margin-bottom: 12px;
    }
    
    /* Category Card */
    .category-box {
        background-color: #f8fafc;
        border-radius: 12px;
        padding: 10px;
        text-align: center;
        border: 1px solid #e2e8f0;
        font-size: 12px;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Fixed Bottom Navigation Container
st.markdown('<div style="position: fixed; bottom: 0; left: 0; right: 0; z-index: 9999; background: white; border-top: 1px solid #e2e8f0;">', unsafe_allow_html=True)

# Real Mobile App Bottom Navigation Bar
selected = option_menu(
    menu_title=None,
    options=["Home", "Search", "Subscriptions", "Profile"],
    icons=["house-fill", "search", "bookmark-heart-fill", "person-fill"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "5px 0", "background-color": "#ffffff", "border-radius": "0px"},
        "icon": {"color": "#64748b", "font-size": "18px"},
        "nav-link": {
            "font-size": "11px",
            "text-align": "center",
            "margin": "0px",
            "padding": "6px",
            "color": "#64748b",
            "font-weight": "500",
        },
        "nav-link-selected": {
            "background-color": "transparent",
            "color": "#2563eb",
            "font-weight": "700"
        },
    }
)

st.markdown('</div>', unsafe_allow_html=True)

# ----------------- HOME SCREEN -----------------
if selected == "Home":
    st.markdown("### 📍 Local Store")
    st.text_input("Search for products or shops...", key="home_search", placeholder="🔍 Search products or shops...")
    
    st.markdown("""
        <div class="banner-card">
            <h3 style='margin:0; color:white;'>Support Local Business</h3>
            <p style='margin:4px 0 0 0; font-size:12px;'>Shop local • Grow together</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("##### Categories")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown('<div class="category-box">🛍️<br>Groceries</div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="category-box">👕<br>Fashion</div>', unsafe_allow_html=True)
    with c3: st.markdown('<div class="category-box">📱<br>Electronics</div>', unsafe_allow_html=True)
    with c4: st.markdown('<div class="category-box">🏠<br>Home</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### Nearby Shops")
    st.markdown("""
        <div class="shop-card">
            <h4 style="margin:0; color:#0f172a;">Sharma General Store</h4>
            <p style="margin:2px 0; font-size:12px; color:#64748b;">📍 1.2 km • ⭐ 4.5 (120)</p>
        </div>
        <div class="shop-card">
            <h4 style="margin:0; color:#0f172a;">Pandey Mobile Shop</h4>
            <p style="margin:2px 0; font-size:12px; color:#64748b;">📍 1.8 km • ⭐ 4.3 (85)</p>
        </div>
    """, unsafe_allow_html=True)

# ----------------- SEARCH SCREEN -----------------
elif selected == "Search":
    st.markdown("### Search")
    st.text_input("Search...", placeholder="Type product or shop name...")
    st.caption("Popular Searches: Mobile, Shoes, Groceries, Dairy")

# ----------------- SUBSCRIPTIONS SCREEN -----------------
elif selected == "Subscriptions":
    st.markdown("### My Subscriptions")
    st.info("Sharma General Store - Following")
    st.info("Pandey Mobile Shop - Following")

# ----------------- PROFILE SCREEN -----------------
elif selected == "Profile":
    st.markdown("### Profile")
    st.subheader("Alok Singh")
    st.caption("alok@gmail.com")
    st.divider()
    st.button("📦 My Orders", use_container_width=True)
    st.button("⚙️ Settings", use_container_width=True)
