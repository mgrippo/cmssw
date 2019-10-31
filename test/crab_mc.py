from CRABClient.UserUtilities import config

config = config()

config.General.transferOutputs = True
config.General.transferLogs    = True

config.JobType.psetName        = 'tau_hlt.py'
config.JobType.pluginName      = 'tau_hlt'
config.JobType.outputFiles     = ['output.root']
config.JobType.maxMemoryMB     = 4000
config.JobType.priority        = 99999

config.Data.splitting          = 'Automatic'

config.Data.publication        = False
#config.Data.outputDatasetTag   = 'doubleTauTriggerOpenPt_2017'

config.Site.storageSite        = 'T2_IT_Pisa'

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    from CRABClient.ClientExceptions import ClientException
    from httplib import HTTPException

    tag = 'deepTau_hlt_mc'

    # We want to put all the CRAB project directories from the tasks we submit here into one common directory.
    # That's why we need to set this parameter (here or above in the configuration file, it does not matter, we will not overwrite it).
    config.General.workArea   = 'crab_' + tag
    config.Data.outLFNDirBase = '/store/user/mgrippo/' + tag

    def submit(config):
        try:
            crabCommand('submit', config = config)
        except HTTPException as hte:
            print "Failed submitting task: %s" % (hte.headers)
        except ClientException as cle:
            print "Failed submitting task: %s" % (cle)

    datasets = {}

    datasets['DYJets'] = ('/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIIFall18wmLHEGS-102X_upgrade2018_realistic_v11-v1/GEN-SIM')

    for k, v in datasets.iteritems():
        config.General.requestName = k
        config.Data.inputDataset          = v[0]
        #config.Data.secondaryInputDataset = v[1]
        print 'submitting config:'
        print config
        submit(config)
