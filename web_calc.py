import streamlit as st
from machining_formulas import (calc_rpm_inches,
                                calc_sfm_inches,
                                calc_feed_rate_inches,
                                calc_material_removal_rate)

st.header("Machining Calculator")

st.subheader("Calculate:")

with st.expander('RPM'):
    st.write("""
        The expander lets you hide details until the user clicks to expand.
        This is useful for FAQs, extra info, or optional settings.
    """)
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=150)
    feedback = st.text_area("Calculate RPM")
    if st.button("Calc"):
        st.success(f"✅ You entered {feedback} ")

with st.expander('Feed Rate'):
    st.write("""
        The expander lets you hide details until the user clicks to expand.
        This is useful for FAQs, extra info, or optional settings.
    """)
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=150)
with st.expander('SFM'):
    st.write("""
        The expander lets you hide details until the user clicks to expand.
        This is useful for FAQs, extra info, or optional settings.
    """)
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=150)
with st.expander('Material Removal Rate'):
    st.write("""
        The expander lets you hide details until the user clicks to expand.
        This is useful for FAQs, extra info, or optional settings.
    """)
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=150)
