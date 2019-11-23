/*! Definition of functions for calulating most used quantities */
#pragma once

int getNtaus(const ROOT::VecOps::RVec<float>& deepTau_VSjet, const ROOT::VecOps::RVec<float>& tau_pt, float deeptau_thr, float pt_thr)
{
    int ntaus = 0;
    for(size_t n = 0; n < tau_pt.size(); ++n){
        if(deepTau_VSjet.at(n) > deeptau_thr && tau_pt.at(n) > pt_thr){
            ++ntaus;
        }
    }
    return ntaus;
}

int getNtaus_base(const ROOT::VecOps::RVec<float>& tau_mediumIsoAbs, const ROOT::VecOps::RVec<float>& tau_mediumIsoRel, const ROOT::VecOps::RVec<float>& tau_pt, float pt_thr)
{
    int ntaus = 0;
    for(size_t n = 0; n < tau_pt.size(); ++n){
        if((tau_mediumIsoAbs.at(n) > 0.5 || tau_mediumIsoRel.at(n) > 0.5) && tau_pt.at(n) > pt_thr){
            ++ntaus;
        }
    }
    return ntaus;
}
