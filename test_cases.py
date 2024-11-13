import MDAnalysis as mda
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.integrate import simps
import time
from matplotlib.patches import Patch
import nglview as nv

from twodanalysis import twod_analysis


top = "dopcchol_Charmm.pdb"
traj = "dopcchol_Charmm.pdb"
tpr = "veamos.tpr"


#top = "membrane.gro"
#traj = "membrane.xtc"
membrane = twod_analysis(top,
                         traj,
                        #tpr=tpr,
                        v_min = -10,
                        v_max = 95,
                        verbose = True,
                        add_radii = True)

#print(membrane.guess_minmax_space())

lipid_list = list(membrane.lipid_list)
lipid_list.remove("CHL1")

layers = ["top", "bot"]
nbins = 50
lipids = membrane.chain_info
#membrane.visualize_polarity()
plt.show()


#for layer in layers:
#    for key in lipid_list:
#        H, edges = membrane.order_histogram(key, layer, nbins, lipids[key])
#        print(key, layer, nbins, lipids[key], 0, 180)
#        plt.imshow(H,cmap = "Spectral", extent = [edges[0][0], edges[0][-1], edges[1][0], edges[1][-1]])
#        plt.colorbar(cmap = "Spectral")
#        plt.savefig(f"{key}_test_{layer}.png")
#        plt.close()
#plt.show()
layer = "top"
#mat_top, edges = membrane.all_lip_order("top", nbins,
#                        start = 0,
#                        final = 100,
#                        step = 1)#


#mat_bot, edges = membrane.all_lip_order("bot", nbins,
#                        start = 0,
#                        final = 100,
#                        step = 1)

membrane.packing_defects(start = 0, final = 10, step =1,nbins = 80, layer = "top", height = True)

#plt.close()
#plt.scatter(mat_top.flatten(), mat_bot.flatten(), alpha = 0.5)
#plt.savefig("corr.png")
#plt.close()

#mat_both, edges = membrane.all_lip_order("both", nbins,
#                        start = 0,
#                        final = 100,
#                        step = 1)



#mat_thi, edges = membrane.thickness(50, start = 0, final = 100, step = 1)
#plt.close()
#plt.scatter(mat_both.flatten(), mat_thi.flatten(), alpha = 0.5)
#plt.savefig("corr_thilip.png")
#plt.close()
#print(membrane.lipid_list)