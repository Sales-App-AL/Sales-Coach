import streamlit as st

# Konfiguration der Seite
st.set_page_config(page_title="Sales-Trainer: Fokus Schule", layout="centered")

def main():
    st.title("🎓 Schul-Vertriebs-Coach")
    st.subheader("Trainiere dein Verhalten in Verkaufsgesprächen")

    # Auswahl des Gesprächspartners
    persona = st.selectbox(
        "Mit wem sprichst du?",
        ["Schulleitung (Fokus: Budget & Vision)", 
         "IT-Beauftragter (Fokus: Technik & Datenschutz)", 
         "Lehrkraft (Fokus: Zeitersparnis & Didaktik)"]
    )

    # Definition der Szenarien
    scenarios = {
        "Schulleitung (Fokus: Budget & Vision)": {
            "frage": "Das klingt interessant, aber wir haben aktuell absolut kein Budget für neue Software.",
            "tipp": "Gehe auf Fördermittel (z.B. DigitalPakt) ein oder betone die langfristige Ersparnis."
        },
        "IT-Beauftragter (Fokus: Technik & Datenschutz)": {
            "frage": "Wie sieht es mit der DSGVO-Konformität aus? Wo liegen die Server?",
            "tipp": "Nenne Fakten zum Serverstandort (z.B. Deutschland) und zur Verschlüsselung."
        },
        "Lehrkraft (Fokus: Zeitersparnis & Didaktik)": {
            "frage": "Noch ein Tool? Ich habe keine Zeit, mich in etwas Neues einzuarbeiten.",
            "tipp": "Betone die intuitive Bedienung und die Zeitersparnis bei der Unterrichtsvorbereitung."
        }
    }

    current_scenario = scenarios[persona]

    # Anzeige der Situation
    st.info(f"**Situation:** {current_scenario['frage']}")

    # Eingabe der Antwort
    user_answer = st.text_area("Deine Antwort:", placeholder="Schreibe hier, wie du reagieren würdest...")

    if st.button("Antwort prüfen"):
        if len(user_answer) < 10:
            st.warning("Deine Antwort ist etwas kurz. Versuche, mehr auf die Bedürfnisse einzugehen.")
        else:
            st.success("Guter Ansatz! Vergleiche deine Antwort mit unserem Coaching-Tipp:")
            st.write(f"💡 **Tipp:** {current_scenario['tipp']}")
            st.balloons()

if __name__ == "__main__":
    main()
