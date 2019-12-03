import FWCore.ParameterSet.Config as cms
import TauTriggerTools.Common

def update(process,summary):
	process.options.wantSummary = cms.untracked.bool(summary)

	process.genFilter = cms.EDFilter("GenTauFilter",
	    genParticles         = cms.InputTag('genParticles'),
	    n_tau_had            = cms.int32(2),
	    n_tau_mu             = cms.int32(0),
	    n_tau_e              = cms.int32(0)
	)

	process.HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v4.insert(0, process.genFilter)

	process.initialFilter.store_hist = cms.bool(False)
	process.initialFilter.store_both = cms.bool(True)
	process.initialFilter.isMC = cms.bool(True)

	process.afterL1Filter.store_hist = cms.bool(True)
	process.afterL1Filter.store_both = cms.bool(False)
	process.afterL1Filter.isMC = cms.bool(True)

	process.intermidiateFilter.store_hist = cms.bool(True)
	process.intermidiateFilter.store_both = cms.bool(False)
	process.intermidiateFilter.isMC = cms.bool(True)

	process.finalFilter.store_hist = cms.bool(False)
	process.finalFilter.store_both = cms.bool(False)
	process.finalFilter.isMC = cms.bool(True)

	return process
