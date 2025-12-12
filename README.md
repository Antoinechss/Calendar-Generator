<h1>
  <img src="https://github.com/user-attachments/assets/451fe7b3-895d-4cf8-9704-e37e25edea98"
       alt="logo"
       width="60"
       style="vertical-align: middle; margin-right: 10px;"/>
  Mission Calendar Generator for Ponts Études Projets
</h1>

<p>
  <em>
    Interactive tool to generate mission timelines with customizable phases, durations,
    and JEHs, exportable as a PNG image.
  </em>
</p>

---

## Overview

This application allows users to generate a **mission timeline calendar** by defining
custom phases, durations, and JEHs (working units), and export the result as a PNG image.

It was developed as a practical tool for **Ponts Études Projets (PEP)**,
the junior consulting association of **École des Ponts**.

The online version is available here:  
https://pepcalendar.streamlit.app/

---

## How to Use

1. Enter the mission start and end dates  
2. Set the total mission duration (in weeks)  
3. Define mission phases (duration, start week, JEHs)  
4. Click **Generate Calendar**  
5. Download the generated PNG image  

---

## Run Locally

```bash
git clone https://github.com/your-username/mission-calendar.git
cd mission-calendar
pip install -r requirements.txt
streamlit run app.py
```
---
## Tech Stack : 

  - Python
  - Streamlit
  - Matplotlib (calendar rendering)
--- 
## Purpose

_This tool is designed to simplify mission planning and communication by providing
a clear, visual, and shareable project timeline._
