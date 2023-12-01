#!/usr/bin/env python

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


### PLOT 1 ###
# Number of sighting with a photo

UFO_data_df = pd.read_csv('/Users/cmdb/qbb2023-answers/QBIO_class/Week10_Dec1/ufo_sightings.csv')

image_df = UFO_data_df['country_code'].value_counts().iloc[0:5]

country_index = image_df.index
counts = image_df.values

fig,ax = plt.subplots()

plt.bar(country_index, counts, color = 'purple', label = 'YES')
ax.set_xlabel("Country")
ax.set_ylabel("Number of Sightings")
ax.set_title("Top Countries with UFO Sightings")

plt.tight_layout()
plt.show()

fig.savefig("counts_of_sightings_UFO.png")


### PLOT 2 ###
# Number of sightings over time - line
"""

fig,ax = plt.subplots()

plt.plot()
ax.set_xlabel("")
ax.set_ylabel("")
ax.set_title("")

plt.tight_layout()
plt.show()

fig.savefig(".png")




### PLOT 3 ###
# During of sightings - histogram

fig,ax = plt.subplots()

plt.hist()
ax.set_xlabel("")
ax.set_ylabel("")
ax.set_title("")

plt.tight_layout()
plt.show()

fig.savefig(".png")
"""


