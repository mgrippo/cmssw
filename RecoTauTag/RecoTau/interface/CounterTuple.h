/*! Definition of a tuple with variables used as inputs to deepTau ID.
This file is part of https://github.com/cms-tau-pog/TauTriggerTools. */

#pragma once

#include "TauTriggerTools/Common/interface/SmartTree.h"

#define VAR2(type, name1, name2) VAR(type, name1) VAR(type, name2)
#define VAR3(type, name1, name2, name3) VAR2(type, name1, name2) VAR(type, name3)
#define VAR4(type, name1, name2, name3, name4) VAR3(type, name1, name2, name3) VAR(type, name4)

#define COUNTER_TUPLE_DATA() \
    /* Event Variables */ \
    VAR(UInt_t, run) /* run number */ \
    VAR(UInt_t, lumi) /* lumi section */ \
    VAR(ULong64_t, evt) /* event number */ \
    VAR(std::vector<Float_t>, tau_pt) /* pt of the tau */ \
    VAR(std::vector<Float_t>, tau_mediumIsoAbs) /* medium PF iso abs for hadronic Tau */ \
    VAR(std::vector<Float_t>, tau_mediumIsoRel) /* medium PF iso rel for hadronic Tau */ \
    VAR(std::vector<Float_t>, deepTau_VSe) /* deepTau_VSe raw discriminator */ \
    VAR(std::vector<Float_t>, deepTau_VSmu) /* deepTau_VSmu raw discriminator */ \
    VAR(std::vector<Float_t>, deepTau_VSjet) /* deepTau_VSjet raw discriminator */ \
    /**/

#define VAR(type, name) DECLARE_BRANCH_VARIABLE(type, name)
DECLARE_TREE(counter_tau, TauIdVars, CounterTuple, COUNTER_TUPLE_DATA, "counter_taus")
#undef VAR

#define VAR(type, name) ADD_DATA_TREE_BRANCH(name)
INITIALIZE_TREE(counter_tau, CounterTuple, COUNTER_TUPLE_DATA)
#undef VAR
#undef VAR2
#undef VAR3
#undef VAR4
#undef COUNTER_TUPLE_DATA

namespace counter_tau {

template<typename T>
constexpr T DefaultFillValue() { return std::numeric_limits<T>::lowest(); }
template<>
constexpr float DefaultFillValue<float>() { return -999.; }
template<>
constexpr int DefaultFillValue<int>() { return -999; }

} // namespace counter_tau
