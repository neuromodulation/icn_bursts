import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import string

ALPHA_BOX = 0.4

def histplot_burst_length(burst_length, bins=9, range=(0, 0.9)):
    """ plot in histogram burst lengths"""
    sns.set(style="white", font_scale=1)
    plt.hist(burst_length, bins=bins, range=range)
    sns.despine()


def boxplot_burst_length(pd_burst_length):
    
    sns.boxplot(x='channel', y='value', hue='med_state',data=pd_burst_length, palette="viridis", 
                boxprops=dict(alpha=ALPHA_BOX),
            showfliers=False,
            whiskerprops={'linewidth':2, "zorder":10, "alpha":ALPHA_BOX},
            capprops={"alpha":ALPHA_BOX},
            medianprops=dict(linestyle='-.', linewidth=5, color="grey", alpha=ALPHA_BOX))
    
    sns.stripplot(x='channel', y='value', hue='med_state', 
                data=pd_burst_length,palette="viridis", dodge=True, s=5)


def plot_betapower_vs_burstlenght(freqs,
    npow_off: list,
    npow_on: list,
    pd_burst_length : pd.DataFrame):

    sns.set(style="white", font_scale=1.2)
    
    plt.figure(figsize=(25,15))

    ax1 = plt.subplot2grid((2, 5), (0, 0), colspan=1) 
    plt.yticks(np.arange(0, 0.2, step=0.05))
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_ylabel('Amplitude (au)')

    axs_col = [ax1]

    for ax_num in np.arange(1, 5):
        ax_ = plt.subplot2grid((2, 5), (0, ax_num), colspan=1) 
        ax_.set_yticks(np.arange(0, 0.2, step=0.05))
        axs_col.append(ax_)

    for ch_idx, ax_ in enumerate(axs_col):
        ax_.set_ylim(0, 0.2)
        ax_.set_xlim(0, 0.2)
        ax_.plot(freqs, npow_off[ch_idx], label='MED OFF')
        ax_.plot(freqs, npow_on[ch_idx], label='MED ON')

    plt.legend(bbox_to_anchor=(1.05, 1),loc=1, borderaxespad=0)
    
    plt.subplot2grid((2, 6), (1,0),colspan=10) 

    boxplot_burst_length(pd_burst_length)

    plt.ylabel('burst duration (s)')
    plt.xlabel('')

    plt.suptitle(' Beta Power vs Burst Duration ECoG Berlin OFF and ON Sub003 Run01 Rest ')
    sns.despine()


def plot_burst_dynamics(freqs, npow_on, npow_off,
    pd_prob_dur: pd.DataFrame,
    pd_dur: pd.DataFrame):

    sns.set(style="white", font_scale=1.3)
    fig,ax = plt.subplots(1,3, figsize=(25,15),)

    plt.subplot(131)
    plt.plot(freqs,npow_on,label= 'OFF ',linewidth=4)
    plt.plot(freqs,npow_off,label= 'ON',linewidth=4)
    plt.xlim(0,60)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Relative spectral power (au)')
    plt.legend(title='Medication', fontsize=15,title_fontsize=15)
            
    plt.subplot(132)           
    alpha_box=0.3
    sns.barplot(data=pd_prob_dur, x='Burst Duration (s)', y='Burst Probability (%)', hue='Medication') 
    plt.legend(title='Medication', fontsize=15,title_fontsize=15)

    plt.subplot(133)
    alpha_box = 0.4
    g = sns.boxplot(x='Location', y='Burst Duration (s)', hue='Medication',data=pd_dur,         
            showfliers=False,meanline=dict(color='r'), showmeans=True,
            whiskerprops={'linewidth':2, "zorder":10, "alpha":alpha_box},
            capprops={"alpha":alpha_box},
            meanprops=dict(linestyle='-.', linewidth=5,color='r'))
    plt.xlabel('Primary Motor Cortex')
    plt.legend(title='Medication', fontsize=15,title_fontsize=15)

    for n, ax in enumerate(ax):   
        ax.text(-0.1, 1.1, string.ascii_uppercase[n], transform=ax.transAxes, 
                size=30, weight='bold')
        
    sns.despine()