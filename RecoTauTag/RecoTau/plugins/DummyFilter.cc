/*! Apply filter on deepTauID producer.
This file is part of https://github.com/cms-tau-pog/TauTriggerTools. */

#include <Compression.h>
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "DataFormats/TauReco/interface/PFTau.h"
#include "RecoTauTag/RecoTau/interface/DeepTauBase.h"
#include "TauTriggerTools/Common/interface/GenTruthTools.h"
#include "RecoTauTag/RecoTau/interface/DeepTauTuple.h"

class DummyFilter : public edm::EDFilter {
public:
    using TauDiscriminator = reco::PFTauDiscriminator;

    DummyFilter(const edm::ParameterSet& cfg) :
    VSe_inputTag(cfg.getParameter<edm::InputTag>("VSe")),
    VSe_inputToken(consumes<TauDiscriminator>(VSe_inputTag)),
    VSmu_inputTag(cfg.getParameter<edm::InputTag>("VSmu")),
    VSmu_inputToken(consumes<TauDiscriminator>(VSmu_inputTag)),
    VSjet_inputTag(cfg.getParameter<edm::InputTag>("VSjet")),
    VSjet_inputToken(consumes<TauDiscriminator>(VSjet_inputTag)),
    looseIsoAbs_inputToken(consumes<TauDiscriminator>(cfg.getParameter<edm::InputTag>("looseIsoAbs"))),
    looseIsoRel_inputToken(consumes<TauDiscriminator>(cfg.getParameter<edm::InputTag>("looseIsoRel"))),
    mediumIsoAbs_inputToken(consumes<TauDiscriminator>(cfg.getParameter<edm::InputTag>("mediumIsoAbs"))),
    mediumIsoRel_inputToken(consumes<TauDiscriminator>(cfg.getParameter<edm::InputTag>("mediumIsoRel"))),
    tightIsoAbs_inputToken(consumes<TauDiscriminator>(cfg.getParameter<edm::InputTag>("tightIsoAbs"))),
    tightIsoRel_inputToken(consumes<TauDiscriminator>(cfg.getParameter<edm::InputTag>("tightIsoRel"))),
    genParticles_token(mayConsume<std::vector<reco::GenParticle>>(cfg.getParameter<edm::InputTag>("genParticles"))),
    taus_token(consumes<std::vector<reco::PFTau>>(cfg.getParameter<edm::InputTag>("taus"))),
    deepTauTuple("deep_taus", &edm::Service<TFileService>()->file(), false)
     {
         produces<bool>();
         std::cout << "Initialized" << std::endl;
     }

     virtual void endJob() override
     {
         deepTauTuple.Write();
     }

private:
    static constexpr float default_value = ::deep_tau::DefaultFillValue<float>();
    static constexpr int default_int_value = ::deep_tau::DefaultFillValue<int>();

    virtual bool filter(edm::Event& event, const edm::EventSetup& es) override
    {
        bool result = true;
        deepTauTuple().run  = event.id().run();
        deepTauTuple().lumi = event.id().luminosityBlock();
        deepTauTuple().evt  = event.id().event();

        edm::Handle<TauDiscriminator> looseIsoAbs;
        event.getByToken(looseIsoAbs_inputToken, looseIsoAbs);

        edm::Handle<TauDiscriminator> looseIsoRel;
        event.getByToken(looseIsoRel_inputToken, looseIsoRel);

        edm::Handle<TauDiscriminator> mediumIsoAbs;
        event.getByToken(mediumIsoAbs_inputToken, mediumIsoAbs);

        edm::Handle<TauDiscriminator> mediumIsoRel;
        event.getByToken(mediumIsoRel_inputToken, mediumIsoRel);

        edm::Handle<TauDiscriminator> tightIsoAbs;
        event.getByToken(tightIsoAbs_inputToken, tightIsoAbs);

        edm::Handle<TauDiscriminator> tightIsoRel;
        event.getByToken(tightIsoRel_inputToken, tightIsoRel);

        edm::Handle<TauDiscriminator> deepTau_VSe;
        event.getByToken(VSe_inputToken, deepTau_VSe);

        edm::Handle<TauDiscriminator> deepTau_VSmu;
        event.getByToken(VSmu_inputToken, deepTau_VSmu);

        edm::Handle<TauDiscriminator> deepTau_VSjet;
        event.getByToken(VSjet_inputToken, deepTau_VSjet);

        edm::Handle<std::vector<reco::GenParticle>> hGenParticles;
        event.getByToken(genParticles_token, hGenParticles);
        auto genParticles = hGenParticles.isValid() ? hGenParticles.product() : nullptr;

        edm::Handle<std::vector<reco::PFTau>> taus;
        event.getByToken(taus_token, taus);
        for(size_t tau_index = 0; tau_index < taus->size(); ++tau_index) {
            const reco::PFTau& tau = taus->at(tau_index);

            deepTauTuple().tau_pt = static_cast<float>(tau.polarP4().pt());
            deepTauTuple().tau_eta = static_cast<float>(tau.polarP4().eta());
            deepTauTuple().tau_phi = static_cast<float>(tau.polarP4().phi());
            deepTauTuple().tau_mass = static_cast<float>(tau.polarP4().mass());

            if(genParticles) {
                const auto gen_match = analysis::gen_truth::LeptonGenMatch(tau.polarP4(), *genParticles);
                deepTauTuple().lepton_gen_match = static_cast<int>(gen_match.match);
            } else {
                deepTauTuple().lepton_gen_match = default_int_value;
            }

            deepTauTuple().tau_decayMode = static_cast<int>(tau.decayMode());
            deepTauTuple().tau_looseIsoAbs = static_cast<float>(looseIsoAbs->value(tau_index));
            deepTauTuple().tau_looseIsoRel = static_cast<float>(looseIsoRel->value(tau_index));
            deepTauTuple().tau_mediumIsoAbs = static_cast<float>(mediumIsoAbs->value(tau_index));
            deepTauTuple().tau_mediumIsoRel = static_cast<float>(mediumIsoRel->value(tau_index));
            deepTauTuple().tau_tightIsoAbs = static_cast<float>(tightIsoAbs->value(tau_index));
            deepTauTuple().tau_tightIsoRel = static_cast<float>(tightIsoRel->value(tau_index));
            deepTauTuple().deepTau_VSe = static_cast<float>(deepTau_VSe->value(tau_index));
            deepTauTuple().deepTau_VSmu = static_cast<float>(deepTau_VSmu->value(tau_index));
            deepTauTuple().deepTau_VSjet = static_cast<float>(deepTau_VSjet->value(tau_index));

            deepTauTuple.Fill();
        }

        return result;
    }


private:
    const edm::InputTag VSe_inputTag;                       // input tag identifying product
    const edm::EDGetTokenT<TauDiscriminator> VSe_inputToken;  // token identifying product
    const edm::InputTag VSmu_inputTag;                       // input tag identifying product
    const edm::EDGetTokenT<TauDiscriminator> VSmu_inputToken;
    const edm::InputTag VSjet_inputTag;                       // input tag identifying product
    const edm::EDGetTokenT<TauDiscriminator> VSjet_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> looseIsoAbs_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> looseIsoRel_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> mediumIsoAbs_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> mediumIsoRel_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> tightIsoAbs_inputToken;
    const edm::EDGetTokenT<TauDiscriminator> tightIsoRel_inputToken;
    edm::EDGetTokenT<std::vector<reco::GenParticle>> genParticles_token;
    edm::EDGetTokenT<std::vector<reco::PFTau>> taus_token;
    deep_tau::DeepTauTuple deepTauTuple;
};


#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DummyFilter);
