#!/usr/bin/env python
"""Inspect ROOT files."""
from __future__ import print_function

import logging as log

import ROOT
from ROOT import TCanvas, TColor, TGaxis, TH1F, TPad, TH2F
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize
ROOT.gInterpreter.Declare('#include "PyInterface.h"')

def GetRate(n_initial, df_zb, deeptau_thr, pt_thr):
    n_events = df_zb.Count()
    df_zb = df_zb.Define('ntaus','getNtaus(deepTau_VSjet,tau_pt,{},{})'.format(deeptau_thr,pt_thr))
    df_zb = df_zb.Filter('ntaus >= 1')#to bechanged to 2!!!
    n_events_passed = df_zb.Count()
    #print("nevents: ",n_events.GetValue())
    #print("n_events_passed: ",n_events_passed.GetValue())
    rate = (float(n_events_passed.GetValue())/float(n_initial))*2544*11245#*77560.28 #forL1
    #print("rate: %2f Hz"%(rate))
    return rate

def GetEfficiency(df_vbf, deeptau_thr, pt_thr,pt_bin_1,pt_bin_2):
    n_events = df_vbf.Count()
    df_vbf = df_vbf.Define('ntaus','getNtaus_inPtBin(deepTau_VSjet,tau_pt,{},{},{},{})'.format(deeptau_thr,pt_thr,pt_bin_1,pt_bin_2))
    df_vbf = df_vbf.Filter('ntaus >= 1')#to bechanged to 2!!!
    n_events_passed = df_vbf.Count()
    #print("nevents: ",n_events.GetValue())
    #print("n_events_passed: ",n_events_passed.GetValue())
    eff = (float(n_events_passed.GetValue())/float(n_events.GetValue()))
    #print("eff: %2f "%(eff))
    return eff

def GetEfficiency_Simple(df_vbf, deeptau_thr, pt_thr):
    n_events = df_vbf.Count()
    df_vbf = df_vbf.Define('ntaus','getNtaus(deepTau_VSjet,tau_pt,{},{})'.format(deeptau_thr,pt_thr))
    df_vbf = df_vbf.Filter('ntaus >= 1')#to bechanged to 2!!!
    n_events_passed = df_vbf.Count()
    eff = (float(n_events_passed.GetValue())/float(n_events.GetValue()))
    return eff

def BaseRate(n_initial, df_zb, pt_thr):
    n_events = df_zb.Count()
    #medium
    df_zb_m = df_zb.Define('ntaus','getNtaus_base(tau_mediumIsoAbs,tau_mediumIsoRel,tau_pt,{})'.format(pt_thr))
    df_zb_m = df_zb_m.Filter('ntaus >= 1')#to bechanged to 2!!!
    n_events_passed_m = df_zb_m.Count()
    rate_m = (float(n_events_passed_m.GetValue())/float(n_initial))*2544*11245#*77560.28 #forL1
    return rate_m

def BaseRate_complete(n_initial, df_zb, pt_thr):
    n_events = df_zb.Count()
    #medium
    df_zb_m = df_zb.Define('ntaus','getNtaus_base(tau_mediumIsoAbs,tau_mediumIsoRel,tau_pt,{})'.format(pt_thr))
    df_zb_m = df_zb_m.Filter('ntaus >= 1')#to bechanged to 2!!!
    n_events_passed_m = df_zb_m.Count()
    rate_m = (float(n_events_passed_m.GetValue())/float(n_initial))*2544*11245#*77560.28 #forL1
    #loose
    df_zb_l = df_zb.Define('ntaus_l','getNtaus_base_loose(tau_looseIsoAbs,tau_looseIsoRel,tau_pt,{})'.format(pt_thr))
    df_zb_l = df_zb_l.Filter('ntaus_l >= 1')#to bechanged to 2!!!
    n_events_passed_l = df_zb_l.Count()
    rate_l = (float(n_events_passed_l.GetValue())/float(n_initial))*2544*11245#*77560.28 #forL1
    # #tight
    df_zb_t = df_zb.Define('ntaus_t','getNtaus_base_tight(tau_tightIsoAbs,tau_tightIsoRel,tau_pt,{})'.format(pt_thr))
    df_zb_t = df_zb_t.Filter('ntaus_t >= 1')#to bechanged to 2!!!
    n_events_passed_t = df_zb_t.Count()
    rate_t = (float(n_events_passed_t.GetValue())/float(n_initial))*2544*11245#*77560.28 #forL1
    return rate_l, rate_m, rate_t

def BaseEfficiency_Simple(df_vbf,pt_thr):
    n_events = df_vbf.Count()
    #medium
    df_vbf_m = df_vbf.Define('ntaus_m','getNtaus_base(tau_mediumIsoAbs,tau_mediumIsoRel,tau_pt,{})'.format(pt_thr))
    df_vbf_m = df_vbf_m.Filter('ntaus_m >= 1')#to bechanged to 2!!!
    n_events_passed_m = df_vbf_m.Count()
    eff_m = (float(n_events_passed_m.GetValue())/float(n_events.GetValue()))
    #loose
    df_vbf_l = df_vbf.Define('ntaus_l','getNtaus_base_loose(tau_looseIsoAbs,tau_looseIsoRel,tau_pt,{})'.format(pt_thr))
    df_vbf_l = df_vbf_l.Filter('ntaus_l >= 1')#to bechanged to 2!!!
    n_events_passed_l = df_vbf_l.Count()
    eff_l = (float(n_events_passed_l.GetValue())/float(n_events.GetValue()))
    #tight
    df_vbf_t = df_vbf.Define('ntaus_t','getNtaus_base_tight(tau_tightIsoAbs,tau_tightIsoRel,tau_pt,{})'.format(pt_thr))
    df_vbf_t = df_vbf_t.Filter('ntaus_t >= 1')#to bechanged to 2!!!
    n_events_passed_t = df_vbf_t.Count()
    eff_t = (float(n_events_passed_t.GetValue())/float(n_events.GetValue()))
    return eff_l, eff_m, eff_t

def BaseEfficiency(df_vbf,pt_thr,pt_bin_1,pt_bin_2):
    n_events = df_vbf.Count()
    #medium
    df_vbf_m = df_vbf.Define('ntaus_m','getNtaus_base_inPtBin_Medium(tau_mediumIsoAbs,tau_mediumIsoRel,tau_pt,{},{},{})'.format(pt_thr,pt_bin_1,pt_bin_2))
    df_vbf_m = df_vbf_m.Filter('ntaus_m >= 1')#to bechanged to 2!!!
    n_events_passed_m = df_vbf_m.Count()
    eff_m = (float(n_events_passed_m.GetValue())/float(n_events.GetValue()))
    #loose
    df_vbf_l = df_vbf.Define('ntaus_l','getNtaus_base_inPtBin_Loose(tau_looseIsoAbs,tau_looseIsoRel,tau_pt,{},{},{})'.format(pt_thr,pt_bin_1,pt_bin_2))
    df_vbf_l = df_vbf_l.Filter('ntaus_l >= 1')#to bechanged to 2!!!
    n_events_passed_l = df_vbf_l.Count()
    eff_l = (float(n_events_passed_l.GetValue())/float(n_events.GetValue()))
    #tight
    df_vbf_t = df_vbf.Define('ntaus_t','getNtaus_base_inPtBin_Tight(tau_tightIsoAbs,tau_tightIsoRel,tau_pt,{},{},{})'.format(pt_thr,pt_bin_1,pt_bin_2))
    df_vbf_t = df_vbf_t.Filter('ntaus_t >= 1')#to bechanged to 2!!!
    n_events_passed_t = df_vbf_t.Count()
    eff_t = (float(n_events_passed_t.GetValue())/float(n_events.GetValue()))
    return eff_l, eff_m, eff_t

#pt_bins = [20,25,30,35,40,45,50,60,70,100,150]
pt_bins = np.array([20,25,30,35])
#pt_thrs = [20,25,30,35,40,45]
pt_thrs = [20,25,30,35]

deeptau_thrs = np.linspace(0.0, 1.0, num=10)
eff_name="efficiency_Tuple.root"
rate_name="rate_Tuple.root"

RDF = ROOT.ROOT.RDataFrame
df_eff = RDF("final_counter", eff_name)
df_rate = RDF("final_counter", rate_name)

# canvas1 = ROOT.TCanvas("pippo1","pippo1")
# canvas1.cd()
# myHisto = df_eff.Histo1D("tau_pt")
# myHisto.Draw()
# canvas1.Print("pt_dataFrame.pdf")

tfile = ROOT.TFile(eff_name)
tfile_rate = ROOT.TFile(rate_name)

initial_rate = []
max_rate = []
efficiency_total = {}
full_deep_rate = {}
full_deep_eff = {}
efficiency_l = {}
efficiency_m = {}
efficiency_t = {}
rate_total_l = {}
rate_total_m = {}
rate_total_t = {}
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
fig4 = plt.figure()
ax4 = fig4.add_subplot(111)

if not tfile.IsZombie() and not tfile_rate.IsZombie():
    f_eff = ROOT.TFile.Open(eff_name)
    f_rate = ROOT.TFile.Open(rate_name)
    initialCounter_eff = f_eff.Get("initial_counter")
    initialCounter_rate = f_rate.Get("initial_counter")

    for thr in pt_thrs:

        efficiency = []
        efficiency_base_l = []
        efficiency_base_m = []
        efficiency_base_t = []
        for pt_index in range(len(pt_bins) - 1):
            #eff vs pt for deep
            print("pt_thr: ",thr)
            print("pt_bin [ ",pt_bins[pt_index],",",pt_bins[pt_index + 1],"]")
            initial_rate.append(GetRate(initialCounter_rate.GetEntries(),df_rate,0,35))
            max_rate.append(GetRate(initialCounter_rate.GetEntries(),df_rate,1,thr))


            def f(deeptau_thr):
                return GetRate(initialCounter_rate.GetEntries(),df_rate,deeptau_thr,thr)-BaseRate(initialCounter_rate.GetEntries(),df_rate,35)

            solution = optimize.root_scalar(f,bracket=[0,1],method='bisect')
            deep_thr = solution.root
            print("Deeptau thr: ",deep_thr)
            eff=GetEfficiency(df_eff,deep_thr,thr,pt_bins[pt_index],pt_bins[pt_index + 1])
            print("efficiency: ", eff)
            efficiency.append(eff)

            #eff vs pt for base
            eff_l, eff_m, eff_t=BaseEfficiency(df_eff,35,pt_bins[pt_index],pt_bins[pt_index + 1])
            efficiency_base_l.append(eff_l)
            efficiency_base_m.append(eff_m)
            efficiency_base_t.append(eff_t)

        efficiency_total[thr]=efficiency
        ax1.plot((pt_bins[1:] + pt_bins[:-1]) / 2,efficiency_total[thr], 'o--') #non disegna le 4 curve per ogni thr
        ax2.plot((pt_bins[1:] + pt_bins[:-1]) / 2,efficiency_base_l, 'r--') #non disegna i punti per ogni pt
        ax2.plot((pt_bins[1:] + pt_bins[:-1]) / 2,efficiency_base_m, 'g')
        ax2.plot((pt_bins[1:] + pt_bins[:-1]) / 2,efficiency_base_t, 'b')

        #eff vs rate deep
        deep_rate = []
        deep_eff = []
        for deep_thr in deeptau_thrs :
            print("deepTau_thr:",deep_thr)
            deep_rate.append(GetRate(initialCounter_rate.GetEntries(),df_rate,deep_thr,thr))
            deep_eff.append(GetEfficiency_Simple(df_eff,deep_thr,thr))
        full_deep_rate[thr] = deep_rate
        full_deep_eff[thr] = deep_eff

        ax3.plot(full_deep_eff[thr], full_deep_rate[thr], 'o--')

        eff_l, eff_m, eff_t=BaseEfficiency_Simple(df_eff,thr)
        rate_l, rate_m, rate_t=BaseRate_complete(initialCounter_rate.GetEntries(),df_rate,thr)
        efficiency_l[thr] = eff_l
        efficiency_m[thr] = eff_m
        efficiency_t[thr] = eff_t

        rate_total_l[thr] = rate_l
        rate_total_m[thr] = rate_m
        rate_total_t[thr] = rate_t

        ax4.plot(efficiency_l[thr],rate_total_l[thr], 'r')
        ax4.plot(efficiency_m[thr],rate_total_m[thr], 'g')
        ax4.plot(efficiency_t[thr],rate_total_t[thr], 'b')

    fig1.savefig("fig1.pdf")
    fig2.savefig("fig2.pdf")
    fig3.savefig("fig3.pdf")
    fig4.savefig("fig4.pdf")


    print("initial_rate vector: ",initial_rate)
    print("max_rate vector: ",max_rate)
    print("efficiency total: ",efficiency_total)





    # canvas = ROOT.TCanvas("pippo","pippo")
    # canvas.cd()
    # myTree.Draw("deepTau_VSjet:tau_pt", "tau_pt<200","colz")
    # canvas.Print("deepTau_vs_pt.pdf")
    # hist = TH2F("hist","hist",100,0,200,1000,0,1)
    # myTree.Draw("deepTau_VSjet:tau_pt>>hist", "tau_pt<200","colz")
    # canvas2 = ROOT.TCanvas("pippo1","pippo1")
    # canvas2.cd()
    # hist.Scale(1/initialCounter.GetEntries())
    # hist.Draw("colz")
    # canvas2.Print("efficiency.pdf")


else:
    print('Could not load file {0!r}'.format(fname))
