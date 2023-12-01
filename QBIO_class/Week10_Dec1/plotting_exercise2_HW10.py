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

time_of_sighting_df = UFO_data_df['day_part'].value_counts()

print(time_of_sighting_df)

order_list = ['night','astronomical dawn','nautical dawn','civil dawn','morning','afternoon','civil dusk','nautical dusk','astronomical dusk']
time_of_sighting_df = time_of_sighting_df.loc[order_list]
print(time_of_sighting_df)
count = time_of_sighting_df.values

fig,ax = plt.subplots()

plt.plot(order_list, count, color = 'green')
ax.set_xlabel("Time of Sighting")
ax.set_ylabel("Number of Sightings")
ax.set_title("Time of Day of Sightings")

plt.tight_layout()
plt.show()

fig.savefig("day_time_sighting.png")


### PLOT 3 ###
# During of sightings - histogram

final_data_df = UFO_data_df[UFO_data_df['duration_seconds'] < 4000]

fig, ax = plt.subplots()

ax.hist(final_data_df['duration_seconds'], color = 'pink', bins = 50)
ax.set_xlabel("Reported Duration (seconds)")
ax.set_ylabel("Number of Sightings")
ax.set_title("Distribution of Duration of UFO Sightings")
fig.tight_layout()
plt.show()

fig.savefig("duration_of_sighting.png")



