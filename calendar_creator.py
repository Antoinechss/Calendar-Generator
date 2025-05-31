import tkinter as tk

mission_start = "10/10/2025"
mission_end = "25/12/2025"
dates = "Du  " + str(mission_start) + "  au  " + str(mission_end)
len_mission = 17
phases = [[1,0,1,1],[3,0,3,3],[7,3,10,2],[3,10,13,1],[2,13,15,0]] # [duration, start, finish, JEHs]
num_phases = len(phases)

root = tk.Tk()
root.title("Mission calendar")

# window parameters

cell_width = 1000
cell_height = 400
margin_side = 150
margin_top = 100
calendarW = 800

canvas = tk.Canvas(root, width=cell_width, height=cell_height, bg="white")
canvas.pack()
week = calendarW//len_mission

barH = 20
bar_space = 20
calendarH = (barH+bar_space)*num_phases # bars are 20 height

# ----------------
# Drawing calendar bars and their labels
# ----------------

for i in range(num_phases) :
    #top left
    x1 = margin_side + phases[i][1]*week
    y1 = margin_top + i*(barH+bar_space)
    #bottom right
    x2 = x1 + phases[i][0]*week
    y2 = margin_top + i*bar_space +(i+1)*barH
    canvas.create_rectangle(x1, y1, x2, y2, fill="#2c3e50", outline="black") # Drawing bar
    lineY =  margin_top + barH + bar_space/2 +i*(barH+bar_space)
    canvas.create_line(margin_side-100,lineY, margin_side-100 + calendarW ,lineY, fill="grey", width=0.5)
    canvas.create_text((x1+x2)//2, y1+barH/2, text=str(phases[i][0]), fill = "white", font=("Quicksand", 10, "bold")) #num of JEH
    phase_description = "Phase " + str(i + 1) + " : " + str(phases[i][3]) + " JEH(s)"
    canvas.create_text(margin_side-60, y1+barH/2, text=phase_description, fill = "black", font=("Quicksand", 10))

# ----------------
# Framing and weeks scale
# ----------------

frame_startX = margin_side-120
frameH = calendarH + 30
frameW = calendarW + 30
canvas.create_rectangle(frame_startX, margin_top-15, margin_side-120+frameW, margin_top-20 + frameH, fill=None, outline="black")

canvas.create_text(margin_side - 60, margin_top-30, text="SEMAINE : ", fill="black", font=("Quicksand", 10))
for i in range(len_mission-1):
    canvas.create_text(margin_side + i*week, margin_top - 30, text=str(i), fill="black", font=("Quicksand", 10))

canvas.create_text((frame_startX+margin_side-120+frameW)//2, margin_top - 60, text=dates, fill="black", font=("Quicksand", 15))



root.mainloop()


