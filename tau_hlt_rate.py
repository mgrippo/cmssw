# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: tau_hlt_rate --python_filename tau_hlt_rate.py --customise=HLTrigger/Configuration/myTauHLT_rate.update --step=HLT:User --data --no_exec --conditions auto:run2_data_GRun --era=Run2_2018 --no_output -n 10 --filein /store/data/Run2018D/ZeroBias9/RAW/v1/000/324/536/00000/C422DF3F-7430-4B49-B0CE-376E6A662328.root
import FWCore.ParameterSet.Config as cms
import os
import re
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('analysis')
options.register('wantSummary', False, VarParsing.multiplicity.singleton, VarParsing.varType.bool,
                 "Print run summary at the end of the job.")
options.parseArguments()

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('HLTdata',Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('HLTrigger.Configuration.HLT_Rate_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring('/store/data/Run2018D/ZeroBias9/RAW/v1/000/324/536/00000/C422DF3F-7430-4B49-B0CE-376E6A662328.root'),
    # fileNames = cms.untracked.vstring('file:raw_ZeroBias/2CA562E1-389F-E811-858A-FA163EE35BE6.root', #ZeroBias RunD
    #                                   'file:raw_ZeroBias/129CA157-37A0-E811-AB9D-FA163E2286AE.root',
    #                                   'file:raw_ZeroBias/125F1594-13A1-E811-AEE7-FA163E6CD0D3.root',
    #                                   'file:raw_ZeroBias/10E9C386-3BA0-E811-8747-FA163ED0CAD6.root'),
    #fileNames = cms.untracked.vstring('file:6845E464-BE71-A048-BB12-22D60B0A1D27.root'), #HLTPhysics RunD
    #fileNames = cms.untracked.vstring('file:294DC28D-761A-5E4B-BF40-78D8D3E7DA35.root'), #HLTPhysics RunD
    fileNames = cms.untracked.vstring('file:/afs/cern.ch/work/m/mgrippo/TauTrigger_2019_new/CMSSW_10_6_3/src/13B7733B-0DCE-0D41-949D-1AD9F6A3896B.root'), #HLTPhysics RunD
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('tau_hlt_rate nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition
process.TFileService = cms.Service('TFileService', fileName=cms.string("rate_Tuple.root"))

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_data_GRun', '')

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule()
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.myTauHLT_rate
from HLTrigger.Configuration.myTauHLT_rate import update

#call to customisation function update imported from HLTrigger.Configuration.myTauHLT_rate
process = update(process,options.wantSummary)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
