import MDAnalysis as mda
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from protein2D_analysis import protein2D_analysis

trj_path='/home/antonio/Desktop/VIRMAT/Paper_PB_KDE/SIMs/RBD-PBLs_wGlyc_closed_layed/glyc_head/rep1/omicron_10/'
u=mda.Universe(f"{trj_path}md_0_1.tpr",f"{trj_path}md_short_compact.xtc")
sel = u.select_atoms("resid 193-200 or protein")
ag_analysis = protein2D_analysis(sel)
ag_analysis.getPositions()
print(ag_analysis.pos.shape)
zlim=60
Nframes=200

'''
########### TEST GENERAL MODULES #############

pos=ag_analysis.getPositions(inplace=False)
pos_selected=ag_analysis.FilterMinFrames(pos,zlim=zlim, Nframes=Nframes, control_plots=False)
print(ag_analysis.pos.shape)
print(pos_selected.shape)
############ TEST POLAR ANALYSIS ############
hist_arr,pos_hist=ag_analysis.PolarAnalysis('resid 193-200 or resid 12',900, sort=[1,2,3,4,5,6,7,8,0],zlim=zlim,control_plots=False,plot=True)
print(hist_arr.shape,pos_hist.shape)
############# TEST RADII of GYRATION ANALYSIS ########

rgs=ag_analysis.getRgs2D()
print(rgs.shape)
ag_analysis.RgPerpvsRgsPar(rgs, 'tab:green',show=True)

# ##########TEST Contour PLOTS ################

paths=ag_analysis.getKDEAnalysis(zlim,Nframes)
protein2D_analysis.plotPathsInLevel(paths,1)
areas=ag_analysis.getAreas(2,getTotal=True)
print(areas)
'''
##### TEST HBONDS PLOTS #####

sel_for_path = u.select_atoms("resid 193-200")
ag_for_path = protein2D_analysis(sel_for_path)
ag_for_path.getPositions()
paths=ag_for_path.getKDEAnalysis(zlim,Nframes)
ag_analysis.getHbonds('resname DOL','resid 193-200', update_selections=False,trj_plot=False)
ag_analysis.plotHbondsPerResidues(paths,contour_lvls_to_plot=[0,5,8],top=5, print_table=True)
# ag_analysis.plotHbondsPerResidues(paths,contour_lvls_to_plot=None, print_table=True)



