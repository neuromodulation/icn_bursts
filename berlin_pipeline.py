from typing import Union
import runpy
from turtle import done

import pandas as pd

from bids import BIDSLayout
import mne_bids
import matplotlib.pyplot as plt
import seaborn as sns
from src import pipeline, plot_utils, preprocessing, postprocessing
import seaborn as sns
import numpy as np
import mne
from scipy.stats import wilcoxon, pearsonr
from scipy.stats import permutation_test

# SCRIPT START #
def main():
    """Run this script."""
    # Load project constants
    project_constants = runpy.run_path("berlin_constants.py")
    data_path = project_constants["data_path"]
    path_bids = project_constants["PATH_BIDS"]
    m1_ids = project_constants["M1_IDS"]
    new_ch_names_map = project_constants["NEW_CH_NAMES_MAP"]
    files = project_constants["files"]
    remove_subjects: Union[str, None] = ["001", "002", "010"]
    if remove_subjects:
        for remove_subject in remove_subjects:
            files = [file for file in files if remove_subject not in file]
    files = preprocessing.pick_runs(files)
    files_x = [f for f in files if "015" in f]

    # Define variables
    burst_char_pd_all = []
    M1_burst_dynamics_all = []
    npow_list_all = []

    #  Process runs #
    for path_run in files:
        entities = mne_bids.get_entities_from_fname(path_run)
        sub = entities["subject"]
        session = entities["session"]
        task = entities["task"]
        acquisition = entities["acquisition"]
        run = entities["run"]
        med = "On" if "MedOn" in entities["session"] else "Off"
        (burst_char_pd, M1_burst_dynamics, npow,) = pipeline.bursts_single_run(
            path_run=path_run,
            path_bids=path_bids,
            sub=sub,
            m1=m1_ids[sub],
            new_ch_names=new_ch_names_map[sub],
            med=med,
            session=session,
            task=task,
            acquisition=acquisition,
            run=run,
        )
        burst_char_pd["Subject"] = sub
        burst_char_pd["Medication"] = med
        burst_char_pd["Run"] = run
        M1_burst_dynamics["Subject"] = sub
        M1_burst_dynamics["Medication"] = med
        M1_burst_dynamics["Run"] = run
        npow["Subject"] = sub
        npow["Medication"] = med
        npow["Run"] = run
        burst_char_pd_all.append(burst_char_pd)
        M1_burst_dynamics_all.append(M1_burst_dynamics)
        npow_list_all.append(npow)

    return (
        burst_char_pd_all,
        M1_burst_dynamics_all,
        npow_list_all,
    )


if __name__ == "__main__":
    (burst_char_pd_all, M1_burst_dynamics_all, npow_list_all,) = main()

# Structure Results in DataFrame
features = pd.concat(burst_char_pd_all)
dist = pd.concat(M1_burst_dynamics_all)
psd = pd.concat(npow_list_all)


# plot_utils.plot_avgm1_burst_features(features)

print("done")

# Average Runs (multiple subs)
avg_features = postprocessing.avg_features_sub(burst_char_pd_all)
df_gavg_dist, df_sub_dist = postprocessing.avg_distribution(M1_burst_dynamics_all)

# plot_utils.plot_avgm1_burst_features(avg_features)
# plot_utils.plot_m1_burst_features(features)

# Distribution of Duration
# plot_utils.plot_distribution(df_gavg_dist, df_sub_dist)

print("done")


# Statistic
on = features[features["Medication"] == "On"]
off = features[features["Medication"] == "Off"]
duration_on = on["Duration (s)"]
duration_off = off["Duration (s)"]
res = wilcoxon(duration_off, duration_on)
res_dur = wilcoxon(duration_off, duration_on)


amplitude_on = on["Amplitude (au)"]
amplitude_off = off["Amplitude (au)"]
res_ampl = wilcoxon(amplitude_off, amplitude_on)


rate_on = on["Rate (/s)"]
rate_off = off["Rate (/s)"]
res_rate = wilcoxon(rate_off, rate_on)

on_dist = dist[dist["Medication"] == "On"]
off_dist = dist[dist["Medication"] == "Off"]
dist_on = on_dist.iloc[:,[7]]
dist_off = off_dist.iloc[:,[7]]
res_dist = wilcoxon(dist_off, dist_on)

res_dur.statistic, res_dur.pvalue
res_ampl.statistic, res_ampl.pvalue
res_rate.statistic, res_rate.pvalue
res_dist.statistic[0], res_dist.pvalue[0]



# Permutation test
x_dur = duration_on
y_dur = duration_off

x_ampl = amplitude_on
y_ampl = amplitude_off

x_rate = rate_on
y_rate = rate_off

# def statistic(x, y):
#    return pearsonr(x, y)
def statistic(x, y):
    return np.mean(x) - np.mean(y)


resi_dur = permutation_test(
    (x_dur.values, y_dur.values),
    statistic,
    vectorized=False,
    permutation_type="samples",
    alternative="two-sided",
)

resi_ampl = permutation_test(
    (x_ampl.values, y_ampl.values),
    statistic,
    vectorized=False,
    permutation_type="samples",
    alternative="two-sided",
)

resi_rate = permutation_test(
    (x_rate.values, y_rate.values),
    statistic,
    vectorized=False,
    permutation_type="samples",
    alternative="two-sided",
)

resi_dist = permutation_test(
    (dist_off.values, dist_on.values),
    statistic,
    vectorized=False,
    permutation_type="samples",
    alternative="two-sided",
)

r_dur, pvalue_dur, null_dur = resi_dur.statistic, resi_dur.pvalue, resi_dur.null_distribution
r_ampl, pvalue_ampl, null_ampl = resi_ampl.statistic, resi_ampl.pvalue, resi_ampl.null_distribution
r_rate, pvalue_rate, null_rate = resi_rate.statistic, resi_rate.pvalue, resi_rate.null_distribution
r_dist, pvalue_dist, null_dist = resi_dist.statistic, resi_dist.pvalue, resi_dist.null_distribution
r_dist, pvalue_dist = r_dist[0], pvalue_dist[0]
print("done")


# Plot Distribution single subject
dist3 = df_sub_dist[df_sub_dist["Subject"] == 3]
dist4 = df_sub_dist[df_sub_dist["Subject"] == 4]
dist5 = df_sub_dist[df_sub_dist["Subject"] == 5]
dist6 = df_sub_dist[df_sub_dist["Subject"] == 6]
dist7 = df_sub_dist[df_sub_dist["Subject"] == 7]
dist8 = df_sub_dist[df_sub_dist["Subject"] == 8]
dist9 = df_sub_dist[df_sub_dist["Subject"] == 9]
dist11 = df_sub_dist[df_sub_dist["Subject"] == 11]
dist12 = df_sub_dist[df_sub_dist["Subject"] == 12]
dist13 = df_sub_dist[df_sub_dist["Subject"] == 13]
dist14 = df_sub_dist[df_sub_dist["Subject"] == 14]
dist15 = df_sub_dist[df_sub_dist["Subject"] == 15]
#dist16 = df_sub_dist[df_sub_dist["Subject"] == 16]

# plot_utils.plot_distribution_sub3(dist3)
# plot_utils.plot_distribution_sub4(dist4)
# plot_utils.plot_distribution_sub5(dist5)
# plot_utils.plot_distribution_sub6(dist6)
# plot_utils.plot_distribution_sub7(dist7)
# plot_utils.plot_distribution_sub8(dist8)
# plot_utils.plot_distribution_sub9(dist9)
# plot_utils.plot_distribution_sub11(dist11)
# plot_utils.plot_distribution_sub12(dist12)
# plot_utils.plot_distribution_sub13(dist13)
# plot_utils.plot_distribution_sub14(dist14)
# plot_utils.plot_distribution_sub15(dist15)
# plot_utils.plot_distribution_sub15(dist16)

(
    psd_s3off,
    psd_s3on,
    psd_s4off,
    psd_s4on,
    psd_s5off,
    psd_s5on,
    psd_s6off,
    psd_s6on,
    psd_s7off,
    psd_s7on,
    psd_s8off,
    psd_s8on,
    psd_s9off,
    psd_s9on,
    psd_s11off,
    psd_s11on,
    psd_s12off,
    psd_s12on,
    psd_s13off,
    psd_s13on,
    psd_s14off,
    psd_s14on,
    psd_s15off,
    psd_s15on,
    #psd_s16off,
    #psd_s16on,
    psd_off,
    psd_on,
) = postprocessing.arrange_psd(npow_list_all)

# PLOTS #
# Features
plot_utils.plot_avgm1_burst_features(avg_features)
plot_utils.plot_m1_burst_features(features)

# Distribution of Duration
plot_utils.plot_distribution(df_gavg_dist, df_sub_dist)

print("done")

# PSD
plot_utils.plot_gavg_psd(psd_off, psd_on)
plot_utils.plot_psd_s3(psd_s3off, psd_s3on)
plot_utils.plot_psd_s4(psd_s4off, psd_s4on)
plot_utils.plot_psd_s5(psd_s5off, psd_s5on)
plot_utils.plot_psd_s6(psd_s6off, psd_s6on)
plot_utils.plot_psd_s7(psd_s7off, psd_s7on)
plot_utils.plot_psd_s8(psd_s8off, psd_s8on)
plot_utils.plot_psd_s9(psd_s9off, psd_s9on)
plot_utils.plot_psd_s11(psd_s11off, psd_s11on)
plot_utils.plot_psd_s12(psd_s12off, psd_s12on)
plot_utils.plot_psd_s13(psd_s13off, psd_s13on)
plot_utils.plot_psd_s14(psd_s14off, psd_s14on)
plot_utils.plot_psd_s15(psd_s15off, psd_s15on)
#plot_utils.plot_psd_s15(psd_s15off, psd_s15on)
#plot_utils.plot_psd_s16(psd_s16off, psd_s16on)

print("done")

from matplotlib.patheffects import PathPatchEffect, SimpleLineShadow, Normal
sns.set()

# Theta
x_ticks = np.arange(-2,9)
# find peak in plot and write frequency down 
peak_3_off = psd_s3off[4:15]
peak_4_off = psd_s4off[6:17]
peak_5_off = psd_s5off[3:14]

peak_6_off = psd_s6off[5:16]
peak_7_off = psd_s7off[4:15]

peak_8_off = psd_s8off[4:15]
peak_9_off = psd_s9off[5:16]
peak_11_off = psd_s11off[3:14]
peak_12_off = psd_s12off[7:18]
peak_13_off = psd_s13off[5:16]
peak_14_off = psd_s14off[3:14]
peak_15_off = psd_s15off[5:16]
peak_g_off = psd_off[5:16]

peak_3_on = psd_s3on[6:17]
peak_4_on = psd_s4on[6:17]
peak_5_on = psd_s5on[4:15]
peak_6_on = psd_s6on[4:15]
peak_7_on = psd_s7on[3:14]
peak_8_on = psd_s8on[2:13]
peak_9_on = psd_s9on[5:16]
peak_11_on = psd_s11on[3:14]
peak_12_on = psd_s12on[7:18]
peak_13_on = psd_s13on[5:16]
peak_14_on = psd_s14on[3:14]
peak_15_on = psd_s15on[5:16]
peak_g_on = psd_on[3:14]

plt.subplot(1,2,1)
plt.plot(x_ticks, peak_3_off,  color='grey', alpha=0.5)
plt.plot(x_ticks, peak_4_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_5_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_6_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_7_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_8_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_9_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_11_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_12_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_13_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_14_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_15_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_g_off, color='red', linewidth=3, path_effects=[SimpleLineShadow(shadow_color="red", linewidth=4),Normal()])
plt.legend(title="Theta", frameon=False)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Relative spectral power (au)")
plt.suptitle('STN')
plt.title('OFF')

plt.subplot(1,2,2)
plt.plot(x_ticks, peak_3_on,  color='grey', alpha=0.5)
plt.plot(x_ticks, peak_4_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_5_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_6_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_7_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_8_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_9_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_11_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_12_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_13_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_14_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_15_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_g_on, color='red', linewidth=3, path_effects=[SimpleLineShadow(shadow_color="red", linewidth=4),Normal()])
plt.legend(title="Theta", frameon=False)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Relative spectral power (au)")
plt.suptitle('STN')
plt.title('ON')

plt.show()



# Beta
x_ticks = np.arange(-5,6)
# find peak in plot and write frequency down 
peak_3_off = psd_s3off[10:21]
peak_4_off = psd_s4off[10:21]
peak_5_off = psd_s5off[12:23]

peak_6_off = psd_s6off[21:32]
peak_7_off = psd_s7off[16:27]

peak_8_off = psd_s8off[11:22]
peak_9_off = psd_s9off[15:26]
peak_11_off = psd_s11off[9:20]
peak_12_off = psd_s12off[19:30]
peak_13_off = psd_s13off[9:20]
peak_14_off = psd_s14off[16:27]
peak_15_off = psd_s15off[10:21]
peak_g_off = psd_off[10:21]

peak_3_on = psd_s3on[10:21]
peak_4_on = psd_s4on[12:23]
peak_5_on = psd_s5on[22:33]
peak_6_on = psd_s6on[22:33]
peak_7_on = psd_s7on[16:27]
peak_8_on = psd_s8on[8:19]
peak_9_on = psd_s9on[15:26]
peak_11_on = psd_s11on[10:21]
peak_12_on = psd_s12on[20:31]
peak_13_on = psd_s13on[19:30]
peak_14_on = psd_s14on[17:28]
peak_15_on = psd_s15on[10:21]
peak_g_on = psd_on[10:21]

plt.subplot(1,2,1)
plt.plot(x_ticks, peak_3_off,  color='grey', alpha=0.5)
plt.plot(x_ticks, peak_4_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_5_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_6_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_7_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_8_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_9_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_11_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_12_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_13_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_14_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_15_off, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_g_off, color='red', linewidth=3, path_effects=[SimpleLineShadow(shadow_color="red", linewidth=5),Normal()])
plt.legend(title="Beta", frameon=False)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Relative spectral power (au)")
plt.suptitle('STN')
plt.title('OFF')

plt.subplot(1,2,2)
plt.plot(x_ticks, peak_3_on,  color='grey', alpha=0.5)
plt.plot(x_ticks, peak_4_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_5_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_6_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_7_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_8_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_9_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_11_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_12_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_13_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_14_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_15_on, color='grey', alpha=0.5)
plt.plot(x_ticks, peak_g_on, color='red', linewidth=3, path_effects=[SimpleLineShadow(shadow_color="red", linewidth=5),Normal()])
plt.legend(title="Beta", frameon=False)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Relative spectral power (au)")
plt.suptitle('STN')
plt.title('ON')

plt.show()
