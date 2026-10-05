import streamlit as st
import sqlite3

# ---------------------------------------------------------
# 1. PAGE CONFIGURATION & STYLING
# ---------------------------------------------------------
st.set_page_config(page_title="Local Store App", page_icon="🛍️", layout="centered")

st.markdown("""
    <style>
    /* Mobile Container Setup */
    .stApp {
        max-width: 450px;
        margin: 0 auto;
        background-color: #f8f9fa;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Header Banner */
    .banner {
        background: linear-gradient(135deg, #007bff, #00c6ff);
        color: white;
        padding: 16px;
        border-radius: 14px;
        margin-bottom: 15px;
    }
    
    /* Shop & Product Cards */
    .card {
        background-color: white;
        padding: 14px;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.06);
        margin-bottom: 12px;
        border: 1px solid #eee;
    }
    .badge {
        background-color: #e3f2fd;
        color: #0d6efd;
        padding: 3px 8px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 600;
    }
    .price-tag {
        color: #28a745;
        font-weight: bold;
        font-size: 15px;
    }
    
    /* Profile Stats */
    .stat-box {
        text-align: center;
        background: white;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 2. DATABASE INITIALIZATION (SQLite)
# ---------------------------------------------------------
def init_db():
    conn = sqlite3.connect("local_store.db")
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS shops 
                      (id INTEGER PRIMARY KEY, name TEXT, category TEXT, distance TEXT, rating REAL, reviews INTEGER, status TEXT)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS products 
                      (id INTEGER PRIMARY KEY, shop_name TEXT, name TEXT, category TEXT, price REAL, brand TEXT, weight TEXT, description TEXT)''')
    
    cursor.execute("SELECT COUNT(*) FROM shops")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO shops VALUES (1, 'Sharma General Store', 'Groceries', '1.2 km', 4.5, 120, 'Open')")
        cursor.execute("INSERT INTO shops VALUES (2, 'Pandey Mobile Shop', 'Electronics', '1.8 km', 4.3, 85, 'Open')")
        cursor.execute("INSERT INTO shops VALUES (3, 'Raju Fashion', 'Fashion', '2.3 km', 4.1, 45, 'Open')")
        cursor.execute("INSERT INTO shops VALUES (4, 'Verma Electronics', 'Electronics', '2.8 km', 4.6, 92, 'Closed')")
        
        cursor.execute("INSERT INTO products VALUES (1, 'Sharma General Store', 'Maggi 2-Min Noodles', 'Groceries', 15.0, 'Nestle', '70 g', 'Tasty and healthy instant noodles for everyone.')")
        cursor.execute("INSERT INTO products VALUES (2, 'Sharma General Store', 'Detergent Powder', 'Groceries', 120.0, 'Surf Excel', '1 kg', 'Effective stain removal detergent.')")
        cursor.execute("INSERT INTO products VALUES (3, 'Sharma General Store', 'Biscuits Packet', 'Groceries', 20.0, 'Parle-G', '250 g', 'Crunchy glucose biscuits.')")
        cursor.execute("INSERT INTO products VALUES (4, 'Sharma General Store', 'Premium Tea', 'Groceries', 60.0, 'Tata Tea', '250 g', 'Rich taste and aroma tea.')")
        
        conn.commit()
    conn.close()

init_db()

# Session State for Page Navigation
if 'page' not in st.session_state:
    st.session_state.page = "🏠 Home"
if 'selected_shop' not in st.session_state:
    st.session_state.selected_shop = None
if 'selected_product' not in st.session_state:
    st.session_state.selected_product = None

# ---------------------------------------------------------
# 3. NAVIGATION BAR
# ---------------------------------------------------------
nav_page = st.radio(
    "",
    ["🏠 Home", "🔍 Search", "🔖 Subscriptions", "👤 Profile"],
    horizontal=True,
    key="nav_radio"
)

if nav_page != st.session_state.page and not (st.session_state.page in ["Shop Detail", "Product Detail", "Add Product"]):
    st.session_state.page = nav_page

st.divider()

# ---------------------------------------------------------
# SCREEN 1: HOME PAGE
# ---------------------------------------------------------
if st.session_state.page == "🏠 Home":
    st.markdown("### 📍 Local Store")
    st.caption("Find your local shops & products")
    
    st.text_input("🔍 Search for products or shops...", key="home_search_input")
    
    st.markdown("""
        <div class="banner">
            <h3 style="margin:0;">Support Local Business</h3>
            <p style="margin:4px 0 0 0; font-size:13px;">Shop local • Grow together ➔</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("#### Categories")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.button("🛒\nGrocery")
    with c2: st.button("👕\nFashion")
    with c3: st.button("📱\nElectronics")
    with c4: st.button("🏠\nHome")
    
    st.markdown("---")
    st.markdown("#### Nearby Shops")
    
    conn = sqlite3.connect("local_store.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, distance, rating, reviews, status FROM shops")
    shops = cursor.fetchall()
    conn.close()
    
    for shop in shops:
        s_id, s_name, s_cat, s_dist, s_rating, s_rev, s_status = shop
        with st.container():
            st.markdown(f"""
                <div class="card">
                    <h4 style="margin:0;">{s_name}</h4>
                    <p style="margin:4px 0; color:#555; font-size:12px;">📍 {s_dist} • <span style="color:green;">{s_status}</span></p>
                    <p style="margin:0; color:#f39c12; font-size:12px;">⭐ {s_rating} ({s_rev} reviews)</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"View Shop ➔ {s_name}", key=f"shop_btn_{s_id}"):
                st.session_state.selected_shop = s_name
                st.session_state.page = "Shop Detail"
                st.rerun()

# ---------------------------------------------------------
# SCREEN 2: SEARCH PAGE
# ---------------------------------------------------------
elif st.session_state.page == "🔍 Search":
    st.markdown("### Search")
    st.text_input("🔍 Search products or shops...", key="search_query")
    
    st.radio("Filter Type:", ["Products", "Shops"], horizontal=True)
    
    st.markdown("#### Popular Searches")
    p1, p2, p3, p4 = st.columns(4)
    p1.caption("Mobile")
    p2.caption("Shoes")
    p3.caption("Groceries")
    p4.caption("Dairy")
    
    st.markdown("#### Recent Searches")
    st.text("🕒 mobile")
    st.text("🕒 shoes")
    st.text("🕒 milk")
    st.text("🕒 laptop")

# ---------------------------------------------------------
# SCREEN 3: SUBSCRIPTIONS PAGE
# ---------------------------------------------------------
elif st.session_state.page == "🔖 Subscriptions":
    st.markdown("### My Subscriptions")
    st.caption("Shops you follow")
    
    st.radio("", ["Shops (4)", "Products (0)"], horizontal=True)
    
    conn = sqlite3.connect("local_store.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, distance FROM shops")
    shops = cursor.fetchall()
    conn.close()
    
    for shop in shops:
        col_a, col_b = st.columns([3, 1])
        with col_a:
            st.markdown(f"**{shop[0]}**\n<br><span style='font-size:12px; color:#666;'>📍 {shop[1]}</span>", unsafe_allow_html=True)
        with col_b:
            st.button("Following", key=f"sub_{shop[0]}")
        st.divider()

# ---------------------------------------------------------
# SCREEN 4: SHOP DETAIL PAGE
# ---------------------------------------------------------
elif st.session_state.page == "Shop Detail":
    if st.button("⬅️️ Back"):
        st.session_state.page = "🏠 Home"
        st.rerun()
        
    shop_name = st.session_state.selected_shop
    st.title(shop_name)
    st.caption("📍 1.2 km • ⭐ 4.5 (120 reviews) • Open")
    st.write("Your one-stop shop for daily essentials, groceries, stationery and more.")
    
    st.button("💙 Follow Shop", use_container_width=True)
    
    st.markdown("#### Top Products")
    
    conn = sqlite3.connect("local_store.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price FROM products WHERE shop_name=?", (shop_name,))
    products = cursor.fetchall()
    conn.close()
    
    for p in products:
        p_id, p_name, p_price = p
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"**{p_name}**\n<br><span class='price-tag'>₹ {p_price}</span>", unsafe_allow_html=True)
        with col2:
            if st.button("Add", key=f"prod_add_{p_id}"):
                st.session_state.selected_product = p_id
                st.session_state.page = "Product Detail"
                st.rerun()
        st.divider()

# ---------------------------------------------------------
# SCREEN 5: PRODUCT DETAILS PAGE
# ---------------------------------------------------------
elif st.session_state.page == "Product Detail":
    if st.button("⬅️ Back to Shop"):
        st.session_state.page = "Shop Detail"
        st.rerun()
        
    p_id = st.session_state.selected_product
    conn = sqlite3.connect("local_store.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, price, brand, category, weight, description, shop_name FROM products WHERE id=?", (p_id,))
    prod = cursor.fetchone()
    conn.close()
    
    if prod:
        name, price, brand, category, weight, desc, s_name = prod
        st.header(name)
        st.markdown(f"<h3 class='price-tag'>₹ {price}</h3>", unsafe_allow_html=True)
        st.caption("⭐ 4.5 (120 reviews) • In Stock")
        
        st.button("🛒 Add to Cart", type="primary", use_container_width=True)
        
        st.markdown("#### Product Details")
        st.write(f"**Brand:** {brand}")
        st.write(f"**Category:** {category}")
        st.write(f"**Weight:** {weight}")
        st.write(f"**Description:** {desc}")
        
        st.markdown("#### Shop Information")
        st.write(f"🏬 **{s_name}**")

# ---------------------------------------------------------
# SCREEN 6: PROFILE PAGE
# ---------------------------------------------------------
elif st.session_state.page == "👤 Profile":
    st.markdown("### Profile")
    
    st.markdown("### 👤 Alok Singh")
    st.caption("alok@gmail.com")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='stat-box'><b>5</b><br><small>Followers</small></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='stat-box'><b>3</b><br><small>Following</small></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='stat-box'><b>12</b><br><small>Likes</small></div>", unsafe_allow_html=True)
        
    st.divider()
    st.button("📦 My Orders", use_container_width=True)
    st.button("🔖 My Subscriptions", use_container_width=True)
    st.button("❤️ My Likes", use_container_width=True)
    
    if st.button("🏪 Shop Dashboard (For Shopkeepers)", use_container_width=True):
        st.session_state.page = "Add Product"
        st.rerun()
        
    st.button("⚙️ Settings", use_container_width=True)
    st.button("❓ Help & Support", use_container_width=True)

# ---------------------------------------------------------
# SCREEN 7: ADD PRODUCT PAGE
# ---------------------------------------------------------
elif st.session_state.page == "Add Product":
    if st.button("⬅️ Back to Profile"):
        st.session_state.page = "👤 Profile"
        st.rerun()
        
    st.markdown("### ➕ Add Product")
    
    uploaded_file = st.file_uploader("Add Product Image", type=["jpg", "png", "jpeg"])
    
    p_name = st.text_input("Product Name *")
    p_cat = st.selectbox("Category *", ["Groceries", "Fashion", "Electronics", "Home & Kitchen"])
    p_price = st.number_input("Price *", min_value=0.0, step=1.0)
    p_desc = st.text_area("Description")
    
    if st.button("Save Product", type="primary", use_container_width=True):
        if p_name and p_price > 0:
            conn = sqlite3.connect("local_store.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO products VALUES (NULL, 'Sharma General Store', ?, ?, ?, 'Generic', '1 unit', ?)", 
                           (p_name, p_cat, p_price, p_desc))
            conn.commit()
            conn.close()
            st.success("✅ Product Saved Successfully!")
        else:
            st.error("कृपया प्रोडक्ट का नाम और कीमत सही भरें।")
