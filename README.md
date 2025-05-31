<h1>
  <img src="https://github.com/user-attachments/assets/451fe7b3-895d-4cf8-9704-e37e25edea98" alt="logo" width="60" style="vertical-align: middle; margin-right: 10px;"/>
Mission Calendar Generator for Ponts Études Projets
</h1>


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
