import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyplot_themes as themes

data_59_string = pd.read_csv('IceCube-59__Search_for_point_sources_using_muon_events.csv')
data_86_string_upgoing = pd.read_csv('first_year_of_IC86_events.csv')

RA_data_59_string = data_59_string['RA(deg)']
RA_data_86_string_upgoing = data_86_string_upgoing['RA']
Dec_data_59_string = data_59_string['Dec.(deg)']
Dec_data_86_string_upgoing = data_86_string_upgoing['Dec']

themes.theme_solarized(scheme="light")
#themes.theme_ggplot2(figsize=[10, 5])
#themes.theme_solarized_light2()

f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex = 'col', sharey = 'row')

ax1.boxplot(RA_data_59_string)
ax2.boxplot(RA_data_86_string_upgoing)
ax3.boxplot(Dec_data_59_string)
ax4.boxplot(Dec_data_86_string_upgoing)

f.text(0.28, 0.02, '59 String Data', ha='center', va='center')
f.text(0.03, 0.70, 'Right Ascension (deg)', ha='center', va='center', rotation='vertical')
f.text(0.75, 0.02, '86 String Data', ha='center', va='center')
f.text(0.03, 0.28, 'Declination Angle (deg)', ha='center', va='center', rotation='vertical')

plt.show()
