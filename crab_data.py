from collections import OrderedDict
from CRABClient.UserUtilities import config

config = config()

config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.psetName        = 'tau_hlt_data.py'
config.JobType.pluginName      = 'tau_hlt'
config.JobType.outputFiles     = ['output_data.root']
config.JobType.maxMemoryMB     = 4000
config.JobType.priority        = 99999

config.Data.splitting          = 'Automatic'
config.Data.lumiMask = 'https://cms-service-dqm.web.cern.ch/cms-service-dqm/CAF/certification/Collisions17/13TeV/PromptReco/Cert_294927-306126_13TeV_PromptReco_Collisions17_JSON.txt'
#config.Data.runRange = '306091-306096'
config.Data.publication        = False

config.Site.storageSite        = 'T2_IT_Pisa'

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    tag = 'doubleTauTrigger_asym_2017_noSkim'

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea   = 'crab_data_' + tag
    config.Data.outLFNDirBase = '/store/group/phys_tau/' + tag + '_data_FULL'

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    datasets = {}

    datasets['ZeroBias_F'] = ('/ZeroBias/Run2017F-PromptReco-v1/MINIAOD',
                                '/ZeroBias/Run2017F-v1/RAW')

    for k, v in datasets.iteritems():
        config.General.requestName = k
        config.Data.inputDataset          = v[0]
        config.Data.secondaryInputDataset = v[1]
        print 'submitting config:'
        print config
        submit(config)
