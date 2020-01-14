import FWCore.ParameterSet.Config as cms

def update(process,summary):
	process.options.wantSummary = cms.untracked.bool(summary)

	process.initialFilter.store_hist = cms.bool(False)
	process.initialFilter.store_both = cms.bool(True)
	process.initialFilter.isMC = cms.bool(False)

	process.afterBeginSequence.store_hist = cms.bool(False)
	process.afterBeginSequence.store_both = cms.bool(True)
	process.afterBeginSequence.isMC = cms.bool(False)

	process.afterL1Filter.store_hist = cms.bool(False)
	process.afterL1Filter.store_both = cms.bool(True)
	process.afterL1Filter.isMC = cms.bool(False)

	process.afterPreDoubleMediumChargedIsoPFTauHPS35Trk1eta2p1Reg.store_hist = cms.bool(False)
	process.afterPreDoubleMediumChargedIsoPFTauHPS35Trk1eta2p1Reg.store_both = cms.bool(True)
	process.afterPreDoubleMediumChargedIsoPFTauHPS35Trk1eta2p1Reg.isMC = cms.bool(False)

	process.afterL2TauJetsL1TauSeededSequence.store_hist = cms.bool(False)
	process.afterL2TauJetsL1TauSeededSequence.store_both = cms.bool(True)
	process.afterL2TauJetsL1TauSeededSequence.isMC = cms.bool(False)

	process.afterDoubleL2Tau26eta2p2.store_hist = cms.bool(False)
	process.afterDoubleL2Tau26eta2p2.store_both = cms.bool(True)
	process.afterDoubleL2Tau26eta2p2.isMC = cms.bool(False)

	process.afterL2p5IsoTauL1TauSeededSequence.store_hist = cms.bool(False)
	process.afterL2p5IsoTauL1TauSeededSequence.store_both = cms.bool(True)
	process.afterL2p5IsoTauL1TauSeededSequence.isMC = cms.bool(False)

	process.afterDoubleL2IsoTau26eta2p2.store_hist = cms.bool(False)
	process.afterDoubleL2IsoTau26eta2p2.store_both = cms.bool(True)
	process.afterDoubleL2IsoTau26eta2p2.isMC = cms.bool(False)

	process.afterRegionalPFTauHPSSequence.store_hist = cms.bool(False)
	process.afterRegionalPFTauHPSSequence.store_both = cms.bool(True)
	process.afterRegionalPFTauHPSSequence.isMC = cms.bool(False)

	process.afterHPSDoublePFTauPt35Eta2p1Trk1Reg.store_hist = cms.bool(False)
	process.afterHPSDoublePFTauPt35Eta2p1Trk1Reg.store_both = cms.bool(True)
	process.afterHPSDoublePFTauPt35Eta2p1Trk1Reg.isMC = cms.bool(False)

	process.afterHpsDoublePFTau35TrackPt1MediumChargedIsolationReg.store_hist = cms.bool(False)
	process.afterHpsDoublePFTau35TrackPt1MediumChargedIsolationReg.store_both = cms.bool(True)
	process.afterHpsDoublePFTau35TrackPt1MediumChargedIsolationReg.isMC = cms.bool(False)

	process.afterHpsL1JetsHLTDoublePFTauTrackPt1MediumChargedIsolationMatchReg.store_hist = cms.bool(False)
	process.afterHpsL1JetsHLTDoublePFTauTrackPt1MediumChargedIsolationMatchReg.store_both = cms.bool(True)
	process.afterHpsL1JetsHLTDoublePFTauTrackPt1MediumChargedIsolationMatchReg.isMC = cms.bool(False)

	process.afterHpsDoublePFTau35TrackPt1MediumChargedIsolationL1HLTMatchedReg.store_hist = cms.bool(False)
	process.afterHpsDoublePFTau35TrackPt1MediumChargedIsolationL1HLTMatchedReg.store_both = cms.bool(True)
	process.afterHpsDoublePFTau35TrackPt1MediumChargedIsolationL1HLTMatchedReg.isMC = cms.bool(False)


	process.finalFilter.store_hist = cms.bool(False)
	process.finalFilter.store_both = cms.bool(False)
	process.finalFilter.isMC = cms.bool(False)

	return process
