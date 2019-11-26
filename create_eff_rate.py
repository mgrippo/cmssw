#!/usr/bin/env python
"""Inspect ROOT files."""
from __future__ import print_function

import logging as log

import ROOT
from ROOT import TCanvas, TColor, TGaxis, TH1F, TPad, TH2F
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize
from statsmodels.stats.proportion import proportion_confint
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
    ci = proportion_confint(count=n_events_passed.GetValue(), nobs=n_initial, alpha=0.32, method='beta')
    err_low = (rate - ci[0]*2544*11245)
    err_up = (ci[1]*2544*11245 - rate)
    return rate, err_low, err_up

def GetEfficiency(df_vbf, deeptau_thr, pt_thr,pt_bin_1,pt_bin_2):
    df_vbf = df_vbf.Define('ntaus_den','getNtaus_inPtBin(deepTau_VSjet,tau_pt,{},{},{},{})'.format(0,0,pt_bin_1,pt_bin_2))
    df_vbf_den = df_vbf.Filter('ntaus_den >= 1')#to bechanged to 2!!!
    n_events = df_vbf_den.Count()
    df_vbf = df_vbf.Define('ntaus','getNtaus_inPtBin(deepTau_VSjet,tau_pt,{},{},{},{})'.format(deeptau_thr,pt_thr,pt_bin_1,pt_bin_2))
    df_vbf_num = df_vbf.Filter('ntaus >= 1')#to bechanged to 2!!!
    n_events_passed = df_vbf_num.Count()
    #print("nevents: ",n_events.GetValue())
    #print("n_events_passed: ",n_events_passed.GetValue())
    eff = (float(n_events_passed.GetValue())/float(n_events.GetValue()))
    #print("eff: %2f "%(eff))
    ci = proportion_confint(count=n_events_passed.GetValue(), nobs=n_events.GetValue(), alpha=0.32, method='beta')
    err_low = (eff - ci[0])
    err_up = (ci[1] - eff)
    return eff, err_low, err_up

def GetEfficiency_Simple(df_vbf, deeptau_thr, pt_thr):
    df_vbf = df_vbf.Define('ntaus_den','getNtaus(deepTau_VSjet,tau_pt,{},{})'.format(0,0))
    df_vbf_den = df_vbf.Filter('ntaus_den >= 1')#to bechanged to 2!!!
    n_events = df_vbf_den.Count()
    df_vbf = df_vbf.Define('ntaus','getNtaus(deepTau_VSjet,tau_pt,{},{})'.format(deeptau_thr,pt_thr))
    df_vbf_num = df_vbf.Filter('ntaus >= 1')#to bechanged to 2!!!
    n_events_passed = df_vbf_num.Count()
    eff = (float(n_events_passed.GetValue())/float(n_events.GetValue()))
    ci = proportion_confint(count=n_events_passed.GetValue(), nobs=n_events.GetValue(), alpha=0.32, method='beta')
    err_low = (eff - ci[0])
    err_up = (ci[1] - eff)
    return eff, err_low, err_up

def BaseRate(n_initial, df_zb, pt_thr):
    n_events = df_zb.Count()
    #medium
    df_zb_m = df_zb.Define('ntaus','getNtaus_base(tau_mediumIsoAbs,tau_mediumIsoRel,tau_pt,{})'.format(pt_thr))
    df_zb_m = df_zb_m.Filter('ntaus >= 1')#to bechanged to 2!!!
    n_events_passed_m = df_zb_m.Count()
    rate_m = (float(n_events_passed_m.GetValue())/float(n_initial))*2544*11245#*77560.28 #forL1
    ci_m = proportion_confint(count=n_events_passed_m.GetValue(), nobs=n_initial, alpha=0.32, method='beta')
    err_low_m = (rate_m - ci_m[0]*2544*11245)
    err_up_m = (ci_m[1]*2544*11245 - rate_m)
    return rate_m, err_low_m, err_up_m

def BaseRate_complete(n_initial, df_zb, pt_thr):
    n_events = df_zb.Count()
    #medium
    df_zb_m = df_zb.Define('ntaus','getNtaus_base(tau_mediumIsoAbs,tau_mediumIsoRel,tau_pt,{})'.format(pt_thr))
    df_zb_m = df_zb_m.Filter('ntaus >= 1')#to bechanged to 2!!!
    n_events_passed_m = df_zb_m.Count()
    rate_m = (float(n_events_passed_m.GetValue())/float(n_initial))*2544*11245#*77560.28 #forL1
    ci_m = proportion_confint(count=n_events_passed_m.GetValue(), nobs=n_initial, alpha=0.32, method='beta')
    err_low_m = (rate_m - ci_m[0]*2544*11245)
    err_up_m = (ci_m[1]*2544*11245 - rate_m)
    #loose
    df_zb_l = df_zb.Define('ntaus_l','getNtaus_base_loose(tau_looseIsoAbs,tau_looseIsoRel,tau_pt,{})'.format(pt_thr))
    df_zb_l = df_zb_l.Filter('ntaus_l >= 1')#to bechanged to 2!!!
    n_events_passed_l = df_zb_l.Count()
    rate_l = (float(n_events_passed_l.GetValue())/float(n_initial))*2544*11245#*77560.28 #forL1
    ci_l = proportion_confint(count=n_events_passed_l.GetValue(), nobs=n_initial, alpha=0.32, method='beta')
    err_low_l = (rate_l - ci_l[0]*2544*11245)
    err_up_l = (ci_l[1]*2544*11245 - rate_l)
    # #tight
    df_zb_t = df_zb.Define('ntaus_t','getNtaus_base_tight(tau_tightIsoAbs,tau_tightIsoRel,tau_pt,{})'.format(pt_thr))
    df_zb_t = df_zb_t.Filter('ntaus_t >= 1')#to bechanged to 2!!!
    n_events_passed_t = df_zb_t.Count()
    rate_t = (float(n_events_passed_t.GetValue())/float(n_initial))*2544*11245#*77560.28 #forL1
    ci_t = proportion_confint(count=n_events_passed_t.GetValue(), nobs=n_initial, alpha=0.32, method='beta')
    err_low_t = (rate_t - ci_t[0]*2544*11245)
    err_up_t = (ci_t[1]*2544*11245 - rate_t)
    return rate_l, err_low_l, err_up_l, rate_m, err_low_m, err_up_m, rate_t, err_low_t, err_up_t

def BaseEfficiency_Simple(df_vbf,pt_thr):
    df_vbf = df_vbf.Define('ntaus_den','getNtaus(deepTau_VSjet,tau_pt,{},{})'.format(0,0))
    df_vbf_den = df_vbf.Filter('ntaus_den >= 1')#to bechanged to 2!!!
    n_events = df_vbf_den.Count()
    #medium
    df_vbf_m = df_vbf.Define('ntaus_m','getNtaus_base(tau_mediumIsoAbs,tau_mediumIsoRel,tau_pt,{})'.format(pt_thr))
    df_vbf_m = df_vbf_m.Filter('ntaus_m >= 1')#to bechanged to 2!!!
    n_events_passed_m = df_vbf_m.Count()
    eff_m = (float(n_events_passed_m.GetValue())/float(n_events.GetValue()))
    ci_m = proportion_confint(count=n_events_passed_m.GetValue(), nobs=n_events.GetValue(), alpha=0.32, method='beta')
    err_low_m = (eff_m - ci_m[0])
    err_up_m = (ci_m[1] - eff_m)
    #loose
    df_vbf_l = df_vbf.Define('ntaus_l','getNtaus_base_loose(tau_looseIsoAbs,tau_looseIsoRel,tau_pt,{})'.format(pt_thr))
    df_vbf_l = df_vbf_l.Filter('ntaus_l >= 1')#to bechanged to 2!!!
    n_events_passed_l = df_vbf_l.Count()
    eff_l = (float(n_events_passed_l.GetValue())/float(n_events.GetValue()))
    ci_l = proportion_confint(count=n_events_passed_l.GetValue(), nobs=n_events.GetValue(), alpha=0.32, method='beta')
    err_low_l = (eff_l - ci_l[0])
    err_up_l = (ci_l[1] - eff_l)
    #tight
    df_vbf_t = df_vbf.Define('ntaus_t','getNtaus_base_tight(tau_tightIsoAbs,tau_tightIsoRel,tau_pt,{})'.format(pt_thr))
    df_vbf_t = df_vbf_t.Filter('ntaus_t >= 1')#to bechanged to 2!!!
    n_events_passed_t = df_vbf_t.Count()
    eff_t = (float(n_events_passed_t.GetValue())/float(n_events.GetValue()))
    ci_t = proportion_confint(count=n_events_passed_t.GetValue(), nobs=n_events.GetValue(), alpha=0.32, method='beta')
    err_low_t = (eff_t - ci_t[0])
    err_up_t = (ci_t[1] - eff_t)
    return eff_l, err_low_l, err_up_l, eff_m, err_low_m, err_up_m, eff_t, err_low_t, err_up_t

def BaseEfficiency(df_vbf,pt_thr,pt_bin_1,pt_bin_2):
    df_vbf = df_vbf.Define('ntaus_den','getNtaus_inPtBin(deepTau_VSjet,tau_pt,{},{},{},{})'.format(0,0,pt_bin_1,pt_bin_2))
    df_vbf_den = df_vbf.Filter('ntaus_den >= 1')#to bechanged to 2!!!
    n_events = df_vbf_den.Count()
    #medium
    df_vbf_m = df_vbf.Define('ntaus_m','getNtaus_base_inPtBin_Medium(tau_mediumIsoAbs,tau_mediumIsoRel,tau_pt,{},{},{})'.format(pt_thr,pt_bin_1,pt_bin_2))
    df_vbf_m = df_vbf_m.Filter('ntaus_m >= 1')#to bechanged to 2!!!
    n_events_passed_m = df_vbf_m.Count()
    eff_m = (float(n_events_passed_m.GetValue())/float(n_events.GetValue()))
    ci_m = proportion_confint(count=n_events_passed_m.GetValue(), nobs=n_events.GetValue(), alpha=0.32, method='beta')
    err_low_m = (eff_m - ci_m[0])
    err_up_m = (ci_m[1] - eff_m)
    #loose
    df_vbf_l = df_vbf.Define('ntaus_l','getNtaus_base_inPtBin_Loose(tau_looseIsoAbs,tau_looseIsoRel,tau_pt,{},{},{})'.format(pt_thr,pt_bin_1,pt_bin_2))
    df_vbf_l = df_vbf_l.Filter('ntaus_l >= 1')#to bechanged to 2!!!
    n_events_passed_l = df_vbf_l.Count()
    eff_l = (float(n_events_passed_l.GetValue())/float(n_events.GetValue()))
    ci_l = proportion_confint(count=n_events_passed_l.GetValue(), nobs=n_events.GetValue(), alpha=0.32, method='beta')
    err_low_l = (eff_l - ci_l[0])
    err_up_l = (ci_l[1] - eff_l)
    #tight
    df_vbf_t = df_vbf.Define('ntaus_t','getNtaus_base_inPtBin_Tight(tau_tightIsoAbs,tau_tightIsoRel,tau_pt,{},{},{})'.format(pt_thr,pt_bin_1,pt_bin_2))
    df_vbf_t = df_vbf_t.Filter('ntaus_t >= 1')#to bechanged to 2!!!
    n_events_passed_t = df_vbf_t.Count()
    eff_t = (float(n_events_passed_t.GetValue())/float(n_events.GetValue()))
    ci_t = proportion_confint(count=n_events_passed_t.GetValue(), nobs=n_events.GetValue(), alpha=0.32, method='beta')
    err_low_t = (eff_t - ci_t[0])
    err_up_t = (ci_t[1] - eff_t)
    return eff_l, err_low_l, err_up_l, eff_m, err_low_m, err_up_m, eff_t, err_low_t, err_up_t

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
error_efficiency_total = {}
full_deep_rate = {}
full_deep_rate_err = {}
full_deep_eff = {}
full_deep_eff_err = {}
efficiency_l = []
efficiency_m = []
efficiency_t = []
efficiency_error_l = np.zeros( (2,len(pt_thrs)) )
efficiency_error_m = np.zeros( (2,len(pt_thrs)) )
efficiency_error_t = np.zeros( (2,len(pt_thrs)) )
rate_total_l = []
rate_total_m = []
rate_total_t = []
rate_error_l = np.zeros( (2,len(pt_thrs)) )
rate_error_m = np.zeros( (2,len(pt_thrs)) )
rate_error_t = np.zeros( (2,len(pt_thrs)) )
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
fig3 = plt.figure()
ax3 = fig3.add_subplot(111)
fig4 = plt.figure()
ax4 = fig4.add_subplot(111)
fig5 = plt.figure()
ax5 = fig5.add_subplot(111)
fig6 = plt.figure()
ax6 = fig6.add_subplot(111)

if not tfile.IsZombie() and not tfile_rate.IsZombie():
    f_eff = ROOT.TFile.Open(eff_name)
    f_rate = ROOT.TFile.Open(rate_name)
    initialCounter_eff = f_eff.Get("initial_counter")
    initialCounter_rate = f_rate.Get("initial_counter")

    for thr_index in range(len(pt_thrs)):
        print("pt_thr: ",pt_thrs[thr_index])
        efficiency = []
        error_efficiency = np.zeros( (2,len(pt_bins) - 1) )
        efficiency_base_l = []
        error_efficiency_l = np.zeros( (2,len(pt_bins) - 1) )
        efficiency_base_m = []
        error_efficiency_m = np.zeros( (2,len(pt_bins) - 1) )
        efficiency_base_t = []
        error_efficiency_t = np.zeros( (2,len(pt_bins) - 1) )

        def f(deeptau_thr):
            rate, err_low, err_up = GetRate(initialCounter_rate.GetEntries(),df_rate,deeptau_thr,pt_thrs[thr_index])
            base_rate, base_err_low, base_err_up = BaseRate(initialCounter_rate.GetEntries(),df_rate,35)
            return rate-base_rate

        solution = optimize.root_scalar(f,bracket=[0,1],method='bisect')
        deep_thr = solution.root
        print("Deeptau thr: ",deep_thr)
        # initial_rate.append(GetRate(initialCounter_rate.GetEntries(),df_rate,0,35))
        # max_rate.append(GetRate(initialCounter_rate.GetEntries(),df_rate,1,thr))
        for pt_index in range(len(pt_bins) - 1):
            #eff vs pt for deep

            print("pt_bin [ ",pt_bins[pt_index],",",pt_bins[pt_index + 1],"]")

            eff, err_low, err_up =GetEfficiency(df_eff,deep_thr,pt_thrs[thr_index],pt_bins[pt_index],pt_bins[pt_index + 1])
            print("efficiency: ", eff)
            efficiency.append(eff)
            error_efficiency[0,pt_index]=err_low
            error_efficiency[1,pt_index]=err_up

            #eff vs pt for base
            eff_l, err_low_l, err_up_l, eff_m, err_low_m, err_up_m, eff_t, err_low_t, err_up_t=BaseEfficiency(df_eff,35,pt_bins[pt_index],pt_bins[pt_index + 1])
            efficiency_base_l.append(eff_l)
            error_efficiency_l[0,pt_index]=err_low_l
            error_efficiency_l[1,pt_index]=err_up_l
            efficiency_base_m.append(eff_m)
            error_efficiency_m[0,pt_index]=err_low_m
            error_efficiency_m[1,pt_index]=err_up_m
            efficiency_base_t.append(eff_t)
            error_efficiency_t[0,pt_index]=err_low_t
            error_efficiency_t[1,pt_index]=err_up_t

        efficiency_total[thr_index]=efficiency
        error_efficiency_total[thr_index]=error_efficiency
        ax1.errorbar((pt_bins[1:] + pt_bins[:-1]) / 2,efficiency_total[thr_index],yerr=error_efficiency_total[thr_index], label=str(pt_thrs[thr_index])+' GeV') #non disegna le 4 curve per ogni thr
        ax1.set_ylabel('Efficiency')
        ax1.set_xlabel('P_{T} [GeV]')
        ax1.legend()

        #eff vs rate deep
        deep_rate = []
        error_deep_rate = np.zeros( (2,len(deeptau_thrs)-1) )
        deep_eff = []
        error_deep_eff = np.zeros( (2,len(deeptau_thrs)-1) )
        for deep_thr_index in range(len(deeptau_thrs) - 1):
            print("deepTau_thr:",deeptau_thrs[deep_thr_index])
            rate_deep, err_low_deep, err_up_deep = GetRate(initialCounter_rate.GetEntries(),df_rate,deeptau_thrs[deep_thr_index],pt_thrs[thr_index])
            deep_rate.append(rate_deep)
            error_deep_rate[0,deep_thr_index]=err_low_deep
            error_deep_rate[1,deep_thr_index]=err_up_deep
            eff_deep, err_low_eff_deep, err_up_eff_deep = GetEfficiency_Simple(df_eff,deeptau_thrs[deep_thr_index],pt_thrs[thr_index])
            deep_eff.append(eff_deep)
            error_deep_eff[0,deep_thr_index]=err_low_eff_deep
            error_deep_eff[1,deep_thr_index]=err_up_eff_deep
        full_deep_rate[thr_index] = deep_rate
        full_deep_rate_err[thr_index] = error_deep_rate
        full_deep_eff[thr_index] = deep_eff
        full_deep_eff_err[thr_index] = error_deep_eff

        ax3.errorbar(full_deep_rate[thr_index], full_deep_eff[thr_index], yerr=full_deep_eff_err[thr_index], xerr=full_deep_rate_err[thr_index], label=str(pt_thrs[thr_index])+' GeV')
        ax3.set_ylabel('Efficiency')
        ax3.set_xlabel('Rate [Hz]')
        ax3.legend()

        eff_l, eff_err_low_l, eff_err_up_l, eff_m, eff_err_low_m, eff_err_up_m, eff_t, eff_err_low_t, eff_err_up_t=BaseEfficiency_Simple(df_eff,pt_thrs[thr_index])
        rate_l, rate_err_low_l, rate_err_up_l, rate_m, rate_err_low_m, rate_err_up_m, rate_t, rate_err_low_t, rate_err_up_t=BaseRate_complete(initialCounter_rate.GetEntries(),df_rate,pt_thrs[thr_index])
        efficiency_l.append(eff_l)
        efficiency_error_l[0,thr_index]=eff_err_low_l
        efficiency_error_l[1,thr_index]=eff_err_up_l
        efficiency_m.append(eff_m)
        efficiency_error_m[0,thr_index]=eff_err_low_m
        efficiency_error_m[1,thr_index]=eff_err_up_m
        efficiency_t.append(eff_t)
        efficiency_error_t[0,thr_index]=eff_err_low_t
        efficiency_error_t[1,thr_index]=eff_err_up_t

        rate_total_l.append(rate_l)
        rate_error_l[0,thr_index]=rate_err_low_l
        rate_error_l[1,thr_index]=rate_err_up_l
        rate_total_m.append(rate_m)
        rate_error_m[0,thr_index]=rate_err_low_m
        rate_error_m[1,thr_index]=rate_err_up_m
        rate_total_t.append(rate_t)
        rate_error_t[0,thr_index]=rate_err_low_t
        rate_error_t[1,thr_index]=rate_err_up_t

        ax4.errorbar(rate_total_l[thr_index],efficiency_l[thr_index],yerr=efficiency_error_l[:,thr_index],xerr=rate_error_l[:,thr_index], label=str(pt_thrs[thr_index])+' GeV')
        ax4.set_ylabel('Efficiency')
        ax4.set_xlabel('Rate [Hz]')
        ax4.legend()
        ax5.errorbar(rate_total_m[thr_index],efficiency_m[thr_index],yerr=efficiency_error_m[:,thr_index],xerr=rate_error_m[:,thr_index], label=str(pt_thrs[thr_index])+' GeV')
        ax5.set_ylabel('Efficiency')
        ax5.set_xlabel('Rate [Hz]')
        ax5.legend()
        ax6.errorbar(rate_total_t[thr_index],efficiency_t[thr_index],yerr=efficiency_error_t[:,thr_index],xerr=rate_error_t[:,thr_index], label=str(pt_thrs[thr_index])+' GeV')
        ax6.set_ylabel('Efficiency')
        ax6.set_xlabel('Rate [Hz]')
        ax6.legend()

    ax2.errorbar((pt_bins[1:] + pt_bins[:-1]) / 2,efficiency_base_l,yerr=error_efficiency_l,  label='Loose cut based') #non disegna i punti per ogni pt
    ax2.errorbar((pt_bins[1:] + pt_bins[:-1]) / 2,efficiency_base_m,yerr=error_efficiency_m,  label='Medium cut based')
    ax2.errorbar((pt_bins[1:] + pt_bins[:-1]) / 2,efficiency_base_t,yerr=error_efficiency_t,  label='Tight cut based')
    ax2.set_ylabel('Efficiency')
    ax2.set_xlabel('P_{T} [GeV]')
    ax2.legend()

    fig1.savefig("fig1.pdf")
    fig2.savefig("fig2.pdf")
    fig3.savefig("fig3.pdf")
    fig4.savefig("fig4.pdf")
    fig5.savefig("fig5.pdf")
    fig6.savefig("fig6.pdf")


    # print("initial_rate vector: ",initial_rate)
    # print("max_rate vector: ",max_rate)
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
