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
        store_both(cfg.getParameter<bool>("store_both")),
        position(cfg.getParameter<std::string>("position")),
        deepTauVSe_inputToken(mayConsume<TauDiscriminator>(cfg.getParameter<edm::InputTag>("deepTauVSe"))),
        deepTauVSmu_inputToken(mayConsume<TauDiscriminator>(cfg.getParameter<edm::InputTag>("deepTauVSmu"))),
        deepTauVSjet_inputToken(mayConsume<TauDiscriminator>(cfg.getParameter<edm::InputTag>("deepTauVSjet"))),
        mediumIsoAbs_inputToken(mayConsume<TauDiscriminator>(cfg.getParameter<edm::InputTag>("mediumIsoAbs"))),
        mediumIsoRel_inputToken(mayConsume<TauDiscriminator>(cfg.getParameter<edm::InputTag>("mediumIsoRel"))),
        looseIsoAbs_inputToken(mayConsume<TauDiscriminator>(cfg.getParameter<edm::InputTag>("looseIsoAbs"))),
        looseIsoRel_inputToken(mayConsume<TauDiscriminator>(cfg.getParameter<edm::InputTag>("looseIsoRel"))),
        tightIsoAbs_inputToken(mayConsume<TauDiscriminator>(cfg.getParameter<edm::InputTag>("tightIsoAbs"))),
        tightIsoRel_inputToken(mayConsume<TauDiscriminator>(cfg.getParameter<edm::InputTag>("tightIsoRel"))),
        original_taus_token(mayConsume<std::vector<reco::PFTau>>(cfg.getParameter<edm::InputTag>("original_taus"))),
        taus_token(mayConsume<std::vector<reco::PFTau>>(cfg.getParameter<edm::InputTag>("taus"))),
        puInfo_token(mayConsume<std::vector<PileupSummaryInfo>>(cfg.getParameter<edm::InputTag>("puInfo"))),
        vertices_token(mayConsume<std::vector<reco::Vertex> >(cfg.getParameter<edm::InputTag>("vertices"))),
        decayMode_token(consumes<reco::PFTauDiscriminator>(cfg.getParameter<edm::InputTag>("decayModeFindingNewDM"))),
        genParticles_token(mayConsume<std::vector<reco::GenParticle>>(cfg.getParameter<edm::InputTag>("genParticles")))
    {
        std::string full_name = position+"_counter";
        std::string full_name_hist = position+"_counter_hist";
        if(store_hist){
            counter = std::make_shared<TH1F>(full_name_hist.c_str(),full_name_hist.c_str(),2,-0.5,1.5);
        }
        else if(store_both){
            counter = std::make_shared<TH1F>(full_name_hist.c_str(),full_name_hist.c_str(),2,-0.5,1.5);
            counterTuple = std::make_shared<counter_tau::CounterTuple>(full_name, &edm::Service<TFileService>()->file(), false);
        }
        else{
            counterTuple = std::make_shared<counter_tau::CounterTuple>(full_name, &edm::Service<TFileService>()->file(), false);
        }
    }

private:
    static constexpr int default_int_value = ::counter_tau::DefaultFillValue<int>();
    static constexpr float default_value = ::counter_tau::DefaultFillValue<float>();

    virtual bool filter(edm::Event& event, const edm::EventSetup&) override
    {
        bool result = true;

        if(store_hist){
            counter->Fill(1);
        }
        else if(store_both){
            counter->Fill(1);

            (*counterTuple)().run  = event.id().run();
            (*counterTuple)().lumi = event.id().luminosityBlock();
            (*counterTuple)().evt  = event.id().event();

            if(isMC){
                edm::Handle<std::vector<reco::GenParticle>> hGenParticles;
                event.getByToken(genParticles_token, hGenParticles);
                genParticles = hGenParticles.isValid() ? hGenParticles.product() : nullptr;

                std::vector<analysis::gen_truth::LeptonMatchResult> lepton_results = analysis::gen_truth::CollectGenLeptons(*genParticles);

                for(unsigned n = 0; n < lepton_results.size(); ++n){
                    const auto gen_match = lepton_results.at(n);
                    (*counterTuple)().lepton_gen_match.push_back(static_cast<int>(gen_match.match));
                    (*counterTuple)().gen_tau_pt.push_back(static_cast<float>(gen_match.visible_p4.pt()));
                    (*counterTuple)().gen_tau_eta.push_back(static_cast<float>(gen_match.visible_p4.eta()));
                    (*counterTuple)().gen_tau_phi.push_back(static_cast<float>(gen_match.visible_p4.phi()));
                    (*counterTuple)().gen_tau_e.push_back(static_cast<float>(gen_match.visible_p4.e()));

                }
            }


            counterTuple->Fill();
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

            edm::Handle<TauDiscriminator> looseIsoAbs;
            event.getByToken(looseIsoAbs_inputToken, looseIsoAbs);

            edm::Handle<TauDiscriminator> looseIsoRel;
            event.getByToken(looseIsoRel_inputToken, looseIsoRel);

            edm::Handle<TauDiscriminator> tightIsoAbs;
            event.getByToken(tightIsoAbs_inputToken, tightIsoAbs);

            edm::Handle<TauDiscriminator> tightIsoRel;
            event.getByToken(tightIsoRel_inputToken, tightIsoRel);

            edm::Handle<std::vector<reco::PFTau>> original_taus;
            event.getByToken(original_taus_token, original_taus);

            edm::Handle<std::vector<reco::PFTau>> taus;
            event.getByToken(taus_token, taus);

            edm::Handle<reco::PFTauDiscriminator> decayModesNew;
            event.getByToken(decayMode_token, decayModesNew);

            if(isMC) {
                edm::Handle<std::vector<PileupSummaryInfo>> puInfo;
                event.getByToken(puInfo_token, puInfo);
                (*counterTuple)().npu = analysis::gen_truth::GetNumberOfPileUpInteractions(puInfo);

                edm::Handle<std::vector<reco::GenParticle>> hGenParticles;
                event.getByToken(genParticles_token, hGenParticles);
                genParticles = hGenParticles.isValid() ? hGenParticles.product() : nullptr;
            }



            (*counterTuple)().run  = event.id().run();
            (*counterTuple)().lumi = event.id().luminosityBlock();
            (*counterTuple)().evt  = event.id().event();

            for(size_t orig_tau_index = 0; orig_tau_index < original_taus->size(); ++orig_tau_index) {
                const reco::PFTau& original_tau = original_taus->at(orig_tau_index);

                if(genParticles) {
                    const auto gen_match = analysis::gen_truth::LeptonGenMatch(original_tau.polarP4(), *genParticles);
                    (*counterTuple)().lepton_gen_match.push_back(static_cast<int>(gen_match.match));
                    (*counterTuple)().gen_tau_pt.push_back(static_cast<float>(gen_match.visible_p4.pt()));
                    (*counterTuple)().gen_tau_eta.push_back(static_cast<float>(gen_match.visible_p4.eta()));
                    (*counterTuple)().gen_tau_phi.push_back(static_cast<float>(gen_match.visible_p4.phi()));
                    (*counterTuple)().gen_tau_e.push_back(static_cast<float>(gen_match.visible_p4.e()));
                } else {
                    (*counterTuple)().lepton_gen_match.push_back(default_int_value);
                    (*counterTuple)().gen_tau_pt.push_back(default_value);
                    (*counterTuple)().gen_tau_eta.push_back(default_value);
                    (*counterTuple)().gen_tau_phi.push_back(default_value);
                    (*counterTuple)().gen_tau_e.push_back(default_value);
                }

                (*counterTuple)().tau_pt.push_back(static_cast<float>(original_tau.polarP4().pt()));
                (*counterTuple)().tau_eta.push_back(static_cast<float>(original_tau.polarP4().eta()));
                (*counterTuple)().tau_mediumIsoAbs.push_back(static_cast<float>(mediumIsoAbs->value(orig_tau_index)));
                (*counterTuple)().tau_mediumIsoRel.push_back(static_cast<float>(mediumIsoRel->value(orig_tau_index)));
                (*counterTuple)().tau_looseIsoAbs.push_back(static_cast<float>(looseIsoAbs->value(orig_tau_index)));
                (*counterTuple)().tau_looseIsoRel.push_back(static_cast<float>(looseIsoRel->value(orig_tau_index)));
                (*counterTuple)().tau_tightIsoAbs.push_back(static_cast<float>(tightIsoAbs->value(orig_tau_index)));
                (*counterTuple)().tau_tightIsoRel.push_back(static_cast<float>(tightIsoRel->value(orig_tau_index)));

                (*counterTuple)().deepTau_VSe.push_back(static_cast<float>(deepTau_VSe->value(orig_tau_index)));
                (*counterTuple)().deepTau_VSmu.push_back(static_cast<float>(deepTau_VSmu->value(orig_tau_index)));
                (*counterTuple)().deepTau_VSjet.push_back(static_cast<float>(deepTau_VSjet->value(orig_tau_index)));
                (*counterTuple)().tau_decayModeFindingNewDMs.push_back(decayModesNew->value(orig_tau_index));

                bool passed_lastFilter = false;
                for(size_t tau_index = 0; tau_index < taus->size(); ++tau_index){
                    const reco::PFTau& tau = taus->at(tau_index);

                    const double deltaR = ROOT::Math::VectorUtil::DeltaR(original_tau.polarP4(),tau.polarP4());
                    if(deltaR < 0.01){
                        passed_lastFilter = true;
                        break;
                    }
                }

                (*counterTuple)().tau_passedLastFilter.push_back(passed_lastFilter);

            }

            counterTuple->Fill();
        }

        return result;
    }

    void endJob()
    {
        if(store_hist){
            //counter->Write();
            edm::Service<TFileService>()->file().WriteTObject(counter.get());
        }
        else if(store_both){
            edm::Service<TFileService>()->file().WriteTObject(counter.get());
            counterTuple->Write();
        }
        else
            counterTuple->Write();
    }

private:
    const bool isMC, store_hist, store_both;
    std::string position;
    const edm::EDGetTokenT<TauDiscriminator> deepTauVSe_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> deepTauVSmu_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> deepTauVSjet_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> mediumIsoAbs_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> mediumIsoRel_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> looseIsoAbs_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> looseIsoRel_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> tightIsoAbs_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> tightIsoRel_inputToken;
    edm::EDGetTokenT<std::vector<reco::PFTau>> original_taus_token;
    edm::EDGetTokenT<std::vector<reco::PFTau>> taus_token;
    edm::EDGetTokenT<std::vector<PileupSummaryInfo>> puInfo_token;
    edm::EDGetTokenT<std::vector<reco::Vertex>> vertices_token;
    edm::EDGetTokenT<reco::PFTauDiscriminator> decayMode_token;
    edm::EDGetTokenT<std::vector<reco::GenParticle>> genParticles_token;
    const std::vector<reco::GenParticle>* genParticles;
    std::shared_ptr<TH1F> counter;
    std::shared_ptr<counter_tau::CounterTuple> counterTuple;

};


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(CounterFilter);
