import FWCore.ParameterSet.Config as cms

def update(process,summary):
	process.options.wantSummary = cms.untracked.bool(summary)

	process.initialFilter.store_hist = cms.bool(False)
	process.initialFilter.store_both = cms.bool(True)
	process.initialFilter.isMC = cms.bool(False)

	process.afterL1Filter.store_hist = cms.bool(True)
	process.afterL1Filter.store_both = cms.bool(False)
	process.afterL1Filter.isMC = cms.bool(False)

	process.intermidiateFilter.store_hist = cms.bool(True)
	process.intermidiateFilter.store_both = cms.bool(False)
	process.intermidiateFilter.isMC = cms.bool(False)

	process.finalFilter.store_hist = cms.bool(False)
	process.finalFilter.store_both = cms.bool(False)
	process.finalFilter.isMC = cms.bool(False)

	return process
