from collections import Counter
from itertools import chain


def fetch(badges: list[str]):

    all_options = []

    if "Div" in badges:
        with open('DiversityandIdentity.txt') as f:
            all_options.append([f.readline()[:-1] for line in f])
    if "Med" in badges:
        with open('MediaandVisualAnalysis.txt') as f:
            all_options.append([f.readline()[:-1] for line in f])
    if "Soc" in badges:
        with open('SocietiesandCulturesofthePast.txt') as f:
            all_options.append([f.readline()[:-1] for line in f])
    if "Glo" in badges:
        with open('GlobalAwareness.txt') as f:
            all_options.append([f.readline()[:-1] for line in f])
    if "Eth" in badges:
        with open('Ethics.txt') as f:
            all_options.append([f.readline()[:-1] for line in f])
    if "Sus" in badges:
        with open('Sustainability.txt') as f:
            all_options.append([f.readline()[:-1] for line in f])

    return Counter(chain(*all_options))
