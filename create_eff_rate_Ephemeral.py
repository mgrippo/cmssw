#!/usr/bin/env python
"""Inspect ROOT files."""
from __future__ import print_function

import logging as log

import ROOT
from ROOT import TCanvas, TColor, TGaxis, TH1F, TPad, TH2F
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize
from scipy import interpolate
from statsmodels.stats.proportion import proportion_confint
ROOT.gInterpreter.Declare('#include "PyInterface.h"')

def GetRate(n_initial, df_zb, deeptau_thr, pt_thr):
    n_events = df_zb.Count()
    df_zb = df_zb.Define('ntaus','getNtaus(deepTau_VSjet,tau_pt,{},{})'.format(deeptau_thr,pt_thr))
    df_zb = df_zb.Filter('ntaus >= 2')#to bechanged to 2!!!
    n_events_passed = df_zb.Count()
    #print("nevents: ",n_events.GetValue())
    #print("n_events_passed: ",n_events_passed.GetValue())
    rate = (float(n_events_passed.GetValue())/float(n_initial))*73455.3448 #forL1
    #print("rate: %2f Hz"%(rate))
    ci = proportion_confint(count=n_events_passed.GetValue(), nobs=n_initial, alpha=0.32, method='beta')
    err_low = (rate - ci[0]*73455.3448)
    err_up = (ci[1]*73455.3448 - rate)
    return rate, err_low, err_up

def GetEfficiency_Simple(n_initial,df_vbf, deeptau_thr, pt_thr):
    # df_vbf = df_vbf.Define('ntaus_den','getNtaus(deepTau_VSjet,tau_pt,{},{})'.format(0,0))
    # df_vbf_den = df_vbf.Filter('ntaus_den >= 2')#to bechanged to 2!!!
    # n_events = df_vbf_den.Count()
    df_vbf = df_vbf.Define('ntaus','getNtaus(deepTau_VSjet,tau_pt,{},{})'.format(deeptau_thr,pt_thr))
    df_vbf_num = df_vbf.Filter('ntaus >= 2')#to bechanged to 2!!!
    n_events_passed = df_vbf_num.Count()
    eff = (float(n_events_passed.GetValue())/float(n_initial))
    ci = proportion_confint(count=n_events_passed.GetValue(), nobs=n_initial, alpha=0.32, method='beta')
    err_low = (eff - ci[0])
    err_up = (ci[1] - eff)
    return eff, err_low, err_up

def BaseRate(n_initial, df_zb, pt_thr):
    n_events = df_zb.Count()
    #medium
    df_zb_m = df_zb.Define('ntaus','getNtaus_base(tau_mediumIsoAbs,tau_mediumIsoRel,tau_pt,{})'.format(pt_thr))
    df_zb_m = df_zb_m.Filter('ntaus >= 2')#to bechanged to 2!!!
    n_events_passed_m = df_zb_m.Count()
    rate_m = (float(n_events_passed_m.GetValue())/float(n_initial))*73455.3448 #L1 rate for my LS
    #rate_m = (float(n_events_passed_m.GetValue())/float(23.31)) #forL1
    ci_m = proportion_confint(count=n_events_passed_m.GetValue(), nobs=n_initial, alpha=0.32, method='beta')
    err_low_m = (rate_m - ci_m[0]*73455.3448)
    err_up_m = (ci_m[1]*73455.3448 - rate_m)
    return rate_m, err_low_m, err_up_m

def BaseRate_complete(n_initial, df_zb, pt_thr):
    n_events = df_zb.Count()
    #medium
    df_zb_m = df_zb.Define('ntaus','getNtaus_base(tau_mediumIsoAbs,tau_mediumIsoRel,tau_pt,{})'.format(pt_thr))
    df_zb_m = df_zb_m.Filter('ntaus >= 2')#to bechanged to 2!!!
    n_events_passed_m = df_zb_m.Count()
    rate_m = (float(n_events_passed_m.GetValue())/float(n_initial))*73455.3448 #forL1
    ci_m = proportion_confint(count=n_events_passed_m.GetValue(), nobs=n_initial, alpha=0.32, method='beta')
    err_low_m = (rate_m - ci_m[0]*73455.3448)
    err_up_m = (ci_m[1]*73455.3448 - rate_m)
    #loose
    df_zb_l = df_zb.Define('ntaus_l','getNtaus_base_loose(tau_looseIsoAbs,tau_looseIsoRel,tau_pt,{})'.format(pt_thr))
    df_zb_l = df_zb_l.Filter('ntaus_l >= 2')#to bechanged to 2!!!
    n_events_passed_l = df_zb_l.Count()
    rate_l = (float(n_events_passed_l.GetValue())/float(n_initial))*73455.3448 #forL1
    ci_l = proportion_confint(count=n_events_passed_l.GetValue(), nobs=n_initial, alpha=0.32, method='beta')
    err_low_l = (rate_l - ci_l[0]*73455.3448)
    err_up_l = (ci_l[1]*73455.3448 - rate_l)
    # #tight
    df_zb_t = df_zb.Define('ntaus_t','getNtaus_base_tight(tau_tightIsoAbs,tau_tightIsoRel,tau_pt,{})'.format(pt_thr))
    df_zb_t = df_zb_t.Filter('ntaus_t >= 2')#to bechanged to 2!!!
    n_events_passed_t = df_zb_t.Count()
    rate_t = (float(n_events_passed_t.GetValue())/float(n_initial))*73455.3448 #forL1
    ci_t = proportion_confint(count=n_events_passed_t.GetValue(), nobs=n_initial, alpha=0.32, method='beta')
    err_low_t = (rate_t - ci_t[0]*73455.3448)
    err_up_t = (ci_t[1]*73455.3448 - rate_t)
    return rate_l, err_low_l, err_up_l, rate_m, err_low_m, err_up_m, rate_t, err_low_t, err_up_t

def BaseEfficiency_Simple(n_initial,df_vbf,pt_thr):
    # df_vbf = df_vbf.Define('ntaus_den','getNtaus(deepTau_VSjet,tau_pt,{},{})'.format(0,0))
    # df_vbf_den = df_vbf.Filter('ntaus_den >= 2')#to bechanged to 2!!!
    # n_events = df_vbf_den.Count()
    #medium
    df_vbf_m = df_vbf.Define('ntaus_m','getNtaus_base(tau_mediumIsoAbs,tau_mediumIsoRel,tau_pt,{})'.format(pt_thr))
    df_vbf_m = df_vbf_m.Filter('ntaus_m >= 2')#to bechanged to 2!!!
    n_events_passed_m = df_vbf_m.Count()
    eff_m = (float(n_events_passed_m.GetValue())/float(n_initial))
    ci_m = proportion_confint(count=n_events_passed_m.GetValue(), nobs=n_initial, alpha=0.32, method='beta')
    err_low_m = (eff_m - ci_m[0])
    err_up_m = (ci_m[1] - eff_m)
    #loose
    df_vbf_l = df_vbf.Define('ntaus_l','getNtaus_base_loose(tau_looseIsoAbs,tau_looseIsoRel,tau_pt,{})'.format(pt_thr))
    df_vbf_l = df_vbf_l.Filter('ntaus_l >= 2')#to bechanged to 2!!!
    n_events_passed_l = df_vbf_l.Count()
    eff_l = (float(n_events_passed_l.GetValue())/float(n_initial))
    ci_l = proportion_confint(count=n_events_passed_l.GetValue(), nobs=n_initial, alpha=0.32, method='beta')
    err_low_l = (eff_l - ci_l[0])
    err_up_l = (ci_l[1] - eff_l)
    #tight
    df_vbf_t = df_vbf.Define('ntaus_t','getNtaus_base_tight(tau_tightIsoAbs,tau_tightIsoRel,tau_pt,{})'.format(pt_thr))
    df_vbf_t = df_vbf_t.Filter('ntaus_t >= 2')#to bechanged to 2!!!
    n_events_passed_t = df_vbf_t.Count()
    eff_t = (float(n_events_passed_t.GetValue())/float(n_initial))
    ci_t = proportion_confint(count=n_events_passed_t.GetValue(), nobs=n_initial, alpha=0.32, method='beta')
    err_low_t = (eff_t - ci_t[0])
    err_up_t = (ci_t[1] - eff_t)
    return eff_l, err_low_l, err_up_l, eff_m, err_low_m, err_up_m, eff_t, err_low_t, err_up_t

def CalculateErrorEff(n_passed,n_initial,eff):
    ci = proportion_confint(count=n_passed, nobs=n_initial, alpha=0.32, method='beta')
    err_low = (eff - ci[0])
    err_up = (ci[1] - eff)
    return err_low, err_up

pt_bins = np.array([20,25,30,35,40,45,50,60,70,100,150,200, 300, 400, 500])
pt_thrs = [20,25,30,35,40,45]
pt_thrs_new = [20,25,30,35,40]

deeptau_thrs = np.linspace(0.0, 1.0, num=100)
eff_name="full_VBF/vbf_full.root"
rate_name="full_Ephemeral/ephemeral_full.root"

RDF = ROOT.ROOT.RDataFrame
df_eff = RDF("final_counter", eff_name)
df_rate = RDF("final_counter", rate_name)

tfile = ROOT.TFile(eff_name)
tfile_rate = ROOT.TFile(rate_name)

initial_rate = []
max_rate = []
efficiency_total = {}
error_efficiency_total = {}
error_pt_total = {}
full_deep_rate = {}
full_deep_rate_err = {}
full_deep_eff = {}
full_deep_eff_err = {}
full_f_xy = {}
full_f_yx = {}
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
# fig1 = plt.figure()
# ax1 = fig1.add_subplot(111)
# fig2 = plt.figure()
# ax2 = fig2.add_subplot(111)
fig = {}
ax = {}
for thr_index in range(len(pt_thrs)):
    fig[thr_index] = plt.figure()
    ax[thr_index] = fig[thr_index].add_subplot(111)

fig_eff = plt.figure()
ax_eff = fig_eff.add_subplot(111)

fig_rate = plt.figure()
ax_rate = fig_rate.add_subplot(111)


if not tfile.IsZombie() and not tfile_rate.IsZombie():
    f_eff = ROOT.TFile.Open(eff_name)
    f_rate = ROOT.TFile.Open(rate_name)
    initialCounter_eff = f_eff.Get("initial_counter_hist")
    afterL1Counter_eff = f_eff.Get("afterL1Filter_counter_hist")
    intermidiateCounter_eff = f_eff.Get("intermidiate_counter_hist")

    df_eff = df_eff.Define('ntaus_den','getNtaus(deepTau_VSjet,tau_pt,{},{})'.format(0,0))
    df_eff_den = df_eff.Filter('ntaus_den >= 2')#to bechanged to 2!!!
    n_events_in_df = df_eff_den.Count()

    print("Efficiency steps in VBF")
    eff_1 = float(afterL1Counter_eff.GetEntries())/float(initialCounter_eff.GetEntries())
    err_low_1, err_up_1 = CalculateErrorEff(float(afterL1Counter_eff.GetEntries()),float(initialCounter_eff.GetEntries()),eff_1)
    print("After L1: ",eff_1," - err low: ", err_low_1, " - err up: ", err_up_1)
    eff_2 = float(intermidiateCounter_eff.GetEntries())/float(initialCounter_eff.GetEntries())
    err_low_2, err_up_2 = CalculateErrorEff(float(intermidiateCounter_eff.GetEntries()),float(initialCounter_eff.GetEntries()),eff_2)
    print("After HLT tau reco before Iso: ",eff_2," - err low: ", err_low_2, " - err up: ", err_up_2)
    eff_3 = float(n_events_in_df.GetValue())/float(initialCounter_eff.GetEntries())
    err_low_3, err_up_3 = CalculateErrorEff(float(n_events_in_df.GetValue()),float(initialCounter_eff.GetEntries()),eff_3)
    print("After HLT tau reco after Iso: ",eff_3," - err low: ", err_low_3, " - err up: ", err_up_3)

    initialCounter_rate = f_rate.Get("initial_counter_hist")

    fix_eff = []
    fix_rate = []
    base_rate, base_err_low, base_err_up = BaseRate(initialCounter_rate.GetEntries(),df_rate,35)
    print("Base Rate: ", base_rate)
    print("Base Rate error low: ", base_err_low)
    print("Base Rate error up: ", base_err_up)
    base_eff_l, base_eff_err_low_l, base_eff_err_up_l, base_eff_m, base_eff_err_low_m, base_eff_err_up_m, base_eff_t, base_eff_err_low_t, base_eff_err_up_t=BaseEfficiency_Simple(initialCounter_eff.GetEntries(),df_eff,35)
    print("Eff base: ", base_eff_m)
    print("Base Eff error low: ", base_eff_err_low_m)
    print("Base Eff error up: ", base_eff_err_up_m)
    for thr_index in range(len(pt_thrs)):
        print("pt_thr: ",pt_thrs[thr_index])
        efficiency = []
        pt_error = np.zeros( (2,len(pt_bins) - 1) )
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

        print("deepTau thr at the fixed rate for 35 GeV for cut based Medium: ", deep_thr)
        fixed_eff_value, fixed_err_low_eff, fixed_err_up_eff = GetEfficiency_Simple(initialCounter_eff.GetEntries(),df_eff,deep_thr,pt_thrs[thr_index])
        #dummy_eff_value, dummy_err_low_eff, dummy_err_up_eff = GetEfficiency_Simple(initialCounter_eff.GetEntries(),df_eff,1,pt_thrs[thr_index])
        fix_eff.append(fixed_eff_value)
        #print("dummy eff: ",dummy_eff_value)

        if(pt_thrs[thr_index] < 45):
            def f_2(deeptau_thr_2):
                eff_value, err_low_eff, err_up_eff = GetEfficiency_Simple(initialCounter_eff.GetEntries(),df_eff,deeptau_thr_2,pt_thrs[thr_index])
                base_eff_l_2, base_eff_err_low_l_2, base_eff_err_up_l_2, base_eff_m_2, base_eff_err_low_m_2, base_eff_err_up_m_2, base_eff_t_2, base_eff_err_low_t_2, base_eff_err_up_t_2=BaseEfficiency_Simple(initialCounter_eff.GetEntries(),df_eff,35)
                #print('debug:',eff_value,"-",base_eff_m_2,"-",deeptau_thr_2,"-",pt_thrs[thr_index])
                return eff_value-base_eff_m_2

            solution_2 = optimize.root_scalar(f_2,bracket=[0,1],method='bisect')
            deep_thr_2 = solution_2.root

            print("deepTau thr at the fixed eff for 35 GeV for cut based Medium: ", deep_thr_2)
            fixed_rate_value, fixed_err_low_rate, fixed_err_up_rate = GetRate(initialCounter_rate.GetEntries(),df_rate,deep_thr_2,pt_thrs[thr_index])
            fix_rate.append(fixed_rate_value)
        #deep_thr = 0 #to check eff is equal to 100%

        ###################### from here
        #eff vs rate deep
        deep_rate = []
        error_deep_rate = np.zeros( (2,len(deeptau_thrs)- 1) )
        deep_eff = []
        error_deep_eff = np.zeros( (2,len(deeptau_thrs)- 1) )
        for deep_thr_index in range(len(deeptau_thrs) - 1): #right order
        #for deep_thr_index in range( len(deeptau_thrs) - 1, -1, -1) : #reversed order
            #print("deepTau_thr:",deeptau_thrs[deep_thr_index])
            rate_deep, err_low_deep, err_up_deep = GetRate(initialCounter_rate.GetEntries(),df_rate,deeptau_thrs[deep_thr_index],pt_thrs[thr_index])
            deep_rate.append(rate_deep)
            error_deep_rate[0,deep_thr_index]=err_low_deep
            error_deep_rate[1,deep_thr_index]=err_up_deep
            eff_deep, err_low_eff_deep, err_up_eff_deep = GetEfficiency_Simple(initialCounter_eff.GetEntries(),df_eff,deeptau_thrs[deep_thr_index],pt_thrs[thr_index])
            deep_eff.append(eff_deep)
            error_deep_eff[0,deep_thr_index]=err_low_eff_deep
            error_deep_eff[1,deep_thr_index]=err_up_eff_deep

        print("Ended deepthrs loop")
        full_deep_rate[thr_index] = deep_rate
        full_deep_rate_err[thr_index] = error_deep_rate
        full_deep_eff[thr_index] = deep_eff
        full_deep_eff_err[thr_index] = error_deep_eff
        #################


        ############## from here
        eff_l, eff_err_low_l, eff_err_up_l, eff_m, eff_err_low_m, eff_err_up_m, eff_t, eff_err_low_t, eff_err_up_t=BaseEfficiency_Simple(initialCounter_eff.GetEntries(),df_eff,pt_thrs[thr_index])
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
        ###########

        ###### from here
        full_f_xy[thr_index] = interpolate.interp1d(full_deep_eff[thr_index], full_deep_rate[thr_index])
        full_f_yx[thr_index] = interpolate.interp1d(full_deep_rate[thr_index], full_deep_eff[thr_index])



        print('deep values at '+str(pt_thrs[thr_index])+' GeV - eff cut based :',efficiency_m[thr_index],'-> diff rate: ',rate_total_m[thr_index] - full_f_xy[thr_index](efficiency_m[thr_index]),'improv: ',(rate_total_m[thr_index] - full_f_xy[thr_index](efficiency_m[thr_index]))/rate_total_m[thr_index])
        print('deep values error low eff cut based:',efficiency_error_m[0,thr_index])
        print('deep values error up eff cut based:',efficiency_error_m[1,thr_index])
        print('deep values at '+str(pt_thrs[thr_index])+' GeV - rate cut based :',rate_total_m[thr_index],'-> diff eff: ',efficiency_m[thr_index] - full_f_yx[thr_index](rate_total_m[thr_index]),'improv: ',(efficiency_m[thr_index] - full_f_yx[thr_index](rate_total_m[thr_index]))/efficiency_m[thr_index])
        print('deep values error low rate cut based:',rate_error_m[0,thr_index])
        print('deep values error up rate cut based:',rate_error_m[1,thr_index])
        ax[thr_index].errorbar(full_deep_eff[thr_index],full_deep_rate[thr_index],  xerr=full_deep_eff_err[thr_index], yerr=full_deep_rate_err[thr_index], marker='o', linestyle='--', label='DeepTau discriminator')
        ax[thr_index].errorbar(efficiency_l[thr_index], rate_total_l[thr_index],  xerr=efficiency_error_l[:,thr_index].reshape((2, 1)), yerr=rate_error_l[:,thr_index].reshape((2, 1)), marker='o', linestyle='--', label='Loose cut based')
        ax[thr_index].errorbar(efficiency_m[thr_index], rate_total_m[thr_index],  xerr=efficiency_error_m[:,thr_index].reshape((2, 1)), yerr=rate_error_m[:,thr_index].reshape((2, 1)), marker='o', linestyle='--', label='Medium cut based')
        ax[thr_index].errorbar(efficiency_t[thr_index], rate_total_t[thr_index],  xerr=efficiency_error_t[:,thr_index].reshape((2, 1)), yerr=rate_error_t[:,thr_index].reshape((2, 1)), marker='o', linestyle='--', label='Tight cut based')
        ax[thr_index].set_xlim([0, 0.06])
        if(pt_thrs[thr_index] < 35):
            ax[thr_index].set_ylim([0, 200])
        else:
            ax[thr_index].set_ylim([0, 80])
        ax[thr_index].set_title('Rate vs efficiency for Pt > '+str(pt_thrs[thr_index])+' GeV')
        ax[thr_index].set_ylabel('Rate [Hz]')
        ax[thr_index].set_xlabel('Efficiency')
        ax[thr_index].grid(True)
        ax[thr_index].legend(loc='upper left')
        ######

        fig[thr_index].savefig('eff_vs_rate_thr_'+str(pt_thrs[thr_index])+'.pdf')

    print("pt thrs:",pt_thrs)
    print("eff deeptau:",fix_eff)
    ax_eff.errorbar(pt_thrs,fix_eff, marker='o', ls='none', label='DeepTau discriminator')
    ax_eff.errorbar(35,base_eff_m, marker='o', ls='none', label='Medium cut based')
    ax_eff.set_title('Efficiency vs pt threshold')
    ax_eff.set_ylabel('Efficiency')
    ax_eff.set_xlabel('Pt [GeV]')
    ax_eff.grid(True)
    ax_eff.legend()

    fig_eff.savefig('eff_vs_pt_thr.pdf')

    print("pt thrs:",pt_thrs_new)
    print("eff deeptau:",fix_rate)
    ax_rate.errorbar(pt_thrs_new,fix_rate, marker='o', ls='none', label='DeepTau discriminator')
    ax_rate.errorbar(35,base_rate, marker='o', ls='none', label='Medium cut based')
    ax_rate.set_title('Rate vs pt threshold')
    ax_rate.set_ylabel('Rate [Hz]')
    ax_rate.set_xlabel('Pt [GeV]')
    ax_rate.grid(True)
    ax_rate.legend()

    fig_rate.savefig('rate_vs_pt_thr.pdf')

else:
    print('Could not load file {0!r}'.format(fname))
