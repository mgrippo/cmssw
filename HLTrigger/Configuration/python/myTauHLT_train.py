import FWCore.ParameterSet.Config as cms

def update(process,summary,isMC,requireGenMatch):
	process.options.wantSummary = cms.untracked.bool(summary)

	process.tauTupleProducer.isMC = isMC
	#process.tauTupleProducer.requireGenMatch = requireGenMatch

	return process
