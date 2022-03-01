# import
import pandas as pd
import numpy as np
import scipy
from scipy.stats import wilcoxon
from openpyxl import Workbook

# 3
# mean duration
# Off
df3_off01_d = pd.read_csv('M1_mean_burst_duration_S3_Off1.csv')
df3_off02_d = pd.read_csv('M1_mean_burst_duration_S3_Off2.csv')
df3_off03_d = pd.read_csv('M1_mean_burst_duration_S3_Off3.csv')

# On 
df3_on01_d = pd.read_csv('M1_mean_burst_duration_S3_On1.csv')
df3_on02_d = pd.read_csv('M1_mean_burst_duration_S3_On2.csv')

# Histogram
# Off
df3_off01_h = pd.read_csv('Histogram_S3_Off1.csv')
df3_off02_h = pd.read_csv('Histogram_S3_Off2.csv')
df3_off03_h = pd.read_csv('Histogram_S3_Off3.csv')

# On 
df3_on01_h = pd.read_csv('Histogram_S3_On1.csv')
df3_on02_h = pd.read_csv('Histogram_S3_On2.csv')

# PSD
# Off
df3_off01_p = pd.read_csv('nPSD_S3_Off1.csv')
df3_off02_p = pd.read_csv('nPSD_S3_Off2.csv')
df3_off03_p = pd.read_csv('nPSD_S3_Off3.csv')

# On 
df3_on01_p = pd.read_csv('nPSD_S3_On1.csv')
df3_on02_p = pd.read_csv('nPSD_S3_On2.csv')

# 4 
# mean duration
# Off
df4_off01_d = pd.read_csv('M1_mean_burst_duration_S4_Off1.csv')
df4_off02_d = pd.read_csv('M1_mean_burst_duration_S4_Off2.csv')

# On 
df4_on01_d = pd.read_csv('M1_mean_burst_duration_S4_On1.csv')
df4_on02_d = pd.read_csv('M1_mean_burst_duration_S4_On2.csv')
df4_on03_d = pd.read_csv('M1_mean_burst_duration_S4_On3.csv')
df4_on04_d = pd.read_csv('M1_mean_burst_duration_S4_On4.csv')
df4_on05_d = pd.read_csv('M1_mean_burst_duration_S4_On5.csv')

# Histogram
# Off
df4_off01_h = pd.read_csv('Histogram_S4_Off1.csv')
df4_off02_h = pd.read_csv('Histogram_S4_Off2.csv')

# On 
df4_on01_h = pd.read_csv('Histogram_S4_On1.csv')
df4_on02_h = pd.read_csv('Histogram_S4_On2.csv')
df4_on03_h = pd.read_csv('Histogram_S4_On3.csv')
df4_on04_h = pd.read_csv('Histogram_S4_On4.csv')
df4_on05_h = pd.read_csv('Histogram_S4_On5.csv')

# PSD
# Off
df4_off01_p = pd.read_csv('nPSD_S4_Off1.csv')
df4_off02_p = pd.read_csv('nPSD_S4_Off2.csv')

# On 
df4_on01_p = pd.read_csv('nPSD_S4_On1.csv')
df4_on02_p = pd.read_csv('nPSD_S4_On2.csv')
df4_on03_p = pd.read_csv('nPSD_S4_On3.csv')
df4_on04_p = pd.read_csv('nPSD_S4_On4.csv')
df4_on05_p = pd.read_csv('nPSD_S4_On5.csv')

# 5
# mean duration
# Off
df5_off01_d = pd.read_csv('M1_mean_burst_duration_S5_Off1.csv')
df5_off02_d = pd.read_csv('M1_mean_burst_duration_S5_Off2.csv')
df5_off03_d = pd.read_csv('M1_mean_burst_duration_S5_Off3.csv')

# On
df5_on01_d = pd.read_csv('M1_mean_burst_duration_S5_On1.csv')
df5_on02_d = pd.read_csv('M1_mean_burst_duration_S5_On2.csv')

# Histogram
# Off
df5_off01_h = pd.read_csv('Histogram_S5_Off1.csv')
df5_off02_h = pd.read_csv('Histogram_S5_Off2.csv')
df5_off03_h = pd.read_csv('Histogram_S5_Off3.csv')

# On
df5_on01_h = pd.read_csv('Histogram_S5_On1.csv')
df5_on02_h = pd.read_csv('Histogram_S5_On2.csv')

# PSD
# Off
df5_off01_p = pd.read_csv('nPSD_S5_Off1.csv')
df5_off02_p = pd.read_csv('nPSD_S5_Off2.csv')
df5_off03_p = pd.read_csv('nPSD_S5_Off3.csv')

# On
df5_on01_p = pd.read_csv('nPSD_S5_On1.csv')
df5_on02_p = pd.read_csv('nPSD_S5_On2.csv')

# 6
# mean duration
# Off
df6_off01_d = pd.read_csv('M1_mean_burst_duration_S6_Off1.csv')
df6_off02_d = pd.read_csv('M1_mean_burst_duration_S6_Off2.csv')

# On
df6_on01_d = pd.read_csv('M1_mean_burst_duration_S6_On1.csv')
df6_on02_d = pd.read_csv('M1_mean_burst_duration_S6_On1.csv')

# Histogram
# Off
df6_off01_h = pd.read_csv('Histogram_S6_Off1.csv')
df6_off02_h = pd.read_csv('Histogram_S6_Off2.csv')

# On
df6_on01_h = pd.read_csv('Histogram_S6_On1.csv')
df6_on02_h = pd.read_csv('Histogram_S6_On1.csv')

# PSD
# Off
df6_off01_p = pd.read_csv('nPSD_S6_Off1.csv')
df6_off02_p = pd.read_csv('nPSD_S6_Off2.csv')

# On
df6_on01_p = pd.read_csv('nPSD_S6_On1.csv')
df6_on02_p = pd.read_csv('nPSD_S6_On1.csv')

# DataFrame adjustments
# 3
df3_off01_d_a =df3_off01_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=3,Medication='OFF',Run=1)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df3_off01_h_a = df3_off01_h.drop(columns='Unnamed: 0').assign(Subject=3,Run=1)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df3_off01_p_a = df3_off01_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=3,Medication='OFF',Run=1)

df3_off02_d_a =df3_off02_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=3,Medication='OFF',Run=2)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df3_off02_h_a = df3_off02_h.drop(columns='Unnamed: 0').assign(Subject=3,Run=2)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df3_off02_p_a = df3_off02_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=3,Medication='OFF',Run=2)

df3_off03_d_a =df3_off03_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=3,Medication='OFF',Run=3)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df3_off03_h_a = df3_off03_h.drop(columns='Unnamed: 0').assign(Subject=3,Run=3)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df3_off03_p_a = df3_off03_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=3,Medication='OFF',Run=3)


df3_on01_d_a =df3_on01_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=3,Medication='ON',Run=1)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df3_on1_h_a = df3_on01_h.drop(columns=['Unnamed: 0','Medication']).assign(Subject=3,Medication='ON',Run=1)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df3_on01_p_a = df3_on01_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=3,Medication='ON',Run=1)

df3_on02_d_a =df3_on02_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=3,Medication='ON',Run=2)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df3_on02_h_a = df3_on02_h.drop(columns=['Unnamed: 0','Medication']).assign(Subject=3,Medication='ON',Run=2)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df3_on02_p_a = df3_on02_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=3,Medication='ON',Run=2)

#4
df4_off01_d_a =df4_off01_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=4,Medication='OFF',Run=1)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df4_off01_h_a = df4_off01_h.drop(columns='Unnamed: 0').assign(Subject=4,Run=1)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df4_off01_p_a = df4_off01_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=4,Medication='OFF',Run=1)

df4_off02_d_a =df4_off02_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=4,Medication='OFF',Run=2)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df4_off02_h_a = df4_off02_h.drop(columns='Unnamed: 0').assign(Subject=4,Run=2)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df4_off02_p_a = df4_off02_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=4,Medication='OFF',Run=2)


df4_on01_d_a =df4_on01_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=4,Medication='ON',Run=1)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df4_on01_h_a = df4_on01_h.drop(columns=['Unnamed: 0','Medication']).assign(Subject=4,Medication='ON',Run=1)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df4_on01_p_a = df4_on01_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=4,Medication='ON',Run=1)

df4_on02_d_a =df4_on02_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=4,Medication='ON',Run=2)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df4_on02_h_a = df4_on02_h.drop(columns=['Unnamed: 0','Medication']).assign(Subject=4,Medication='ON',Run=2)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df4_on02_p_a = df4_on02_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=4,Medication='ON',Run=2)

df4_on03_d_a =df4_on03_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=4,Medication='ON',Run=3)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df4_on03_h_a = df4_on03_h.drop(columns=['Unnamed: 0','Medication']).assign(Subject=4,Medication='ON',Run=3)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df4_on03_p_a = df4_on03_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=4,Medication='ON',Run=3)

df4_on04_d_a =df4_on04_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=4,Medication='ON',Run=4)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df4_on04_h_a = df4_on04_h.drop(columns=['Unnamed: 0','Medication']).assign(Subject=4,Medication='ON',Run=4)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df4_on04_p_a = df4_on04_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=4,Medication='ON',Run=4)

df4_on05_d_a =df4_on05_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=4,Medication='ON',Run=5)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df4_on5_h_a = df4_on05_h.drop(columns=['Unnamed: 0','Medication']).assign(Subject=4,Medication='ON',Run=5)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df4_on05_p_a = df4_on05_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=4,Medication='ON',Run=5)

# 5
df5_off01_d_a =df5_off01_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=5,Medication='OFF',Run=1)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df5_off01_h_a = df5_off01_h.drop(columns='Unnamed: 0').assign(Subject=5,Run=1)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df5_off01_p_a = df5_off01_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=5,Medication='OFF',Run=1)

df5_off02_d_a =df5_off02_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=5,Medication='OFF',Run=2)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df5_off02_h_a = df5_off02_h.drop(columns='Unnamed: 0').assign(Subject=5,Run=2)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df5_off02_p_a = df5_off02_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=5,Medication='OFF',Run=2)

df5_off03_d_a =df5_off03_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=5,Medication='OFF',Run=3)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df5_off03_h_a = df5_off03_h.drop(columns='Unnamed: 0').assign(Subject=5,Run=3)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df5_off03_p_a = df5_off03_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=5,Medication='OFF',Run=3)


df5_on01_d_a =df5_on01_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=5,Medication='ON',Run=1)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df5_on01_h_a = df5_on01_h.drop(columns=['Unnamed: 0','Medication']).assign(Subject=5,Medication='ON',Run=1)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df5_on01_p_a = df5_on01_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=5,Medication='ON',Run=1)

df5_on02_d_a =df5_on02_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=5,Medication='ON',Run=2)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df5_on02_h_a = df5_on02_h.drop(columns=['Unnamed: 0','Medication']).assign(Subject=5,Medication='ON',Run=2)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df5_on02_p_a = df5_on02_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=5,Medication='ON',Run=2)

# 6
df6_off01_d_a =df6_off01_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=6,Medication='OFF',Run=1)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df6_off01_h_a = df6_off01_h.drop(columns='Unnamed: 0').assign(Subject=6,Run=1)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df6_off01_p_a = df6_off01_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=6,Medication='OFF',Run=1)

df6_off02_d_a =df6_off02_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=6,Medication='OFF',Run=2)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df6_off02_h_a = df6_off02_h.drop(columns='Unnamed: 0').assign(Subject=6,Run=2)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df6_off02_p_a = df6_off02_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=6,Medication='OFF',Run=2)


df6_on01_d_a =df6_on01_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=6,Medication='ON',Run=1)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df6_on01_h_a = df6_on01_h.drop(columns=['Unnamed: 0','Medication']).assign(Subject=6,Medication='ON',Run=1)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df6_on01_p_a = df6_on01_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=6,Medication='ON',Run=1)

df6_on02_d_a =df6_on02_d.rename(columns={'Unnamed: 0': "Channel"}).assign(Subject=6,Medication='ON',Run=2)[['Subject','Medication','Run','Channel','mean_burst_duration (s)']]
df6_on02_h_a = df6_on02_h.drop(columns=['Unnamed: 0','Medication']).assign(Subject=6,Medication='ON',Run=2)[['Subject','Medication','Run','Burst Duration (s)','Burst Probability (%)']]
df6_on02_p_a = df6_on02_p.rename(columns={'Unnamed: 0':'Channel'}).assign(Subject=6,Medication='ON',Run=2)

# Concat Feautures
# Mean Duration
df_md = pd.concat([df3_off01_d_a,df3_off02_d_a,df3_off03_d_a,df3_on01_d_a,df3_on02_d_a,
                    df4_off01_d_a,df4_off02_d_a,df4_on01_d_a,df4_on02_d_a,df4_on03_d_a,df4_on04_d_a,df4_on05_d_a,
                    df5_off01_d_a,df5_off02_d_a,df5_off03_d_a, df5_on01_d_a,df5_on02_d_a, 
                    df6_off01_d_a, df6_off02_d_a, df6_on01_d_a,df6_on02_d_a])

# Histogram
df_h = pd.concat([df3_off01_h_a,df3_off02_h_a,df3_off03_h_a,df3_on1_h_a,df3_on02_h_a,
                    df4_off01_h_a,df4_off02_h_a,df4_on01_h_a,df4_on02_h_a,df4_on03_h_a,df4_on04_h_a,df4_on5_h_a,
                    df5_off01_h_a,df5_off02_h_a,df5_off03_h_a, df5_on01_h_a,df5_on02_h_a, 
                    df6_off01_h_a, df6_off02_h_a, df6_on01_h_a,df6_on02_h_a])

# PSD
df_p = pd.concat([df3_off01_p_a,df3_off02_p_a,df3_off03_p_a,df3_on01_p_a,df3_on02_p_a,
                    df4_off01_p_a,df4_off02_p_a,df4_on01_p_a,df4_on02_p_a,df4_on03_p_a,df4_on04_p_a,df4_on05_p_a,
                    df5_off01_p_a,df5_off02_p_a,df5_off03_p_a, df5_on01_p_a,df5_on02_p_a, 
                    df6_off01_p_a, df6_off02_p_a, df6_on01_p_a,df6_on02_p_a])

# Save to Excel File
df_md.to_excel('mean_duration.xlsx')
df_h.to_excel('M1_Histogram_Duration.xlsx')
df_p.to_excel('PSD.xlsx')