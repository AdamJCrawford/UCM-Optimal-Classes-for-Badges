from collections import Counter
from itertools import chain


def fetch_classes(badges: dict[str, int]):

    all_options = []

    if badges["Diversity and Identity"].get():
        with open("Classes/DiversityandIdentity.txt") as f:
            all_options.append([f.readline()[:-1] for line in f][:-1])

    if badges["Ethics"].get():
        with open("Classes/Ethics.txt") as f:
            all_options.append([f.readline()[:-1] for line in f][:-1])

    if badges["Global Awareness"].get():
        with open("Classes/GlobalAwareness.txt") as f:
            all_options.append([f.readline()[:-1] for line in f][:-1])

    if badges["Media and Visual Analysis"].get():
        with open("Classes/MediaandVisualAnalysis.txt") as f:
            all_options.append([f.readline()[:-1] for line in f][:-1])

    if badges["Societies and Cultures of the Past"].get():
        with open("Classes/SocietiesandCulturesofthePast.txt") as f:
            all_options.append([f.readline()[:-1] for line in f][:-1])

    if badges["Sustainability"].get():
        with open("Classes/Sustainability.txt") as f:
            all_options.append([f.readline()[:-1] for line in f][:-1])

    return Counter(chain(*all_options))
