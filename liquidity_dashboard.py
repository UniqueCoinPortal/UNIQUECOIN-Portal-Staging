import streamlit as st

st.set_page_config(page_title="UNIQ Liquidity Pulse Monitor", layout="centered")

st.title("💧 UNIQ Liquidity Pulse Monitor")

st.subheader("📈 Price & Depth")
st.metric(label="Current Price", value="$0.042")
st.metric(label="Liquidity Depth", value="$12,500")

st.subheader("📊 APR & Pool Metrics")
st.write("APR: 8.2%")
st.write("Pool Size: 300,000 UNIQ")

st.subheader("📜 Manifest")
with open("liquidity_manifest.md", "r") as f:
    manifest = f.read()
st.code(manifest, language="markdown")
