import streamlit as st
from openai import OpenAI

# Konfiguration der Seite
st.set_page_config(page_title="Sales-Trainer: KI-Edition", layout="centered")

def main():
    st.title("🎓 Schul-Vertriebs-Coach (KI)")
    st.subheader("Trainiere mit echtem KI-Feedback")

    # 1. API-Schlüssel Eingabe (Sicher über die App)
    st.info("Um das KI-Feedback zu nutzen, benötigst du einen OpenAI API-Schlüssel.")
    api_key = st.text_input("Dein OpenAI API-Schlüssel (beginnt mit sk-...):", type="password")
    
    # 2. Auswahl des Gesprächspartners
    persona = st.selectbox(
        "Mit wem sprichst du?",
        ["Schulleitung (Fokus: Budget & Vision)", 
         "IT-Beauftragter (Fokus: Technik & Datenschutz)", 
         "Lehrkraft (Fokus: Zeitersparnis & Didaktik)"]
    )

    # 3. Definition der Szenarien
    scenarios = {
        "Schulleitung (Fokus: Budget & Vision)": "Das klingt interessant, aber wir haben aktuell absolut kein Budget für neue Software.",
        "IT-Beauftragter (Fokus: Technik & Datenschutz)": "Wie sieht es mit der DSGVO-Konformität aus? Wo liegen die Server?",
        "Lehrkraft (Fokus: Zeitersparnis & Didaktik)": "Noch ein Tool? Ich habe keine Zeit, mich in etwas Neues einzuarbeiten."
    }

    current_scenario = scenarios[persona]
    st.warning(f"**Der Einwand des Kunden:** {current_scenario}")

    # 4. Eingabe deiner Antwort
    user_answer = st.text_area("Deine Antwort:", placeholder="Schreibe hier, wie du reagieren würdest...")

    # 5. KI-Überprüfung
    if st.button("Antwort durch KI prüfen lassen"):
        if not api_key:
            st.error("Bitte gib oben deinen OpenAI API-Schlüssel ein.")
        elif len(user_answer) < 10:
            st.error("Deine Antwort ist etwas kurz. Versuche, genauer auf den Kunden einzugehen.")
        else:
            with st.spinner("Dein KI-Coach analysiert die Argumentation..."):
                try:
                    # Verbindung zu OpenAI herstellen
                    client = OpenAI(api_key=api_key)
                    
                    # Die geheime Anweisung an die KI, wie sie sich verhalten soll
                    system_prompt = f"""
                    Du bist ein professioneller und motivierender Sales-Coach für Software an Schulen.
                    Dein Schüler spricht gerade mit dieser Zielgruppe: {persona}.
                    Der Einwand des Kunden war: "{current_scenario}".
                    Die Antwort des Schülers lautet: "{user_answer}".
                    
                    Bewerte die Antwort des Schülers. 
                    1. Was war gut an der Argumentation?
                    2. Was könnte man besser machen oder noch hinzufügen, um den Kunden wirklich zu überzeugen?
                    Antworte in 3 bis 4 kurzen, verständlichen Sätzen und sei konstruktiv.
                    """
                    
                    # Anfrage an das moderne gpt-4o-mini Modell senden
                    response = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": system_prompt}]
                    )
                    
                    # Das generierte Feedback anzeigen
                    feedback = response.choices[0].message.content
                    st.success("Hier ist das Feedback deines KI-Coaches:")
                    st.write(feedback)
                    st.balloons()
                    
                except Exception as e:
                    st.error("Es gab ein Problem. Bitte prüfe, ob dein API-Schlüssel korrekt ist.")

if __name__ == "__main__":
    main()

