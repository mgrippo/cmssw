/*! Definition of functions for calulating most used quantities */
#pragma once

int getNtaus_original(const ROOT::VecOps::RVec<float>& tau_pt)
{
    int ntaus = 0;
    for(size_t n = 0; n < tau_pt.size(); ++n){
        ++ntaus;
    }
    return ntaus;
}

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

int getNtaus_inPtBin(const ROOT::VecOps::RVec<float>& deepTau_VSjet, const ROOT::VecOps::RVec<float>& tau_pt, float deeptau_thr, float pt_thr, float pt_bin_1, float pt_bin_2)
{
    int ntaus = 0;
    for(size_t n = 0; n < tau_pt.size(); ++n){
        if(deepTau_VSjet.at(n) > deeptau_thr && tau_pt.at(n) > pt_thr && tau_pt.at(n) > pt_bin_1 && tau_pt.at(n) < pt_bin_2){
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

int getNtaus_base_loose(const ROOT::VecOps::RVec<float>& tau_looseIsoAbs, const ROOT::VecOps::RVec<float>& tau_looseIsoRel, const ROOT::VecOps::RVec<float>& tau_pt, float pt_thr)
{
    int ntaus = 0;
    for(size_t n = 0; n < tau_pt.size(); ++n){
        if((tau_looseIsoAbs.at(n) > 0.5 || tau_looseIsoRel.at(n) > 0.5) && tau_pt.at(n) > pt_thr){
            ++ntaus;
        }
    }
    return ntaus;
}

int getNtaus_base_tight(const ROOT::VecOps::RVec<float>& tau_tightIsoAbs, const ROOT::VecOps::RVec<float>& tau_tightIsoRel, const ROOT::VecOps::RVec<float>& tau_pt, float pt_thr)
{
    int ntaus = 0;
    for(size_t n = 0; n < tau_pt.size(); ++n){
        if((tau_tightIsoAbs.at(n) > 0.5 || tau_tightIsoRel.at(n) > 0.5) && tau_pt.at(n) > pt_thr){
            ++ntaus;
        }
    }
    return ntaus;
}

int getNtaus_base_inPtBin_Medium(const ROOT::VecOps::RVec<float>& tau_mediumIsoAbs, const ROOT::VecOps::RVec<float>& tau_mediumIsoRel, const ROOT::VecOps::RVec<float>& tau_pt, float pt_thr, float pt_bin_1, float pt_bin_2)
{
    int ntaus = 0;
    for(size_t n = 0; n < tau_pt.size(); ++n){
        if((tau_mediumIsoAbs.at(n) > 0.5 || tau_mediumIsoRel.at(n) > 0.5) && tau_pt.at(n) > pt_thr && tau_pt.at(n) > pt_bin_1 && tau_pt.at(n) < pt_bin_2){
            ++ntaus;
        }
    }
    return ntaus;
}

int getNtaus_base_inPtBin_Loose(const ROOT::VecOps::RVec<float>& tau_looseIsoAbs, const ROOT::VecOps::RVec<float>& tau_looseIsoRel, const ROOT::VecOps::RVec<float>& tau_pt, float pt_thr, float pt_bin_1, float pt_bin_2)
{
    int ntaus = 0;
    for(size_t n = 0; n < tau_pt.size(); ++n){
        if((tau_looseIsoAbs.at(n) > 0.5 || tau_looseIsoRel.at(n) > 0.5) && tau_pt.at(n) > pt_thr && tau_pt.at(n) > pt_bin_1 && tau_pt.at(n) < pt_bin_2){
            ++ntaus;
        }
    }
    return ntaus;
}

int getNtaus_base_inPtBin_Tight(const ROOT::VecOps::RVec<float>& tau_tightIsoAbs, const ROOT::VecOps::RVec<float>& tau_tightIsoRel, const ROOT::VecOps::RVec<float>& tau_pt, float pt_thr, float pt_bin_1, float pt_bin_2)
{
    int ntaus = 0;
    for(size_t n = 0; n < tau_pt.size(); ++n){
        if((tau_tightIsoAbs.at(n) > 0.5 || tau_tightIsoRel.at(n) > 0.5) && tau_pt.at(n) > pt_thr && tau_pt.at(n) > pt_bin_1 && tau_pt.at(n) < pt_bin_2){
            ++ntaus;
        }
    }
    return ntaus;
}
