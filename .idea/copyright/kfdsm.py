#!/usr/bin/python
# -*- coding: UTF-8 -*-


import matplotlib.pyplot as plt
import numpy as np

# data = np.arange(10)
# plt.plot(data)


X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

plot(X,C)
plot(X,S)

show()
