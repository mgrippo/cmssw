#!/usr/bin/env python
"""Inspect ROOT files."""
from __future__ import print_function

import logging as log

import ROOT
import math
from ROOT import TCanvas, TColor, TGaxis, TH1F, TPad, TH2F, TChain, TSelector, TTree, TEfficiency, TVector2

chain = TChain("taus")

filepath = ''
f = open("training_VBF/input.txt", "r")
for line in f:
  print(line)
  chain.AddFile(line[:-1])

print(chain.GetEntries())

pt = ROOT.TH1D("data","p_{T}, data" ,100,0,200)
gen_pt = ROOT.TH1D("gen_pt","gen p_{T}, data" ,100,0,200)
gen_pt_l1_match = ROOT.TH1D("gen_pt_l1_match","gen p_{T} L1 match" ,100,0,200)
gen_pt_calo_match = ROOT.TH1D("gen_pt_calo_match","gen p_{T} Calo match" ,100,0,200)
gen_pt_and_match = ROOT.TH1D("gen_pt_and_match","gen p_{T} L1 and Calo match" ,100,0,200)
gen_pt_or_match = ROOT.TH1D("gen_pt_or_match","gen p_{T} L1 or Calo match" ,100,0,200)
canvas = ROOT.TCanvas("canvas")
canvas.cd()

for i_event in range(0,chain.GetEntries()):
    chain.GetEntry(i_event)
    lepton_gen_match_value = getattr(chain ,"lepton_gen_match")
    lepton_gen_visible_p4_pt_value = getattr(chain ,"lepton_gen_visible_p4_pt")
    lepton_gen_visible_p4_eta_value = getattr(chain ,"lepton_gen_visible_p4_eta")
    lepton_gen_visible_p4_phi_value = getattr(chain ,"lepton_gen_visible_p4_phi")
    l1Tau_pt_value = getattr(chain ,"l1Tau_pt")
    l1Tau_eta_value = getattr(chain ,"l1Tau_eta")
    l1Tau_phi_value = getattr(chain ,"l1Tau_phi")
    l1Tau_hwIso_value = getattr(chain ,"l1Tau_hwIso")
    caloTau_pt_value = getattr(chain ,"caloTau_pt")
    caloTau_eta_value = getattr(chain ,"caloTau_eta")
    caloTau_phi_value = getattr(chain ,"caloTau_phi")
    for i_gen in range(len(lepton_gen_match_value)):
        if lepton_gen_match_value[i_gen] != 5:
            continue
        if abs(lepton_gen_visible_p4_eta_value[i_gen]) >= 2.1:
            continue
        gen_pt.Fill(lepton_gen_visible_p4_pt_value[i_gen])
        l1_match = False
        for i_l1 in range(len(l1Tau_pt_value)):
            if abs(l1Tau_eta_value[i_l1]) >= 2.1:
                continue
            if l1Tau_hwIso_value[i_l1] <= 0:
                continue
            delta_eta = l1Tau_eta_value[i_l1] - lepton_gen_visible_p4_eta_value[i_gen]
            delta_phi = ROOT.TVector2.Phi_mpi_pi(l1Tau_phi_value[i_l1] - lepton_gen_visible_p4_phi_value[i_gen])
            deltaR = math.sqrt(delta_eta*delta_eta + delta_phi*delta_phi)
            if deltaR < 0.5:
                l1_match = True
        calo_match = False
        for i_calo in range(len(caloTau_pt_value)):
            if abs(caloTau_eta_value[i_calo]) >= 2.1:
                continue
            delta_eta = caloTau_eta_value[i_calo] - lepton_gen_visible_p4_eta_value[i_gen]
            delta_phi = ROOT.TVector2.Phi_mpi_pi(caloTau_phi_value[i_calo] - lepton_gen_visible_p4_phi_value[i_gen])
            deltaR = math.sqrt(delta_eta*delta_eta + delta_phi*delta_phi)
            if deltaR < 0.5:
                calo_match = True
        if(l1_match):
            gen_pt_l1_match.Fill(lepton_gen_visible_p4_pt_value[i_gen])
        if(calo_match):
            gen_pt_calo_match.Fill(lepton_gen_visible_p4_pt_value[i_gen])
        if(l1_match and calo_match):
            gen_pt_and_match.Fill(lepton_gen_visible_p4_pt_value[i_gen])
        if(l1_match or calo_match):
            gen_pt_or_match.Fill(lepton_gen_visible_p4_pt_value[i_gen])


l1_efficiency = ROOT.TEfficiency(gen_pt_l1_match,gen_pt)
l1_efficiency.Draw()
l1_efficiency.SetTitle("Efficiency; p_{T} [GeV]; efficiency")

calo_efficiency = ROOT.TEfficiency(gen_pt_calo_match,gen_pt)
calo_efficiency.SetLineColor(2)
calo_efficiency.Draw("same")

and_efficiency = ROOT.TEfficiency(gen_pt_and_match,gen_pt)
and_efficiency.SetLineColor(3)
and_efficiency.Draw("same")

or_efficiency = ROOT.TEfficiency(gen_pt_or_match,gen_pt)
or_efficiency.SetLineColor(4)
or_efficiency.Draw("same")

leg = ROOT.TLegend(0.25, 0.5, 0.6, 0.7)
leg.AddEntry(l1_efficiency, "L1 Efficiency")
leg.AddEntry(calo_efficiency, "Calo Efficiency")
leg.AddEntry(and_efficiency, "L1 and Calo Efficiency")
leg.AddEntry(or_efficiency, "L1 or Calo Efficiency")
leg.Draw()
#canvas.BuildLegend()
canvas.Print("Efficiency.pdf")
