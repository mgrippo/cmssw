/*! Definition of a tuple with variables used as inputs to deepTau ID.
This file is part of https://github.com/cms-tau-pog/TauTriggerTools. */

#pragma once

#include "TauTriggerTools/Common/interface/SmartTree.h"

#define VAR2(type, name1, name2) VAR(type, name1) VAR(type, name2)
#define VAR3(type, name1, name2, name3) VAR2(type, name1, name2) VAR(type, name3)
#define VAR4(type, name1, name2, name3, name4) VAR3(type, name1, name2, name3) VAR(type, name4)

#define DEEPTAU_TUPLE_DATA() \
    /* Event Variables */ \
    VAR(UInt_t, run) /* run number */ \
    VAR(UInt_t, lumi) /* lumi section */ \
    VAR(ULong64_t, evt) /* event number */ \
    VAR4(Float_t, tau_pt, tau_eta, tau_phi, tau_mass) /* 4-momentum of the tau */ \
    VAR(Int_t, lepton_gen_match) /* matching with leptons on the generator level (see Htautau Twiki for details):
                                    Electron = 1, Muon = 2, TauElectron = 3, TauMuon = 4, Tau = 5, NoMatch = 6 */ \
    VAR(Int_t, tau_decayMode) /* tau decay mode */ \
    VAR(Float_t, tau_looseIsoAbs) /* loose PF iso abs for hadronic Tau */ \
    VAR(Float_t, tau_looseIsoRel) /* loose PF iso rel for hadronic Tau */ \
    VAR(Float_t, tau_mediumIsoAbs) /* medium PF iso abs for hadronic Tau */ \
    VAR(Float_t, tau_mediumIsoRel) /* medium PF iso rel for hadronic Tau */ \
    VAR(Float_t, tau_tightIsoAbs) /* tight PF iso abs for hadronic Tau */ \
    VAR(Float_t, tau_tightIsoRel) /* tight PF iso rel for hadronic Tau */ \
    VAR(Float_t, deepTau_VSe) /* deepTau_VSe raw discriminator */ \
    VAR(Float_t, deepTau_VSmu) /* deepTau_VSmu raw discriminator */ \
    VAR(Float_t, deepTau_VSjet) /* deepTau_VSjet raw discriminator */ \
    /**/

#define VAR(type, name) DECLARE_BRANCH_VARIABLE(type, name)
DECLARE_TREE(deep_tau, TauIdVars, DeepTauTuple, DEEPTAU_TUPLE_DATA, "deep_taus")
#undef VAR

#define VAR(type, name) ADD_DATA_TREE_BRANCH(name)
INITIALIZE_TREE(deep_tau, DeepTauTuple, DEEPTAU_TUPLE_DATA)
#undef VAR
#undef VAR2
#undef VAR3
#undef VAR4
#undef DEEPTAU_TUPLE_DATA

namespace deep_tau {

template<typename T>
constexpr T DefaultFillValue() { return std::numeric_limits<T>::lowest(); }
template<>
constexpr float DefaultFillValue<float>() { return -999.; }
template<>
constexpr int DefaultFillValue<int>() { return -999; }

} // namespace deep_tau
