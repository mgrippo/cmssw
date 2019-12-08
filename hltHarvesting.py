import FWCore.ParameterSet.Config as cms

process = cms.Process('HARVESTING')

# read all the DQMIO files produced by the previous jobs
process.source = cms.Source("DQMRootSource",
    fileNames = cms.untracked.vstring(
        "file:DQM_00.root",
        "file:DQM_01.root",
        ...
    )
)

# DQMStore service
process.load('DQMServices.Core.DQMStore_cfi')

# FastTimerService client
process.load('HLTrigger.Timer.fastTimerServiceClient_cfi')
process.fastTimerServiceClient.dqmPath = "HLT/TimerService"

# timing VS lumi
process.fastTimerServiceClient.doPlotsVsScalLumi  = cms.bool(True)
process.fastTimerServiceClient.doPlotsVsPixelLumi = cms.bool(False)
process.fastTimerServiceClient.scalLumiME = cms.PSet(
        folder = cms.string('HLT/LumiMonitoring'),
        name   = cms.string('lumiVsLS'),
        nbins  = cms.int32(5000),
        xmin   = cms.double(0),
        xmax   = cms.double(20000)
    )

# DQM file saver
process.load('DQMServices.Components.DQMFileSaver_cfi')
process.dqmSaver.workflow = "/HLT/FastTimerService/All"

process.DQMFileSaverOutput = cms.EndPath( process.fastTimerServiceClient + process.dqmSaver )
