import streamlit as st
import json
import os
from pathlib import Path

# Base directory (where this script lives)
BASE_DIR = Path(__file__).parent

# --- Safe file loaders ---
def load_contributors():
    file_path = BASE_DIR / "contributors.json"
    if file_path.exists():
        with open(file_path, "r") as f:
            return json.load(f)
    # Fallback placeholder
    return [
        {"name": "Placeholder User", "role": "Contributor"},
        {"name": "Demo Admin", "role": "Administrator"}
    ]

def load_mutations():
    file_path = BASE_DIR / "mutation_log.md"
    if file_path.exists():
        with open(file_path, "r") as f:
            return f.read()
    # Fallback placeholder
    return "# 🧬 Mutation History\n\nNo mutations have been recorded yet.\n"

# --- Load data safely ---
contributors = load_contributors()
mutations = load_mutations()
current = contributors[0] if contributors else {"name": "Unknown", "role": "N/A"}

# --- Streamlit UI ---
st.set_page_config(page_title="UniqueCoin Contributor Portal", layout="centered")

st.title("🌌 UniqueCoin Contributor Portal")

st.subheader("🚀 Current Contributor")
st.info(f"**{current['name']}** — {current['role']}\n\nStatus: Onboarding Stage")

st.subheader("🎭 Roles")
roles = [c["role"] for c in contributors]
st.write("\n".join(roles))

st.subheader("🧬 Mutation History")
st.code(mutations, language="markdown")
