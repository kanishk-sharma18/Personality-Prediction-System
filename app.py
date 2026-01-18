import streamlit as st
import pandas as pd
from model import predict_personality

st.set_page_config(
    page_title="Personality Prediction",
    layout="centered"
)

st.markdown("""
<style>
div[role="radiogroup"] > label {
    font-size: 20px !important;
    padding: 12px 18px !important;
    margin-right: 12px !important;
}

div[role="radiogroup"] input[type="radio"] {
    transform: scale(1.7);
    margin-right: 8px;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    "<h1 style='text-align:center;'>🧠 Personality Prediction System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align:center;'>Rate yourself from 1 (Low) to 5 (High)</h3>",
    unsafe_allow_html=True
)

st.markdown("<h2>I feel energetic around people</h2>", unsafe_allow_html=True)
social_energy = st.radio(
    "social_energy",
    [1, 2, 3, 4, 5],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("<h2>I prefer spending time alone</h2>", unsafe_allow_html=True)
alone_time_preference = st.radio(
    "alone_time_preference",
    [1, 2, 3, 4, 5],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("<h2>I am talkative</h2>", unsafe_allow_html=True)
talkativeness = st.radio(
    "talkativeness",
    [1, 2, 3, 4, 5],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("<h2>I feel comfortable in groups</h2>", unsafe_allow_html=True)
group_comfort = st.radio(
    "group_comfort",
    [1, 2, 3, 4, 5],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("<h2>I enjoy parties and social events</h2>", unsafe_allow_html=True)
party_liking = st.radio(
    "party_liking",
    [1, 2, 3, 4, 5],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("<h2>I am comfortable with public speaking</h2>", unsafe_allow_html=True)
public_speaking_comfort = st.radio(
    "public_speaking_comfort",
    [1, 2, 3, 4, 5],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("<h2>I am friendly with new people</h2>", unsafe_allow_html=True)
friendliness = st.radio(
    "friendliness",
    [1, 2, 3, 4, 5],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔮 Predict Personality"):

    user_input = pd.DataFrame([{
        'social_energy': social_energy,
        'alone_time_preference': alone_time_preference,
        'talkativeness': talkativeness,
        'group_comfort': group_comfort,
        'party_liking': party_liking,
        'public_speaking_comfort': public_speaking_comfort,
        'friendliness': friendliness
    }])

    score, personality = predict_personality(user_input)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("<h2>🔍 Result</h2>", unsafe_allow_html=True)

    st.markdown(
        f"<h1 style='color:#4CAF50;'>Personality: {personality}</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        f"<h2>Social Score: {score}</h2>",
        unsafe_allow_html=True
    )
