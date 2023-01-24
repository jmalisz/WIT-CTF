# -*- coding: utf-8 -*-
"""CTF-Lab1/2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b0Duyqo5N8c4nvR1mHKOlXdqpVqPupCU
"""

import numpy as np
import matplotlib.pyplot as plt

path1 = '/content/2023.01.23-17.34.53.dbmeter.txt'
path2 = '/content/2023.01.23-17.36.08.dbmeter.txt'

# plik z danymi 1
with open(path1) as f:
  n_cols1 = len(f.readline().split("\t"))

# plik z danymi 2
with open(path1) as f:
  n_cols2 = len(f.readline().split("\t"))

# moc sygnału w danym zakresie częstliwości dla każdej sekundy pomiaru
freqData1 = np.loadtxt(path1, skiprows=1, usecols=np.arange(3,n_cols+1))
freqData2 = np.loadtxt(path2, skiprows=1, usecols=np.arange(3,n_cols+1))

# poziom głoności w całym paśmie dla każdej sekundy pomiaru
loudnessData1 = np.loadtxt(path1, skiprows=1, usecols=2)
loudnessData2 = np.loadtxt(path2, skiprows=1, usecols=2)

# etykiety danych do wizualiacji
labels = np.loadtxt(path1, dtype=str, max_rows=1, usecols=np.arange(2,n_cols))

# uśrednienie mocy sygnału w poszczególnych pasmach za cały okres pomiaru
meanFreqData1 = np.mean(freqData1,axis=0)
meanFreqData2 = np.mean(freqData2,axis=0)

plt.figure(figsize=(4,3),dpi=200)
plt.plot(range(1,n_cols-1),meanFreqData1, label="Ściana")
plt.bar(range(1,n_cols-1),meanFreqData1, label="Ściana")
plt.plot(range(1,n_cols-1),meanFreqData2, label="Róg")
plt.bar(range(1,n_cols-1),meanFreqData2, label="Róg")
plt.xticks(range(1,n_cols-1), labels, rotation=90, fontsize=6)
plt.yticks(fontsize=6)
plt.legend()
plt.title('Uśrednione widmo w pasmach oktawowych')

plt.figure(figsize=(4,3),dpi=200)
plt.plot(loudnessData1, label="Ściana")
plt.plot(loudnessData2, label="Róg")
plt.legend()
plt.title('Poziom głośności')