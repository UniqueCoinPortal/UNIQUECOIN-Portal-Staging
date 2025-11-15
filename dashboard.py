import streamlit as st
import json

# Load contributors
with open("contributors.json", "r") as f:
    contributors = json.load(f)

# Load mutation log
with open("mutation_log.md", "r") as f:
    mutations = f.read()

# Current contributor
current = contributors[0]

st.set_page_config(page_title="UniqueCoin Contributor Portal", layout="centered")

st.title("🌌 UniqueCoin Contributor Portal")

st.subheader("🚀 Current Contributor")
st.info(f"**{current['name']}** — {current['role']}\n\nStatus: Onboarding Stage")

st.subheader("🎭 Roles")
roles = [c["role"] for c in contributors]
st.write("\n".join(roles))

st.subheader("🧬 Mutation History")
st.code(mutations, language="markdown")

import streamlit as st
import json

# Load contributors
with open("contributors.json", "r") as f:
    contributors = json.load(f)

# Load mutation log
with open("mutation_log.md", "r") as f:
    mutations = f.read()

# Current contributor
current = contributors[0]

st.set_page_config(page_title="UniqueCoin Contributor Portal", layout="centered")

st.title("🌌 UniqueCoin Contributor Portal")

st.subheader("🚀 Current Contributor")
st.info(f"**{current['name']}** — {current['role']}\n\nStatus: Onboarding Stage")

st.subheader("🎭 Roles")
roles = [c["role"] for c in contributors]
st.write("\n".join(roles))

st.subheader("🧬 Mutation History")
st.code(mutations, language="markdown")
