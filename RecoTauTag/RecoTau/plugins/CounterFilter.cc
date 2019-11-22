/*! Apply tau trigger selection vetoes.
This file is part of https://github.com/cms-tau-pog/TauTriggerTools. */

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/Common/interface/TriggerResults.h"

#include "TauTriggerTools/Common/interface/AnalysisTypes.h"
#include "TauTriggerTools/Common/interface/CutTools.h"
#include "TauTriggerTools/Common/interface/PatHelpers.h"
#include "TauTriggerTools/Common/interface/GenTruthTools.h"

#include "DataFormats/TauReco/interface/PFTau.h"
#include "RecoTauTag/RecoTau/interface/DeepTauBase.h"
#include "RecoTauTag/RecoTau/interface/CounterTuple.h"

class CounterFilter : public edm::EDFilter {
public:
    using TauDiscriminator = reco::PFTauDiscriminator;

    CounterFilter(const edm::ParameterSet& cfg) :
        isMC(cfg.getParameter<bool>("isMC")),
        store_hist(cfg.getParameter<bool>("store_hist")),
        position(cfg.getParameter<std::string>("position")),
        deepTauVSe_inputToken(mayConsume<TauDiscriminator>(cfg.getParameter<edm::InputTag>("deepTauVSe"))),
        deepTauVSmu_inputToken(mayConsume<TauDiscriminator>(cfg.getParameter<edm::InputTag>("deepTauVSmu"))),
        deepTauVSjet_inputToken(mayConsume<TauDiscriminator>(cfg.getParameter<edm::InputTag>("deepTauVSjet"))),
        mediumIsoAbs_inputToken(mayConsume<TauDiscriminator>(cfg.getParameter<edm::InputTag>("mediumIsoAbs"))),
        mediumIsoRel_inputToken(mayConsume<TauDiscriminator>(cfg.getParameter<edm::InputTag>("mediumIsoRel"))),
        taus_token(mayConsume<std::vector<reco::PFTau>>(cfg.getParameter<edm::InputTag>("taus"))),
        puInfo_token(mayConsume<std::vector<PileupSummaryInfo>>(cfg.getParameter<edm::InputTag>("puInfo"))),
        vertices_token(mayConsume<std::vector<reco::Vertex> >(cfg.getParameter<edm::InputTag>("vertices"))),
        decayMode_token(consumes<reco::PFTauDiscriminator>(cfg.getParameter<edm::InputTag>("decayModeFindingNewDM")))
    {
        std::string full_name = position+"_counter";
        if(store_hist){
            counter = std::make_shared<TH1F>(full_name.c_str(),full_name.c_str(),2,-0.5,1.5);
        }
        else{
            std::cout << "Pippo" << std::endl;
            counterTuple = std::make_shared<counter_tau::CounterTuple>(full_name, &edm::Service<TFileService>()->file(), false);
        }
    }

private:
    virtual bool filter(edm::Event& event, const edm::EventSetup&) override
    {
        bool result = true;

        if(store_hist){
            counter->Fill(1);
        }
        else{
            edm::Handle<std::vector<reco::Vertex>> vertices;
            event.getByToken(vertices_token, vertices);
            (*counterTuple)().npv = static_cast<int>(vertices->size());

            edm::Handle<TauDiscriminator> deepTau_VSe;
            event.getByToken(deepTauVSe_inputToken, deepTau_VSe);

            edm::Handle<TauDiscriminator> deepTau_VSmu;
            event.getByToken(deepTauVSmu_inputToken, deepTau_VSmu);

            edm::Handle<TauDiscriminator> deepTau_VSjet;
            event.getByToken(deepTauVSjet_inputToken, deepTau_VSjet);

            edm::Handle<TauDiscriminator> mediumIsoAbs;
            event.getByToken(mediumIsoAbs_inputToken, mediumIsoAbs);

            edm::Handle<TauDiscriminator> mediumIsoRel;
            event.getByToken(mediumIsoRel_inputToken, mediumIsoRel);

            edm::Handle<std::vector<reco::PFTau>> taus;
            event.getByToken(taus_token, taus);

            edm::Handle<reco::PFTauDiscriminator> decayModesNew;
            event.getByToken(decayMode_token, decayModesNew);

            if(isMC) {
                edm::Handle<std::vector<PileupSummaryInfo>> puInfo;
                event.getByToken(puInfo_token, puInfo);
                (*counterTuple)().npu = analysis::gen_truth::GetNumberOfPileUpInteractions(puInfo);
            }

            (*counterTuple)().run  = event.id().run();
            (*counterTuple)().lumi = event.id().luminosityBlock();
            (*counterTuple)().evt  = event.id().event();

            for(size_t tau_index = 0; tau_index < taus->size(); ++tau_index) {
                const reco::PFTau& tau = taus->at(tau_index);

                (*counterTuple)().tau_pt.push_back(static_cast<float>(tau.polarP4().pt()));
                (*counterTuple)().tau_mediumIsoAbs.push_back(static_cast<float>(mediumIsoAbs->value(tau_index)));
                (*counterTuple)().tau_mediumIsoRel.push_back(static_cast<float>(mediumIsoRel->value(tau_index)));

                (*counterTuple)().deepTau_VSe.push_back(static_cast<float>(deepTau_VSe->value(tau_index)));
                (*counterTuple)().deepTau_VSmu.push_back(static_cast<float>(deepTau_VSmu->value(tau_index)));
                (*counterTuple)().deepTau_VSjet.push_back(static_cast<float>(deepTau_VSjet->value(tau_index)));
                (*counterTuple)().tau_decayModeFindingNewDMs.push_back(decayModesNew->value(tau_index));

                counterTuple->Fill();
            }
        }

        return result;
    }

    void endJob()
    {
        if(store_hist){
            //counter->Write();
            edm::Service<TFileService>()->file().WriteTObject(counter.get());
        }
        else
            counterTuple->Write();
    }

private:
    const bool isMC, store_hist;
    std::string position;
    const edm::EDGetTokenT<TauDiscriminator> deepTauVSe_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> deepTauVSmu_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> deepTauVSjet_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> mediumIsoAbs_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> mediumIsoRel_inputToken;
    edm::EDGetTokenT<std::vector<reco::PFTau>> taus_token;
    edm::EDGetTokenT<std::vector<PileupSummaryInfo>> puInfo_token;
    edm::EDGetTokenT<std::vector<reco::Vertex>> vertices_token;
    edm::EDGetTokenT<reco::PFTauDiscriminator> decayMode_token;
    std::shared_ptr<TH1F> counter;
    std::shared_ptr<counter_tau::CounterTuple> counterTuple;

};


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(CounterFilter);
