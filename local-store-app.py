import streamlit as st
import sqlite3

# Page Configuration
st.set_page_config(page_title="Local Store", page_icon="🏪", layout="centered", initial_sidebar_state="collapsed")

# Custom CSS for Mobile Native Look & Style Matching Image
st.markdown("""
<style>
    /* Hide Streamlit Header & Footer elements */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Main app container */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 5rem;
        max-width: 450px;
    }
    
    /* Search Bar Customization */
    div[data-baseweb="input"] {
        border-radius: 12px !important;
        background-color: #f1f5f9 !important;
        border: none !important;
    }
    
    /* Banner Styling */
    .banner-card {
        background: linear-gradient(135deg, #0284c7 0%, #38bdf8 100%);
        border-radius: 16px;
        padding: 18px;
        color: white;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(2, 132, 199, 0.2);
    }
    
    /* Category Icons Container */
    .category-box {
        background-color: #f8fafc;
        border-radius: 14px;
        padding: 12px 8px;
        text-align: center;
        border: 1px solid #e2e8f0;
        font-size: 12px;
        font-weight: 600;
        color: #334155;
    }
    
    /* Shop Card Design */
    .shop-card {
        background: white;
        border-radius: 14px;
        padding: 14px;
        border: 1px solid #f1f5f9;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        margin-bottom: 15px;
    }
    
    /* Bottom Navigation Styling */
    div[data-testid="stRadio"] > label {
        display: none;
    }
    div[data-testid="stRadio"] > div {
        flex-direction: row;
        justify-content: space-around;
        background-color: #ffffff;
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        z-index: 999;
        padding: 10px 0px;
        border-top: 1px solid #e2e8f0;
        box-shadow: 0 -2px 10px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# App Title & Header
st.markdown("### 📍 Local Store")
st.caption("Find your local shops & products")

# Bottom Navigation Bar Simulation
nav = st.radio(
    "",
    ["🏠 Home", "🔍 Search", "🔖 Subscriptions", "👤 Profile"],
    horizontal=True,
    label_visibility="collapsed"
)

# ----------------- HOME PAGE -----------------
if nav == "🏠 Home":
    st.text_input("🔍 Search for products or shops...", key="home_search")
    
    # Hero Banner
    st.markdown("""
        <div class="banner-card">
            <h3 style='margin:0; color:white;'>Support Local Business</h3>
            <p style='margin:4px 0 0 0; font-size:13px; opacity:0.9;'>Shop local • Grow together</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Categories
    st.markdown("##### Categories")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.markdown('<div class="category-box">🛍️<br>Groceries</div>', unsafe_allow_html=True)
    with col2: st.markdown('<div class="category-box">👕<br>Fashion</div>', unsafe_allow_html=True)
    with col3: st.markdown('<div class="category-box">📱<br>Electronics</div>', unsafe_allow_html=True)
    with col4: st.markdown('<div class="category-box">🏠<br>Home</div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("##### Nearby Shops")
    
    # Shop 1
    st.markdown("""
        <div class="shop-card">
            <h4 style="margin:0; color:#1e293b;">Sharma General Store</h4>
            <p style="margin:2px 0; font-size:12px; color:#64748b;">📍 1.2 km • ⭐ 4.5 (120)</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Shop 2
    st.markdown("""
        <div class="shop-card">
            <h4 style="margin:0; color:#1e293b;">Pandey Mobile Shop</h4>
            <p style="margin:2px 0; font-size:12px; color:#64748b;">📍 1.8 km • ⭐ 4.3 (85)</p>
        </div>
    """, unsafe_allow_html=True)

# ----------------- SEARCH PAGE -----------------
elif nav == "🔍 Search":
    st.markdown("### Search")
    st.text_input("Search products or shops...", key="search_page_input")
    st.markdown("##### Popular Searches")
    st.info("Mobile • Shoes • Groceries • Dairy")

# ----------------- SUBSCRIPTIONS PAGE -----------------
elif nav == "🔖 Subscriptions":
    st.markdown("### My Subscriptions")
    st.caption("Shops you follow")
    
    st.button("Following: Sharma General Store")
    st.button("Following: Pandey Mobile Shop")

# ----------------- PROFILE PAGE -----------------
elif nav == "👤 Profile":
    st.markdown("### My Profile")
    st.subheader("Alok Singh")
    st.caption("alok@gmail.com")
    
    st.divider()
    st.button("📦 My Orders")
    st.button("🔖 My Subscriptions")
    st.button("⚙️ Settings")
