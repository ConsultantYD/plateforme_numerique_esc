from streamlit_bokeh_events import streamlit_bokeh_events
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
import streamlit as st

units_list = [
    "GC 1201",
    "GC 1202",
    "GC 1203",
    "GC 1204",
    "GC 1205",
    "GC 1209",
]

st.sidebar.selectbox("Choisir votre unité", units_list)
st.sidebar.button("Utiliser ma position")
st.sidebar.title("À Propos")
st.sidebar.info(
    "La plateforme numérique ESC est un outil ... \n\n" +
    "Le programme ESC est un programme de la Garde Côtière ...")
#st.sidebar.image('logo.png')
st.sidebar.title("Auteur")
st.sidebar.info("Ysael Desage")
