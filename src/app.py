import streamlit as st
from src import database

st.set_page_config(page_title="AI Property Deal Hunter", layout="wide")

st.title("🏠 AI Property Deal Hunter Dashboard")
st.caption("View, search, and filter real estate deals scored by the AI engine.")

try:
    df = database.get_listings()
    st.success(f"✅ Loaded {len(df)} listings.")
except Exception as e:
    st.error(f"Failed to load data: {e}")
    df = None

if df is not None and not df.empty:
    with st.sidebar:
        st.header("🔍 Filters")
        cities = df["city"].unique()
        selected_cities = st.multiselect("City", cities, default=cities)
        min_score = st.slider("Minimum Deal Score", 0, 100, 0)

    filtered = df[df["city"].isin(selected_cities) & (df["deal_score"] >= min_score)]
    st.write(f"### Showing {len(filtered)} matching deals")
    st.dataframe(filtered.sort_values("deal_score", ascending=False), use_container_width=True)
else:
    st.warning("No data found in the database.")