# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: tau_hlt_train_new --python_filename tau_hlt_train_new.py --customise=HLTrigger/Configuration/myTauHLT_train_new.update --step=HLT:User --mc --no_exec --conditions auto:run2_mc_GRun --era=Run2_2018 --no_output -n 10 --filein /store/mc/RunIISpring18DR/VBFHToTauTau_M125_13TeV_powheg_pythia8/GEN-SIM-RAW/NZSPU28to70_100X_upgrade2018_realistic_v10-v1/90000/00CAF27C-A02C-E811-BC5C-02163E01770D.root
import FWCore.ParameterSet.Config as cms
import os
import re
from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing('analysis')
options.register('wantSummary', False, VarParsing.multiplicity.singleton, VarParsing.varType.bool,
                 "Print run summary at the end of the job.")
options.register('isMC', True, VarParsing.multiplicity.singleton, VarParsing.varType.bool,
                 "Define if the sample is MC")
options.register('requireGenMatch', True, VarParsing.multiplicity.singleton, VarParsing.varType.bool,
                 "Store only taus/jets that have GenLeptonMatch or GenQcdMatch.")
options.parseArguments()

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018

process = cms.Process('HLTmc',Run2_2018)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('HLTrigger.Configuration.HLT_MinTauSeq_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(200)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/afs/cern.ch/work/m/mgrippo/TauTrigger_2019_new/CMSSW_10_6_3/src/00CAF27C-A02C-E811-BC5C-02163E01770D.root'), #VBF
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('tau_hlt_train_new nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition
process.TFileService = cms.Service('TFileService', fileName=cms.string("deepTauTuple_Train_tuple.root"))

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc_GRun', '')

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)

# Schedule definition
process.schedule = cms.Schedule()
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.myTauHLT_train_new
from HLTrigger.Configuration.myTauHLT_train_new import update

#call to customisation function update imported from HLTrigger.Configuration.myTauHLT_train_new
process = update(process,options.wantSummary,options.isMC,options.requireGenMatch)

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
