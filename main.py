from collections import Counter

with open('DiversityandIdentity.txt') as f:
    data1 = [f.readline()[:-1] for line in f]

with open('MediaandVisualAnalysis.txt') as f:
    data2 = [f.readline()[:-1] for line in f]

with open('SocietiesandCulturesofthePast.txt') as f:
    data3 = [f.readline()[:-1] for line in f]

with open('GlobalAwareness.txt') as f:
    data4 = [f.readline()[:-1] for line in f]

with open('Ethics.txt') as f:
    data5 = [f.readline()[:-1] for line in f]

with open('Sustainability.txt') as f:
    data6 = [f.readline()[:-1] for line in f]



all_options = data1 + data2 + data3 + data4 + data5
print(Counter(all_options))
