/*! Produce synchronization tree.
This file is part of https://github.com/hh-italian-group/h-tautau. */

#include "AnalysisTools/Run/include/program_main.h"
#include "AnalysisTools/Core/include/RootExt.h"
#include "AnalysisTools/Core/include/TextIO.h"
#include "AnalysisTools/Core/include/ProgressReporter.h"
#include "RecoTauTag/RecoTau/interface/CounterTuple.h"

struct Arguments {
    REQ_ARG(std::string, input_file);
    REQ_ARG(std::string, output_file);
};

class FlattenProducer {
public:
    using CounterTuple = counter_tau::CounterTuple;

    FlattenProducer(const Arguments& _args) : args(_args), outputFile(root_ext::CreateRootFile(args.output_file()))
    {

    }

    void Run()
    {
        std::cout << boost::format("Processing input file '%1%' into output file '%2%'.\n")
                   % args.input_file() % args.output_file();

        auto originalFile = root_ext::OpenRootFile(args.input_file());
        CounterTuple originalTuple("final_counter",originalFile.get(),true);
        CounterTuple flattenTuple("final_flatten_counter", outputFile.get(), false);
        const Long64_t n_entries = originalTuple.GetEntries();

        for(Long64_t current_entry = 0; current_entry < n_entries; ++current_entry) {
            originalTuple.GetEntry(current_entry);
            FillFlattenTuple(flattenTuple, originalTuple.data());
            flattenTuple.Fill();
        }

        flattenTuple.Write();

    }

private:

    void FillFlattenTuple(CounterTuple& flattenTuple, const counter_tau::TauIdVars& event)
    {
        for(unsigned n = 0; n < event.tau_pt.size(); ++n){
            flattenTuple().run  = event.run;
            flattenTuple().lumi = event.lumi;
            flattenTuple().evt  = event.evt;
            flattenTuple().npu = event.npu;

            flattenTuple().lepton_gen_match.push_back(event.lepton_gen_match.at(n));
            flattenTuple().gen_tau_pt.push_back(event.gen_tau_pt.at(n));
            flattenTuple().gen_tau_eta.push_back(event.gen_tau_eta.at(n));
            flattenTuple().gen_tau_phi.push_back(event.gen_tau_phi.at(n));
            flattenTuple().gen_tau_e.push_back(event.gen_tau_e.at(n));

            flattenTuple().tau_pt.push_back(event.tau_pt.at(n));
            flattenTuple().tau_eta.push_back(event.tau_eta.at(n));
            flattenTuple().tau_mediumIsoAbs.push_back(event.tau_mediumIsoAbs.at(n));
            flattenTuple().tau_mediumIsoRel.push_back(event.tau_mediumIsoRel.at(n));
            flattenTuple().tau_looseIsoAbs.push_back(event.tau_looseIsoAbs.at(n));
            flattenTuple().tau_looseIsoRel.push_back(event.tau_looseIsoRel.at(n));
            flattenTuple().tau_tightIsoAbs.push_back(event.tau_tightIsoAbs.at(n));
            flattenTuple().tau_tightIsoRel.push_back(event.tau_tightIsoRel.at(n));

            flattenTuple().deepTau_VSe.push_back(event.deepTau_VSe.at(n));
            flattenTuple().deepTau_VSmu.push_back(event.deepTau_VSmu.at(n));
            flattenTuple().deepTau_VSjet.push_back(event.deepTau_VSjet.at(n));
            flattenTuple().tau_decayModeFindingNewDMs.push_back(event.tau_decayModeFindingNewDMs.at(n));

            flattenTuple().tau_passedLastFilter.push_back(event.tau_passedLastFilter.at(n));
        }

    }

private:
    Arguments args;
    std::shared_ptr<TFile> outputFile;

};

PROGRAM_MAIN(FlattenProducer, Arguments)
