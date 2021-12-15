from itertools import chain
from pprint import pprint
import copy
from collections import Counter
lines = """
PPFCHPFNCKOKOSBVCFPP

VC -> N
SC -> H
CK -> P
OK -> O
KV -> O
HS -> B
OH -> O
VN -> F
FS -> S
ON -> B
OS -> H
PC -> B
BP -> O
OO -> N
BF -> K
CN -> B
FK -> F
NP -> K
KK -> H
CB -> S
CV -> K
VS -> F
SF -> N
KB -> H
KN -> F
CP -> V
BO -> N
SS -> O
HF -> H
NN -> F
PP -> O
VP -> H
BB -> K
VB -> N
OF -> N
SH -> S
PO -> F
OC -> S
NS -> C
FH -> N
FP -> C
SO -> P
VK -> C
HP -> O
PV -> S
HN -> K
NB -> C
NV -> K
NK -> B
FN -> C
VV -> N
BN -> N
BH -> S
FO -> V
PK -> N
PS -> O
CO -> K
NO -> K
SV -> C
KO -> V
HC -> B
BC -> N
PB -> C
SK -> S
FV -> K
HO -> O
CF -> O
HB -> P
SP -> N
VH -> P
NC -> K
KC -> B
OV -> P
BK -> F
FB -> F
FF -> V
CS -> F
CC -> H
SB -> C
VO -> V
VF -> O
KP -> N
HV -> H
PF -> H
KH -> P
KS -> S
BS -> H
PH -> S
SN -> K
HK -> P
FC -> N
PN -> S
HH -> N
OB -> P
BV -> S
KF -> N
OP -> H
NF -> V
CH -> K
NH -> P
"""
# lines = """
# NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C
# """
lines = lines.strip()
lines = lines.split('\n\n')
template = lines[0]
rules = lines[1].split("\n")
rules = dict([rule.split(" -> ") for rule in rules])

# print(template, rules)


def grow(template):
    pairs = []
    for i in range(len(template) - 1):
        pairs.append(template[i]+template[i+1])
    for i in range(len(pairs)):
        if pairs[i] in rules:
            pairs[i] = pairs[i][0] + rules[pairs[i]] + pairs[i][1]
    polymer = ""
    for i in range(len(pairs)):
        if i == 0:
            polymer += str((pairs[i]))
        else:
            polymer += str(pairs[i][1:])
    return polymer


def part1(template):
    polymer = template
    for _ in range(10):
        print(_, Counter(polymer))
        polymer = grow(template)
        template = polymer
    histogram = Counter(polymer)
    return histogram.most_common()[0][1] - histogram.most_common()[-1][1]


def part2(template):
    polymer = template
    for _ in range(10):
        print(_, Counter(polymer))
        polymer = grow(template)
        template = polymer
        print(Counter(polymer).most_common()[0],
              Counter(polymer).most_common()[-1])
    histogram = Counter(polymer)
    return histogram.most_common()[0][1] - histogram.most_common()[-1][1]


print(part1(template))
print(part2(template))
