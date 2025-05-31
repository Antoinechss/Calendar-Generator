import matplotlib.pyplot as plt

def generate_calendar(mission_start, mission_end, len_mission, phases, filename="calendrier_mission.png"):
    num_phases = len(phases)
    fig, ax = plt.subplots(figsize=(12, 1 + num_phases))
    plt.rcParams['font.family'] = 'Quicksand'

    for i, phase in enumerate(phases[::-1]):
        duration, start, end, jeh = phase
        ax.broken_barh([(start, duration)], (i, 0.8), facecolors="#2c3e50", edgecolors="black")
        ax.text(start + duration / 2, i + 0.4, f"{duration}", color="white", ha="center", va="center", fontsize=12)
        ax.text(-0.2, i + 0.4, f"Phase {i + 1} : {jeh} JEH(s)", ha="right", va="center", fontsize=11)

    ax.set_xlim(0, len_mission)
    ax.set_ylim(0, num_phases + 1)  # espace pour les semaines
    ax.invert_yaxis()
    ax.set_xlabel("Semaines")
    ax.set_yticks([])
    ax.set_xticks(range(0, len_mission + 1))
    ax.set_title(f"Du {mission_start} au {mission_end}")
    ax.grid(axis='x', linestyle="--", alpha=0.3)

    plt.tight_layout()
    fig.savefig(filename, bbox_inches='tight')
    return filename