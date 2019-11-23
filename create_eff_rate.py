#!/usr/bin/env python
"""Inspect ROOT files."""
from __future__ import print_function

import logging as log

import ROOT
from ROOT import TCanvas, TColor, TGaxis, TH1F, TPad, TH2F
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

def GetEfficiency(df_vbf, deeptau_thr, pt_thr):
    n_events = df_vbf.Count()
    df_vbf = df_vbf.Define('ntaus','getNtaus(deepTau_VSjet,tau_pt,{},{})'.format(deeptau_thr,pt_thr))
    df_vbf = df_vbf.Filter('ntaus >= 1')#to bechanged to 2!!!
    n_events_passed = df_vbf.Count()
    #print("nevents: ",n_events.GetValue())
    #print("n_events_passed: ",n_events_passed.GetValue())
    eff = (float(n_events_passed.GetValue())/float(n_events.GetValue()))
    #print("eff: %2f "%(eff))
    return eff

def BaseRate(n_initial, df_zb, pt_thr):
    n_events = df_zb.Count()
    df_zb = df_zb.Define('ntaus','getNtaus_base(tau_mediumIsoAbs,tau_mediumIsoRel,tau_pt,{})'.format(pt_thr))
    df_zb = df_zb.Filter('ntaus >= 1')#to bechanged to 2!!!
    n_events_passed = df_zb.Count()
    #print("nevents: ",n_events.GetValue())
    #print("n_events_passed: ",n_events_passed.GetValue())
    rate = (float(n_events_passed.GetValue())/float(n_initial))*2544*11245#*77560.28 #forL1
    #print("base rate: %2f Hz"%(rate))
    return rate

pt_ranges = [20,30,40,50,70,100,1000]
pt_thrs = [20,25,30,35,40,45]
eff_name="efficiency_VBF/efficiency_VBF.root"
rate_name="rate_ZeroBias/rate_ZeroBias.root"

RDF = ROOT.ROOT.RDataFrame
df_eff = RDF("final_counter", eff_name)
df_rate = RDF("final_counter", rate_name)

canvas1 = ROOT.TCanvas("pippo1","pippo1")
canvas1.cd()
myHisto = df_eff.Histo1D("tau_pt")
myHisto.Draw()
canvas1.Print("pt_dataFrame.pdf")

tfile = ROOT.TFile(eff_name)
tfile_rate = ROOT.TFile(rate_name)

initial_rate = []
max_rate = []
efficiency = []
if not tfile.IsZombie() and not tfile_rate.IsZombie():
    f_eff = ROOT.TFile.Open(eff_name)
    f_rate = ROOT.TFile.Open(rate_name)
    initialCounter_eff = f_eff.Get("initial_counter")
    initialCounter_rate = f_rate.Get("initial_counter")

    for thr in pt_thrs:
        print("pt_thr: ",thr)
        initial_rate.append(GetRate(initialCounter_rate.GetEntries(),df_rate,0,thr))
        max_rate.append(GetRate(initialCounter_rate.GetEntries(),df_rate,1,thr))


        def f(deeptau_thr):
            return GetRate(initialCounter_rate.GetEntries(),df_rate,deeptau_thr,thr)-BaseRate(initialCounter_rate.GetEntries(),df_rate,thr)

        solution = optimize.root_scalar(f,x0=0.2,x1=0.25,method='secant')
        deep_thr = solution.root
        print("Deeptau thr: ",deep_thr)

        efficiency.append(GetEfficiency(df_eff,deep_thr,thr))

    print("initial_rate vector: ",initial_rate)
    print("max_rate vector: ",max_rate)
    print("efficiency vector: ",efficiency)



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
