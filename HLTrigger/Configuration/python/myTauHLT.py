import FWCore.ParameterSet.Config as cms
import TauTriggerTools.Common

def update(process,summary,isMC,requireGenMatch):
	process.options.wantSummary = cms.untracked.bool(summary)

	process.genFilter = cms.EDFilter("GenTauFilter",
	    genParticles         = cms.InputTag('genParticles'),
	    n_tau_had            = cms.int32(2),
	    n_tau_mu             = cms.int32(0),
	    n_tau_e              = cms.int32(0)
	)
	#process.genFilterPath = cms.Path(process.genFilter)
	#process.schedule.insert(0, process.genFilterPath)
	#process.HLT_DoubleMediumChargedIsoPFTauHPS35_Trk1_eta2p1_Reg_v4.insert(0, process.genFilter)

	process.tauTupleProducer.isMC = isMC
	process.tauTupleProducer.requireGenMatch = requireGenMatch
	return process
