import streamlit as st
import pandas as pd

st.set_page_config(page_title="REGIMEGUARD Public Demo", layout="wide")
st.title("REGIMEGUARD — Public Demo (Universal Core Only)")

st.markdown("**21 Universal Attractor Families** validated across cloud/tree/sun/windshield (p < 0.0005)")

core = pd.read_csv("universal_core_families.csv")
consistency = pd.read_csv("universal_core_consistency_summary.csv")
metrics = pd.read_csv("universal_core_metrics_by_domain.csv")

col1, col2, col3 = st.columns([2, 3, 3])

with col1:
    st.subheader("Universal Core Families")
    st.dataframe(core, use_container_width=True)

with col2:
    st.subheader("Consistency Rankings (top 10)")
    st.dataframe(consistency[["family_uid", "domains_present", "omega_attractor_score_mean", 
                              "omega_attractor_score_std", "return_probability_mean", 
                              "basin_score_mean"]].head(10), use_container_width=True)

with col3:
    st.subheader("Per-Domain Metrics (sample)")
    st.dataframe(metrics.head(10), use_container_width=True)

st.markdown("---")
st.caption("This demo uses only the publicly validated universal core. Full enterprise console is private.")