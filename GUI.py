import tkinter as tk
import matplotlib as plt

window = tk.Tk()
window.attributes("-fullscreen", True, "-alpha", .96)
window.configure(bg='black')

top_bar_label = tk.Label(
    window, text="UCM Optimal Class for Badges", fg='white', bg="gray", width=224, height=2).grid(column=0, row=0)

minimize_btn = tk.Button(window, text='--', command=lambda: window.wm_state("iconic"),
                         fg='white', bg="gray", width=5, height=2).grid(column=1, row=0)

exit_btn = tk.Button(window, text='Exit', command=window.destroy, fg='white',
                     bg="gray", width=5, height=2).grid(column=2, row=0)

DiversityandIdentity_checkbutton = None
MediaandVisualAnalysis_checkbutton = None
SocietiesandCulturesofthePast_checkbutton = None
GlobalAwareness_checkbutton = None
Ethics_checkbutton = None
Sustainability_checkbutton = None

CHECKBUTTONS = [DiversityandIdentity_checkbutton, MediaandVisualAnalysis_checkbutton,
                SocietiesandCulturesofthePast_checkbutton, GlobalAwareness_checkbutton,
                Ethics_checkbutton, Sustainability_checkbutton]

TEXT = ["Diversity and Identity", "Media and Visual Analysis",
        "Societies and Cultures of the Past", "Global Awareness", "Ethics", "Sustainability"]

for i, txt in enumerate(TEXT):
    CHECKBUTTONS[i] = tk.Checkbutton(window, text=txt, onvalue=1, offvalue=0, fg='white', bg="gray",
                                     width=25, height=2, anchor="w").grid(sticky="W", column=0, row=i + 1)


window.mainloop()
