import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import string
from src import plot_utils

ALPHA_BOX = 0.4

df1 = pd.read_excel (r'/Users/alidzaye/Desktop/MeanBurstDuration_BerlinGroupResults.xlsx',sheet_name='sub1')
df3 = pd.read_excel (r'/Users/alidzaye/Desktop/MeanBurstDuration_BerlinGroupResults.xlsx',sheet_name='sub3')
df4 = pd.read_excel (r'/Users/alidzaye/Desktop/MeanBurstDuration_BerlinGroupResults.xlsx',sheet_name='sub4')
df5 = pd.read_excel (r'/Users/alidzaye/Desktop/MeanBurstDuration_BerlinGroupResults.xlsx',sheet_name='sub5')
df6 = pd.read_excel (r'/Users/alidzaye/Desktop/MeanBurstDuration_BerlinGroupResults.xlsx',sheet_name='sub6')
df7 = pd.read_excel (r'/Users/alidzaye/Desktop/MeanBurstDuration_BerlinGroupResults.xlsx',sheet_name='sub7')
df8 = pd.read_excel (r'/Users/alidzaye/Desktop/MeanBurstDuration_BerlinGroupResults.xlsx',sheet_name='sub8')
print(df8)

mdur_s1_off1 = df1['mean burst duration(s)']
mdur_s1_off2 = df1['mean burst duration(s).1']
mdur_s1_on1 = df1['mean burst duration(s).2']
mdur_s1_on2 = df1['mean burst duration(s).3']

mdur_s3_off1 = df3['mean burst duration(s)']
mdur_s3_off2 = df3['mean burst duration(s).1']
mdur_s3_off3 = df3['mean burst duration(s).2']
mdur_s3_on1 = df3['mean burst duration(s).3']
mdur_s3_on2 = df3['mean burst duration(s).4']

mdur_s4_off1 = df4['mean burst duration(s)']
mdur_s4_off2 = df4['mean burst duration(s).1']
mdur_s4_on1 = df4['mean burst duration(s).2']
mdur_s4_on2 = df4['mean burst duration(s).3']
mdur_s4_on3 = df4['mean burst duration(s).4']
mdur_s4_on4 = df4['mean burst duration(s).5']
mdur_s4_on5 = df4['mean burst duration(s).6']

mdur_s5_off1 = df5['mean burst duration(s)']
mdur_s5_off2 = df5['mean burst duration(s).1']
mdur_s5_off3 = df5['mean burst duration(s).2']
mdur_s5_on1 = df5['mean burst duration(s).3']
mdur_s5_on2 = df5['mean burst duration(s).4']

mdur_s6_off1 = df6['mean burst duration(s)']
mdur_s6_off2 = df6['mean burst duration(s).1']
mdur_s6_on1 = df6['mean burst duration(s).2']
mdur_s6_on2 = df6['mean burst duration(s).3']

mdur_s7_off1 = df7['mean burst duration(s)']
mdur_s7_on1 = df7['mean burst duration(s).1']
mdur_s7_on2 = df7['mean burst duration(s).2']
mdur_s7_on3 = df7['mean burst duration(s).3']
mdur_s7_on4 = df7['mean burst duration(s).4']

mdur_s8_off1 = df8['mean burst duration(s)']
mdur_s8_on1 = df8['mean burst duration(s).1']
mdur_s8_on2 = df8['mean burst duration(s).2']
print(mdur_s8_on2)

#sub1
channels = np.array(['postcentral','precentral_1','precentral_2','prefrontal_1','prefrontal_2'])
elec = np.array([channels, channels, channels, channels])
electrodes = np.reshape(elec,20)

burst_dur = np.array([mdur_s1_off1,mdur_s1_off2,mdur_s1_on1,mdur_s1_on2])
burst_duration = np.reshape(burst_dur,20)

med_off1 = np.array(['med_off1','med_off1','med_off1','med_off1','med_off1'])
med_off2 = np.array(['med_off2','med_off2','med_off2','med_off2','med_off2'])
med_on1 = np.array(['med_on1','med_on1','med_on1', 'med_on1','med_on1'])
med_on2 = np.array(['med_on2','med_on2','med_on2', 'med_on2','med_on2'])
run = np.array([med_off1,med_off2,med_on1,med_on2])
runs = np.reshape(run,20)

df = pd.DataFrame({'Electrodes': electrodes,
                    'Mean Beta Burst Duration (s)': burst_duration,
                  "Runs": runs})

df.to_csv('sub1_meanduration4.csv')

sns.set(style="white", font_scale=1.3)
sns.catplot(x="Runs", y="Mean Beta Burst Duration (s)", hue="Electrodes", kind = 'bar', data=df)
plt.title('Berlin subject 1')
sns.despine()

#sub3
channels = np.array(['ECoG_L1-L2','ECoG_L2-L3','ECoG_L3-L4','ECoG_L4-L5','ECoG_L5-L6'])
elec = np.array([channels, channels, channels, channels])
electrodes = np.reshape(elec,20)

burst_dur = np.array([mdur_s3_off1,mdur_s3_off2,mdur_s3_off3,mdur_s3_on1,mdur_s3_on2])
burst_duration = np.reshape(burst_dur,20)

med_off1 = np.array(['med_off1','med_off1','med_off1','med_off1','med_off1'])
med_off2 = np.array(['med_off2','med_off2','med_off2','med_off2','med_off2'])
med_on1 = np.array(['med_on1','med_on1','med_on1', 'med_on1','med_on1'])
med_on2 = np.array(['med_on2','med_on2','med_on2', 'med_on2','med_on2'])
run = np.array([med_off1,med_off2,med_on1,med_on2])
runs = np.reshape(run,20)

df = pd.DataFrame({'Electrodes': electrodes,
                    'Beta Burst Duration (s)': burst_duration,
                  "Runs": runs})

df.to_csv('sub1_meanduration.csv')

sns.set(style="white", font_scale=1.3)
sns.catplot(x="Runs", y="Beta Burst Duration (s)", hue="Electrodes", kind = 'bar', data=df)
plt.title('Berlin subject 1')
sns.despine()

#sub1
channels = np.array(['ECoG_L1-L2','ECoG_L2-L3','ECoG_L3-L4','ECoG_L4-L5','ECoG_L5-L6'])
elec = np.array([channels, channels, channels, channels])
electrodes = np.reshape(elec,20)

burst_dur = np.array([mdur_s1_off1,mdur_s1_off2,mdur_s1_on1,mdur_s1_on2])
burst_duration = np.reshape(burst_dur,20)

med_off1 = np.array(['med_off1','med_off1','med_off1','med_off1','med_off1'])
med_off2 = np.array(['med_off2','med_off2','med_off2','med_off2','med_off2'])
med_on1 = np.array(['med_on1','med_on1','med_on1', 'med_on1','med_on1'])
med_on2 = np.array(['med_on2','med_on2','med_on2', 'med_on2','med_on2'])
run = np.array([med_off1,med_off2,med_on1,med_on2])
runs = np.reshape(run,20)

df = pd.DataFrame({'Electrodes': electrodes,
                    'Beta Burst Duration (s)': burst_duration,
                  "Runs": runs})

df.to_csv('sub1_meanduration.csv')

sns.set(style="white", font_scale=1.3)
sns.catplot(x="Runs", y="Beta Burst Duration (s)", hue="Electrodes", kind = 'bar', data=df)
plt.title('Berlin subject 1')
sns.despine()

#sub1
channels = np.array(['ECoG_L1-L2','ECoG_L2-L3','ECoG_L3-L4','ECoG_L4-L5','ECoG_L5-L6'])
elec = np.array([channels, channels, channels, channels])
electrodes = np.reshape(elec,20)

burst_dur = np.array([mdur_s1_off1,mdur_s1_off2,mdur_s1_on1,mdur_s1_on2])
burst_duration = np.reshape(burst_dur,20)

med_off1 = np.array(['med_off1','med_off1','med_off1','med_off1','med_off1'])
med_off2 = np.array(['med_off2','med_off2','med_off2','med_off2','med_off2'])
med_on1 = np.array(['med_on1','med_on1','med_on1', 'med_on1','med_on1'])
med_on2 = np.array(['med_on2','med_on2','med_on2', 'med_on2','med_on2'])
run = np.array([med_off1,med_off2,med_on1,med_on2])
runs = np.reshape(run,20)

df = pd.DataFrame({'Electrodes': electrodes,
                    'Beta Burst Duration (s)': burst_duration,
                  "Runs": runs})

df.to_csv('sub1_meanduration.csv')

sns.set(style="white", font_scale=1.3)
sns.catplot(x="Runs", y="Beta Burst Duration (s)", hue="Electrodes", kind = 'bar', data=df)
plt.title('Berlin subject 1')
sns.despine()

#sub1
channels = np.array(['ECoG_L1-L2','ECoG_L2-L3','ECoG_L3-L4','ECoG_L4-L5','ECoG_L5-L6'])
elec = np.array([channels, channels, channels, channels])
electrodes = np.reshape(elec,20)

burst_dur = np.array([mdur_s1_off1,mdur_s1_off2,mdur_s1_on1,mdur_s1_on2])
burst_duration = np.reshape(burst_dur,20)

med_off1 = np.array(['med_off1','med_off1','med_off1','med_off1','med_off1'])
med_off2 = np.array(['med_off2','med_off2','med_off2','med_off2','med_off2'])
med_on1 = np.array(['med_on1','med_on1','med_on1', 'med_on1','med_on1'])
med_on2 = np.array(['med_on2','med_on2','med_on2', 'med_on2','med_on2'])
run = np.array([med_off1,med_off2,med_on1,med_on2])
runs = np.reshape(run,20)

df = pd.DataFrame({'Electrodes': electrodes,
                    'Beta Burst Duration (s)': burst_duration,
                  "Runs": runs})

df.to_csv('sub1_meanduration.csv')

sns.set(style="white", font_scale=1.3)
sns.catplot(x="Runs", y="Beta Burst Duration (s)", hue="Electrodes", kind = 'bar', data=df)
plt.title('Berlin subject 1')
sns.despine()

#sub1
channels = np.array(['ECoG_L1-L2','ECoG_L2-L3','ECoG_L3-L4','ECoG_L4-L5','ECoG_L5-L6'])
elec = np.array([channels, channels, channels, channels])
electrodes = np.reshape(elec,20)

burst_dur = np.array([mdur_s1_off1,mdur_s1_off2,mdur_s1_on1,mdur_s1_on2])
burst_duration = np.reshape(burst_dur,20)

med_off1 = np.array(['med_off1','med_off1','med_off1','med_off1','med_off1'])
med_off2 = np.array(['med_off2','med_off2','med_off2','med_off2','med_off2'])
med_on1 = np.array(['med_on1','med_on1','med_on1', 'med_on1','med_on1'])
med_on2 = np.array(['med_on2','med_on2','med_on2', 'med_on2','med_on2'])
run = np.array([med_off1,med_off2,med_on1,med_on2])
runs = np.reshape(run,20)

df = pd.DataFrame({'Electrodes': electrodes,
                    'Beta Burst Duration (s)': burst_duration,
                  "Runs": runs})

df.to_csv('sub1_meanduration.csv')

sns.set(style="white", font_scale=1.3)
sns.catplot(x="Runs", y="Beta Burst Duration (s)", hue="Electrodes", kind = 'bar', data=df)
plt.title('Berlin subject 1')
sns.despine()

#sub1
channels = np.array(['ECoG_L1-L2','ECoG_L2-L3','ECoG_L3-L4','ECoG_L4-L5','ECoG_L5-L6'])
elec = np.array([channels, channels, channels, channels])
electrodes = np.reshape(elec,20)

burst_dur = np.array([mdur_s1_off1,mdur_s1_off2,mdur_s1_on1,mdur_s1_on2])
burst_duration = np.reshape(burst_dur,20)

med_off1 = np.array(['med_off1','med_off1','med_off1','med_off1','med_off1'])
med_off2 = np.array(['med_off2','med_off2','med_off2','med_off2','med_off2'])
med_on1 = np.array(['med_on1','med_on1','med_on1', 'med_on1','med_on1'])
med_on2 = np.array(['med_on2','med_on2','med_on2', 'med_on2','med_on2'])
run = np.array([med_off1,med_off2,med_on1,med_on2])
runs = np.reshape(run,20)

df = pd.DataFrame({'Electrodes': electrodes,
                    'Beta Burst Duration (s)': burst_duration,
                  "Runs": runs})

df.to_csv('sub1_meanduration.csv')

sns.set(style="white", font_scale=1.3)
sns.catplot(x="Runs", y="Beta Burst Duration (s)", hue="Electrodes", kind = 'bar', data=df)
plt.title('Berlin subject 1')
sns.despine()

 




