import tkinter as tk
from get_badge_information import fetch_classes
from counter_to_text import make_txt_file


window = tk.Tk()
window.title("UC Merced Optimal Classes for Badges")
window.attributes("-alpha", .96)
window.configure(bg='black')

CHECKBUTTONS = [None] * 6

TEXT = {"Diversity and Identity": tk.IntVar(), "Media and Visual Analysis": tk.IntVar(),
        "Societies and Cultures of the Past": tk.IntVar(), "Global Awareness": tk.IntVar(),
        "Ethics": tk.IntVar(), "Sustainability": tk.IntVar()}

submit_btn = tk.Button(window, text='Submit', command=lambda: create_graph(TEXT), fg="white",
                       bg="gray", width=28, anchor='w').grid(sticky="nsw", column=1, row=1)


for i, txt in enumerate(TEXT):
    CHECKBUTTONS[i] = tk.Checkbutton(window, text=txt, fg="white", bg="gray", anchor='w',
                                     selectcolor="black", activeforeground="white",
                                     activebackground="gray", variable=TEXT[txt])
for i in range(len(CHECKBUTTONS)):
    CHECKBUTTONS[i].grid(sticky="nesw", row=i + 1)


def create_graph(badges: dict[str, int]):
    cntr = fetch_classes(badges)
    make_txt_file(cntr)
    for i in range(len(TEXT)):
        CHECKBUTTONS[i].deselect()


window.mainloop()
