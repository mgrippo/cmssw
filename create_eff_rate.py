#!/usr/bin/env python
"""Inspect ROOT files."""
from __future__ import print_function

import logging as log

import ROOT
from ROOT import TCanvas, TColor, TGaxis, TH1F, TPad, TH2F
ROOT.gInterpreter.Declare('#include "PyInterface.h"')

def GetRate(n_initial, df_zb, deeptau_thr, pt_thr):
    n_events = df_zb.Count()
    df_zb = df_zb.Define('ntaus','getNtaus(deepTau_VSjet,tau_pt,{},{})'.format(deeptau_thr,pt_thr))
    df_zb = df_zb.Filter('ntaus >= 2')
    n_events_passed = df_zb.Count()
    print("nevents: ",n_events.GetValue())
    print("n_events_passed: ",n_events_passed.GetValue())



def GetEfficiency(n_initial, df_vbf, deeptau_thr, pt_thr):
    n_taus = df_zb.Filter('deepTau_VSjet > {} && tau_pt > {}'.format(deeptau_thr,pt_thr)).Count()
    if(n_taus >= 2):
        print("Found 2 taus in ZB: ",n_taus)

pt_ranges = [20,30,40,50,70,100,1000]
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

GetRate(100,df_rate,0,0)
GetRate(100,df_eff,0,0)

tfile = ROOT.TFile(eff_name)
tfile_rate = ROOT.TFile(rate_name)
if not tfile.IsZombie() and not tfile_rate.IsZombie():
    # Print this, rather than log it, so users know what the file's called
    print('Loaded {0!r}'.format(eff_name))
    print('Loaded {0!r}'.format(rate_name))
    f = ROOT.TFile.Open(eff_name)
    f_rate = ROOT.TFile.Open(rate_name)
    myTree = f.Get("final_counter")
    myTree_rate = f_rate.Get("final_counter")
    initialCounter = f.Get("initial_counter")
    initialCounter_rate = f_rate.Get("initial_counter")
    print('Entries initial counter eff: ',initialCounter.GetEntries())
    print('Entries initial counter rate: ',initialCounter_rate.GetEntries())
    canvas = ROOT.TCanvas("pippo","pippo")
    canvas.cd()
    myTree.Draw("deepTau_VSjet:tau_pt", "tau_pt<200","colz")
    canvas.Print("deepTau_vs_pt.pdf")
    hist = TH2F("hist","hist",100,0,200,1000,0,1)
    myTree.Draw("deepTau_VSjet:tau_pt>>hist", "tau_pt<200","colz")
    canvas2 = ROOT.TCanvas("pippo1","pippo1")
    canvas2.cd()
    hist.Scale(1/initialCounter.GetEntries())
    hist.Draw("colz")
    canvas2.Print("efficiency.pdf")


else:
    print('Could not load file {0!r}'.format(fname))
