# -*- coding: utf-8 -*-
"""bred plots

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RURL6U4GgF9WY9FJSZaXCfH_NvzNRLEh
"""

!pip install plotly pandas scipy
import plotly.express as px
import pandas as pd
from scipy.stats import spearmanr

medians1 = [4, 2, 2, 2, 3, 1]
medians1_mus = [4, 2, 2, 2, 2, 1]
medians1_non = [4, 2, 2, 1, 3, 1]

medians2 = [4, 2, 2, 3, 1, 1]
medians2_mus = [4, 2, 1, 2, 2, 1]
medians2_non = [4, 2, 2, 3, 1, 1]

df = pd.DataFrame({
    'sample': list(range(1, 7)) * 3 + list(range(7, 13)) * 3,
    'median_similarity': medians1 + medians1_mus + medians1_non + medianshttps://web.whatsapp.com/2 + medians2_mus + medians2_non,
    'category': (['total'] * 6 + ['musicians'] * 6 + ['non-musicians'] * 6) * 2,
    'set': ['first group'] * 18 + ['second group'] * 18, 
})

fig = px.line(df, x='sample', y='median_similarity', color='category', markers=True)
fig.show()

group1sim = [
    [3, 3, 2, 1, 2, 1],
    [4, 2, 2, 1, 3, 1],
    [4, 2, 1, 2, 2, 1],
    [5, 2, 2, 2, 3, 1],
    [4, 2, 1, 1, 3, 1],
    [4, 4, 2, 3, 3, 1],
]

group2sim = [
    [3, 2, 2, 5, 2, 1],
    [4, 2, 1, 2, 3, 1],
    [4, 2, 2, 1, 1, 1],
    [4, 2, 2, 3, 1, 1],
    [4, 1, 1, 3, 1, 1],
    [4, 1, 1, 1, 1, 1],
    [5, 3, 1, 4, 3, 2],
    [4, 1, 2, 3, 2, 1],
    [4, 3, 2, 2, 1, 1],
]

df = pd.DataFrame({
    'similarity': sum(group1sim, []) + sum(group2sim, []),
    'samples': list(range(1, 7)) * (6 + 9),
    'group': ['first group'] * (6 * 6) + ['second group'] * (6 * 9),
})

fig = px.histogram(df, x='samples', y='similarity', facet_col='group')
fig.show()

musicnn1 = [0.7253895401954651, 0.3090124726295471, 0.33075031638145447, 0.2771308720111847, 0.6863495707511902, 0.10920700430870056]
musicnn2 = [0.8009942770004272, 0.3733898997306824, 0.25702691078186035, 0.5441051125526428, 0.2379208207130432, -0.01808742992579937]

df = pd.DataFrame({
    'similarity': musicnn1 + musicnn2,
    'sample': list(range(1, 13)),
    'group': ['first group'] * 6 + ['second group'] * 6,
})

fig = px.line(df, x='sample', y='similarity', markers=True)
fig.show()

melody_sim1 = [
    [5, 1, 1, 1, 1, 1],
    [5, 1, 1, 1, 2, 1],
    [5, 2, 1, 2, 3, 1],
    [4, 1, 1, 3, 1, 1],
    [5, 2, 1, 1, 3, 1],
    [4, 3, 2, 3, 2, 1],
]

melody_sim2 = [
    [5, 3, 2, 5, 2, 1],
    [4, 1, 1, 2, 3, 1],
    [3, 4, 3, 2, 1, 1],
    [5, 1, 2, 2, 1, 1],
    [5, 1, 1, 3, 1, 1],
    [4, 1, 1, 1, 1, 1],
    [5, 3, 2, 3, 5, 1],
    [4, 1, 2, 3, 1, 1],
    [4, 1, 4, 4, 2, 1],
]

rhythm_sim1 = [
    [5, 1, 1, 2, 2, 1],
    [3, 2, 1, 1, 4, 1],
    [2, 4, 1, 2, 2, 1],
    [5, 2, 2, 2, 5, 1],
    [4, 1, 2, 1, 3, 2],
    [2, 4, 1, 2, 4, 1],
]

rhythm_sim2 = [
    [2, 3, 3, 5, 3, 2],
    [4, 3, 1, 2, 3, 1],
    [2, 1, 1, 2, 1, 1],
    [4, 2, 2, 2, 1, 1],
    [4, 1, 1, 3, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [4, 4, 1, 4, 1, 5],
    [5, 2, 3, 4, 2, 1],
    [2, 3, 1, 1, 2, 2],
]

harmony_sim1 = [
    [4, 1, 1, 2, 3, 2],
    [5, 3, 3, 2, 3, 1],
    [4, 3, 1, 1, 2, 1],
    [5, 4, 3, 1, 2, 1],
    [2, 2, 2, 2, 2, 2],
    [4, 4, 2, 4, 2, 1],
]

harmony_sim2 = [
    [4, 2, 2, 5, 2, 1],
    [3, 2, 2, 2, 4, 1],
    [4, 3, 1, 1, 1, 1],
    [5, 2, 1, 3, 1, 1],
    [3, 1, 1, 3, 1, 1],
    [4, 1, 1, 1, 1, 1],
    [5, 3, 1, 3, 2, 1],
    [3, 2, 2, 4, 3, 1],
    [3, 4, 1, 1, 1, 1],
]

timbre_sim1 = [
    [3, 2, 2, 2, 3, 2],
    [5, 3, 2, 2, 4, 1],
    [5, 2, 1, 1, 1, 1],
    [5, 2, 4, 3, 3, 1],
    [3, 1, 2, 2, 2, 2],
    [4, 2, 3, 4, 4, 1],
]

timbre_sim2 = [
    [4, 1, 3, 5, 3, 1],
    [5, 2, 1, 1, 1, 1],
    [4, 2, 1, 1, 1, 1],
    [3, 4, 4, 4, 3, 1],
    [5, 1, 1, 3, 1, 1],
    [4, 4, 1, 2, 1, 1],
    [5, 3, 1, 4, 2, 2],
    [3, 1, 2, 3, 2, 1],
    [4, 2, 3, 3, 1, 1],
]

coef, p = spearmanr(sum(group1sim, []), sum(melody_sim1, []))
print(f"Group1 - Spearman's coefficient: {coef}, p value: {p}")
melody1 = coef
coef, p = spearmanr(sum(group2sim, []), sum(melody_sim2, []))
print(f"Group2 - Spearman's coefficient: {coef}, p value: {p}")
melody2 = coef

coef, p = spearmanr(sum(group1sim, []), sum(rhythm_sim1, []))
print(f"Group1 - Spearman's coefficient: {coef}, p value: {p}")
rhythm1 = coef
coef, p = spearmanr(sum(group2sim, []), sum(rhythm_sim2, []))
print(f"Group2 - Spearman's coefficient: {coef}, p value: {p}")
rhythm2 = coef

coef, p = spearmanr(sum(group1sim, []), sum(harmony_sim1, []))
print(f"Group1 - Spearman's coefficient: {coef}, p value: {p}")
harmony1 = coef
coef, p = spearmanr(sum(group2sim, []), sum(harmony_sim2, []))
print(f"Group2 - Spearman's coefficient: {coef}, p value: {p}")
harmony2 = coef

coef, p = spearmanr(sum(group1sim, []), sum(timbre_sim1, []))
print(f"Group1 - Spearman's coefficient: {coef}, p value: {p}")
timbre1 = coef
coef, p = spearmanr(sum(group2sim, []), sum(timbre_sim2, []))
print(f"Group2 - Spearman's coefficient: {coef}, p value: {p}")
timbre2 = coef

