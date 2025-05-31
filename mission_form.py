import streamlit as st
from calendar_creator import generate_calendar

st.set_page_config(layout="wide")
st.title("Calendrier de mission PEP")

# Saisie des données
mission_start = st.text_input("Date de début de mission (jj/mm/aaaa)")
mission_end = st.text_input("Date de fin de mission (jj/mm/aaaa)")
len_mission = st.number_input("Durée de la mission en semaines", min_value=1)

st.markdown("---")

num_phases = st.number_input("Nombre de phases", min_value=1)
phases = []

st.markdown("Détails des phases")
for i in range(int(num_phases)):
    with st.expander(f"Phase {i+1}"):
        duration = st.number_input(f"Durée de la phase {i+1} (en semaines)", min_value=1, key=f"dur_{i}")
        start = st.number_input(f"Semaine de début de la phase {i+1}", min_value=0, max_value=int(len_mission)-1, key=f"start_{i}")
        jehs = st.number_input(f"Nombre de JEH(s) pour la phase {i+1}", min_value=0, key=f"jeh_{i}")
        phases.append([duration, start, start + duration, jehs])

st.markdown("---")

# Génération
if st.button("Générer le calendrier") and phases:
    phases = phases[::-1]
    filename = generate_calendar(mission_start, mission_end, len_mission, phases)
    st.image(filename, use_column_width=True)
    with open(filename, "rb") as f:
        st.download_button("Télécharger le calendrier en png", f, file_name="calendrier_mission.png")
