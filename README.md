# Calendar-Generator ![logo-couleur](https://github.com/user-attachments/assets/a744f79b-dfa5-46a6-aec0-4c4ed2f944ae)


This application lets you generate a mission timeline with customizable phases, durations, and JEHs (working units), then download it as a png image. It was made as a tool for Ponts Etudes Projets, the junior consulting association from Ponts Uni. 

Online tool is available here : [https://pepcalendar.streamlit.app/](https://pepcalendar.streamlit.app/)


How to Use

1. Enter mission start and end dates
2. Set the total mission duration (in weeks)
3. Define your phases (duration, start week, JEHs)
4. Click **Generate Calendar**
5. Download the PNG image


Run Locally 

```bash
git clone https://github.com/your-username/mission-calendar.git
cd mission-calendar
pip install -r requirements.txt
streamlit run app.py
