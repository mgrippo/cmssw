# hltGetConfiguration /users/mgrippo/deepTauTraining_HLT_2/V1 --path HLTriggerFirstPath,HLT_IsoMu20_eta2p1_MediumChargedIsoPFTauHPS27_eta2p1_CrossL1_v1,HLTriggerFinalPath,HLTAnalyzerEndpath --unprescale --cff

# /users/mgrippo/deepTauTraining_HLT_2/V1 (CMSSW_10_6_0_pre4)

import FWCore.ParameterSet.Config as cms

fragment = cms.ProcessFragment( "HLT" )

fragment.HLTConfigVersion = cms.PSet(
  tableName = cms.string('/users/mgrippo/deepTauTraining_HLT_2/V1')
)

fragment.hltGetConditions = cms.EDAnalyzer( "EventSetupRecordDataGetter",
    toGet = cms.VPSet(
    ),
    verbose = cms.untracked.bool( False )
)
fragment.hltGetRaw = cms.EDAnalyzer( "HLTGetRaw",
    RawDataCollection = cms.InputTag( "rawDataCollector" )
)
fragment.hltBoolFalse = cms.EDFilter( "HLTBool",
    result = cms.bool( False )
)
fragment.hltTriggerType = cms.EDFilter( "HLTTriggerTypeFilter",
    SelectedTriggerType = cms.int32( 1 )
)
fragment.hltGtStage2Digis = cms.EDProducer( "L1TRawToDigi",
    lenSlinkTrailer = cms.untracked.int32( 8 ),
    lenAMC13Header = cms.untracked.int32( 8 ),
    CTP7 = cms.untracked.bool( False ),
    lenAMC13Trailer = cms.untracked.int32( 8 ),
    Setup = cms.string( "stage2::GTSetup" ),
    MinFeds = cms.uint32( 0 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    lenSlinkHeader = cms.untracked.int32( 8 ),
    MTF7 = cms.untracked.bool( False ),
    FWId = cms.uint32( 0 ),
    TMTCheck = cms.bool( True ),
    lenAMCTrailer = cms.untracked.int32( 0 ),
    debug = cms.untracked.bool( False ),
    FedIds = cms.vint32( 1404 ),
    lenAMCHeader = cms.untracked.int32( 8 ),
    DmxFWId = cms.uint32( 0 ),
    FWOverride = cms.bool( False )
)
fragment.hltGtStage2ObjectMap = cms.EDProducer( "L1TGlobalProducer",
    L1DataBxInEvent = cms.int32( 5 ),
    JetInputTag = cms.InputTag( 'hltGtStage2Digis','Jet' ),
    AlgorithmTriggersUnmasked = cms.bool( True ),
    EmulateBxInEvent = cms.int32( 1 ),
    AlgorithmTriggersUnprescaled = cms.bool( True ),
    PrintL1Menu = cms.untracked.bool( False ),
    PrescaleCSVFile = cms.string( "prescale_L1TGlobal.csv" ),
    Verbosity = cms.untracked.int32( 0 ),
    AlgoBlkInputTag = cms.InputTag( "hltGtStage2Digis" ),
    EtSumInputTag = cms.InputTag( 'hltGtStage2Digis','EtSum' ),
    ProduceL1GtDaqRecord = cms.bool( True ),
    PrescaleSet = cms.uint32( 1 ),
    ExtInputTag = cms.InputTag( "hltGtStage2Digis" ),
    EGammaInputTag = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
    TriggerMenuLuminosity = cms.string( "startup" ),
    ProduceL1GtObjectMapRecord = cms.bool( True ),
    AlternativeNrBxBoardDaq = cms.uint32( 0 ),
    GetPrescaleColumnFromData = cms.bool( False ),
    TauInputTag = cms.InputTag( 'hltGtStage2Digis','Tau' ),
    BstLengthBytes = cms.int32( -1 ),
    MuonInputTag = cms.InputTag( 'hltGtStage2Digis','Muon' )
)
fragment.hltScalersRawToDigi = cms.EDProducer( "ScalersRawToDigi",
    scalersInputTag = cms.InputTag( "rawDataCollector" )
)
fragment.hltOnlineBeamSpot = cms.EDProducer( "BeamSpotOnlineProducer",
    maxZ = cms.double( 40.0 ),
    src = cms.InputTag( "hltScalersRawToDigi" ),
    gtEvmLabel = cms.InputTag( "" ),
    changeToCMSCoordinates = cms.bool( False ),
    setSigmaZ = cms.double( 0.0 ),
    maxRadius = cms.double( 2.0 )
)
fragment.hltStripTrackerHVOn = cms.EDFilter( "DetectorStateFilter",
    DcsStatusLabel = cms.untracked.InputTag( "hltScalersRawToDigi" ),
    DebugOn = cms.untracked.bool( False ),
    DetectorType = cms.untracked.string( "sistrip" )
)
fragment.hltPixelTrackerHVOn = cms.EDFilter( "DetectorStateFilter",
    DcsStatusLabel = cms.untracked.InputTag( "hltScalersRawToDigi" ),
    DebugOn = cms.untracked.bool( False ),
    DetectorType = cms.untracked.string( "pixel" )
)
fragment.hltMuonDTDigis = cms.EDProducer( "DTuROSRawToDigi",
    debug = cms.untracked.bool( False ),
    inputLabel = cms.InputTag( "rawDataCollector" )
)
fragment.hltDt1DRecHits = cms.EDProducer( "DTRecHitProducer",
    debug = cms.untracked.bool( False ),
    recAlgoConfig = cms.PSet(
      maxTime = cms.double( 420.0 ),
      debug = cms.untracked.bool( False ),
      stepTwoFromDigi = cms.bool( False ),
      tTrigModeConfig = cms.PSet(
        debug = cms.untracked.bool( False ),
        tofCorrType = cms.int32( 0 ),
        tTrigLabel = cms.string( "" ),
        wirePropCorrType = cms.int32( 0 ),
        doTOFCorrection = cms.bool( True ),
        vPropWire = cms.double( 24.4 ),
        doT0Correction = cms.bool( True ),
        doWirePropCorrection = cms.bool( True )
      ),
      useUncertDB = cms.bool( True ),
      doVdriftCorr = cms.bool( True ),
      minTime = cms.double( -3.0 ),
      tTrigMode = cms.string( "DTTTrigSyncFromDB" )
    ),
    dtDigiLabel = cms.InputTag( "hltMuonDTDigis" ),
    recAlgo = cms.string( "DTLinearDriftFromDBAlgo" )
)
fragment.hltDt4DSegments = cms.EDProducer( "DTRecSegment4DProducer",
    debug = cms.untracked.bool( False ),
    Reco4DAlgoName = cms.string( "DTCombinatorialPatternReco4D" ),
    recHits2DLabel = cms.InputTag( "dt2DSegments" ),
    recHits1DLabel = cms.InputTag( "hltDt1DRecHits" ),
    Reco4DAlgoConfig = cms.PSet(
      Reco2DAlgoConfig = cms.PSet(
        AlphaMaxPhi = cms.double( 1.0 ),
        debug = cms.untracked.bool( False ),
        segmCleanerMode = cms.int32( 2 ),
        AlphaMaxTheta = cms.double( 0.9 ),
        hit_afterT0_resolution = cms.double( 0.03 ),
        performT0_vdriftSegCorrection = cms.bool( False ),
        recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
        recAlgoConfig = cms.PSet(
          maxTime = cms.double( 420.0 ),
          debug = cms.untracked.bool( False ),
          stepTwoFromDigi = cms.bool( False ),
          tTrigModeConfig = cms.PSet(
            debug = cms.untracked.bool( False ),
            tofCorrType = cms.int32( 0 ),
            tTrigLabel = cms.string( "" ),
            wirePropCorrType = cms.int32( 0 ),
            doTOFCorrection = cms.bool( True ),
            vPropWire = cms.double( 24.4 ),
            doT0Correction = cms.bool( True ),
            doWirePropCorrection = cms.bool( True )
          ),
          useUncertDB = cms.bool( True ),
          doVdriftCorr = cms.bool( True ),
          minTime = cms.double( -3.0 ),
          tTrigMode = cms.string( "DTTTrigSyncFromDB" )
        ),
        MaxAllowedHits = cms.uint32( 50 ),
        nUnSharedHitsMin = cms.int32( 2 ),
        nSharedHitsMax = cms.int32( 2 ),
        performT0SegCorrection = cms.bool( False ),
        perform_delta_rejecting = cms.bool( False )
      ),
      Reco2DAlgoName = cms.string( "DTCombinatorialPatternReco" ),
      debug = cms.untracked.bool( False ),
      segmCleanerMode = cms.int32( 2 ),
      AllDTRecHits = cms.bool( True ),
      hit_afterT0_resolution = cms.double( 0.03 ),
      performT0_vdriftSegCorrection = cms.bool( False ),
      recAlgo = cms.string( "DTLinearDriftFromDBAlgo" ),
      recAlgoConfig = cms.PSet(
        maxTime = cms.double( 420.0 ),
        debug = cms.untracked.bool( False ),
        stepTwoFromDigi = cms.bool( False ),
        tTrigModeConfig = cms.PSet(
          debug = cms.untracked.bool( False ),
          tofCorrType = cms.int32( 0 ),
          tTrigLabel = cms.string( "" ),
          wirePropCorrType = cms.int32( 0 ),
          doTOFCorrection = cms.bool( True ),
          vPropWire = cms.double( 24.4 ),
          doT0Correction = cms.bool( True ),
          doWirePropCorrection = cms.bool( True )
        ),
        useUncertDB = cms.bool( True ),
        doVdriftCorr = cms.bool( True ),
        minTime = cms.double( -3.0 ),
        tTrigMode = cms.string( "DTTTrigSyncFromDB" )
      ),
      nUnSharedHitsMin = cms.int32( 2 ),
      nSharedHitsMax = cms.int32( 2 ),
      performT0SegCorrection = cms.bool( False ),
      perform_delta_rejecting = cms.bool( False )
    )
)
fragment.hltMuonCSCDigis = cms.EDProducer( "CSCDCCUnpacker",
    PrintEventNumber = cms.untracked.bool( False ),
    SuppressZeroLCT = cms.untracked.bool( True ),
    UseExaminer = cms.bool( True ),
    Debug = cms.untracked.bool( False ),
    ErrorMask = cms.uint32( 0 ),
    InputObjects = cms.InputTag( "rawDataCollector" ),
    ExaminerMask = cms.uint32( 535558134 ),
    runDQM = cms.untracked.bool( False ),
    UnpackStatusDigis = cms.bool( False ),
    VisualFEDInspect = cms.untracked.bool( False ),
    FormatedEventDump = cms.untracked.bool( False ),
    UseFormatStatus = cms.bool( True ),
    UseSelectiveUnpacking = cms.bool( True ),
    VisualFEDShort = cms.untracked.bool( False )
)
fragment.hltCsc2DRecHits = cms.EDProducer( "CSCRecHitDProducer",
    XTasymmetry_ME1b = cms.double( 0.0 ),
    XTasymmetry_ME1a = cms.double( 0.0 ),
    ConstSyst_ME1a = cms.double( 0.022 ),
    ConstSyst_ME41 = cms.double( 0.0 ),
    CSCWireTimeWindowHigh = cms.int32( 15 ),
    CSCStripxtalksOffset = cms.double( 0.03 ),
    CSCUseCalibrations = cms.bool( True ),
    CSCUseTimingCorrections = cms.bool( True ),
    CSCNoOfTimeBinsForDynamicPedestal = cms.int32( 2 ),
    XTasymmetry_ME22 = cms.double( 0.0 ),
    UseFivePoleFit = cms.bool( True ),
    XTasymmetry_ME21 = cms.double( 0.0 ),
    ConstSyst_ME21 = cms.double( 0.0 ),
    ConstSyst_ME12 = cms.double( 0.0 ),
    ConstSyst_ME31 = cms.double( 0.0 ),
    ConstSyst_ME22 = cms.double( 0.0 ),
    ConstSyst_ME13 = cms.double( 0.0 ),
    ConstSyst_ME32 = cms.double( 0.0 ),
    readBadChambers = cms.bool( True ),
    CSCWireTimeWindowLow = cms.int32( 0 ),
    NoiseLevel_ME13 = cms.double( 8.0 ),
    XTasymmetry_ME41 = cms.double( 0.0 ),
    NoiseLevel_ME32 = cms.double( 9.0 ),
    NoiseLevel_ME31 = cms.double( 9.0 ),
    CSCStripClusterChargeCut = cms.double( 25.0 ),
    ConstSyst_ME1b = cms.double( 0.007 ),
    CSCStripClusterSize = cms.untracked.int32( 3 ),
    CSCStripPeakThreshold = cms.double( 10.0 ),
    readBadChannels = cms.bool( False ),
    NoiseLevel_ME12 = cms.double( 9.0 ),
    UseParabolaFit = cms.bool( False ),
    CSCUseReducedWireTimeWindow = cms.bool( False ),
    XTasymmetry_ME13 = cms.double( 0.0 ),
    XTasymmetry_ME12 = cms.double( 0.0 ),
    wireDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCWireDigi' ),
    CSCDebug = cms.untracked.bool( False ),
    CSCUseGasGainCorrections = cms.bool( False ),
    XTasymmetry_ME31 = cms.double( 0.0 ),
    XTasymmetry_ME32 = cms.double( 0.0 ),
    UseAverageTime = cms.bool( False ),
    NoiseLevel_ME1a = cms.double( 7.0 ),
    NoiseLevel_ME1b = cms.double( 8.0 ),
    CSCWireClusterDeltaT = cms.int32( 1 ),
    CSCUseStaticPedestals = cms.bool( False ),
    stripDigiTag = cms.InputTag( 'hltMuonCSCDigis','MuonCSCStripDigi' ),
    CSCstripWireDeltaTime = cms.int32( 8 ),
    NoiseLevel_ME21 = cms.double( 9.0 ),
    NoiseLevel_ME22 = cms.double( 9.0 ),
    NoiseLevel_ME41 = cms.double( 9.0 )
)
fragment.hltCscSegments = cms.EDProducer( "CSCSegmentProducer",
    inputObjects = cms.InputTag( "hltCsc2DRecHits" ),
    algo_psets = cms.VPSet(
      cms.PSet(  parameters_per_chamber_type = cms.vint32( 2, 1, 1, 1, 1, 1, 1, 1, 1, 1 ),
        algo_psets = cms.VPSet(
          cms.PSet(  dYclusBoxMax = cms.double( 8.0 ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            maxRatioResidualPrune = cms.double( 3.0 ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            maxRecHitsInCluster = cms.int32( 20 ),
            useShowering = cms.bool( False ),
            BPMinImprovement = cms.double( 10000.0 ),
            curvePenalty = cms.double( 2.0 ),
            ForceCovariance = cms.bool( False ),
            yweightPenalty = cms.double( 1.5 ),
            dPhiFineMax = cms.double( 0.025 ),
            SeedBig = cms.double( 0.0015 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            Covariance = cms.double( 0.0 ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            Pruning = cms.bool( True ),
            tanPhiMax = cms.double( 0.5 ),
            onlyBestSegment = cms.bool( False ),
            dXclusBoxMax = cms.double( 4.0 ),
            maxDTheta = cms.double( 999.0 ),
            preClustering = cms.bool( True ),
            preClusteringUseChaining = cms.bool( True ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            prePrun = cms.bool( True ),
            CorrectTheErrors = cms.bool( True ),
            ForceCovarianceAll = cms.bool( False ),
            NormChi2Cut2D = cms.double( 20.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            minHitsPerSegment = cms.int32( 3 ),
            dRPhiFineMax = cms.double( 8.0 ),
            maxDPhi = cms.double( 999.0 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            BrutePruning = cms.bool( True ),
            prePrunLimit = cms.double( 3.17 )
          ),
          cms.PSet(  dYclusBoxMax = cms.double( 8.0 ),
            hitDropLimit4Hits = cms.double( 0.6 ),
            maxRatioResidualPrune = cms.double( 3.0 ),
            curvePenaltyThreshold = cms.double( 0.85 ),
            maxRecHitsInCluster = cms.int32( 24 ),
            useShowering = cms.bool( False ),
            BPMinImprovement = cms.double( 10000.0 ),
            curvePenalty = cms.double( 2.0 ),
            ForceCovariance = cms.bool( False ),
            yweightPenalty = cms.double( 1.5 ),
            dPhiFineMax = cms.double( 0.025 ),
            SeedBig = cms.double( 0.0015 ),
            NormChi2Cut3D = cms.double( 10.0 ),
            Covariance = cms.double( 0.0 ),
            CSCDebug = cms.untracked.bool( False ),
            tanThetaMax = cms.double( 1.2 ),
            Pruning = cms.bool( True ),
            tanPhiMax = cms.double( 0.5 ),
            onlyBestSegment = cms.bool( False ),
            dXclusBoxMax = cms.double( 4.0 ),
            maxDTheta = cms.double( 999.0 ),
            preClustering = cms.bool( True ),
            preClusteringUseChaining = cms.bool( True ),
            yweightPenaltyThreshold = cms.double( 1.0 ),
            hitDropLimit6Hits = cms.double( 0.3333 ),
            prePrun = cms.bool( True ),
            CorrectTheErrors = cms.bool( True ),
            ForceCovarianceAll = cms.bool( False ),
            NormChi2Cut2D = cms.double( 20.0 ),
            SeedSmall = cms.double( 2.0E-4 ),
            minHitsPerSegment = cms.int32( 3 ),
            dRPhiFineMax = cms.double( 8.0 ),
            maxDPhi = cms.double( 999.0 ),
            hitDropLimit5Hits = cms.double( 0.8 ),
            BrutePruning = cms.bool( True ),
            prePrunLimit = cms.double( 3.17 )
          )
        ),
        algo_name = cms.string( "CSCSegAlgoST" ),
        chamber_types = cms.vstring( 'ME1/a',
          'ME1/b',
          'ME1/2',
          'ME1/3',
          'ME2/1',
          'ME2/2',
          'ME3/1',
          'ME3/2',
          'ME4/1',
          'ME4/2' )
      )
    ),
    algo_type = cms.int32( 1 )
)
fragment.hltMuonRPCDigis = cms.EDProducer( "RPCUnpackingModule",
    InputLabel = cms.InputTag( "rawDataCollector" ),
    doSynchro = cms.bool( False )
)
fragment.hltRpcRecHits = cms.EDProducer( "RPCRecHitProducer",
    recAlgoConfig = cms.PSet(  ),
    deadvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCDeadVec.dat" ),
    rpcDigiLabel = cms.InputTag( "hltMuonRPCDigis" ),
    maskvecfile = cms.FileInPath( "RecoLocalMuon/RPCRecHit/data/RPCMaskVec.dat" ),
    recAlgo = cms.string( "RPCRecHitStandardAlgo" ),
    deadSource = cms.string( "File" ),
    maskSource = cms.string( "File" )
)
fragment.hltL2OfflineMuonSeeds = cms.EDProducer( "MuonSeedGenerator",
    EnableDTMeasurement = cms.bool( True ),
    EnableCSCMeasurement = cms.bool( True ),
    EnableME0Measurement = cms.bool( False ),
    SMB_21 = cms.vdouble( 1.043, -0.124, 0.0, 0.183, 0.0, 0.0 ),
    SMB_20 = cms.vdouble( 1.011, -0.052, 0.0, 0.188, 0.0, 0.0 ),
    SMB_22 = cms.vdouble( 1.474, -0.758, 0.0, 0.185, 0.0, 0.0 ),
    OL_2213 = cms.vdouble( 0.117, 0.0, 0.0, 0.044, 0.0, 0.0 ),
    SME_11 = cms.vdouble( 3.295, -1.527, 0.112, 0.378, 0.02, 0.0 ),
    SME_13 = cms.vdouble( -1.286, 1.711, 0.0, 0.356, 0.0, 0.0 ),
    SME_12 = cms.vdouble( 0.102, 0.599, 0.0, 0.38, 0.0, 0.0 ),
    DT_34_2_scale = cms.vdouble( -11.901897, 0.0 ),
    OL_1213_0_scale = cms.vdouble( -4.488158, 0.0 ),
    OL_1222_0_scale = cms.vdouble( -5.810449, 0.0 ),
    DT_13 = cms.vdouble( 0.315, 0.068, -0.127, 0.051, -0.002, 0.0 ),
    DT_12 = cms.vdouble( 0.183, 0.054, -0.087, 0.028, 0.002, 0.0 ),
    DT_14 = cms.vdouble( 0.359, 0.052, -0.107, 0.072, -0.004, 0.0 ),
    CSC_13_3_scale = cms.vdouble( -1.701268, 0.0 ),
    DT_24_2_scale = cms.vdouble( -6.63094, 0.0 ),
    CSC_23 = cms.vdouble( -0.081, 0.113, -0.029, 0.015, 0.008, 0.0 ),
    CSC_24 = cms.vdouble( 0.004, 0.021, -0.002, 0.053, 0.0, 0.0 ),
    OL_2222 = cms.vdouble( 0.107, 0.0, 0.0, 0.04, 0.0, 0.0 ),
    DT_14_2_scale = cms.vdouble( -4.808546, 0.0 ),
    SMB_10 = cms.vdouble( 1.387, -0.038, 0.0, 0.19, 0.0, 0.0 ),
    SMB_11 = cms.vdouble( 1.247, 0.72, -0.802, 0.229, -0.075, 0.0 ),
    SMB_12 = cms.vdouble( 2.128, -0.956, 0.0, 0.199, 0.0, 0.0 ),
    SME_21 = cms.vdouble( -0.529, 1.194, -0.358, 0.472, 0.086, 0.0 ),
    SME_22 = cms.vdouble( -1.207, 1.491, -0.251, 0.189, 0.243, 0.0 ),
    DT_13_2_scale = cms.vdouble( -4.257687, 0.0 ),
    CSC_34 = cms.vdouble( 0.062, -0.067, 0.019, 0.021, 0.003, 0.0 ),
    SME_22_0_scale = cms.vdouble( -3.457901, 0.0 ),
    DT_24_1_scale = cms.vdouble( -7.490909, 0.0 ),
    OL_1232_0_scale = cms.vdouble( -5.964634, 0.0 ),
    SMB_32 = cms.vdouble( 0.67, -0.327, 0.0, 0.22, 0.0, 0.0 ),
    SME_13_0_scale = cms.vdouble( 0.104905, 0.0 ),
    SMB_22_0_scale = cms.vdouble( 1.346681, 0.0 ),
    CSC_12_1_scale = cms.vdouble( -6.434242, 0.0 ),
    DT_34 = cms.vdouble( 0.044, 0.004, -0.013, 0.029, 0.003, 0.0 ),
    ME0RecSegmentLabel = cms.InputTag( "me0Segments" ),
    SME_32 = cms.vdouble( -0.901, 1.333, -0.47, 0.41, 0.073, 0.0 ),
    SME_31 = cms.vdouble( -1.594, 1.482, -0.317, 0.487, 0.097, 0.0 ),
    SMB_32_0_scale = cms.vdouble( -3.054156, 0.0 ),
    crackEtas = cms.vdouble( 0.2, 1.6, 1.7 ),
    SME_11_0_scale = cms.vdouble( 1.325085, 0.0 ),
    SMB_20_0_scale = cms.vdouble( 1.486168, 0.0 ),
    DT_13_1_scale = cms.vdouble( -4.520923, 0.0 ),
    CSC_24_1_scale = cms.vdouble( -6.055701, 0.0 ),
    CSC_01_1_scale = cms.vdouble( -1.915329, 0.0 ),
    DT_23 = cms.vdouble( 0.13, 0.023, -0.057, 0.028, 0.004, 0.0 ),
    DT_24 = cms.vdouble( 0.176, 0.014, -0.051, 0.051, 0.003, 0.0 ),
    SMB_12_0_scale = cms.vdouble( 2.283221, 0.0 ),
    deltaPhiSearchWindow = cms.double( 0.25 ),
    SMB_30_0_scale = cms.vdouble( -3.629838, 0.0 ),
    SME_42 = cms.vdouble( -0.003, 0.005, 0.005, 0.608, 0.076, 0.0 ),
    SME_41 = cms.vdouble( -0.003, 0.005, 0.005, 0.608, 0.076, 0.0 ),
    deltaEtaSearchWindow = cms.double( 0.2 ),
    CSC_12_2_scale = cms.vdouble( -1.63622, 0.0 ),
    DT_34_1_scale = cms.vdouble( -13.783765, 0.0 ),
    CSC_34_1_scale = cms.vdouble( -11.520507, 0.0 ),
    OL_2213_0_scale = cms.vdouble( -7.239789, 0.0 ),
    CSC_13_2_scale = cms.vdouble( -6.077936, 0.0 ),
    CSC_12_3_scale = cms.vdouble( -1.63622, 0.0 ),
    deltaEtaCrackSearchWindow = cms.double( 0.25 ),
    SME_21_0_scale = cms.vdouble( -0.040862, 0.0 ),
    OL_1232 = cms.vdouble( 0.184, 0.0, 0.0, 0.066, 0.0, 0.0 ),
    DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
    SMB_10_0_scale = cms.vdouble( 2.448566, 0.0 ),
    CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
    CSC_23_2_scale = cms.vdouble( -6.079917, 0.0 ),
    scaleDT = cms.bool( True ),
    DT_12_2_scale = cms.vdouble( -3.518165, 0.0 ),
    OL_1222 = cms.vdouble( 0.848, -0.591, 0.0, 0.062, 0.0, 0.0 ),
    CSC_23_1_scale = cms.vdouble( -19.084285, 0.0 ),
    OL_1213 = cms.vdouble( 0.96, -0.737, 0.0, 0.052, 0.0, 0.0 ),
    CSC_02 = cms.vdouble( 0.612, -0.207, 0.0, 0.067, -0.001, 0.0 ),
    CSC_03 = cms.vdouble( 0.787, -0.338, 0.029, 0.101, -0.008, 0.0 ),
    CSC_01 = cms.vdouble( 0.166, 0.0, 0.0, 0.031, 0.0, 0.0 ),
    DT_23_1_scale = cms.vdouble( -5.320346, 0.0 ),
    SMB_30 = cms.vdouble( 0.505, -0.022, 0.0, 0.215, 0.0, 0.0 ),
    SMB_31 = cms.vdouble( 0.549, -0.145, 0.0, 0.207, 0.0, 0.0 ),
    crackWindow = cms.double( 0.04 ),
    CSC_14_3_scale = cms.vdouble( -1.969563, 0.0 ),
    SMB_31_0_scale = cms.vdouble( -3.323768, 0.0 ),
    DT_12_1_scale = cms.vdouble( -3.692398, 0.0 ),
    SMB_21_0_scale = cms.vdouble( 1.58384, 0.0 ),
    DT_23_2_scale = cms.vdouble( -5.117625, 0.0 ),
    SME_12_0_scale = cms.vdouble( 2.279181, 0.0 ),
    DT_14_1_scale = cms.vdouble( -5.644816, 0.0 ),
    beamSpotTag = cms.InputTag( "hltOnlineBeamSpot" ),
    SMB_11_0_scale = cms.vdouble( 2.56363, 0.0 ),
    CSC_13 = cms.vdouble( 0.901, -1.302, 0.533, 0.045, 0.005, 0.0 ),
    CSC_14 = cms.vdouble( 0.606, -0.181, -0.002, 0.111, -0.003, 0.0 ),
    OL_2222_0_scale = cms.vdouble( -7.667231, 0.0 ),
    CSC_12 = cms.vdouble( -0.161, 0.254, -0.047, 0.042, -0.007, 0.0 )
)
fragment.hltL2MuonSeeds = cms.EDProducer( "L2MuonSeedGeneratorFromL1T",
    OfflineSeedLabel = cms.untracked.InputTag( "hltL2OfflineMuonSeeds" ),
    SetMinPtEndcapTo = cms.double( 1.0 ),
    SortType = cms.uint32( 0 ),
    ServiceParameters = cms.PSet(
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'SteppingHelixPropagatorAny' )
    ),
    CentralBxOnly = cms.bool( True ),
    InputObjects = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    MatchDR = cms.vdouble( 0.3 ),
    L1MaxEta = cms.double( 2.5 ),
    EtaMatchingBins = cms.vdouble( 0.0, 2.5 ),
    L1MinPt = cms.double( 0.0 ),
    L1MinQuality = cms.uint32( 7 ),
    GMTReadoutCollection = cms.InputTag( "" ),
    UseUnassociatedL1 = cms.bool( False ),
    UseOfflineSeed = cms.untracked.bool( True ),
    MatchType = cms.uint32( 0 ),
    Propagator = cms.string( "SteppingHelixPropagatorAny" ),
    SetMinPtBarrelTo = cms.double( 3.5 )
)
fragment.hltL2Muons = cms.EDProducer( "L2MuonProducer",
    ServiceParameters = cms.PSet(
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny',
        'hltESPFastSteppingHelixPropagatorOpposite' )
    ),
    InputObjects = cms.InputTag( "hltL2MuonSeeds" ),
    SeedTransformerParameters = cms.PSet(
      Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
      NMinRecHits = cms.uint32( 2 ),
      RescaleError = cms.double( 100.0 ),
      Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      UseSubRecHits = cms.bool( False ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
    ),
    L2TrajBuilderParameters = cms.PSet(
      BWFilterParameters = cms.PSet(
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        BWSeedType = cms.string( "fromGenerator" ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        EnableRPCMeasurement = cms.bool( True ),
        MuonTrajectoryUpdatorParameters = cms.PSet(
          ExcludeRPCFromFit = cms.bool( False ),
          Granularity = cms.int32( 0 ),
          MaxChi2 = cms.double( 25.0 ),
          RescaleError = cms.bool( False ),
          RescaleErrorFactor = cms.double( 100.0 ),
          UseInvalidHits = cms.bool( True )
        ),
        EnableCSCMeasurement = cms.bool( True ),
        MaxChi2 = cms.double( 100.0 ),
        FitDirection = cms.string( "outsideIn" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        NumberOfSigma = cms.double( 3.0 ),
        EnableDTMeasurement = cms.bool( True )
      ),
      DoSeedRefit = cms.bool( False ),
      FilterParameters = cms.PSet(
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        RPCRecSegmentLabel = cms.InputTag( "hltRpcRecHits" ),
        EnableRPCMeasurement = cms.bool( True ),
        MuonTrajectoryUpdatorParameters = cms.PSet(
          ExcludeRPCFromFit = cms.bool( False ),
          Granularity = cms.int32( 0 ),
          MaxChi2 = cms.double( 25.0 ),
          RescaleError = cms.bool( False ),
          RescaleErrorFactor = cms.double( 100.0 ),
          UseInvalidHits = cms.bool( True )
        ),
        EnableCSCMeasurement = cms.bool( True ),
        MaxChi2 = cms.double( 1000.0 ),
        FitDirection = cms.string( "insideOut" ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        NumberOfSigma = cms.double( 3.0 ),
        EnableDTMeasurement = cms.bool( True )
      ),
      SeedPosition = cms.string( "in" ),
      DoBackwardFilter = cms.bool( True ),
      DoRefit = cms.bool( False ),
      NavigationType = cms.string( "Standard" ),
      SeedTransformerParameters = cms.PSet(
        Fitter = cms.string( "hltESPKFFittingSmootherForL2Muon" ),
        NMinRecHits = cms.uint32( 2 ),
        RescaleError = cms.double( 100.0 ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
        UseSubRecHits = cms.bool( False ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
      ),
      SeedPropagator = cms.string( "hltESPFastSteppingHelixPropagatorAny" )
    ),
    DoSeedRefit = cms.bool( False ),
    TrackLoaderParameters = cms.PSet(
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      DoSmoothing = cms.bool( False ),
      VertexConstraint = cms.bool( True ),
      MuonUpdatorAtVertexParameters = cms.PSet(
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 ),
        BeamSpotPosition = cms.vdouble( 0.0, 0.0, 0.0 ),
        Propagator = cms.string( "hltESPFastSteppingHelixPropagatorOpposite" )
      ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
    ),
    MuonTrajectoryBuilder = cms.string( "Exhaustive" )
)
fragment.hltL2MuonCandidates = cms.EDProducer( "L2MuonCandidateProducer",
    InputObjects = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
fragment.hltSiPixelDigis = cms.EDProducer( "SiPixelRawToDigi",
    UseQualityInfo = cms.bool( False ),
    UsePilotBlade = cms.bool( False ),
    UsePhase1 = cms.bool( True ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    IncludeErrors = cms.bool( True ),
    ErrorList = cms.vint32( 29 ),
    Regions = cms.PSet(  ),
    Timing = cms.untracked.bool( False ),
    CablingMapLabel = cms.string( "" ),
    UserErrorList = cms.vint32(  )
)
fragment.hltSiPixelClusters = cms.EDProducer( "SiPixelClusterProducer",
    src = cms.InputTag( "hltSiPixelDigis" ),
    ChannelThreshold = cms.int32( 1000 ),
    Phase2DigiBaseline = cms.double( 1200.0 ),
    ElectronPerADCGain = cms.double( 135.0 ),
    Phase2ReadoutMode = cms.int32( -1 ),
    maxNumberOfClusters = cms.int32( 40000 ),
    ClusterThreshold_L1 = cms.int32( 2000 ),
    MissCalibrate = cms.bool( True ),
    VCaltoElectronGain = cms.int32( 47 ),
    VCaltoElectronGain_L1 = cms.int32( 50 ),
    VCaltoElectronOffset = cms.int32( -60 ),
    SplitClusters = cms.bool( False ),
    payloadType = cms.string( "HLT" ),
    Phase2Calibration = cms.bool( False ),
    Phase2KinkADC = cms.int32( 8 ),
    ClusterMode = cms.string( "PixelThresholdClusterizer" ),
    SeedThreshold = cms.int32( 1000 ),
    VCaltoElectronOffset_L1 = cms.int32( -670 ),
    ClusterThreshold = cms.int32( 4000 )
)
fragment.hltSiPixelClustersCache = cms.EDProducer( "SiPixelClusterShapeCacheProducer",
    src = cms.InputTag( "hltSiPixelClusters" ),
    onDemand = cms.bool( False )
)
fragment.hltSiPixelRecHits = cms.EDProducer( "SiPixelRecHitConverter",
    VerboseLevel = cms.untracked.int32( 0 ),
    src = cms.InputTag( "hltSiPixelClusters" ),
    CPE = cms.string( "hltESPPixelCPEGeneric" )
)
fragment.hltSiStripExcludedFEDListProducer = cms.EDProducer( "SiStripExcludedFEDListProducer",
    ProductLabel = cms.InputTag( "rawDataCollector" )
)
fragment.hltSiStripRawToClustersFacility = cms.EDProducer( "SiStripClusterizerFromRaw",
    ProductLabel = cms.InputTag( "rawDataCollector" ),
    Clusterizer = cms.PSet(
      QualityLabel = cms.string( "" ),
      ClusterThreshold = cms.double( 5.0 ),
      SeedThreshold = cms.double( 3.0 ),
      Algorithm = cms.string( "ThreeThresholdAlgorithm" ),
      ChannelThreshold = cms.double( 2.0 ),
      MaxAdjacentBad = cms.uint32( 0 ),
      setDetId = cms.bool( True ),
      MaxSequentialHoles = cms.uint32( 0 ),
      RemoveApvShots = cms.bool( True ),
      clusterChargeCut = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
      MaxSequentialBad = cms.uint32( 1 )
    ),
    onDemand = cms.bool( True ),
    HybridZeroSuppressed = cms.bool( False ),
    Algorithms = cms.PSet(
      CommonModeNoiseSubtractionMode = cms.string( "Median" ),
      useCMMeanMap = cms.bool( False ),
      TruncateInSuppressor = cms.bool( True ),
      doAPVRestore = cms.bool( False ),
      SiStripFedZeroSuppressionMode = cms.uint32( 4 ),
      PedestalSubtractionFedMode = cms.bool( True ),
      Use10bitsTruncation = cms.bool( False )
    ),
    DoAPVEmulatorCheck = cms.bool( False )
)
fragment.hltSiStripClusters = cms.EDProducer( "MeasurementTrackerEventProducer",
    inactivePixelDetectorLabels = cms.VInputTag( 'hltSiPixelDigis' ),
    Phase2TrackerCluster1DProducer = cms.string( "" ),
    measurementTracker = cms.string( "hltESPMeasurementTracker" ),
    pixelClusterProducer = cms.string( "hltSiPixelClusters" ),
    switchOffPixelsIfEmpty = cms.bool( True ),
    badPixelFEDChannelCollectionLabels = cms.VInputTag( 'hltSiPixelDigis' ),
    inactiveStripDetectorLabels = cms.VInputTag( 'hltSiStripExcludedFEDListProducer' ),
    skipClusters = cms.InputTag( "" ),
    pixelCablingMapLabel = cms.string( "" ),
    stripClusterProducer = cms.string( "hltSiStripRawToClustersFacility" )
)
fragment.hltIterL3OISeedsFromL2Muons = cms.EDProducer( "TSGForOIFromL2",
    hitsToTry = cms.int32( 1 ),
    tsosDiff2 = cms.double( 0.02 ),
    adjustErrorsDynamicallyForHitless = cms.bool( True ),
    SF6 = cms.double( 2.0 ),
    SF4 = cms.double( 7.0 ),
    SF5 = cms.double( 10.0 ),
    propagatorName = cms.string( "PropagatorWithMaterialParabolicMf" ),
    SF3 = cms.double( 5.0 ),
    SF1 = cms.double( 3.0 ),
    minEtaForTEC = cms.double( 0.7 ),
    fixedErrorRescaleFactorForHits = cms.double( 1.0 ),
    maxSeeds = cms.uint32( 20 ),
    maxEtaForTOB = cms.double( 1.8 ),
    pT3 = cms.double( 70.0 ),
    pT2 = cms.double( 30.0 ),
    pT1 = cms.double( 13.0 ),
    layersToTry = cms.int32( 2 ),
    fixedErrorRescaleFactorForHitless = cms.double( 2.0 ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    SF2 = cms.double( 4.0 ),
    numL2ValidHitsCutAllEta = cms.uint32( 20 ),
    adjustErrorsDynamicallyForHits = cms.bool( False ),
    eta4 = cms.double( 1.2 ),
    src = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
    eta6 = cms.double( 1.4 ),
    eta7 = cms.double( 2.1 ),
    eta1 = cms.double( 0.2 ),
    eta2 = cms.double( 0.3 ),
    eta3 = cms.double( 1.0 ),
    UseHitLessSeeds = cms.bool( True ),
    estimator = cms.string( "hltESPChi2MeasurementEstimator100" ),
    numL2ValidHitsCutAllEndcap = cms.uint32( 30 ),
    debug = cms.untracked.bool( False ),
    maxHitSeeds = cms.uint32( 1 ),
    eta5 = cms.double( 1.6 ),
    tsosDiff1 = cms.double( 0.2 ),
    maxHitlessSeeds = cms.uint32( 5 )
)
fragment.hltIterL3OITrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIterL3OISeedsFromL2Muons" ),
    maxSeedsBeforeCleaning = cms.uint32( 5000 ),
    SimpleMagneticField = cms.string( "" ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterial" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialOpposite" )
    ),
    TrajectoryCleaner = cms.string( "muonSeededTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( True ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 500000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryBuilder" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "CkfTrajectoryBuilder" )
)
fragment.hltIterL3OIMuCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIterL3OITrackCandidates" ),
    SimpleMagneticField = cms.string( "" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    Fitter = cms.string( "hltESPKFFittingSmootherWithOutliersRejectionAndRK" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "hltESPMeasurementTracker" ),
    AlgorithmName = cms.string( "iter10" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( False ),
    Propagator = cms.string( "PropagatorWithMaterial" )
)
fragment.hltIterL3OIMuonTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIterL3OIMuCtfWithMaterialTracks" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "Notused" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet(
      minPixelHits = cms.vint32( 0, 0, 1 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 100.0 ),
      dr_par = cms.PSet(
        d0err = cms.vdouble( 0.003, 0.003, 3.40282346639E38 ),
        dr_par2 = cms.vdouble( 0.3, 0.3, 3.40282346639E38 ),
        dr_par1 = cms.vdouble( 0.4, 0.4, 3.40282346639E38 ),
        dr_exp = cms.vint32( 4, 4, 2147483647 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 3.40282346639E38 )
      ),
      maxLostLayers = cms.vint32( 4, 3, 2 ),
      min3DLayers = cms.vint32( 1, 2, 1 ),
      dz_par = cms.PSet(
        dz_par1 = cms.vdouble( 0.4, 0.4, 3.40282346639E38 ),
        dz_par2 = cms.vdouble( 0.35, 0.35, 3.40282346639E38 ),
        dz_exp = cms.vint32( 4, 4, 2147483647 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 3.40282346639E38 ),
      maxChi2n = cms.vdouble( 10.0, 1.0, 0.4 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 5, 5 )
    ),
    ignoreVertices = cms.bool( True )
)
fragment.hltIterL3OIMuonTrackSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltIterL3OIMuCtfWithMaterialTracks" ),
    originalQualVals = cms.InputTag( 'hltIterL3OIMuonTrackCutClassifier','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltIterL3OIMuonTrackCutClassifier','MVAValues' )
)
fragment.hltL3MuonsIterL3OI = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet(
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' )
    ),
    L3TrajBuilderParameters = cms.PSet(
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      GlobalMuonTrackMatcher = cms.PSet(
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_2 = cms.double( 15.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        Quality_3 = cms.double( 7.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        Quality_1 = cms.double( 20.0 ),
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        LocChi2Cut = cms.double( 0.001 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        MinPt = cms.double( 1.0 ),
        MinP = cms.double( 2.5 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      tkTrajUseVertex = cms.bool( False ),
      MuonTrackingRegionBuilder = cms.PSet(
        Rescale_Dz = cms.double( 4.0 ),
        Pt_fixed = cms.bool( False ),
        Eta_fixed = cms.bool( True ),
        Eta_min = cms.double( 0.1 ),
        DeltaZ = cms.double( 24.2 ),
        maxRegions = cms.int32( 2 ),
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        UseVertex = cms.bool( False ),
        Z_fixed = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Rescale_phi = cms.double( 3.0 ),
        DeltaEta = cms.double( 0.2 ),
        precise = cms.bool( True ),
        OnDemand = cms.int32( -1 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        MeasurementTrackerName = cms.InputTag( "hltESPMeasurementTracker" ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Pt_min = cms.double( 3.0 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        Phi_fixed = cms.bool( True ),
        DeltaR = cms.double( 0.025 ),
        input = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
        DeltaPhi = cms.double( 0.15 ),
        Phi_min = cms.double( 0.1 ),
        Rescale_eta = cms.double( 3.0 )
      ),
      TrackTransformer = cms.PSet(
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
      ),
      tkTrajBeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      RefitRPCHits = cms.bool( True ),
      tkTrajVertex = cms.InputTag( "Notused" ),
      GlbRefitterParameters = cms.PSet(
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        RefitFlag = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        PropDirForCosmics = cms.bool( False ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        HitThreshold = cms.int32( 1 ),
        DYTthrs = cms.vint32( 30, 15 ),
        TrackerSkipSystem = cms.int32( -1 ),
        RefitDirection = cms.string( "insideOut" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        TrackerSkipSection = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonHitsOption = cms.int32( 1 ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
      ),
      PCut = cms.double( 2.5 ),
      tkTrajMaxDXYBeamSpot = cms.double( 9999.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      tkTrajMaxChi2 = cms.double( 9999.0 ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      ScaleTECyFactor = cms.double( -1.0 ),
      tkTrajLabel = cms.InputTag( "hltIterL3OIMuonTrackSelectionHighPurity" )
    ),
    TrackLoaderParameters = cms.PSet(
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      DoSmoothing = cms.bool( True ),
      SmoothTkTrack = cms.untracked.bool( False ),
      VertexConstraint = cms.bool( False ),
      MuonUpdatorAtVertexParameters = cms.PSet(
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" )
      ),
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
fragment.hltIterL3OIL3MuonsLinksCombination = cms.EDProducer( "L3TrackLinksCombiner",
    labels = cms.VInputTag( 'hltL3MuonsIterL3OI' )
)
fragment.hltIterL3OIL3Muons = cms.EDProducer( "L3TrackCombiner",
    labels = cms.VInputTag( 'hltL3MuonsIterL3OI' )
)
fragment.hltIterL3OIL3MuonCandidates = cms.EDProducer( "L3MuonCandidateProducer",
    InputLinksObjects = cms.InputTag( "hltIterL3OIL3MuonsLinksCombination" ),
    InputObjects = cms.InputTag( "hltIterL3OIL3Muons" ),
    MuonPtOption = cms.string( "Tracker" )
)
fragment.hltL2SelectorForL3IO = cms.EDProducer( "HLTMuonL2SelectorForL3IO",
    MaxNormalizedChi2 = cms.double( 20.0 ),
    MinNmuonHits = cms.int32( 1 ),
    MinNhits = cms.int32( 1 ),
    applyL3Filters = cms.bool( False ),
    MaxPtDifference = cms.double( 0.3 ),
    l3OISrc = cms.InputTag( "hltIterL3OIL3MuonCandidates" ),
    InputLinks = cms.InputTag( "hltIterL3OIL3MuonsLinksCombination" ),
    l2Src = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
fragment.hltIterL3MuonPixelTracksFilter = cms.EDProducer( "PixelTrackFilterByKinematicsProducer",
    chi2 = cms.double( 1000.0 ),
    nSigmaTipMaxTolerance = cms.double( 0.0 ),
    ptMin = cms.double( 0.1 ),
    nSigmaInvPtTolerance = cms.double( 0.0 ),
    tipMax = cms.double( 1.0 )
)
fragment.hltIterL3MuonPixelTracksFitter = cms.EDProducer( "PixelFitterByHelixProjectionsProducer",
    scaleErrorsForBPix1 = cms.bool( False ),
    scaleFactor = cms.double( 0.65 )
)
fragment.hltIterL3MuonPixelTracksTrackingRegions = cms.EDProducer( "MuonTrackingRegionEDProducer",
    precise = cms.bool( True ),
    Eta_fixed = cms.bool( True ),
    Eta_min = cms.double( 0.0 ),
    Z_fixed = cms.bool( True ),
    MeasurementTrackerName = cms.InputTag( "" ),
    maxRegions = cms.int32( 5 ),
    Pt_min = cms.double( 2.0 ),
    Rescale_Dz = cms.double( 4.0 ),
    PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
    PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
    vertexCollection = cms.InputTag( "notUsed" ),
    Phi_fixed = cms.bool( True ),
    input = cms.InputTag( "hltL2SelectorForL3IO" ),
    DeltaR = cms.double( 0.025 ),
    OnDemand = cms.int32( -1 ),
    DeltaZ = cms.double( 24.2 ),
    Rescale_phi = cms.double( 3.0 ),
    Rescale_eta = cms.double( 3.0 ),
    DeltaEta = cms.double( 0.2 ),
    Phi_min = cms.double( 0.0 ),
    DeltaPhi = cms.double( 0.15 ),
    UseVertex = cms.bool( False ),
    EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
    EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    Pt_fixed = cms.bool( True )
)
fragment.hltIterL3MuonPixelLayerQuadruplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3+BPix4',
      'BPix1+BPix2+BPix3+FPix1_pos',
      'BPix1+BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos+FPix2_pos',
      'BPix1+BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_neg+FPix2_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  )
)
fragment.hltIterL3MuonPixelTracksHitDoublets = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltIterL3MuonPixelTracksTrackingRegions" ),
    layerPairs = cms.vuint32( 0, 1, 2 ),
    clusterCheck = cms.InputTag( "" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElementTotal = cms.uint32( 50000000 ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltIterL3MuonPixelLayerQuadruplets" )
)
fragment.hltIterL3MuonPixelTracksHitQuadruplets = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAThetaCut = cms.double( 0.005 ),
    SeedComparitorPSet = cms.PSet(
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCache" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltIterL3MuonPixelTracksHitDoublets" ),
    fitFastCircle = cms.bool( True ),
    CAHardPtCut = cms.double( 0.0 ),
    maxChi2 = cms.PSet(
      value2 = cms.double( 50.0 ),
      value1 = cms.double( 200.0 ),
      pt1 = cms.double( 0.7 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 2.0 )
    ),
    CAPhiCut = cms.double( 0.2 ),
    useBendingCorrection = cms.bool( True ),
    fitFastCircleChi2Cut = cms.bool( True )
)
fragment.hltIterL3MuonPixelTracks = cms.EDProducer( "PixelTrackProducer",
    Filter = cms.InputTag( "hltIterL3MuonPixelTracksFilter" ),
    Cleaner = cms.string( "hltPixelTracksCleanerBySharedHits" ),
    passLabel = cms.string( "" ),
    Fitter = cms.InputTag( "hltIterL3MuonPixelTracksFitter" ),
    SeedingHitSets = cms.InputTag( "hltIterL3MuonPixelTracksHitQuadruplets" )
)
fragment.hltIterL3MuonPixelVertices = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltIterL3MuonPixelTracks" ),
    PtMin = cms.double( 1.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 5.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.05 )
)
fragment.hltIterL3MuonTrimmedPixelVertices = cms.EDProducer( "PixelVertexCollectionTrimmer",
    minSumPt2 = cms.double( 0.0 ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) ),
    maxVtx = cms.uint32( 100 ),
    fractionSumPt2 = cms.double( 0.3 ),
    src = cms.InputTag( "hltIterL3MuonPixelVertices" )
)
fragment.hltIter0IterL3MuonPixelSeedsFromPixelTracks = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 0.3 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( False ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromProtoTracks" ) ),
    InputVertexCollection = cms.InputTag( "hltIterL3MuonTrimmedPixelVertices" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    InputCollection = cms.InputTag( "hltIterL3MuonPixelTracks" ),
    originRadius = cms.double( 0.1 )
)
fragment.hltIter0IterL3MuonCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter0IterL3MuonPixelSeedsFromPixelTracks" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "none" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter0IterL3MuonPSetGroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "GroupedCkfTrajectoryBuilder" )
)
fragment.hltIter0IterL3MuonCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter0IterL3MuonCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter0" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
fragment.hltIter0IterL3MuonTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter0IterL3MuonCtfWithMaterialTracks" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltIterL3MuonTrimmedPixelVertices" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet(
      minPixelHits = cms.vint32( 0, 3, 4 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 100.0 ),
      dr_par = cms.PSet(
        d0err = cms.vdouble( 0.003, 0.003, 3.40282346639E38 ),
        dr_par2 = cms.vdouble( 0.3, 0.3, 3.40282346639E38 ),
        dr_par1 = cms.vdouble( 0.4, 0.4, 3.40282346639E38 ),
        dr_exp = cms.vint32( 4, 4, 2147483647 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 3.40282346639E38 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 3, 4 ),
      dz_par = cms.PSet(
        dz_par1 = cms.vdouble( 0.4, 0.4, 3.40282346639E38 ),
        dz_par2 = cms.vdouble( 0.35, 0.35, 3.40282346639E38 ),
        dz_exp = cms.vint32( 4, 4, 2147483647 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 3.40282346639E38 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 4 )
    ),
    ignoreVertices = cms.bool( False )
)
fragment.hltIter0IterL3MuonTrackSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltIter0IterL3MuonCtfWithMaterialTracks" ),
    originalQualVals = cms.InputTag( 'hltIter0IterL3MuonTrackCutClassifier','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltIter0IterL3MuonTrackCutClassifier','MVAValues' )
)
fragment.hltIter2IterL3MuonClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 16.0 ),
    trajectories = cms.InputTag( "hltIter0IterL3MuonTrackSelectionHighPurity" ),
    oldClusterRemovalInfo = cms.InputTag( "" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClusters" ),
    TrackQuality = cms.string( "highPurity" )
)
fragment.hltIter2IterL3MuonMaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter2IterL3MuonClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClusters" )
)
fragment.hltIter2IterL3MuonPixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix2+BPix3+BPix4',
      'BPix1+BPix3+BPix4',
      'BPix1+BPix2+BPix4',
      'BPix2+BPix3+FPix1_pos',
      'BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix2+FPix1_pos+FPix2_pos',
      'BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix2_pos+FPix3_pos',
      'FPix1_neg+FPix2_neg+FPix3_neg',
      'BPix1+BPix3+FPix1_pos',
      'BPix1+BPix2+FPix2_pos',
      'BPix1+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix2_neg',
      'BPix1+FPix2_neg+FPix3_neg',
      'BPix1+FPix1_neg+FPix3_neg',
      'BPix1+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_pos+FPix3_pos' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter2IterL3MuonClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter2IterL3MuonClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  )
)
fragment.hltIter2IterL3MuonPixelClusterCheck = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" )
)
fragment.hltIter2IterL3MuonPixelHitDoublets = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltIterL3MuonPixelTracksTrackingRegions" ),
    layerPairs = cms.vuint32( 0, 1 ),
    clusterCheck = cms.InputTag( "hltIter2IterL3MuonPixelClusterCheck" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElementTotal = cms.uint32( 50000000 ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltIter2IterL3MuonPixelLayerTriplets" )
)
fragment.hltIter2IterL3MuonPixelHitTriplets = cms.EDProducer( "CAHitTripletEDProducer",
    CAHardPtCut = cms.double( 0.3 ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltIter2IterL3MuonPixelHitDoublets" ),
    CAThetaCut = cms.double( 0.015 ),
    maxChi2 = cms.PSet(
      value2 = cms.double( 6.0 ),
      value1 = cms.double( 100.0 ),
      pt1 = cms.double( 0.8 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 8.0 )
    ),
    CAPhiCut = cms.double( 0.1 ),
    useBendingCorrection = cms.bool( True )
)
fragment.hltIter2IterL3MuonPixelSeeds = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltIter2IterL3MuonPixelHitTriplets" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
fragment.hltIter2IterL3MuonCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter2IterL3MuonPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2IterL3MuonMaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2IterL3MuonPSetGroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
fragment.hltIter2IterL3MuonCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter2IterL3MuonCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2IterL3MuonMaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter2" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
fragment.hltIter2IterL3MuonTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter2IterL3MuonCtfWithMaterialTracks" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltIterL3MuonTrimmedPixelVertices" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet(
      minPixelHits = cms.vint32( 0, 0, 0 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 100.0 ),
      dr_par = cms.PSet(
        d0err = cms.vdouble( 0.003, 0.003, 3.40282346639E38 ),
        dr_par2 = cms.vdouble( 3.40282346639E38, 0.3, 3.40282346639E38 ),
        dr_par1 = cms.vdouble( 3.40282346639E38, 0.4, 3.40282346639E38 ),
        dr_exp = cms.vint32( 4, 4, 2147483647 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 3.40282346639E38 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 0, 0 ),
      dz_par = cms.PSet(
        dz_par1 = cms.vdouble( 3.40282346639E38, 0.4, 3.40282346639E38 ),
        dz_par2 = cms.vdouble( 3.40282346639E38, 0.35, 3.40282346639E38 ),
        dz_exp = cms.vint32( 4, 4, 2147483647 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 3.40282346639E38 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 3 )
    ),
    ignoreVertices = cms.bool( False )
)
fragment.hltIter2IterL3MuonTrackSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltIter2IterL3MuonCtfWithMaterialTracks" ),
    originalQualVals = cms.InputTag( 'hltIter2IterL3MuonTrackCutClassifier','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltIter2IterL3MuonTrackCutClassifier','MVAValues' )
)
fragment.hltIter2IterL3MuonMerged = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter0IterL3MuonTrackSelectionHighPurity','hltIter2IterL3MuonTrackSelectionHighPurity' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet(
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter0IterL3MuonTrackSelectionHighPurity','hltIter2IterL3MuonTrackSelectionHighPurity' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltIter3IterL3MuonClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 16.0 ),
    trajectories = cms.InputTag( "hltIter2IterL3MuonTrackSelectionHighPurity" ),
    oldClusterRemovalInfo = cms.InputTag( "hltIter2IterL3MuonClustersRefRemoval" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClusters" ),
    TrackQuality = cms.string( "highPurity" )
)
fragment.hltIter3IterL3MuonMaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter3IterL3MuonClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClusters" )
)
fragment.hltIter3IterL3MuonPixelLayerPairs = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix1+BPix4',
      'BPix2+BPix3',
      'BPix2+BPix4',
      'BPix3+BPix4',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix1+FPix3_pos',
      'BPix1+FPix3_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'BPix3+FPix1_pos',
      'BPix3+FPix1_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix3_pos',
      'FPix1_neg+FPix3_neg',
      'FPix2_pos+FPix3_pos',
      'FPix2_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter3IterL3MuonClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter3IterL3MuonClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  )
)
fragment.hltIter3IterL3MuonL2Candidates = cms.EDProducer( "ConcreteChargedCandidateProducer",
    src = cms.InputTag( "hltL2SelectorForL3IO" ),
    particleType = cms.string( "mu+" )
)
fragment.hltIter3IterL3MuonTrackingRegions = cms.EDProducer( "CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet(
      vertexCollection = cms.InputTag( "notUsed" ),
      zErrorVetex = cms.double( 0.2 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorBeamSpot = cms.double( 24.2 ),
      maxNVertices = cms.int32( 1 ),
      maxNRegions = cms.int32( 2 ),
      nSigmaZVertex = cms.double( 3.0 ),
      nSigmaZBeamSpot = cms.double( 4.0 ),
      ptMin = cms.double( 2.0 ),
      mode = cms.string( "BeamSpotSigma" ),
      input = cms.InputTag( "hltIter3IterL3MuonL2Candidates" ),
      searchOpt = cms.bool( False ),
      whereToUseMeasurementTracker = cms.string( "Never" ),
      originRadius = cms.double( 0.015 ),
      measurementTrackerName = cms.InputTag( "" ),
      precise = cms.bool( True ),
      deltaEta = cms.double( 0.1 ),
      deltaPhi = cms.double( 0.1 )
    )
)
fragment.hltIter3IterL3MuonPixelClusterCheck = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" )
)
fragment.hltIter3IterL3MuonPixelHitDoublets = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltIter3IterL3MuonTrackingRegions" ),
    layerPairs = cms.vuint32( 0 ),
    clusterCheck = cms.InputTag( "hltIter3IterL3MuonPixelClusterCheck" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( False ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElementTotal = cms.uint32( 50000000 ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltIter3IterL3MuonPixelLayerPairs" )
)
fragment.hltIter3IterL3MuonPixelSeeds = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltIter3IterL3MuonPixelHitDoublets" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
fragment.hltIter3IterL3MuonCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter3IterL3MuonPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter3IterL3MuonMaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2IterL3MuonPSetGroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
fragment.hltIter3IterL3MuonCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter3IterL3MuonCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter3IterL3MuonMaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter3" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
fragment.hltIter3IterL3MuonTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter3IterL3MuonCtfWithMaterialTracks" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltIterL3MuonTrimmedPixelVertices" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet(
      minPixelHits = cms.vint32( 0, 0, 0 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 100.0 ),
      dr_par = cms.PSet(
        d0err = cms.vdouble( 0.003, 0.003, 3.40282346639E38 ),
        dr_par2 = cms.vdouble( 3.40282346639E38, 0.3, 3.40282346639E38 ),
        dr_par1 = cms.vdouble( 3.40282346639E38, 0.4, 3.40282346639E38 ),
        dr_exp = cms.vint32( 4, 4, 2147483647 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 3.40282346639E38 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 0, 0 ),
      dz_par = cms.PSet(
        dz_par1 = cms.vdouble( 3.40282346639E38, 0.4, 3.40282346639E38 ),
        dz_par2 = cms.vdouble( 3.40282346639E38, 0.35, 3.40282346639E38 ),
        dz_exp = cms.vint32( 4, 4, 2147483647 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 3.40282346639E38 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 3 )
    ),
    ignoreVertices = cms.bool( False )
)
fragment.hltIter3IterL3MuonTrackSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltIter3IterL3MuonCtfWithMaterialTracks" ),
    originalQualVals = cms.InputTag( 'hltIter3IterL3MuonTrackCutClassifier','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltIter3IterL3MuonTrackCutClassifier','MVAValues' )
)
fragment.hltIter3IterL3MuonMerged = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter2IterL3MuonMerged','hltIter3IterL3MuonTrackSelectionHighPurity' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet(
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter2IterL3MuonMerged','hltIter3IterL3MuonTrackSelectionHighPurity' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltL3MuonsIterL3IO = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet(
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' )
    ),
    L3TrajBuilderParameters = cms.PSet(
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      GlobalMuonTrackMatcher = cms.PSet(
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_2 = cms.double( 15.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        Quality_3 = cms.double( 7.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        Quality_1 = cms.double( 20.0 ),
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        LocChi2Cut = cms.double( 0.001 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        MinPt = cms.double( 1.0 ),
        MinP = cms.double( 2.5 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      tkTrajUseVertex = cms.bool( False ),
      MuonTrackingRegionBuilder = cms.PSet(
        Rescale_Dz = cms.double( 4.0 ),
        Pt_fixed = cms.bool( True ),
        Eta_fixed = cms.bool( True ),
        Eta_min = cms.double( 0.1 ),
        DeltaZ = cms.double( 24.2 ),
        maxRegions = cms.int32( 2 ),
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        UseVertex = cms.bool( False ),
        Z_fixed = cms.bool( True ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Rescale_phi = cms.double( 3.0 ),
        DeltaEta = cms.double( 0.04 ),
        precise = cms.bool( True ),
        OnDemand = cms.int32( -1 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        MeasurementTrackerName = cms.InputTag( "hltESPMeasurementTracker" ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Pt_min = cms.double( 3.0 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        Phi_fixed = cms.bool( True ),
        DeltaR = cms.double( 0.025 ),
        input = cms.InputTag( "hltL2SelectorForL3IO" ),
        DeltaPhi = cms.double( 0.15 ),
        Phi_min = cms.double( 0.1 ),
        Rescale_eta = cms.double( 3.0 )
      ),
      TrackTransformer = cms.PSet(
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
      ),
      tkTrajBeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      RefitRPCHits = cms.bool( True ),
      tkTrajVertex = cms.InputTag( "hltIterL3MuonPixelVertices" ),
      GlbRefitterParameters = cms.PSet(
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        RefitFlag = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        PropDirForCosmics = cms.bool( False ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        HitThreshold = cms.int32( 1 ),
        DYTthrs = cms.vint32( 30, 15 ),
        TrackerSkipSystem = cms.int32( -1 ),
        RefitDirection = cms.string( "insideOut" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        TrackerSkipSection = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonHitsOption = cms.int32( 1 ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
      ),
      PCut = cms.double( 2.5 ),
      tkTrajMaxDXYBeamSpot = cms.double( 9999.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      matchToSeeds = cms.bool( True ),
      tkTrajMaxChi2 = cms.double( 9999.0 ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      ScaleTECyFactor = cms.double( -1.0 ),
      tkTrajLabel = cms.InputTag( "hltIter3IterL3MuonMerged" )
    ),
    TrackLoaderParameters = cms.PSet(
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      DoSmoothing = cms.bool( False ),
      SmoothTkTrack = cms.untracked.bool( False ),
      VertexConstraint = cms.bool( False ),
      MuonUpdatorAtVertexParameters = cms.PSet(
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" )
      ),
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
fragment.hltIterL3MuonsFromL2LinksCombination = cms.EDProducer( "L3TrackLinksCombiner",
    labels = cms.VInputTag( 'hltL3MuonsIterL3OI','hltL3MuonsIterL3IO' )
)
fragment.hltL1MuonsPt0 = cms.EDProducer( "HLTL1TMuonSelector",
    L1MinPt = cms.double( -1.0 ),
    CentralBxOnly = cms.bool( True ),
    InputObjects = cms.InputTag( 'hltGtStage2Digis','Muon' ),
    L1MinQuality = cms.uint32( 7 ),
    L1MaxEta = cms.double( 5.0 )
)
fragment.hltIterL3FromL1MuonPixelTracksTrackingRegions = cms.EDProducer( "CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet(
      vertexCollection = cms.InputTag( "notUsed" ),
      zErrorVetex = cms.double( 0.2 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorBeamSpot = cms.double( 24.2 ),
      maxNVertices = cms.int32( 1 ),
      maxNRegions = cms.int32( 2 ),
      nSigmaZVertex = cms.double( 3.0 ),
      nSigmaZBeamSpot = cms.double( 4.0 ),
      ptMin = cms.double( 10.0 ),
      mode = cms.string( "BeamSpotSigma" ),
      input = cms.InputTag( "hltL1MuonsPt0" ),
      searchOpt = cms.bool( False ),
      whereToUseMeasurementTracker = cms.string( "Never" ),
      originRadius = cms.double( 0.2 ),
      measurementTrackerName = cms.InputTag( "" ),
      precise = cms.bool( True ),
      deltaEta = cms.double( 0.35 ),
      deltaPhi = cms.double( 0.2 )
    )
)
fragment.hltIterL3FromL1MuonPixelLayerQuadruplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3+BPix4',
      'BPix1+BPix2+BPix3+FPix1_pos',
      'BPix1+BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos+FPix2_pos',
      'BPix1+BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_neg+FPix2_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  )
)
fragment.hltIterL3FromL1MuonPixelTracksHitDoublets = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltIterL3FromL1MuonPixelTracksTrackingRegions" ),
    layerPairs = cms.vuint32( 0, 1, 2 ),
    clusterCheck = cms.InputTag( "" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElementTotal = cms.uint32( 50000000 ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltIterL3FromL1MuonPixelLayerQuadruplets" )
)
fragment.hltIterL3FromL1MuonPixelTracksHitQuadruplets = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAThetaCut = cms.double( 0.005 ),
    SeedComparitorPSet = cms.PSet(
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCache" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltIterL3FromL1MuonPixelTracksHitDoublets" ),
    fitFastCircle = cms.bool( True ),
    CAHardPtCut = cms.double( 0.0 ),
    maxChi2 = cms.PSet(
      value2 = cms.double( 50.0 ),
      value1 = cms.double( 200.0 ),
      pt1 = cms.double( 0.7 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 2.0 )
    ),
    CAPhiCut = cms.double( 0.2 ),
    useBendingCorrection = cms.bool( True ),
    fitFastCircleChi2Cut = cms.bool( True )
)
fragment.hltIterL3FromL1MuonPixelTracks = cms.EDProducer( "PixelTrackProducer",
    Filter = cms.InputTag( "hltIterL3MuonPixelTracksFilter" ),
    Cleaner = cms.string( "hltPixelTracksCleanerBySharedHits" ),
    passLabel = cms.string( "" ),
    Fitter = cms.InputTag( "hltIterL3MuonPixelTracksFitter" ),
    SeedingHitSets = cms.InputTag( "hltIterL3FromL1MuonPixelTracksHitQuadruplets" )
)
fragment.hltIterL3FromL1MuonPixelVertices = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltIterL3MuonPixelTracks" ),
    PtMin = cms.double( 1.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 5.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.05 )
)
fragment.hltIterL3FromL1MuonTrimmedPixelVertices = cms.EDProducer( "PixelVertexCollectionTrimmer",
    minSumPt2 = cms.double( 0.0 ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) ),
    maxVtx = cms.uint32( 100 ),
    fractionSumPt2 = cms.double( 0.3 ),
    src = cms.InputTag( "hltIterL3FromL1MuonPixelVertices" )
)
fragment.hltIter0IterL3FromL1MuonPixelSeedsFromPixelTracks = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 0.3 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( False ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromProtoTracks" ) ),
    InputVertexCollection = cms.InputTag( "hltIterL3FromL1MuonTrimmedPixelVertices" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    InputCollection = cms.InputTag( "hltIterL3FromL1MuonPixelTracks" ),
    originRadius = cms.double( 0.1 )
)
fragment.hltIter0IterL3FromL1MuonCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter0IterL3FromL1MuonPixelSeedsFromPixelTracks" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( True ),
    RedundantSeedCleaner = cms.string( "none" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( True ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter0IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "GroupedCkfTrajectoryBuilder" )
)
fragment.hltIter0IterL3FromL1MuonCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter0IterL3FromL1MuonCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter0" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
fragment.hltIter0IterL3FromL1MuonTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter0IterL3FromL1MuonCtfWithMaterialTracks" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltIterL3FromL1MuonTrimmedPixelVertices" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet(
      minPixelHits = cms.vint32( 0, 3, 4 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 100.0 ),
      dr_par = cms.PSet(
        d0err = cms.vdouble( 0.003, 0.003, 3.40282346639E38 ),
        dr_par2 = cms.vdouble( 0.3, 0.3, 3.40282346639E38 ),
        dr_par1 = cms.vdouble( 0.4, 0.4, 3.40282346639E38 ),
        dr_exp = cms.vint32( 4, 4, 2147483647 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 3.40282346639E38 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 3, 4 ),
      dz_par = cms.PSet(
        dz_par1 = cms.vdouble( 0.4, 0.4, 3.40282346639E38 ),
        dz_par2 = cms.vdouble( 0.35, 0.35, 3.40282346639E38 ),
        dz_exp = cms.vint32( 4, 4, 2147483647 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 3.40282346639E38, 3.40282346639E38, 3.40282346639E38 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 4 )
    ),
    ignoreVertices = cms.bool( False )
)
fragment.hltIter0IterL3FromL1MuonTrackSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltIter0IterL3FromL1MuonCtfWithMaterialTracks" ),
    originalQualVals = cms.InputTag( 'hltIter0IterL3FromL1MuonTrackCutClassifier','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltIter0IterL3FromL1MuonTrackCutClassifier','MVAValues' )
)
fragment.hltIter2IterL3FromL1MuonClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 16.0 ),
    trajectories = cms.InputTag( "hltIter0IterL3FromL1MuonTrackSelectionHighPurity" ),
    oldClusterRemovalInfo = cms.InputTag( "" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClusters" ),
    TrackQuality = cms.string( "highPurity" )
)
fragment.hltIter2IterL3FromL1MuonMaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter2IterL3FromL1MuonClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClusters" )
)
fragment.hltIter2IterL3FromL1MuonPixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix2+BPix3+BPix4',
      'BPix1+BPix3+BPix4',
      'BPix1+BPix2+BPix4',
      'BPix2+BPix3+FPix1_pos',
      'BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix2+FPix1_pos+FPix2_pos',
      'BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix2_pos+FPix3_pos',
      'FPix1_neg+FPix2_neg+FPix3_neg',
      'BPix1+BPix3+FPix1_pos',
      'BPix1+BPix2+FPix2_pos',
      'BPix1+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix2_neg',
      'BPix1+FPix2_neg+FPix3_neg',
      'BPix1+FPix1_neg+FPix3_neg',
      'BPix1+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_pos+FPix3_pos' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter2IterL3FromL1MuonClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter2IterL3FromL1MuonClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  )
)
fragment.hltIter2IterL3FromL1MuonPixelClusterCheck = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" )
)
fragment.hltIter2IterL3FromL1MuonPixelHitDoublets = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltIterL3FromL1MuonPixelTracksTrackingRegions" ),
    layerPairs = cms.vuint32( 0, 1 ),
    clusterCheck = cms.InputTag( "hltIter2IterL3FromL1MuonPixelClusterCheck" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElementTotal = cms.uint32( 50000000 ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltIter2IterL3FromL1MuonPixelLayerTriplets" )
)
fragment.hltIter2IterL3FromL1MuonPixelHitTriplets = cms.EDProducer( "CAHitTripletEDProducer",
    CAHardPtCut = cms.double( 0.3 ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltIter2IterL3FromL1MuonPixelHitDoublets" ),
    CAThetaCut = cms.double( 0.015 ),
    maxChi2 = cms.PSet(
      value2 = cms.double( 6.0 ),
      value1 = cms.double( 100.0 ),
      pt1 = cms.double( 0.8 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 8.0 )
    ),
    CAPhiCut = cms.double( 0.1 ),
    useBendingCorrection = cms.bool( True )
)
fragment.hltIter2IterL3FromL1MuonPixelSeeds = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltIter2IterL3FromL1MuonPixelHitTriplets" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
fragment.hltIter2IterL3FromL1MuonCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter2IterL3FromL1MuonPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2IterL3FromL1MuonMaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
fragment.hltIter2IterL3FromL1MuonCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter2IterL3FromL1MuonCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2IterL3FromL1MuonMaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter2" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
fragment.hltIter2IterL3FromL1MuonTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter2IterL3FromL1MuonCtfWithMaterialTracks" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltIterL3FromL1MuonTrimmedPixelVertices" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet(
      minPixelHits = cms.vint32( 0, 0, 0 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 100.0 ),
      dr_par = cms.PSet(
        d0err = cms.vdouble( 0.003, 0.003, 3.40282346639E38 ),
        dr_par2 = cms.vdouble( 3.40282346639E38, 0.3, 3.40282346639E38 ),
        dr_par1 = cms.vdouble( 3.40282346639E38, 0.4, 3.40282346639E38 ),
        dr_exp = cms.vint32( 4, 4, 2147483647 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 3.40282346639E38 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 0, 0 ),
      dz_par = cms.PSet(
        dz_par1 = cms.vdouble( 3.40282346639E38, 0.4, 3.40282346639E38 ),
        dz_par2 = cms.vdouble( 3.40282346639E38, 0.35, 3.40282346639E38 ),
        dz_exp = cms.vint32( 4, 4, 2147483647 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 3.40282346639E38 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 3 )
    ),
    ignoreVertices = cms.bool( False )
)
fragment.hltIter2IterL3FromL1MuonTrackSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltIter2IterL3FromL1MuonCtfWithMaterialTracks" ),
    originalQualVals = cms.InputTag( 'hltIter2IterL3FromL1MuonTrackCutClassifier','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltIter2IterL3FromL1MuonTrackCutClassifier','MVAValues' )
)
fragment.hltIter2IterL3FromL1MuonMerged = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter0IterL3FromL1MuonTrackSelectionHighPurity','hltIter2IterL3FromL1MuonTrackSelectionHighPurity' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet(
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter0IterL3FromL1MuonTrackSelectionHighPurity','hltIter2IterL3FromL1MuonTrackSelectionHighPurity' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltIter3IterL3FromL1MuonClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 16.0 ),
    trajectories = cms.InputTag( "hltIter2IterL3FromL1MuonTrackSelectionHighPurity" ),
    oldClusterRemovalInfo = cms.InputTag( "hltIter2IterL3FromL1MuonClustersRefRemoval" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClusters" ),
    TrackQuality = cms.string( "highPurity" )
)
fragment.hltIter3IterL3FromL1MuonMaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter3IterL3FromL1MuonClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClusters" )
)
fragment.hltIter3IterL3FromL1MuonPixelLayerPairs = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix1+BPix4',
      'BPix2+BPix3',
      'BPix2+BPix4',
      'BPix3+BPix4',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix1+FPix3_pos',
      'BPix1+FPix3_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'BPix3+FPix1_pos',
      'BPix3+FPix1_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix3_pos',
      'FPix1_neg+FPix3_neg',
      'FPix2_pos+FPix3_pos',
      'FPix2_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter3IterL3FromL1MuonClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter3IterL3FromL1MuonClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  )
)
fragment.hltIter3IterL3FromL1MuonTrackingRegions = cms.EDProducer( "CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet(
      vertexCollection = cms.InputTag( "notUsed" ),
      zErrorVetex = cms.double( 0.2 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorBeamSpot = cms.double( 24.2 ),
      maxNVertices = cms.int32( 1 ),
      maxNRegions = cms.int32( 2 ),
      nSigmaZVertex = cms.double( 3.0 ),
      nSigmaZBeamSpot = cms.double( 4.0 ),
      ptMin = cms.double( 10.0 ),
      mode = cms.string( "BeamSpotSigma" ),
      input = cms.InputTag( "hltL1MuonsPt0" ),
      searchOpt = cms.bool( False ),
      whereToUseMeasurementTracker = cms.string( "Never" ),
      originRadius = cms.double( 0.015 ),
      measurementTrackerName = cms.InputTag( "" ),
      precise = cms.bool( True ),
      deltaEta = cms.double( 0.2 ),
      deltaPhi = cms.double( 0.1 )
    )
)
fragment.hltIter3IterL3FromL1MuonPixelClusterCheck = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 10000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" )
)
fragment.hltIter3IterL3FromL1MuonPixelHitDoublets = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltIter3IterL3FromL1MuonTrackingRegions" ),
    layerPairs = cms.vuint32( 0 ),
    clusterCheck = cms.InputTag( "hltIter3IterL3FromL1MuonPixelClusterCheck" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( False ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElementTotal = cms.uint32( 50000000 ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltIter3IterL3FromL1MuonPixelLayerPairs" )
)
fragment.hltIter3IterL3FromL1MuonPixelSeeds = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltIter3IterL3FromL1MuonPixelHitDoublets" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
fragment.hltIter3IterL3FromL1MuonCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter3IterL3FromL1MuonPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter3IterL3FromL1MuonMaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2IterL3MuonPSetGroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
fragment.hltIter3IterL3FromL1MuonCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter3IterL3FromL1MuonCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter3IterL3FromL1MuonMaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter3" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
fragment.hltIter3IterL3FromL1MuonTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter3IterL3FromL1MuonCtfWithMaterialTracks" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltIterL3FromL1MuonTrimmedPixelVertices" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet(
      minPixelHits = cms.vint32( 0, 0, 0 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 100.0 ),
      dr_par = cms.PSet(
        d0err = cms.vdouble( 0.003, 0.003, 3.40282346639E38 ),
        dr_par2 = cms.vdouble( 3.40282346639E38, 0.3, 3.40282346639E38 ),
        dr_par1 = cms.vdouble( 3.40282346639E38, 0.4, 3.40282346639E38 ),
        dr_exp = cms.vint32( 4, 4, 2147483647 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 3.40282346639E38 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 0, 0 ),
      dz_par = cms.PSet(
        dz_par1 = cms.vdouble( 3.40282346639E38, 0.4, 3.40282346639E38 ),
        dz_par2 = cms.vdouble( 3.40282346639E38, 0.35, 3.40282346639E38 ),
        dz_exp = cms.vint32( 4, 4, 2147483647 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 3.40282346639E38 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 3 )
    ),
    ignoreVertices = cms.bool( False )
)
fragment.hltIter3IterL3FromL1MuonTrackSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltIter3IterL3FromL1MuonCtfWithMaterialTracks" ),
    originalQualVals = cms.InputTag( 'hltIter3IterL3FromL1MuonTrackCutClassifier','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltIter3IterL3FromL1MuonTrackCutClassifier','MVAValues' )
)
fragment.hltIter3IterL3FromL1MuonMerged = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter2IterL3FromL1MuonMerged','hltIter3IterL3FromL1MuonTrackSelectionHighPurity' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet(
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter2IterL3FromL1MuonMerged','hltIter3IterL3FromL1MuonTrackSelectionHighPurity' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltIterL3MuonMerged = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIterL3OIMuonTrackSelectionHighPurity','hltIter3IterL3MuonMerged' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet(
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIterL3OIMuonTrackSelectionHighPurity','hltIter3IterL3MuonMerged' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltIterL3MuonAndMuonFromL1Merged = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIterL3MuonMerged','hltIter3IterL3FromL1MuonMerged' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet(
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIterL3MuonMerged','hltIter3IterL3FromL1MuonMerged' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltIterL3GlbMuon = cms.EDProducer( "L3MuonProducer",
    ServiceParameters = cms.PSet(
      RPCLayers = cms.bool( True ),
      UseMuonNavigation = cms.untracked.bool( True ),
      Propagators = cms.untracked.vstring( 'hltESPSmartPropagatorAny',
        'SteppingHelixPropagatorAny',
        'hltESPSmartPropagator',
        'hltESPSteppingHelixPropagatorOpposite' )
    ),
    L3TrajBuilderParameters = cms.PSet(
      PtCut = cms.double( 1.0 ),
      TrackerPropagator = cms.string( "SteppingHelixPropagatorAny" ),
      GlobalMuonTrackMatcher = cms.PSet(
        Chi2Cut_3 = cms.double( 200.0 ),
        DeltaDCut_2 = cms.double( 10.0 ),
        Eta_threshold = cms.double( 1.2 ),
        Quality_2 = cms.double( 15.0 ),
        DeltaDCut_1 = cms.double( 40.0 ),
        Quality_3 = cms.double( 7.0 ),
        DeltaDCut_3 = cms.double( 15.0 ),
        Quality_1 = cms.double( 20.0 ),
        Pt_threshold1 = cms.double( 0.0 ),
        DeltaRCut_2 = cms.double( 0.2 ),
        DeltaRCut_1 = cms.double( 0.1 ),
        Pt_threshold2 = cms.double( 9.99999999E8 ),
        Chi2Cut_1 = cms.double( 50.0 ),
        Chi2Cut_2 = cms.double( 50.0 ),
        DeltaRCut_3 = cms.double( 1.0 ),
        LocChi2Cut = cms.double( 0.001 ),
        Propagator = cms.string( "hltESPSmartPropagator" ),
        MinPt = cms.double( 1.0 ),
        MinP = cms.double( 2.5 )
      ),
      ScaleTECxFactor = cms.double( -1.0 ),
      tkTrajUseVertex = cms.bool( False ),
      MuonTrackingRegionBuilder = cms.PSet(
        Rescale_Dz = cms.double( 4.0 ),
        Pt_fixed = cms.bool( False ),
        Eta_fixed = cms.bool( True ),
        Eta_min = cms.double( 0.1 ),
        DeltaZ = cms.double( 24.2 ),
        maxRegions = cms.int32( 2 ),
        EtaR_UpperLimit_Par1 = cms.double( 0.25 ),
        UseVertex = cms.bool( False ),
        Z_fixed = cms.bool( False ),
        PhiR_UpperLimit_Par1 = cms.double( 0.6 ),
        PhiR_UpperLimit_Par2 = cms.double( 0.2 ),
        Rescale_phi = cms.double( 3.0 ),
        DeltaEta = cms.double( 0.2 ),
        precise = cms.bool( True ),
        OnDemand = cms.int32( -1 ),
        EtaR_UpperLimit_Par2 = cms.double( 0.15 ),
        MeasurementTrackerName = cms.InputTag( "hltESPMeasurementTracker" ),
        vertexCollection = cms.InputTag( "pixelVertices" ),
        Pt_min = cms.double( 3.0 ),
        beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
        Phi_fixed = cms.bool( True ),
        DeltaR = cms.double( 0.025 ),
        input = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' ),
        DeltaPhi = cms.double( 0.15 ),
        Phi_min = cms.double( 0.1 ),
        Rescale_eta = cms.double( 3.0 )
      ),
      TrackTransformer = cms.PSet(
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        RefitDirection = cms.string( "insideOut" ),
        RefitRPCHits = cms.bool( True ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
        Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
      ),
      tkTrajBeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      RefitRPCHits = cms.bool( True ),
      tkTrajVertex = cms.InputTag( "Notused" ),
      GlbRefitterParameters = cms.PSet(
        Fitter = cms.string( "hltESPL3MuKFTrajectoryFitter" ),
        DTRecSegmentLabel = cms.InputTag( "hltDt4DSegments" ),
        RefitFlag = cms.bool( True ),
        SkipStation = cms.int32( -1 ),
        Chi2CutRPC = cms.double( 1.0 ),
        PropDirForCosmics = cms.bool( False ),
        CSCRecSegmentLabel = cms.InputTag( "hltCscSegments" ),
        HitThreshold = cms.int32( 1 ),
        DYTthrs = cms.vint32( 30, 15 ),
        TrackerSkipSystem = cms.int32( -1 ),
        RefitDirection = cms.string( "insideOut" ),
        Chi2CutCSC = cms.double( 150.0 ),
        Chi2CutDT = cms.double( 10.0 ),
        RefitRPCHits = cms.bool( True ),
        TrackerSkipSection = cms.int32( -1 ),
        Propagator = cms.string( "hltESPSmartPropagatorAny" ),
        DoPredictionsOnly = cms.bool( False ),
        TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
        MuonHitsOption = cms.int32( 1 ),
        MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" )
      ),
      PCut = cms.double( 2.5 ),
      tkTrajMaxDXYBeamSpot = cms.double( 9999.0 ),
      TrackerRecHitBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      tkTrajMaxChi2 = cms.double( 9999.0 ),
      MuonRecHitBuilder = cms.string( "hltESPMuonTransientTrackingRecHitBuilder" ),
      ScaleTECyFactor = cms.double( -1.0 ),
      tkTrajLabel = cms.InputTag( "hltIterL3MuonAndMuonFromL1Merged" )
    ),
    TrackLoaderParameters = cms.PSet(
      MuonSeededTracksInstance = cms.untracked.string( "L2Seeded" ),
      TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      DoSmoothing = cms.bool( True ),
      SmoothTkTrack = cms.untracked.bool( False ),
      VertexConstraint = cms.bool( False ),
      MuonUpdatorAtVertexParameters = cms.PSet(
        MaxChi2 = cms.double( 1000000.0 ),
        BeamSpotPositionErrors = cms.vdouble( 0.1, 0.1, 5.3 ),
        Propagator = cms.string( "hltESPSteppingHelixPropagatorOpposite" )
      ),
      PutTkTrackIntoEvent = cms.untracked.bool( False ),
      Smoother = cms.string( "hltESPKFTrajectorySmootherForMuonTrackLoader" )
    ),
    MuonCollectionLabel = cms.InputTag( 'hltL2Muons','UpdatedAtVtx' )
)
fragment.hltIterL3MuonsNoID = cms.EDProducer( "MuonIdProducer",
    TrackExtractorPSet = cms.PSet(
      Diff_z = cms.double( 0.2 ),
      inputTrackCollection = cms.InputTag( "hltIter3IterL3FromL1MuonMerged" ),
      Chi2Ndof_Max = cms.double( 1.0E64 ),
      BeamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
      DR_Veto = cms.double( 0.01 ),
      Pt_Min = cms.double( -1.0 ),
      DR_Max = cms.double( 1.0 ),
      NHits_Min = cms.uint32( 0 ),
      Chi2Prob_Min = cms.double( -1.0 ),
      Diff_r = cms.double( 0.1 ),
      BeamlineOption = cms.string( "BeamSpotFromEvent" ),
      ComponentName = cms.string( "TrackExtractor" )
    ),
    maxAbsEta = cms.double( 3.0 ),
    fillGlobalTrackRefits = cms.bool( False ),
    arbitrationCleanerOptions = cms.PSet(
      OverlapDTheta = cms.double( 0.02 ),
      Overlap = cms.bool( True ),
      Clustering = cms.bool( True ),
      ME1a = cms.bool( True ),
      ClusterDTheta = cms.double( 0.02 ),
      ClusterDPhi = cms.double( 0.6 ),
      OverlapDPhi = cms.double( 0.0786 )
    ),
    globalTrackQualityInputTag = cms.InputTag( "glbTrackQual" ),
    fillShowerDigis = cms.bool( False ),
    addExtraSoftMuons = cms.bool( False ),
    debugWithTruthMatching = cms.bool( False ),
    CaloExtractorPSet = cms.PSet(
      DR_Veto_H = cms.double( 0.1 ),
      CenterConeOnCalIntersection = cms.bool( False ),
      NoiseTow_EE = cms.double( 0.15 ),
      Noise_EB = cms.double( 0.025 ),
      Noise_HE = cms.double( 0.2 ),
      DR_Veto_E = cms.double( 0.07 ),
      NoiseTow_EB = cms.double( 0.04 ),
      Noise_EE = cms.double( 0.1 ),
      UseRecHitsFlag = cms.bool( False ),
      DR_Max = cms.double( 1.0 ),
      DepositLabel = cms.untracked.string( "Cal" ),
      Noise_HO = cms.double( 0.2 ),
      DR_Veto_HO = cms.double( 0.1 ),
      Threshold_H = cms.double( 0.5 ),
      PrintTimeReport = cms.untracked.bool( False ),
      Threshold_E = cms.double( 0.2 ),
      PropagatorName = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      ComponentName = cms.string( "CaloExtractorByAssociator" ),
      Threshold_HO = cms.double( 0.5 ),
      DepositInstanceLabels = cms.vstring( 'ecal',
        'hcal',
        'ho' ),
      ServiceParameters = cms.PSet(
        RPCLayers = cms.bool( False ),
        UseMuonNavigation = cms.untracked.bool( False ),
        Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' )
      ),
      TrackAssociatorParameters = cms.PSet(
        useMuon = cms.bool( False ),
        truthMatch = cms.bool( False ),
        usePreshower = cms.bool( False ),
        dRPreshowerPreselection = cms.double( 0.2 ),
        muonMaxDistanceSigmaY = cms.double( 0.0 ),
        useEcal = cms.bool( False ),
        muonMaxDistanceSigmaX = cms.double( 0.0 ),
        dRMuon = cms.double( 9999.0 ),
        dREcal = cms.double( 1.0 ),
        CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
        DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
        EBRecHitCollectionLabel = cms.InputTag( "Notused" ),
        CaloTowerCollectionLabel = cms.InputTag( "Notused" ),
        propagateAllDirections = cms.bool( True ),
        muonMaxDistanceY = cms.double( 5.0 ),
        useHO = cms.bool( False ),
        muonMaxDistanceX = cms.double( 5.0 ),
        trajectoryUncertaintyTolerance = cms.double( -1.0 ),
        useHcal = cms.bool( False ),
        HBHERecHitCollectionLabel = cms.InputTag( "Notused" ),
        accountForTrajectoryChangeCalo = cms.bool( False ),
        dREcalPreselection = cms.double( 1.0 ),
        useCalo = cms.bool( True ),
        dRMuonPreselection = cms.double( 0.2 ),
        EERecHitCollectionLabel = cms.InputTag( "Notused" ),
        dRHcal = cms.double( 1.0 ),
        dRHcalPreselection = cms.double( 1.0 ),
        HORecHitCollectionLabel = cms.InputTag( "Notused" )
      ),
      Noise_HB = cms.double( 0.2 )
    ),
    runArbitrationCleaner = cms.bool( False ),
    fillEnergy = cms.bool( False ),
    TrackerKinkFinderParameters = cms.PSet(
      usePosition = cms.bool( False ),
      diagonalOnly = cms.bool( False )
    ),
    TimingFillerParameters = cms.PSet(
      DTTimingParameters = cms.PSet(
        HitError = cms.double( 6.0 ),
        MatchParameters = cms.PSet(
          TightMatchDT = cms.bool( False ),
          DTradius = cms.double( 0.01 ),
          TightMatchCSC = cms.bool( True ),
          CSCsegments = cms.InputTag( "hltCscSegments" ),
          DTsegments = cms.InputTag( "hltDt4DSegments" )
        ),
        debug = cms.bool( False ),
        DoWireCorr = cms.bool( False ),
        RequireBothProjections = cms.bool( False ),
        DTTimeOffset = cms.double( 2.7 ),
        PruneCut = cms.double( 10000.0 ),
        DTsegments = cms.InputTag( "hltDt4DSegments" ),
        UseSegmentT0 = cms.bool( False ),
        HitsMin = cms.int32( 5 ),
        DropTheta = cms.bool( True ),
        ServiceParameters = cms.PSet(
          RPCLayers = cms.bool( True ),
          Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' )
        )
      ),
      UseCSC = cms.bool( True ),
      CSCTimingParameters = cms.PSet(
        MatchParameters = cms.PSet(
          TightMatchDT = cms.bool( False ),
          DTradius = cms.double( 0.01 ),
          TightMatchCSC = cms.bool( True ),
          CSCsegments = cms.InputTag( "hltCscSegments" ),
          DTsegments = cms.InputTag( "hltDt4DSegments" )
        ),
        debug = cms.bool( False ),
        CSCWireTimeOffset = cms.double( 0.0 ),
        CSCStripError = cms.double( 7.0 ),
        CSCTimeOffset = cms.double( 0.0 ),
        CSCWireError = cms.double( 8.6 ),
        PruneCut = cms.double( 100.0 ),
        CSCsegments = cms.InputTag( "hltCscSegments" ),
        UseStripTime = cms.bool( True ),
        CSCStripTimeOffset = cms.double( 0.0 ),
        UseWireTime = cms.bool( True ),
        ServiceParameters = cms.PSet(
          RPCLayers = cms.bool( True ),
          Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' )
        )
      ),
      ErrorDT = cms.double( 6.0 ),
      EcalEnergyCut = cms.double( 0.4 ),
      UseECAL = cms.bool( True ),
      ErrorEB = cms.double( 2.085 ),
      UseDT = cms.bool( True ),
      ErrorEE = cms.double( 6.95 ),
      ErrorCSC = cms.double( 7.4 )
    ),
    inputCollectionTypes = cms.vstring( 'inner tracks',
      'links',
      'outer tracks' ),
    arbitrateTrackerMuons = cms.bool( True ),
    minCaloCompatibility = cms.double( 0.6 ),
    ecalDepositName = cms.string( "ecal" ),
    minP = cms.double( 0.0 ),
    fillIsolation = cms.bool( False ),
    jetDepositName = cms.string( "jets" ),
    hoDepositName = cms.string( "ho" ),
    writeIsoDeposits = cms.bool( False ),
    maxAbsPullX = cms.double( 4.0 ),
    maxAbsPullY = cms.double( 9999.0 ),
    minPt = cms.double( 2.0 ),
    TrackAssociatorParameters = cms.PSet(
      useMuon = cms.bool( True ),
      truthMatch = cms.bool( False ),
      usePreshower = cms.bool( False ),
      dRPreshowerPreselection = cms.double( 0.2 ),
      muonMaxDistanceSigmaY = cms.double( 0.0 ),
      useEcal = cms.bool( False ),
      muonMaxDistanceSigmaX = cms.double( 0.0 ),
      dRMuon = cms.double( 9999.0 ),
      dREcal = cms.double( 9999.0 ),
      CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
      DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
      EBRecHitCollectionLabel = cms.InputTag( "Notused" ),
      CaloTowerCollectionLabel = cms.InputTag( "Notused" ),
      propagateAllDirections = cms.bool( True ),
      muonMaxDistanceY = cms.double( 5.0 ),
      useHO = cms.bool( False ),
      muonMaxDistanceX = cms.double( 5.0 ),
      trajectoryUncertaintyTolerance = cms.double( -1.0 ),
      useHcal = cms.bool( False ),
      HBHERecHitCollectionLabel = cms.InputTag( "Notused" ),
      accountForTrajectoryChangeCalo = cms.bool( False ),
      dREcalPreselection = cms.double( 0.05 ),
      useCalo = cms.bool( False ),
      dRMuonPreselection = cms.double( 0.2 ),
      EERecHitCollectionLabel = cms.InputTag( "Notused" ),
      dRHcal = cms.double( 9999.0 ),
      dRHcalPreselection = cms.double( 0.2 ),
      HORecHitCollectionLabel = cms.InputTag( "Notused" )
    ),
    storeCrossedHcalRecHits = cms.bool( False ),
    JetExtractorPSet = cms.PSet(
      JetCollectionLabel = cms.InputTag( "Notused" ),
      DR_Veto = cms.double( 0.1 ),
      DR_Max = cms.double( 1.0 ),
      ExcludeMuonVeto = cms.bool( True ),
      PrintTimeReport = cms.untracked.bool( False ),
      PropagatorName = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      ComponentName = cms.string( "JetExtractor" ),
      ServiceParameters = cms.PSet(
        RPCLayers = cms.bool( False ),
        UseMuonNavigation = cms.untracked.bool( False ),
        Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' )
      ),
      TrackAssociatorParameters = cms.PSet(
        useMuon = cms.bool( False ),
        truthMatch = cms.bool( False ),
        usePreshower = cms.bool( False ),
        dRPreshowerPreselection = cms.double( 0.2 ),
        muonMaxDistanceSigmaY = cms.double( 0.0 ),
        useEcal = cms.bool( False ),
        muonMaxDistanceSigmaX = cms.double( 0.0 ),
        dRMuon = cms.double( 9999.0 ),
        dREcal = cms.double( 0.5 ),
        CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
        DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
        EBRecHitCollectionLabel = cms.InputTag( "Notused" ),
        CaloTowerCollectionLabel = cms.InputTag( "Notused" ),
        propagateAllDirections = cms.bool( True ),
        muonMaxDistanceY = cms.double( 5.0 ),
        useHO = cms.bool( False ),
        muonMaxDistanceX = cms.double( 5.0 ),
        trajectoryUncertaintyTolerance = cms.double( -1.0 ),
        useHcal = cms.bool( False ),
        HBHERecHitCollectionLabel = cms.InputTag( "Notused" ),
        accountForTrajectoryChangeCalo = cms.bool( False ),
        dREcalPreselection = cms.double( 0.5 ),
        useCalo = cms.bool( True ),
        dRMuonPreselection = cms.double( 0.2 ),
        EERecHitCollectionLabel = cms.InputTag( "Notused" ),
        dRHcal = cms.double( 0.5 ),
        dRHcalPreselection = cms.double( 0.5 ),
        HORecHitCollectionLabel = cms.InputTag( "Notused" )
      ),
      Threshold = cms.double( 5.0 )
    ),
    fillGlobalTrackQuality = cms.bool( False ),
    minPCaloMuon = cms.double( 1.0E9 ),
    maxAbsDy = cms.double( 9999.0 ),
    fillCaloCompatibility = cms.bool( False ),
    fillMatching = cms.bool( True ),
    MuonCaloCompatibility = cms.PSet(
      delta_eta = cms.double( 0.02 ),
      delta_phi = cms.double( 0.02 ),
      allSiPMHO = cms.bool( False ),
      MuonTemplateFileName = cms.FileInPath( "RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root" ),
      PionTemplateFileName = cms.FileInPath( "RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root" )
    ),
    fillTrackerKink = cms.bool( False ),
    ShowerDigiFillerParameters = cms.PSet(
      cscDigiCollectionLabel = cms.InputTag( 'muonCSCDigis','MuonCSCStripDigi' ),
      dtDigiCollectionLabel = cms.InputTag( "muonDTDigis" ),
      digiMaxDistanceX = cms.double( 25.0 )
    ),
    hcalDepositName = cms.string( "hcal" ),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double( 2.0 ),
    inputCollectionLabels = cms.VInputTag( 'hltIterL3MuonAndMuonFromL1Merged','hltIterL3GlbMuon','hltL2Muons:UpdatedAtVtx' ),
    trackDepositName = cms.string( "tracker" ),
    maxAbsDx = cms.double( 3.0 ),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double( 200.0 ),
    minNumberOfMatches = cms.int32( 1 )
)
fragment.hltIterL3Muons = cms.EDProducer( "MuonIDFilterProducerForHLT",
    maxNormalizedChi2 = cms.double( 9999.0 ),
    minPt = cms.double( 0.0 ),
    applyTriggerIdLoose = cms.bool( True ),
    minNMuonHits = cms.int32( 0 ),
    minPixHits = cms.int32( 0 ),
    requiredTypeMask = cms.uint32( 0 ),
    minNMuonStations = cms.int32( 0 ),
    minPixLayer = cms.int32( 0 ),
    minNTrkLayers = cms.int32( 0 ),
    minTrkHits = cms.int32( 0 ),
    inputMuonCollection = cms.InputTag( "hltIterL3MuonsNoID" ),
    allowedTypeMask = cms.uint32( 0 ),
    typeMuon = cms.uint32( 0 )
)
fragment.hltL3MuonsIterL3Links = cms.EDProducer( "MuonLinksProducer",
    inputCollection = cms.InputTag( "hltIterL3Muons" )
)
fragment.hltIterL3MuonTracks = cms.EDProducer( "HLTMuonTrackSelector",
    muon = cms.InputTag( "hltIterL3Muons" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    track = cms.InputTag( "hltIterL3MuonAndMuonFromL1Merged" ),
    copyMVA = cms.bool( False ),
    originalMVAVals = cms.InputTag( "none" )
)
fragment.hltIterL3MuonCandidates = cms.EDProducer( "L3MuonCandidateProducerFromMuons",
    InputObjects = cms.InputTag( "hltIterL3Muons" )
)
fragment.hltEcalDigis = cms.EDProducer( "EcalRawToDigi",
    orderedDCCIdList = cms.vint32( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54 ),
    FedLabel = cms.InputTag( "listfeds" ),
    eventPut = cms.bool( True ),
    srpUnpacking = cms.bool( True ),
    syncCheck = cms.bool( True ),
    headerUnpacking = cms.bool( True ),
    feUnpacking = cms.bool( True ),
    orderedFedList = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    tccUnpacking = cms.bool( True ),
    numbTriggerTSamples = cms.int32( 1 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    numbXtalTSamples = cms.int32( 10 ),
    feIdCheck = cms.bool( True ),
    FEDs = cms.vint32( 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654 ),
    silentMode = cms.untracked.bool( True ),
    DoRegional = cms.bool( False ),
    forceToKeepFRData = cms.bool( False ),
    memUnpacking = cms.bool( True )
)
fragment.hltEcalUncalibRecHit = cms.EDProducer( "EcalUncalibRecHitProducer",
    EEdigiCollection = cms.InputTag( 'hltEcalDigis','eeDigis' ),
    EBdigiCollection = cms.InputTag( 'hltEcalDigis','ebDigis' ),
    EEhitCollection = cms.string( "EcalUncalibRecHitsEE" ),
    EBhitCollection = cms.string( "EcalUncalibRecHitsEB" ),
    algo = cms.string( "EcalUncalibRecHitWorkerMultiFit" ),
    algoPSet = cms.PSet(
      ebSpikeThreshold = cms.double( 1.042 ),
      EBtimeFitLimits_Upper = cms.double( 1.4 ),
      EEtimeFitLimits_Lower = cms.double( 0.2 ),
      timealgo = cms.string( "None" ),
      EBtimeNconst = cms.double( 28.5 ),
      prefitMaxChiSqEE = cms.double( 10.0 ),
      outOfTimeThresholdGain12mEB = cms.double( 5.0 ),
      outOfTimeThresholdGain12mEE = cms.double( 1000.0 ),
      EEtimeFitParameters = cms.vdouble( -2.390548, 3.553628, -17.62341, 67.67538, -133.213, 140.7432, -75.41106, 16.20277 ),
      prefitMaxChiSqEB = cms.double( 25.0 ),
      simplifiedNoiseModelForGainSwitch = cms.bool( True ),
      EBtimeFitParameters = cms.vdouble( -2.015452, 3.130702, -12.3473, 41.88921, -82.83944, 91.01147, -50.35761, 11.05621 ),
      selectiveBadSampleCriteriaEB = cms.bool( False ),
      dynamicPedestalsEB = cms.bool( False ),
      useLumiInfoRunHeader = cms.bool( False ),
      EBamplitudeFitParameters = cms.vdouble( 1.138, 1.652 ),
      doPrefitEE = cms.bool( False ),
      dynamicPedestalsEE = cms.bool( False ),
      selectiveBadSampleCriteriaEE = cms.bool( False ),
      outOfTimeThresholdGain61pEE = cms.double( 1000.0 ),
      outOfTimeThresholdGain61pEB = cms.double( 5.0 ),
      activeBXs = cms.vint32( -5, -4, -3, -2, -1, 0, 1, 2, 3, 4 ),
      EcalPulseShapeParameters = cms.PSet(
        EEPulseShapeTemplate = cms.vdouble( 0.116442, 0.756246, 1.0, 0.897182, 0.686831, 0.491506, 0.344111, 0.245731, 0.174115, 0.123361, 0.0874288, 0.061957 ),
        EEdigiCollection = cms.string( "" ),
        EcalPreMixStage2 = cms.bool( False ),
        EcalPreMixStage1 = cms.bool( False ),
        EBPulseShapeCovariance = cms.vdouble( 3.001E-6, 1.233E-5, 0.0, -4.416E-6, -4.571E-6, -3.614E-6, -2.636E-6, -1.286E-6, -8.41E-7, -5.296E-7, 0.0, 0.0, 1.233E-5, 6.154E-5, 0.0, -2.2E-5, -2.309E-5, -1.838E-5, -1.373E-5, -7.334E-6, -5.088E-6, -3.745E-6, -2.428E-6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -4.416E-6, -2.2E-5, 0.0, 8.319E-6, 8.545E-6, 6.792E-6, 5.059E-6, 2.678E-6, 1.816E-6, 1.223E-6, 8.245E-7, 5.589E-7, -4.571E-6, -2.309E-5, 0.0, 8.545E-6, 9.182E-6, 7.219E-6, 5.388E-6, 2.853E-6, 1.944E-6, 1.324E-6, 9.083E-7, 6.335E-7, -3.614E-6, -1.838E-5, 0.0, 6.792E-6, 7.219E-6, 6.016E-6, 4.437E-6, 2.385E-6, 1.636E-6, 1.118E-6, 7.754E-7, 5.556E-7, -2.636E-6, -1.373E-5, 0.0, 5.059E-6, 5.388E-6, 4.437E-6, 3.602E-6, 1.917E-6, 1.322E-6, 9.079E-7, 6.529E-7, 4.752E-7, -1.286E-6, -7.334E-6, 0.0, 2.678E-6, 2.853E-6, 2.385E-6, 1.917E-6, 1.375E-6, 9.1E-7, 6.455E-7, 4.693E-7, 3.657E-7, -8.41E-7, -5.088E-6, 0.0, 1.816E-6, 1.944E-6, 1.636E-6, 1.322E-6, 9.1E-7, 9.115E-7, 6.062E-7, 4.436E-7, 3.422E-7, -5.296E-7, -3.745E-6, 0.0, 1.223E-6, 1.324E-6, 1.118E-6, 9.079E-7, 6.455E-7, 6.062E-7, 7.217E-7, 4.862E-7, 3.768E-7, 0.0, -2.428E-6, 0.0, 8.245E-7, 9.083E-7, 7.754E-7, 6.529E-7, 4.693E-7, 4.436E-7, 4.862E-7, 6.509E-7, 4.418E-7, 0.0, 0.0, 0.0, 5.589E-7, 6.335E-7, 5.556E-7, 4.752E-7, 3.657E-7, 3.422E-7, 3.768E-7, 4.418E-7, 6.142E-7 ),
        ESdigiCollection = cms.string( "" ),
        EBdigiCollection = cms.string( "" ),
        EBCorrNoiseMatrixG01 = cms.vdouble( 1.0, 0.73354, 0.64442, 0.58851, 0.55425, 0.53082, 0.51916, 0.51097, 0.50732, 0.50409 ),
        EBCorrNoiseMatrixG12 = cms.vdouble( 1.0, 0.71073, 0.55721, 0.46089, 0.40449, 0.35931, 0.33924, 0.32439, 0.31581, 0.30481 ),
        EBCorrNoiseMatrixG06 = cms.vdouble( 1.0, 0.70946, 0.58021, 0.49846, 0.45006, 0.41366, 0.39699, 0.38478, 0.37847, 0.37055 ),
        EEPulseShapeCovariance = cms.vdouble( 3.941E-5, 3.333E-5, 0.0, -1.449E-5, -1.661E-5, -1.424E-5, -1.183E-5, -6.842E-6, -4.915E-6, -3.411E-6, 0.0, 0.0, 3.333E-5, 2.862E-5, 0.0, -1.244E-5, -1.431E-5, -1.233E-5, -1.032E-5, -5.883E-6, -4.154E-6, -2.902E-6, -2.128E-6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.449E-5, -1.244E-5, 0.0, 5.84E-6, 6.649E-6, 5.72E-6, 4.812E-6, 2.708E-6, 1.869E-6, 1.33E-6, 9.186E-7, 6.446E-7, -1.661E-5, -1.431E-5, 0.0, 6.649E-6, 7.966E-6, 6.898E-6, 5.794E-6, 3.157E-6, 2.184E-6, 1.567E-6, 1.084E-6, 7.575E-7, -1.424E-5, -1.233E-5, 0.0, 5.72E-6, 6.898E-6, 6.341E-6, 5.347E-6, 2.859E-6, 1.991E-6, 1.431E-6, 9.839E-7, 6.886E-7, -1.183E-5, -1.032E-5, 0.0, 4.812E-6, 5.794E-6, 5.347E-6, 4.854E-6, 2.628E-6, 1.809E-6, 1.289E-6, 9.02E-7, 6.146E-7, -6.842E-6, -5.883E-6, 0.0, 2.708E-6, 3.157E-6, 2.859E-6, 2.628E-6, 1.863E-6, 1.296E-6, 8.882E-7, 6.108E-7, 4.283E-7, -4.915E-6, -4.154E-6, 0.0, 1.869E-6, 2.184E-6, 1.991E-6, 1.809E-6, 1.296E-6, 1.217E-6, 8.669E-7, 5.751E-7, 3.882E-7, -3.411E-6, -2.902E-6, 0.0, 1.33E-6, 1.567E-6, 1.431E-6, 1.289E-6, 8.882E-7, 8.669E-7, 9.522E-7, 6.717E-7, 4.293E-7, 0.0, -2.128E-6, 0.0, 9.186E-7, 1.084E-6, 9.839E-7, 9.02E-7, 6.108E-7, 5.751E-7, 6.717E-7, 7.911E-7, 5.493E-7, 0.0, 0.0, 0.0, 6.446E-7, 7.575E-7, 6.886E-7, 6.146E-7, 4.283E-7, 3.882E-7, 4.293E-7, 5.493E-7, 7.027E-7 ),
        EBPulseShapeTemplate = cms.vdouble( 0.0113979, 0.758151, 1.0, 0.887744, 0.673548, 0.474332, 0.319561, 0.215144, 0.147464, 0.101087, 0.0693181, 0.0475044 ),
        EECorrNoiseMatrixG01 = cms.vdouble( 1.0, 0.72698, 0.62048, 0.55691, 0.51848, 0.49147, 0.47813, 0.47007, 0.46621, 0.46265 ),
        EECorrNoiseMatrixG12 = cms.vdouble( 1.0, 0.71373, 0.44825, 0.30152, 0.21609, 0.14786, 0.11772, 0.10165, 0.09465, 0.08098 ),
        UseLCcorrection = cms.untracked.bool( True ),
        EECorrNoiseMatrixG06 = cms.vdouble( 1.0, 0.71217, 0.47464, 0.34056, 0.26282, 0.20287, 0.17734, 0.16256, 0.15618, 0.14443 )
      ),
      doPrefitEB = cms.bool( False ),
      addPedestalUncertaintyEE = cms.double( 0.0 ),
      addPedestalUncertaintyEB = cms.double( 0.0 ),
      gainSwitchUseMaxSampleEB = cms.bool( True ),
      EEtimeNconst = cms.double( 31.8 ),
      EEamplitudeFitParameters = cms.vdouble( 1.89, 1.4 ),
      chi2ThreshEE_ = cms.double( 50.0 ),
      eePulseShape = cms.vdouble( 5.2E-5, -5.26E-5, 6.66E-5, 0.1168, 0.7575, 1.0, 0.8876, 0.6732, 0.4741, 0.3194 ),
      outOfTimeThresholdGain12pEB = cms.double( 5.0 ),
      gainSwitchUseMaxSampleEE = cms.bool( False ),
      mitigateBadSamplesEB = cms.bool( False ),
      outOfTimeThresholdGain12pEE = cms.double( 1000.0 ),
      ebPulseShape = cms.vdouble( 5.2E-5, -5.26E-5, 6.66E-5, 0.1168, 0.7575, 1.0, 0.8876, 0.6732, 0.4741, 0.3194 ),
      ampErrorCalculation = cms.bool( False ),
      mitigateBadSamplesEE = cms.bool( False ),
      amplitudeThresholdEB = cms.double( 10.0 ),
      kPoorRecoFlagEB = cms.bool( True ),
      amplitudeThresholdEE = cms.double( 10.0 ),
      EBtimeFitLimits_Lower = cms.double( 0.2 ),
      kPoorRecoFlagEE = cms.bool( False ),
      EEtimeFitLimits_Upper = cms.double( 1.4 ),
      outOfTimeThresholdGain61mEE = cms.double( 1000.0 ),
      EEtimeConstantTerm = cms.double( 1.0 ),
      EBtimeConstantTerm = cms.double( 0.6 ),
      chi2ThreshEB_ = cms.double( 65.0 ),
      outOfTimeThresholdGain61mEB = cms.double( 5.0 )
    )
)
fragment.hltEcalDetIdToBeRecovered = cms.EDProducer( "EcalDetIdToBeRecoveredProducer",
    ebIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebDetIdToBeRecovered = cms.string( "ebDetId" ),
    integrityTTIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityTTIdErrors' ),
    eeIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    ebFEToBeRecovered = cms.string( "ebFE" ),
    ebIntegrityGainErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainErrors' ),
    eeDetIdToBeRecovered = cms.string( "eeDetId" ),
    eeIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    eeIntegrityChIdErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityChIdErrors' ),
    ebIntegrityGainSwitchErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityGainSwitchErrors' ),
    ebSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    eeSrFlagCollection = cms.InputTag( "hltEcalDigis" ),
    integrityBlockSizeErrors = cms.InputTag( 'hltEcalDigis','EcalIntegrityBlockSizeErrors' ),
    eeFEToBeRecovered = cms.string( "eeFE" )
)
fragment.hltEcalRecHit = cms.EDProducer( "EcalRecHitProducer",
    recoverEEVFE = cms.bool( False ),
    EErechitCollection = cms.string( "EcalRecHitsEE" ),
    recoverEBIsolatedChannels = cms.bool( False ),
    recoverEBVFE = cms.bool( False ),
    laserCorrection = cms.bool( True ),
    EBLaserMIN = cms.double( 0.5 ),
    killDeadChannels = cms.bool( True ),
    dbStatusToBeExcludedEB = cms.vint32( 14, 78, 142 ),
    EEuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEE' ),
    EBLaserMAX = cms.double( 3.0 ),
    EELaserMIN = cms.double( 0.5 ),
    ebFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebFE' ),
    EELaserMAX = cms.double( 8.0 ),
    recoverEEIsolatedChannels = cms.bool( False ),
    eeDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeDetId' ),
    recoverEBFE = cms.bool( True ),
    algo = cms.string( "EcalRecHitWorkerSimple" ),
    ebDetIdToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','ebDetId' ),
    singleChannelRecoveryThreshold = cms.double( 8.0 ),
    ChannelStatusToBeExcluded = cms.vstring(  ),
    EBrechitCollection = cms.string( "EcalRecHitsEB" ),
    singleChannelRecoveryMethod = cms.string( "NeuralNetworks" ),
    recoverEEFE = cms.bool( True ),
    triggerPrimitiveDigiCollection = cms.InputTag( 'hltEcalDigis','EcalTriggerPrimitives' ),
    dbStatusToBeExcludedEE = cms.vint32( 14, 78, 142 ),
    flagsMapDBReco = cms.PSet(
      kGood = cms.vstring( 'kOk',
        'kDAC',
        'kNoLaser',
        'kNoisy' ),
      kNeighboursRecovered = cms.vstring( 'kFixedG0',
        'kNonRespondingIsolated',
        'kDeadVFE' ),
      kDead = cms.vstring( 'kNoDataNoTP' ),
      kNoisy = cms.vstring( 'kNNoisy',
        'kFixedG6',
        'kFixedG1' ),
      kTowerRecovered = cms.vstring( 'kDeadFE' )
    ),
    EBuncalibRecHitCollection = cms.InputTag( 'hltEcalUncalibRecHit','EcalUncalibRecHitsEB' ),
    skipTimeCalib = cms.bool( True ),
    algoRecover = cms.string( "EcalRecHitWorkerRecover" ),
    eeFEToBeRecovered = cms.InputTag( 'hltEcalDetIdToBeRecovered','eeFE' ),
    cleaningConfig = cms.PSet(
      e6e2thresh = cms.double( 0.04 ),
      tightenCrack_e6e2_double = cms.double( 3.0 ),
      e4e1Threshold_endcap = cms.double( 0.3 ),
      tightenCrack_e4e1_single = cms.double( 3.0 ),
      tightenCrack_e1_double = cms.double( 2.0 ),
      cThreshold_barrel = cms.double( 4.0 ),
      e4e1Threshold_barrel = cms.double( 0.08 ),
      tightenCrack_e1_single = cms.double( 2.0 ),
      e4e1_b_barrel = cms.double( -0.024 ),
      e4e1_a_barrel = cms.double( 0.04 ),
      ignoreOutOfTimeThresh = cms.double( 1.0E9 ),
      cThreshold_endcap = cms.double( 15.0 ),
      e4e1_b_endcap = cms.double( -0.0125 ),
      e4e1_a_endcap = cms.double( 0.02 ),
      cThreshold_double = cms.double( 10.0 )
    ),
    logWarningEtThreshold_EB_FE = cms.double( 50.0 ),
    logWarningEtThreshold_EE_FE = cms.double( 50.0 )
)
fragment.hltHcalDigis = cms.EDProducer( "HcalRawToDigi",
    saveQIE10DataNSamples = cms.untracked.vint32(  ),
    ExpectedOrbitMessageTime = cms.untracked.int32( -1 ),
    FilterDataQuality = cms.bool( True ),
    silent = cms.untracked.bool( True ),
    saveQIE11DataNSamples = cms.untracked.vint32(  ),
    HcalFirstFED = cms.untracked.int32( 700 ),
    InputLabel = cms.InputTag( "rawDataCollector" ),
    ComplainEmptyData = cms.untracked.bool( False ),
    ElectronicsMap = cms.string( "" ),
    UnpackCalib = cms.untracked.bool( True ),
    UnpackUMNio = cms.untracked.bool( True ),
    FEDs = cms.untracked.vint32(  ),
    saveQIE11DataTags = cms.untracked.vstring(  ),
    UnpackTTP = cms.untracked.bool( False ),
    UnpackZDC = cms.untracked.bool( True ),
    saveQIE10DataTags = cms.untracked.vstring(  ),
    lastSample = cms.int32( 9 ),
    UnpackerMode = cms.untracked.int32( 0 ),
    firstSample = cms.int32( 0 )
)
fragment.hltHbhePhase1Reco = cms.EDProducer( "HBHEPhase1Reconstructor",
    tsFromDB = cms.bool( False ),
    setPulseShapeFlagsQIE8 = cms.bool( True ),
    use8ts = cms.bool( False ),
    digiLabelQIE11 = cms.InputTag( "hltHcalDigis" ),
    saveDroppedInfos = cms.bool( False ),
    setNoiseFlagsQIE8 = cms.bool( True ),
    saveEffectivePedestal = cms.bool( True ),
    digiLabelQIE8 = cms.InputTag( "hltHcalDigis" ),
    sipmQTSShift = cms.int32( 0 ),
    processQIE11 = cms.bool( True ),
    pulseShapeParametersQIE11 = cms.PSet(  ),
    algoConfigClass = cms.string( "" ),
    saveInfos = cms.bool( False ),
    flagParametersQIE11 = cms.PSet(  ),
    makeRecHits = cms.bool( True ),
    pulseShapeParametersQIE8 = cms.PSet(
      UseDualFit = cms.bool( True ),
      LinearCut = cms.vdouble( -3.0, -0.054, -0.054 ),
      TriangleIgnoreSlow = cms.bool( False ),
      TS4TS5LowerThreshold = cms.vdouble( 100.0, 120.0, 160.0, 200.0, 300.0, 500.0 ),
      LinearThreshold = cms.vdouble( 20.0, 100.0, 100000.0 ),
      RightSlopeSmallCut = cms.vdouble( 1.08, 1.16, 1.16 ),
      TS4TS5UpperThreshold = cms.vdouble( 70.0, 90.0, 100.0, 400.0 ),
      TS3TS4ChargeThreshold = cms.double( 70.0 ),
      R45PlusOneRange = cms.double( 0.2 ),
      TS4TS5LowerCut = cms.vdouble( -1.0, -0.7, -0.5, -0.4, -0.3, 0.1 ),
      RightSlopeThreshold = cms.vdouble( 250.0, 400.0, 100000.0 ),
      TS3TS4UpperChargeThreshold = cms.double( 20.0 ),
      MinimumChargeThreshold = cms.double( 20.0 ),
      RightSlopeCut = cms.vdouble( 5.0, 4.15, 4.15 ),
      RMS8MaxThreshold = cms.vdouble( 20.0, 100.0, 100000.0 ),
      MinimumTS4TS5Threshold = cms.double( 100.0 ),
      LeftSlopeThreshold = cms.vdouble( 250.0, 500.0, 100000.0 ),
      TS5TS6ChargeThreshold = cms.double( 70.0 ),
      TrianglePeakTS = cms.uint32( 10000 ),
      TS5TS6UpperChargeThreshold = cms.double( 20.0 ),
      RightSlopeSmallThreshold = cms.vdouble( 150.0, 200.0, 100000.0 ),
      RMS8MaxCut = cms.vdouble( -13.5, -11.5, -11.5 ),
      TS4TS5ChargeThreshold = cms.double( 70.0 ),
      R45MinusOneRange = cms.double( 0.2 ),
      LeftSlopeCut = cms.vdouble( 5.0, 2.55, 2.55 ),
      TS4TS5UpperCut = cms.vdouble( 1.0, 0.8, 0.75, 0.72 )
    ),
    flagParametersQIE8 = cms.PSet(
      hitEnergyMinimum = cms.double( 1.0 ),
      pulseShapeParameterSets = cms.VPSet(
        cms.PSet(  pulseShapeParameters = cms.vdouble( 0.0, 100.0, -50.0, 0.0, -15.0, 0.15 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 100.0, 2000.0, -50.0, 0.0, -5.0, 0.05 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( 2000.0, 1000000.0, -50.0, 0.0, 95.0, 0.0 )        ),
        cms.PSet(  pulseShapeParameters = cms.vdouble( -1000000.0, 1000000.0, 45.0, 0.1, 1000000.0, 0.0 )        )
      ),
      nominalPedestal = cms.double( 3.0 ),
      hitMultiplicityThreshold = cms.int32( 17 )
    ),
    setNegativeFlagsQIE8 = cms.bool( False ),
    setNegativeFlagsQIE11 = cms.bool( False ),
    processQIE8 = cms.bool( True ),
    algorithm = cms.PSet(
      ts4Thresh = cms.double( 0.0 ),
      meanTime = cms.double( 0.0 ),
      nnlsThresh = cms.double( 1.0E-11 ),
      nMaxItersMin = cms.int32( 500 ),
      timeSigmaSiPM = cms.double( 2.5 ),
      applyTimeSlew = cms.bool( True ),
      timeSlewParsType = cms.int32( 3 ),
      ts4Max = cms.vdouble( 100.0, 20000.0, 30000.0 ),
      samplesToAdd = cms.int32( 2 ),
      deltaChiSqThresh = cms.double( 0.001 ),
      applyTimeConstraint = cms.bool( False ),
      timeSigmaHPD = cms.double( 5.0 ),
      useMahi = cms.bool( True ),
      correctForPhaseContainment = cms.bool( True ),
      respCorrM3 = cms.double( 1.0 ),
      pulseJitter = cms.double( 1.0 ),
      applyPedConstraint = cms.bool( False ),
      fitTimes = cms.int32( 1 ),
      nMaxItersNNLS = cms.int32( 500 ),
      applyTimeSlewM3 = cms.bool( True ),
      meanPed = cms.double( 0.0 ),
      ts4Min = cms.double( 0.0 ),
      applyPulseJitter = cms.bool( False ),
      useM2 = cms.bool( False ),
      timeMin = cms.double( -12.5 ),
      useM3 = cms.bool( False ),
      chiSqSwitch = cms.double( 15.0 ),
      dynamicPed = cms.bool( True ),
      tdcTimeShift = cms.double( 0.0 ),
      correctionPhaseNS = cms.double( 6.0 ),
      firstSampleShift = cms.int32( 0 ),
      activeBXs = cms.vint32( -1, 0, 1 ),
      ts4chi2 = cms.vdouble( 15.0, 15.0 ),
      timeMax = cms.double( 12.5 ),
      Class = cms.string( "SimpleHBHEPhase1Algo" )
    ),
    setLegacyFlagsQIE8 = cms.bool( False ),
    sipmQNTStoSum = cms.int32( 3 ),
    setPulseShapeFlagsQIE11 = cms.bool( False ),
    setLegacyFlagsQIE11 = cms.bool( False ),
    setNoiseFlagsQIE11 = cms.bool( False ),
    dropZSmarkedPassed = cms.bool( True ),
    recoParamsFromDB = cms.bool( True )
)
fragment.hltHbhereco = cms.EDProducer( "HBHEPlan1Combiner",
    hbheInput = cms.InputTag( "hltHbhePhase1Reco" ),
    usePlan1Mode = cms.bool( True ),
    ignorePlan1Topology = cms.bool( False ),
    algorithm = cms.PSet(  Class = cms.string( "SimplePlan1RechitCombiner" ) )
)
fragment.hltHfprereco = cms.EDProducer( "HFPreReconstructor",
    soiShift = cms.int32( 0 ),
    sumAllTimeSlices = cms.bool( False ),
    dropZSmarkedPassed = cms.bool( True ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    tsFromDB = cms.bool( False ),
    forceSOI = cms.int32( -1 )
)
fragment.hltHfreco = cms.EDProducer( "HFPhase1Reconstructor",
    setNoiseFlags = cms.bool( True ),
    algoConfigClass = cms.string( "HFPhase1PMTParams" ),
    PETstat = cms.PSet(
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_R_29 = cms.vdouble( 0.8 ),
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      short_R_29 = cms.vdouble( 0.8 ),
      long_R = cms.vdouble( 0.98 ),
      short_R = cms.vdouble( 0.8 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    runHFStripFilter = cms.bool( False ),
    inputLabel = cms.InputTag( "hltHfprereco" ),
    S9S1stat = cms.PSet(
      shortEnergyParams = cms.vdouble( 35.1773, 35.37, 35.7933, 36.4472, 37.3317, 38.4468, 39.7925, 41.3688, 43.1757, 45.2132, 47.4813, 49.98, 52.7093 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      isS8S1 = cms.bool( False ),
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      longEnergyParams = cms.vdouble( 43.5, 45.7, 48.32, 51.36, 54.82, 58.7, 63.0, 67.72, 72.86, 78.42, 84.4, 90.8, 97.62 ),
      short_optimumSlope = cms.vdouble( -99999.0, 0.0164905, 0.0238698, 0.0321383, 0.041296, 0.0513428, 0.0622789, 0.0741041, 0.0868186, 0.100422, 0.135313, 0.136289, 0.0589927 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    checkChannelQualityForDepth3and4 = cms.bool( False ),
    useChannelQualityFromDB = cms.bool( False ),
    algorithm = cms.PSet(
      tfallIfNoTDC = cms.double( -101.0 ),
      triseIfNoTDC = cms.double( -100.0 ),
      rejectAllFailures = cms.bool( True ),
      energyWeights = cms.vdouble( 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 2.0, 0.0, 2.0, 0.0, 2.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 2.0, 0.0, 2.0, 0.0, 2.0, 0.0, 1.0 ),
      soiPhase = cms.uint32( 1 ),
      timeShift = cms.double( 0.0 ),
      tlimits = cms.vdouble( -1000.0, 1000.0, -1000.0, 1000.0 ),
      Class = cms.string( "HFFlexibleTimeCheck" )
    ),
    S8S1stat = cms.PSet(
      shortEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      shortETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      long_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      isS8S1 = cms.bool( True ),
      longETParams = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ),
      longEnergyParams = cms.vdouble( 40.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0 ),
      short_optimumSlope = cms.vdouble( 0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1 ),
      HcalAcceptSeverityLevel = cms.int32( 9 )
    ),
    HFStripFilter = cms.PSet(
      timeMax = cms.double( 6.0 ),
      seedHitIetaMax = cms.int32( 35 ),
      gap = cms.int32( 2 ),
      verboseLevel = cms.untracked.int32( 10 ),
      wedgeCut = cms.double( 0.05 ),
      stripThreshold = cms.double( 40.0 ),
      maxStripTime = cms.double( 10.0 ),
      maxThreshold = cms.double( 100.0 ),
      lstrips = cms.int32( 2 )
    )
)
fragment.hltHoreco = cms.EDProducer( "HcalHitReconstructor",
    digiTimeFromDB = cms.bool( True ),
    mcOOTCorrectionName = cms.string( "" ),
    S9S1stat = cms.PSet(  ),
    saturationParameters = cms.PSet(  maxADCvalue = cms.int32( 127 ) ),
    tsFromDB = cms.bool( True ),
    samplesToAdd = cms.int32( 4 ),
    mcOOTCorrectionCategory = cms.string( "MC" ),
    dataOOTCorrectionName = cms.string( "" ),
    correctionPhaseNS = cms.double( 13.0 ),
    HFInWindowStat = cms.PSet(  ),
    digiLabel = cms.InputTag( "hltHcalDigis" ),
    setHSCPFlags = cms.bool( False ),
    firstAuxTS = cms.int32( 4 ),
    digistat = cms.PSet(  ),
    hfTimingTrustParameters = cms.PSet(  ),
    PETstat = cms.PSet(  ),
    setSaturationFlags = cms.bool( False ),
    setNegativeFlags = cms.bool( False ),
    useLeakCorrection = cms.bool( False ),
    setTimingTrustFlags = cms.bool( False ),
    S8S1stat = cms.PSet(  ),
    correctForPhaseContainment = cms.bool( True ),
    correctForTimeslew = cms.bool( True ),
    setNoiseFlags = cms.bool( False ),
    correctTiming = cms.bool( False ),
    recoParamsFromDB = cms.bool( True ),
    Subdetector = cms.string( "HO" ),
    dataOOTCorrectionCategory = cms.string( "Data" ),
    dropZSmarkedPassed = cms.bool( True ),
    setPulseShapeFlags = cms.bool( False ),
    firstSample = cms.int32( 4 )
)
fragment.hltTowerMakerForAll = cms.EDProducer( "CaloTowersCreator",
    EBSumThreshold = cms.double( 0.2 ),
    MomHBDepth = cms.double( 0.2 ),
    UseEtEBTreshold = cms.bool( False ),
    hfInput = cms.InputTag( "hltHfreco" ),
    AllowMissingInputs = cms.bool( False ),
    HEDThreshold1 = cms.double( 0.8 ),
    MomEEDepth = cms.double( 0.0 ),
    EESumThreshold = cms.double( 0.45 ),
    HBGrid = cms.vdouble(  ),
    HcalAcceptSeverityLevelForRejectedHit = cms.uint32( 9999 ),
    HBThreshold = cms.double( 0.7 ),
    EcalSeveritiesToBeUsedInBadTowers = cms.vstring(  ),
    UseEcalRecoveredHits = cms.bool( False ),
    MomConstrMethod = cms.int32( 1 ),
    MomHEDepth = cms.double( 0.4 ),
    HcalThreshold = cms.double( -1000.0 ),
    HF2Weights = cms.vdouble(  ),
    HOWeights = cms.vdouble(  ),
    EEGrid = cms.vdouble(  ),
    UseSymEBTreshold = cms.bool( False ),
    EEWeights = cms.vdouble(  ),
    EEWeight = cms.double( 1.0 ),
    UseHO = cms.bool( False ),
    HBWeights = cms.vdouble(  ),
    HF1Weight = cms.double( 1.0 ),
    missingHcalRescaleFactorForEcal = cms.double( 0.0 ),
    HESThreshold1 = cms.double( 0.8 ),
    HEDWeights = cms.vdouble(  ),
    EBWeight = cms.double( 1.0 ),
    HF1Grid = cms.vdouble(  ),
    EBWeights = cms.vdouble(  ),
    HOWeight = cms.double( 1.0E-99 ),
    HESWeight = cms.double( 1.0 ),
    HESThreshold = cms.double( 0.8 ),
    hbheInput = cms.InputTag( "hltHbhereco" ),
    HF2Weight = cms.double( 1.0 ),
    HBThreshold1 = cms.double( 0.7 ),
    HF2Threshold = cms.double( 0.85 ),
    HcalAcceptSeverityLevel = cms.uint32( 9 ),
    HBThreshold2 = cms.double( 0.7 ),
    EEThreshold = cms.double( 0.3 ),
    HOThresholdPlus1 = cms.double( 3.5 ),
    HOThresholdPlus2 = cms.double( 3.5 ),
    HF1Weights = cms.vdouble(  ),
    hoInput = cms.InputTag( "hltHoreco" ),
    HF1Threshold = cms.double( 0.5 ),
    HcalPhase = cms.int32( 0 ),
    HESGrid = cms.vdouble(  ),
    EcutTower = cms.double( -1000.0 ),
    UseRejectedRecoveredEcalHits = cms.bool( False ),
    UseEtEETreshold = cms.bool( False ),
    HESWeights = cms.vdouble(  ),
    HOThresholdMinus1 = cms.double( 3.5 ),
    EcalRecHitSeveritiesToBeExcluded = cms.vstring( 'kTime',
      'kWeird',
      'kBad' ),
    HEDWeight = cms.double( 1.0 ),
    UseSymEETreshold = cms.bool( False ),
    HEDThreshold = cms.double( 0.8 ),
    UseRejectedHitsOnly = cms.bool( False ),
    EBThreshold = cms.double( 0.07 ),
    HEDGrid = cms.vdouble(  ),
    UseHcalRecoveredHits = cms.bool( False ),
    HOThresholdMinus2 = cms.double( 3.5 ),
    HOThreshold0 = cms.double( 3.5 ),
    ecalInputs = cms.VInputTag( 'hltEcalRecHit:EcalRecHitsEB','hltEcalRecHit:EcalRecHitsEE' ),
    UseRejectedRecoveredHcalHits = cms.bool( False ),
    MomEBDepth = cms.double( 0.3 ),
    HBWeight = cms.double( 1.0 ),
    HF2Grid = cms.vdouble(  ),
    HOGrid = cms.vdouble(  ),
    EBGrid = cms.vdouble(  )
)
fragment.hltAK4CaloJetsPF = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    useMassDropTagger = cms.bool( False ),
    doAreaFastjet = cms.bool( False ),
    muMin = cms.double( -1.0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( False ),
    subtractorName = cms.string( "" ),
    dRMax = cms.double( -1.0 ),
    useExplicitGhosts = cms.bool( False ),
    puWidth = cms.double( 0.0 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    R0 = cms.double( -1.0 ),
    jetType = cms.string( "CaloJet" ),
    muCut = cms.double( -1.0 ),
    subjetPtMin = cms.double( -1.0 ),
    csRParam = cms.double( -1.0 ),
    MinVtxNdof = cms.int32( 5 ),
    minSeed = cms.uint32( 0 ),
    voronoiRfact = cms.double( -9.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "AntiKt" ),
    writeCompound = cms.bool( False ),
    muMax = cms.double( -1.0 ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    restrictInputs = cms.bool( False ),
    useDynamicFiltering = cms.bool( False ),
    nExclude = cms.uint32( 0 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    yMin = cms.double( -1.0 ),
    jetCollInstanceName = cms.string( "" ),
    useFiltering = cms.bool( False ),
    maxInputs = cms.uint32( 1 ),
    rFiltFactor = cms.double( -1.0 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    rFilt = cms.double( -1.0 ),
    yMax = cms.double( -1.0 ),
    zcut = cms.double( -1.0 ),
    useTrimming = cms.bool( False ),
    puCenters = cms.vdouble(  ),
    MaxVtxZ = cms.double( 15.0 ),
    rParam = cms.double( 0.4 ),
    csRho_EtaMax = cms.double( -1.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    dRMin = cms.double( -1.0 ),
    gridSpacing = cms.double( -1.0 ),
    doFastJetNonUniform = cms.bool( False ),
    usePruning = cms.bool( False ),
    maxDepth = cms.int32( -1 ),
    yCut = cms.double( -1.0 ),
    useSoftDrop = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    UseOnlyOnePV = cms.bool( False ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    correctShape = cms.bool( False ),
    rcut_factor = cms.double( -1.0 ),
    src = cms.InputTag( "hltTowerMakerForAll" ),
    gridMaxRapidity = cms.double( -1.0 ),
    sumRecHits = cms.bool( False ),
    jetPtMin = cms.double( 1.0 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "NotUsed" ),
    verbosity = cms.int32( 0 ),
    inputEtMin = cms.double( 0.3 ),
    useConstituentSubtraction = cms.bool( False ),
    beta = cms.double( -1.0 ),
    trimPtFracMin = cms.double( -1.0 ),
    radiusPU = cms.double( 0.4 ),
    nFilt = cms.int32( -1 ),
    useKtPruning = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    useCMSBoostedTauSeedingAlgorithm = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    writeJetsWithConst = cms.bool( False ),
    inputEMin = cms.double( 0.0 )
)
fragment.hltAK4CaloJetsPFEt5 = cms.EDFilter( "EtMinCaloJetSelector",
    filter = cms.bool( False ),
    src = cms.InputTag( "hltAK4CaloJetsPF" ),
    etMin = cms.double( 5.0 )
)
fragment.hltTauJet5 = cms.EDFilter( "HLT1CaloJet",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltAK4CaloJetsPFEt5" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 ),
    MinPt = cms.double( 5.0 )
)
fragment.hltPixelTracksFilter = cms.EDProducer( "PixelTrackFilterByKinematicsProducer",
    chi2 = cms.double( 1000.0 ),
    nSigmaTipMaxTolerance = cms.double( 0.0 ),
    ptMin = cms.double( 0.1 ),
    nSigmaInvPtTolerance = cms.double( 0.0 ),
    tipMax = cms.double( 1.0 )
)
fragment.hltPixelTracksFitter = cms.EDProducer( "PixelFitterByHelixProjectionsProducer",
    scaleErrorsForBPix1 = cms.bool( False ),
    scaleFactor = cms.double( 0.65 )
)
fragment.hltPixelTracksTrackingRegions = cms.EDProducer( "GlobalTrackingRegionFromBeamSpotEDProducer",
    RegionPSet = cms.PSet(
      nSigmaZ = cms.double( 4.0 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      ptMin = cms.double( 0.8 ),
      originRadius = cms.double( 0.02 ),
      precise = cms.bool( True )
    )
)
fragment.hltPixelLayerQuadruplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3+BPix4',
      'BPix1+BPix2+BPix3+FPix1_pos',
      'BPix1+BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos+FPix2_pos',
      'BPix1+BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_neg+FPix2_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  )
)
fragment.hltPixelTracksHitDoublets = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltPixelTracksTrackingRegions" ),
    layerPairs = cms.vuint32( 0, 1, 2 ),
    clusterCheck = cms.InputTag( "" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElementTotal = cms.uint32( 50000000 ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltPixelLayerQuadruplets" )
)
fragment.hltPixelTracksHitQuadruplets = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAThetaCut = cms.double( 0.002 ),
    SeedComparitorPSet = cms.PSet(
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "LowPtClusterShapeSeedComparitor" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCache" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltPixelTracksHitDoublets" ),
    fitFastCircle = cms.bool( True ),
    CAHardPtCut = cms.double( 0.0 ),
    maxChi2 = cms.PSet(
      value2 = cms.double( 50.0 ),
      value1 = cms.double( 200.0 ),
      pt1 = cms.double( 0.7 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 2.0 )
    ),
    CAPhiCut = cms.double( 0.2 ),
    useBendingCorrection = cms.bool( True ),
    fitFastCircleChi2Cut = cms.bool( True )
)
fragment.hltPixelTracks = cms.EDProducer( "PixelTrackProducer",
    Filter = cms.InputTag( "hltPixelTracksFilter" ),
    Cleaner = cms.string( "hltPixelTracksCleanerBySharedHits" ),
    passLabel = cms.string( "" ),
    Fitter = cms.InputTag( "hltPixelTracksFitter" ),
    SeedingHitSets = cms.InputTag( "hltPixelTracksHitQuadruplets" )
)
fragment.hltPixelVertices = cms.EDProducer( "PixelVertexProducer",
    WtAverage = cms.bool( True ),
    Method2 = cms.bool( True ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) ),
    Verbosity = cms.int32( 0 ),
    UseError = cms.bool( True ),
    TrackCollection = cms.InputTag( "hltPixelTracks" ),
    PtMin = cms.double( 1.0 ),
    NTrkMin = cms.int32( 2 ),
    ZOffset = cms.double( 5.0 ),
    Finder = cms.string( "DivisiveVertexFinder" ),
    ZSeparation = cms.double( 0.05 )
)
fragment.hltTrimmedPixelVertices = cms.EDProducer( "PixelVertexCollectionTrimmer",
    minSumPt2 = cms.double( 0.0 ),
    PVcomparer = cms.PSet(  refToPSet_ = cms.string( "HLTPSetPvClusterComparerForIT" ) ),
    maxVtx = cms.uint32( 100 ),
    fractionSumPt2 = cms.double( 0.3 ),
    src = cms.InputTag( "hltPixelVertices" )
)
fragment.hltIter0PFLowPixelSeedsFromPixelTracks = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 0.3 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( False ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromProtoTracks" ) ),
    InputVertexCollection = cms.InputTag( "hltTrimmedPixelVertices" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    InputCollection = cms.InputTag( "hltPixelTracks" ),
    originRadius = cms.double( 0.1 )
)
fragment.hltIter0PFlowCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter0PFLowPixelSeedsFromPixelTracks" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter0GroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
fragment.hltIter0PFlowCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter0PFlowCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltSiStripClusters" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter0" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
fragment.hltIter0PFlowTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter0PFlowCtfWithMaterialTracks" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltTrimmedPixelVertices" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet(
      minPixelHits = cms.vint32( 0, 3, 4 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
      dr_par = cms.PSet(
        d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
        dr_par2 = cms.vdouble( 0.3, 0.3, 0.3 ),
        dr_par1 = cms.vdouble( 0.4, 0.4, 0.4 ),
        dr_exp = cms.vint32( 4, 4, 4 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 3, 4 ),
      dz_par = cms.PSet(
        dz_par1 = cms.vdouble( 0.4, 0.4, 0.4 ),
        dz_par2 = cms.vdouble( 0.35, 0.35, 0.35 ),
        dz_exp = cms.vint32( 4, 4, 4 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 16.0 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 4 )
    ),
    ignoreVertices = cms.bool( False )
)
fragment.hltIter0PFlowTrackSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltIter0PFlowCtfWithMaterialTracks" ),
    originalQualVals = cms.InputTag( 'hltIter0PFlowTrackCutClassifier','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltIter0PFlowTrackCutClassifier','MVAValues' )
)
fragment.hltIter1ClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 9.0 ),
    trajectories = cms.InputTag( "hltIter0PFlowTrackSelectionHighPurity" ),
    oldClusterRemovalInfo = cms.InputTag( "" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClusters" ),
    TrackQuality = cms.string( "highPurity" )
)
fragment.hltIter1MaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter1ClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClusters" )
)
fragment.hltIter1PixelLayerQuadruplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3+BPix4',
      'BPix1+BPix2+BPix3+FPix1_pos',
      'BPix1+BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos+FPix2_pos',
      'BPix1+BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_neg+FPix2_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter1ClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter1ClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  )
)
fragment.hltIter1PFlowPixelTrackingRegions = cms.EDProducer( "GlobalTrackingRegionWithVerticesEDProducer",
    RegionPSet = cms.PSet(
      useFixedError = cms.bool( True ),
      nSigmaZ = cms.double( 4.0 ),
      VertexCollection = cms.InputTag( "hltTrimmedPixelVertices" ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      useFoundVertices = cms.bool( True ),
      fixedError = cms.double( 0.2 ),
      sigmaZVertex = cms.double( 3.0 ),
      useFakeVertices = cms.bool( False ),
      ptMin = cms.double( 0.4 ),
      originRadius = cms.double( 0.05 ),
      precise = cms.bool( True ),
      useMultipleScattering = cms.bool( False )
    )
)
fragment.hltIter1PFlowPixelClusterCheck = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 40000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" )
)
fragment.hltIter1PFlowPixelHitDoublets = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltIter1PFlowPixelTrackingRegions" ),
    layerPairs = cms.vuint32( 0, 1, 2 ),
    clusterCheck = cms.InputTag( "hltIter1PFlowPixelClusterCheck" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElementTotal = cms.uint32( 50000000 ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltIter1PixelLayerQuadruplets" )
)
fragment.hltIter1PFlowPixelHitQuadruplets = cms.EDProducer( "CAHitQuadrupletEDProducer",
    CAThetaCut = cms.double( 0.004 ),
    SeedComparitorPSet = cms.PSet(
      clusterShapeHitFilter = cms.string( "ClusterShapeHitFilter" ),
      ComponentName = cms.string( "none" ),
      clusterShapeCacheSrc = cms.InputTag( "hltSiPixelClustersCache" )
    ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltIter1PFlowPixelHitDoublets" ),
    fitFastCircle = cms.bool( True ),
    CAHardPtCut = cms.double( 0.0 ),
    maxChi2 = cms.PSet(
      value2 = cms.double( 100.0 ),
      value1 = cms.double( 1000.0 ),
      pt1 = cms.double( 0.4 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 2.0 )
    ),
    CAPhiCut = cms.double( 0.3 ),
    useBendingCorrection = cms.bool( True ),
    fitFastCircleChi2Cut = cms.bool( True )
)
fragment.hltIter1PixelTracks = cms.EDProducer( "PixelTrackProducer",
    Filter = cms.InputTag( "hltPixelTracksFilter" ),
    Cleaner = cms.string( "hltPixelTracksCleanerBySharedHits" ),
    passLabel = cms.string( "" ),
    Fitter = cms.InputTag( "hltPixelTracksFitter" ),
    SeedingHitSets = cms.InputTag( "hltIter1PFlowPixelHitQuadruplets" )
)
fragment.hltIter1PFLowPixelSeedsFromPixelTracks = cms.EDProducer( "SeedGeneratorFromProtoTracksEDProducer",
    useEventsWithNoVertex = cms.bool( True ),
    originHalfLength = cms.double( 0.3 ),
    useProtoTrackKinematics = cms.bool( False ),
    usePV = cms.bool( False ),
    SeedCreatorPSet = cms.PSet(  refToPSet_ = cms.string( "HLTSeedFromProtoTracks" ) ),
    InputVertexCollection = cms.InputTag( "hltTrimmedPixelVertices" ),
    TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
    InputCollection = cms.InputTag( "hltIter1PixelTracks" ),
    originRadius = cms.double( 0.1 )
)
fragment.hltIter1PFlowCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter1PFLowPixelSeedsFromPixelTracks" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter1MaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter1GroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
fragment.hltIter1PFlowCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter1PFlowCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter1MaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter1" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
fragment.hltIter1PFlowTrackCutClassifierPrompt = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter1PFlowCtfWithMaterialTracks" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltTrimmedPixelVertices" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet(
      minPixelHits = cms.vint32( 0, 0, 2 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
      dr_par = cms.PSet(
        d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
        dr_par2 = cms.vdouble( 3.40282346639E38, 1.0, 0.85 ),
        dr_par1 = cms.vdouble( 3.40282346639E38, 1.0, 0.9 ),
        dr_exp = cms.vint32( 3, 3, 3 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 0, 0 ),
      dz_par = cms.PSet(
        dz_par1 = cms.vdouble( 3.40282346639E38, 1.0, 0.9 ),
        dz_par2 = cms.vdouble( 3.40282346639E38, 1.0, 0.8 ),
        dz_exp = cms.vint32( 3, 3, 3 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 3.40282346639E38, 1.0, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 16.0 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 3.40282346639E38, 1.0, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 3 )
    ),
    ignoreVertices = cms.bool( False )
)
fragment.hltIter1PFlowTrackCutClassifierDetached = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter1PFlowCtfWithMaterialTracks" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltTrimmedPixelVertices" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet(
      minPixelHits = cms.vint32( 0, 0, 1 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
      dr_par = cms.PSet(
        d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
        dr_par2 = cms.vdouble( 1.0, 1.0, 1.0 ),
        dr_par1 = cms.vdouble( 1.0, 1.0, 1.0 ),
        dr_exp = cms.vint32( 4, 4, 4 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
      ),
      maxLostLayers = cms.vint32( 99, 3, 3 ),
      min3DLayers = cms.vint32( 1, 2, 3 ),
      dz_par = cms.PSet(
        dz_par1 = cms.vdouble( 1.0, 1.0, 1.0 ),
        dz_par2 = cms.vdouble( 1.0, 1.0, 1.0 ),
        dz_exp = cms.vint32( 4, 4, 4 )
      ),
      minNVtxTrk = cms.int32( 2 ),
      maxDz = cms.vdouble( 3.40282346639E38, 1.0, 3.40282346639E38 ),
      minNdof = cms.vdouble( -1.0, -1.0, -1.0 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 16.0 ),
      maxChi2n = cms.vdouble( 1.0, 0.7, 0.4 ),
      maxDr = cms.vdouble( 3.40282346639E38, 1.0, 3.40282346639E38 ),
      minLayers = cms.vint32( 5, 5, 5 )
    ),
    ignoreVertices = cms.bool( False )
)
fragment.hltIter1PFlowTrackCutClassifierMerged = cms.EDProducer( "ClassifierMerger",
    inputClassifiers = cms.vstring( 'hltIter1PFlowTrackCutClassifierPrompt',
      'hltIter1PFlowTrackCutClassifierDetached' )
)
fragment.hltIter1PFlowTrackSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltIter1PFlowCtfWithMaterialTracks" ),
    originalQualVals = cms.InputTag( 'hltIter1PFlowTrackCutClassifierMerged','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltIter1PFlowTrackCutClassifierMerged','MVAValues' )
)
fragment.hltIter1Merged = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter0PFlowTrackSelectionHighPurity','hltIter1PFlowTrackSelectionHighPurity' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet(
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter0PFlowTrackSelectionHighPurity','hltIter1PFlowTrackSelectionHighPurity' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltIter1TrackRefsForJets4Iter2 = cms.EDProducer( "ChargedRefCandidateProducer",
    src = cms.InputTag( "hltIter1Merged" ),
    particleType = cms.string( "pi+" )
)
fragment.hltAK4Iter1TrackJets4Iter2 = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    useMassDropTagger = cms.bool( False ),
    doAreaFastjet = cms.bool( False ),
    muMin = cms.double( -1.0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( False ),
    subtractorName = cms.string( "" ),
    dRMax = cms.double( -1.0 ),
    useExplicitGhosts = cms.bool( False ),
    puWidth = cms.double( 0.0 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    R0 = cms.double( -1.0 ),
    jetType = cms.string( "TrackJet" ),
    muCut = cms.double( -1.0 ),
    subjetPtMin = cms.double( -1.0 ),
    csRParam = cms.double( -1.0 ),
    MinVtxNdof = cms.int32( 0 ),
    minSeed = cms.uint32( 14327 ),
    voronoiRfact = cms.double( 0.9 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "AntiKt" ),
    writeCompound = cms.bool( False ),
    muMax = cms.double( -1.0 ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    restrictInputs = cms.bool( False ),
    useDynamicFiltering = cms.bool( False ),
    nExclude = cms.uint32( 0 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    yMin = cms.double( -1.0 ),
    jetCollInstanceName = cms.string( "" ),
    useFiltering = cms.bool( False ),
    maxInputs = cms.uint32( 1 ),
    rFiltFactor = cms.double( -1.0 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    rFilt = cms.double( -1.0 ),
    yMax = cms.double( -1.0 ),
    zcut = cms.double( -1.0 ),
    useTrimming = cms.bool( False ),
    puCenters = cms.vdouble(  ),
    MaxVtxZ = cms.double( 30.0 ),
    rParam = cms.double( 0.4 ),
    csRho_EtaMax = cms.double( -1.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    dRMin = cms.double( -1.0 ),
    gridSpacing = cms.double( -1.0 ),
    doFastJetNonUniform = cms.bool( False ),
    usePruning = cms.bool( False ),
    maxDepth = cms.int32( -1 ),
    yCut = cms.double( -1.0 ),
    useSoftDrop = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.5 ),
    UseOnlyOnePV = cms.bool( True ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    correctShape = cms.bool( False ),
    rcut_factor = cms.double( -1.0 ),
    src = cms.InputTag( "hltIter1TrackRefsForJets4Iter2" ),
    gridMaxRapidity = cms.double( -1.0 ),
    sumRecHits = cms.bool( False ),
    jetPtMin = cms.double( 7.5 ),
    puPtMin = cms.double( 0.0 ),
    srcPVs = cms.InputTag( "hltTrimmedPixelVertices" ),
    verbosity = cms.int32( 0 ),
    inputEtMin = cms.double( 0.1 ),
    useConstituentSubtraction = cms.bool( False ),
    beta = cms.double( -1.0 ),
    trimPtFracMin = cms.double( -1.0 ),
    radiusPU = cms.double( 0.4 ),
    nFilt = cms.int32( -1 ),
    useKtPruning = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.2 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    useCMSBoostedTauSeedingAlgorithm = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    writeJetsWithConst = cms.bool( False ),
    inputEMin = cms.double( 0.0 )
)
fragment.hltIter1TrackAndTauJets4Iter2 = cms.EDProducer( "TauJetSelectorForHLTTrackSeeding",
    fractionMinCaloInTauCone = cms.double( 0.7 ),
    fractionMaxChargedPUInCaloCone = cms.double( 0.3 ),
    tauConeSize = cms.double( 0.2 ),
    ptTrkMaxInCaloCone = cms.double( 1.4 ),
    isolationConeSize = cms.double( 0.5 ),
    inputTrackJetTag = cms.InputTag( "hltAK4Iter1TrackJets4Iter2" ),
    nTrkMaxInCaloCone = cms.int32( 0 ),
    inputCaloJetTag = cms.InputTag( "hltAK4CaloJetsPFEt5" ),
    etaMinCaloJet = cms.double( -2.7 ),
    etaMaxCaloJet = cms.double( 2.7 ),
    ptMinCaloJet = cms.double( 10.0 ),
    inputTrackTag = cms.InputTag( "hltIter1Merged" )
)
fragment.hltIter2ClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 16.0 ),
    trajectories = cms.InputTag( "hltIter1PFlowTrackSelectionHighPurity" ),
    oldClusterRemovalInfo = cms.InputTag( "hltIter1ClustersRefRemoval" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClusters" ),
    TrackQuality = cms.string( "highPurity" )
)
fragment.hltIter2MaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltIter2ClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClusters" )
)
fragment.hltIter2PixelLayerTriplets = cms.EDProducer( "SeedingLayersEDProducer",
    layerList = cms.vstring( 'BPix1+BPix2+BPix3',
      'BPix2+BPix3+BPix4',
      'BPix1+BPix3+BPix4',
      'BPix1+BPix2+BPix4',
      'BPix2+BPix3+FPix1_pos',
      'BPix2+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix1_pos',
      'BPix1+BPix2+FPix1_neg',
      'BPix2+FPix1_pos+FPix2_pos',
      'BPix2+FPix1_neg+FPix2_neg',
      'BPix1+FPix1_pos+FPix2_pos',
      'BPix1+FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix2_pos+FPix3_pos',
      'FPix1_neg+FPix2_neg+FPix3_neg',
      'BPix1+BPix3+FPix1_pos',
      'BPix1+BPix2+FPix2_pos',
      'BPix1+BPix3+FPix1_neg',
      'BPix1+BPix2+FPix2_neg',
      'BPix1+FPix2_neg+FPix3_neg',
      'BPix1+FPix1_neg+FPix3_neg',
      'BPix1+FPix2_pos+FPix3_pos',
      'BPix1+FPix1_pos+FPix3_pos' ),
    MTOB = cms.PSet(  ),
    TEC = cms.PSet(  ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter2ClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    MTEC = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    TID = cms.PSet(  ),
    TOB = cms.PSet(  ),
    BPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltIter2ClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    TIB = cms.PSet(  )
)
fragment.hltIter2PFlowPixelTrackingRegions = cms.EDProducer( "CandidateSeededTrackingRegionsEDProducer",
    RegionPSet = cms.PSet(
      vertexCollection = cms.InputTag( "hltTrimmedPixelVertices" ),
      zErrorVetex = cms.double( 0.05 ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorBeamSpot = cms.double( 15.0 ),
      maxNVertices = cms.int32( 10 ),
      maxNRegions = cms.int32( 100 ),
      nSigmaZVertex = cms.double( 4.0 ),
      nSigmaZBeamSpot = cms.double( 3.0 ),
      ptMin = cms.double( 0.4 ),
      mode = cms.string( "VerticesFixed" ),
      input = cms.InputTag( "hltIter1TrackAndTauJets4Iter2" ),
      searchOpt = cms.bool( True ),
      whereToUseMeasurementTracker = cms.string( "ForSiStrips" ),
      originRadius = cms.double( 0.025 ),
      measurementTrackerName = cms.InputTag( "hltIter2MaskedMeasurementTrackerEvent" ),
      precise = cms.bool( True ),
      deltaEta = cms.double( 0.8 ),
      deltaPhi = cms.double( 0.8 )
    )
)
fragment.hltIter2PFlowPixelClusterCheck = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 40000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" )
)
fragment.hltIter2PFlowPixelHitDoublets = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "hltIter2PFlowPixelTrackingRegions" ),
    layerPairs = cms.vuint32( 0, 1 ),
    clusterCheck = cms.InputTag( "hltIter2PFlowPixelClusterCheck" ),
    produceSeedingHitSets = cms.bool( False ),
    produceIntermediateHitDoublets = cms.bool( True ),
    trackingRegionsSeedingLayers = cms.InputTag( "" ),
    maxElementTotal = cms.uint32( 50000000 ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "hltIter2PixelLayerTriplets" )
)
fragment.hltIter2PFlowPixelHitTriplets = cms.EDProducer( "CAHitTripletEDProducer",
    CAHardPtCut = cms.double( 0.3 ),
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    extraHitRPhitolerance = cms.double( 0.032 ),
    doublets = cms.InputTag( "hltIter2PFlowPixelHitDoublets" ),
    CAThetaCut = cms.double( 0.004 ),
    maxChi2 = cms.PSet(
      value2 = cms.double( 6.0 ),
      value1 = cms.double( 100.0 ),
      pt1 = cms.double( 0.4 ),
      enabled = cms.bool( True ),
      pt2 = cms.double( 8.0 )
    ),
    CAPhiCut = cms.double( 0.1 ),
    useBendingCorrection = cms.bool( True )
)
fragment.hltIter2PFlowPixelSeeds = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsTripletOnlyEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltIter2PFlowPixelHitTriplets" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
fragment.hltIter2PFlowCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltIter2PFlowPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2MaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2GroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
fragment.hltIter2PFlowCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltIter2PFlowCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltIter2MaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltIter2" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
fragment.hltIter2PFlowTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltIter2PFlowCtfWithMaterialTracks" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltTrimmedPixelVertices" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet(
      minPixelHits = cms.vint32( 0, 0, 0 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
      dr_par = cms.PSet(
        d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
        dr_par2 = cms.vdouble( 3.40282346639E38, 0.3, 0.3 ),
        dr_par1 = cms.vdouble( 3.40282346639E38, 0.4, 0.4 ),
        dr_exp = cms.vint32( 4, 4, 4 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 0, 0 ),
      dz_par = cms.PSet(
        dz_par1 = cms.vdouble( 3.40282346639E38, 0.4, 0.4 ),
        dz_par2 = cms.vdouble( 3.40282346639E38, 0.35, 0.35 ),
        dz_exp = cms.vint32( 4, 4, 4 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 16.0 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 3 )
    ),
    ignoreVertices = cms.bool( False )
)
fragment.hltIter2PFlowTrackSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltIter2PFlowCtfWithMaterialTracks" ),
    originalQualVals = cms.InputTag( 'hltIter2PFlowTrackCutClassifier','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltIter2PFlowTrackCutClassifier','MVAValues' )
)
fragment.hltIter2Merged = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter1Merged','hltIter2PFlowTrackSelectionHighPurity' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet(
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter1Merged','hltIter2PFlowTrackSelectionHighPurity' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltDoubletRecoveryClustersRefRemoval = cms.EDProducer( "TrackClusterRemover",
    trackClassifier = cms.InputTag( '','QualityMasks' ),
    minNumberOfLayersWithMeasBeforeFiltering = cms.int32( 0 ),
    maxChi2 = cms.double( 16.0 ),
    trajectories = cms.InputTag( "hltIter2PFlowTrackSelectionHighPurity" ),
    oldClusterRemovalInfo = cms.InputTag( "hltIter2ClustersRefRemoval" ),
    stripClusters = cms.InputTag( "hltSiStripRawToClustersFacility" ),
    overrideTrkQuals = cms.InputTag( "" ),
    pixelClusters = cms.InputTag( "hltSiPixelClusters" ),
    TrackQuality = cms.string( "highPurity" )
)
fragment.hltDoubletRecoveryMaskedMeasurementTrackerEvent = cms.EDProducer( "MaskedMeasurementTrackerEventProducer",
    clustersToSkip = cms.InputTag( "hltDoubletRecoveryClustersRefRemoval" ),
    OnDemand = cms.bool( False ),
    src = cms.InputTag( "hltSiStripClusters" )
)
fragment.hltDoubletRecoveryPixelLayersAndRegions = cms.EDProducer( "PixelInactiveAreaTrackingRegionsSeedingLayersProducer",
    inactivePixelDetectorLabels = cms.VInputTag( 'hltSiPixelDigis' ),
    layerList = cms.vstring( 'BPix1+BPix2',
      'BPix1+BPix3',
      'BPix1+BPix4',
      'BPix2+BPix3',
      'BPix2+BPix4',
      'BPix3+BPix4',
      'BPix1+FPix1_pos',
      'BPix1+FPix1_neg',
      'BPix1+FPix2_pos',
      'BPix1+FPix2_neg',
      'BPix1+FPix3_pos',
      'BPix1+FPix3_neg',
      'BPix2+FPix1_pos',
      'BPix2+FPix1_neg',
      'BPix2+FPix2_pos',
      'BPix2+FPix2_neg',
      'BPix3+FPix1_pos',
      'BPix3+FPix1_neg',
      'FPix1_pos+FPix2_pos',
      'FPix1_neg+FPix2_neg',
      'FPix1_pos+FPix3_pos',
      'FPix1_neg+FPix3_neg',
      'FPix2_pos+FPix3_pos',
      'FPix2_neg+FPix3_neg' ),
    MTOB = cms.PSet(  ),
    MTIB = cms.PSet(  ),
    RegionPSet = cms.PSet(
      precise = cms.bool( True ),
      beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
      zErrorBeamSpot = cms.double( 15.0 ),
      nSigmaZVertex = cms.double( 3.0 ),
      nSigmaZBeamSpot = cms.double( 4.0 ),
      measurementTrackerName = cms.InputTag( "hltDoubletRecoveryMaskedMeasurementTrackerEvent" ),
      extraEta = cms.double( 0.0 ),
      vertexCollection = cms.InputTag( "hltTrimmedPixelVertices" ),
      ptMin = cms.double( 1.2 ),
      searchOpt = cms.bool( False ),
      whereToUseMeasurementTracker = cms.string( "ForSiStrips" ),
      maxNVertices = cms.int32( 3 ),
      extraPhi = cms.double( 0.0 ),
      originRadius = cms.double( 0.015 ),
      zErrorVertex = cms.double( 0.03 ),
      operationMode = cms.string( "VerticesFixed" )
    ),
    TEC = cms.PSet(  ),
    ignoreSingleFPixPanelModules = cms.bool( True ),
    TID = cms.PSet(  ),
    BPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0027 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltDoubletRecoveryClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.006 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    MTID = cms.PSet(  ),
    FPix = cms.PSet(
      hitErrorRPhi = cms.double( 0.0051 ),
      TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
      skipClusters = cms.InputTag( "hltDoubletRecoveryClustersRefRemoval" ),
      useErrorsFromParam = cms.bool( True ),
      hitErrorRZ = cms.double( 0.0036 ),
      HitProducer = cms.string( "hltSiPixelRecHits" )
    ),
    MTEC = cms.PSet(  ),
    badPixelFEDChannelCollectionLabels = cms.VInputTag( 'hltSiPixelDigis' ),
    debug = cms.untracked.bool( False ),
    TOB = cms.PSet(  ),
    createPlottingFiles = cms.untracked.bool( False ),
    TIB = cms.PSet(  )
)
fragment.hltDoubletRecoveryPFlowPixelClusterCheck = cms.EDProducer( "ClusterCheckerEDProducer",
    cut = cms.string( "" ),
    silentClusterCheck = cms.untracked.bool( False ),
    MaxNumberOfCosmicClusters = cms.uint32( 50000 ),
    PixelClusterCollectionLabel = cms.InputTag( "hltSiPixelClusters" ),
    doClusterCheck = cms.bool( False ),
    MaxNumberOfPixelClusters = cms.uint32( 40000 ),
    ClusterCollectionLabel = cms.InputTag( "hltSiStripClusters" )
)
fragment.hltDoubletRecoveryPFlowPixelHitDoublets = cms.EDProducer( "HitPairEDProducer",
    trackingRegions = cms.InputTag( "" ),
    layerPairs = cms.vuint32( 0 ),
    clusterCheck = cms.InputTag( "hltDoubletRecoveryPFlowPixelClusterCheck" ),
    produceSeedingHitSets = cms.bool( True ),
    produceIntermediateHitDoublets = cms.bool( False ),
    trackingRegionsSeedingLayers = cms.InputTag( "hltDoubletRecoveryPixelLayersAndRegions" ),
    maxElementTotal = cms.uint32( 50000000 ),
    maxElement = cms.uint32( 0 ),
    seedingLayers = cms.InputTag( "" )
)
fragment.hltDoubletRecoveryPFlowPixelSeeds = cms.EDProducer( "SeedCreatorFromRegionConsecutiveHitsEDProducer",
    SeedComparitorPSet = cms.PSet(  ComponentName = cms.string( "none" ) ),
    forceKinematicWithRegionDirection = cms.bool( False ),
    magneticField = cms.string( "ParabolicMf" ),
    SeedMomentumForBOFF = cms.double( 5.0 ),
    OriginTransverseErrorMultiplier = cms.double( 1.0 ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    MinOneOverPtError = cms.double( 1.0 ),
    seedingHitSets = cms.InputTag( "hltDoubletRecoveryPFlowPixelHitDoublets" ),
    propagator = cms.string( "PropagatorWithMaterialParabolicMf" )
)
fragment.hltDoubletRecoveryPFlowCkfTrackCandidates = cms.EDProducer( "CkfTrackCandidateMaker",
    src = cms.InputTag( "hltDoubletRecoveryPFlowPixelSeeds" ),
    maxSeedsBeforeCleaning = cms.uint32( 1000 ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    TransientInitialStateEstimatorParameters = cms.PSet(
      propagatorAlongTISE = cms.string( "PropagatorWithMaterialParabolicMf" ),
      numberMeasurementsForFit = cms.int32( 4 ),
      propagatorOppositeTISE = cms.string( "PropagatorWithMaterialParabolicMfOpposite" )
    ),
    TrajectoryCleaner = cms.string( "hltESPTrajectoryCleanerBySharedHits" ),
    MeasurementTrackerEvent = cms.InputTag( "hltDoubletRecoveryMaskedMeasurementTrackerEvent" ),
    cleanTrajectoryAfterInOut = cms.bool( False ),
    useHitsSplitting = cms.bool( False ),
    RedundantSeedCleaner = cms.string( "CachingSeedCleanerBySharedInput" ),
    reverseTrajectories = cms.bool( False ),
    doSeedingRegionRebuilding = cms.bool( False ),
    maxNSeeds = cms.uint32( 100000 ),
    TrajectoryBuilderPSet = cms.PSet(  refToPSet_ = cms.string( "HLTIter2GroupedCkfTrajectoryBuilderIT" ) ),
    NavigationSchool = cms.string( "SimpleNavigationSchool" ),
    TrajectoryBuilder = cms.string( "" )
)
fragment.hltDoubletRecoveryPFlowCtfWithMaterialTracks = cms.EDProducer( "TrackProducer",
    src = cms.InputTag( "hltDoubletRecoveryPFlowCkfTrackCandidates" ),
    SimpleMagneticField = cms.string( "ParabolicMf" ),
    clusterRemovalInfo = cms.InputTag( "" ),
    beamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    MeasurementTrackerEvent = cms.InputTag( "hltDoubletRecoveryMaskedMeasurementTrackerEvent" ),
    Fitter = cms.string( "hltESPFittingSmootherIT" ),
    useHitsSplitting = cms.bool( False ),
    MeasurementTracker = cms.string( "" ),
    AlgorithmName = cms.string( "hltDoubletRecovery" ),
    alias = cms.untracked.string( "ctfWithMaterialTracks" ),
    NavigationSchool = cms.string( "" ),
    TrajectoryInEvent = cms.bool( False ),
    TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
    GeometricInnerState = cms.bool( True ),
    useSimpleMF = cms.bool( True ),
    Propagator = cms.string( "hltESPRungeKuttaTrackerPropagator" )
)
fragment.hltDoubletRecoveryPFlowTrackCutClassifier = cms.EDProducer( "TrackCutClassifier",
    src = cms.InputTag( "hltDoubletRecoveryPFlowCtfWithMaterialTracks" ),
    beamspot = cms.InputTag( "hltOnlineBeamSpot" ),
    vertices = cms.InputTag( "hltTrimmedPixelVertices" ),
    qualityCuts = cms.vdouble( -0.7, 0.1, 0.7 ),
    mva = cms.PSet(
      minPixelHits = cms.vint32( 0, 0, 0 ),
      maxDzWrtBS = cms.vdouble( 3.40282346639E38, 24.0, 15.0 ),
      dr_par = cms.PSet(
        d0err = cms.vdouble( 0.003, 0.003, 0.003 ),
        dr_par2 = cms.vdouble( 3.40282346639E38, 0.3, 0.3 ),
        dr_par1 = cms.vdouble( 3.40282346639E38, 0.4, 0.4 ),
        dr_exp = cms.vint32( 4, 4, 4 ),
        d0err_par = cms.vdouble( 0.001, 0.001, 0.001 )
      ),
      maxLostLayers = cms.vint32( 1, 1, 1 ),
      min3DLayers = cms.vint32( 0, 0, 0 ),
      dz_par = cms.PSet(
        dz_par1 = cms.vdouble( 3.40282346639E38, 0.4, 0.4 ),
        dz_par2 = cms.vdouble( 3.40282346639E38, 0.35, 0.35 ),
        dz_exp = cms.vint32( 4, 4, 4 )
      ),
      minNVtxTrk = cms.int32( 3 ),
      maxDz = cms.vdouble( 0.5, 0.2, 3.40282346639E38 ),
      minNdof = cms.vdouble( 1.0E-5, 1.0E-5, 1.0E-5 ),
      maxChi2 = cms.vdouble( 9999.0, 25.0, 16.0 ),
      maxChi2n = cms.vdouble( 1.2, 1.0, 0.7 ),
      maxDr = cms.vdouble( 0.5, 0.03, 3.40282346639E38 ),
      minLayers = cms.vint32( 3, 3, 3 )
    ),
    ignoreVertices = cms.bool( False )
)
fragment.hltDoubletRecoveryPFlowTrackSelectionHighPurity = cms.EDProducer( "TrackCollectionFilterCloner",
    minQuality = cms.string( "highPurity" ),
    copyExtras = cms.untracked.bool( True ),
    copyTrajectories = cms.untracked.bool( False ),
    originalSource = cms.InputTag( "hltDoubletRecoveryPFlowCtfWithMaterialTracks" ),
    originalQualVals = cms.InputTag( 'hltDoubletRecoveryPFlowTrackCutClassifier','QualityMasks' ),
    originalMVAVals = cms.InputTag( 'hltDoubletRecoveryPFlowTrackCutClassifier','MVAValues' )
)
fragment.hltMergedTracks = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIter2Merged','hltDoubletRecoveryPFlowTrackSelectionHighPurity' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet(
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIter2Merged','hltDoubletRecoveryPFlowTrackSelectionHighPurity' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltPFMuonMerging = cms.EDProducer( "TrackListMerger",
    ShareFrac = cms.double( 0.19 ),
    writeOnlyTrkQuals = cms.bool( False ),
    MinPT = cms.double( 0.05 ),
    allowFirstHitShare = cms.bool( True ),
    copyExtras = cms.untracked.bool( True ),
    Epsilon = cms.double( -0.001 ),
    selectedTrackQuals = cms.VInputTag( 'hltIterL3MuonTracks','hltMergedTracks' ),
    indivShareFrac = cms.vdouble( 1.0, 1.0 ),
    MaxNormalizedChisq = cms.double( 1000.0 ),
    copyMVA = cms.bool( False ),
    FoundHitBonus = cms.double( 5.0 ),
    LostHitPenalty = cms.double( 20.0 ),
    setsToMerge = cms.VPSet(
      cms.PSet(  pQual = cms.bool( False ),
        tLists = cms.vint32( 0, 1 )
      )
    ),
    MinFound = cms.int32( 3 ),
    hasSelector = cms.vint32( 0, 0 ),
    TrackProducers = cms.VInputTag( 'hltIterL3MuonTracks','hltMergedTracks' ),
    trackAlgoPriorityOrder = cms.string( "hltESPTrackAlgoPriorityOrder" ),
    newQuality = cms.string( "confirmed" )
)
fragment.hltMuonLinks = cms.EDProducer( "MuonLinksProducerForHLT",
    pMin = cms.double( 2.5 ),
    InclusiveTrackerTrackCollection = cms.InputTag( "hltPFMuonMerging" ),
    shareHitFraction = cms.double( 0.8 ),
    LinkCollection = cms.InputTag( "hltL3MuonsIterL3Links" ),
    ptMin = cms.double( 2.5 )
)
fragment.hltMuons = cms.EDProducer( "MuonIdProducer",
    TrackExtractorPSet = cms.PSet(
      Diff_z = cms.double( 0.2 ),
      inputTrackCollection = cms.InputTag( "hltPFMuonMerging" ),
      Chi2Ndof_Max = cms.double( 1.0E64 ),
      BeamSpotLabel = cms.InputTag( "hltOnlineBeamSpot" ),
      DR_Veto = cms.double( 0.01 ),
      Pt_Min = cms.double( -1.0 ),
      DR_Max = cms.double( 1.0 ),
      DepositLabel = cms.untracked.string( "" ),
      NHits_Min = cms.uint32( 0 ),
      Chi2Prob_Min = cms.double( -1.0 ),
      Diff_r = cms.double( 0.1 ),
      BeamlineOption = cms.string( "BeamSpotFromEvent" ),
      ComponentName = cms.string( "TrackExtractor" )
    ),
    maxAbsEta = cms.double( 3.0 ),
    fillGlobalTrackRefits = cms.bool( False ),
    arbitrationCleanerOptions = cms.PSet(
      OverlapDTheta = cms.double( 0.02 ),
      Overlap = cms.bool( True ),
      Clustering = cms.bool( True ),
      ME1a = cms.bool( True ),
      ClusterDTheta = cms.double( 0.02 ),
      ClusterDPhi = cms.double( 0.6 ),
      OverlapDPhi = cms.double( 0.0786 )
    ),
    globalTrackQualityInputTag = cms.InputTag( "glbTrackQual" ),
    fillShowerDigis = cms.bool( False ),
    addExtraSoftMuons = cms.bool( False ),
    debugWithTruthMatching = cms.bool( False ),
    CaloExtractorPSet = cms.PSet(
      DR_Veto_H = cms.double( 0.1 ),
      CenterConeOnCalIntersection = cms.bool( False ),
      NoiseTow_EE = cms.double( 0.15 ),
      Noise_EB = cms.double( 0.025 ),
      Noise_HE = cms.double( 0.2 ),
      DR_Veto_E = cms.double( 0.07 ),
      NoiseTow_EB = cms.double( 0.04 ),
      Noise_EE = cms.double( 0.1 ),
      UseRecHitsFlag = cms.bool( False ),
      DR_Max = cms.double( 1.0 ),
      DepositLabel = cms.untracked.string( "Cal" ),
      Noise_HO = cms.double( 0.2 ),
      DR_Veto_HO = cms.double( 0.1 ),
      Threshold_H = cms.double( 0.5 ),
      PrintTimeReport = cms.untracked.bool( False ),
      Threshold_E = cms.double( 0.2 ),
      PropagatorName = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      ComponentName = cms.string( "CaloExtractorByAssociator" ),
      Threshold_HO = cms.double( 0.5 ),
      DepositInstanceLabels = cms.vstring( 'ecal',
        'hcal',
        'ho' ),
      ServiceParameters = cms.PSet(
        RPCLayers = cms.bool( False ),
        UseMuonNavigation = cms.untracked.bool( False ),
        Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' )
      ),
      TrackAssociatorParameters = cms.PSet(
        useMuon = cms.bool( False ),
        truthMatch = cms.bool( False ),
        usePreshower = cms.bool( False ),
        dRPreshowerPreselection = cms.double( 0.2 ),
        muonMaxDistanceSigmaY = cms.double( 0.0 ),
        useEcal = cms.bool( False ),
        muonMaxDistanceSigmaX = cms.double( 0.0 ),
        dRMuon = cms.double( 9999.0 ),
        dREcal = cms.double( 1.0 ),
        CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
        DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
        EBRecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
        CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForAll" ),
        propagateAllDirections = cms.bool( True ),
        muonMaxDistanceY = cms.double( 5.0 ),
        useHO = cms.bool( False ),
        muonMaxDistanceX = cms.double( 5.0 ),
        trajectoryUncertaintyTolerance = cms.double( -1.0 ),
        useHcal = cms.bool( False ),
        HBHERecHitCollectionLabel = cms.InputTag( "hltHbhereco" ),
        accountForTrajectoryChangeCalo = cms.bool( False ),
        dREcalPreselection = cms.double( 1.0 ),
        useCalo = cms.bool( True ),
        dRMuonPreselection = cms.double( 0.2 ),
        EERecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
        dRHcal = cms.double( 1.0 ),
        dRHcalPreselection = cms.double( 1.0 ),
        HORecHitCollectionLabel = cms.InputTag( "hltHoreco" )
      ),
      Noise_HB = cms.double( 0.2 )
    ),
    runArbitrationCleaner = cms.bool( False ),
    fillEnergy = cms.bool( True ),
    TrackerKinkFinderParameters = cms.PSet(
      usePosition = cms.bool( False ),
      diagonalOnly = cms.bool( False )
    ),
    TimingFillerParameters = cms.PSet(
      DTTimingParameters = cms.PSet(
        HitError = cms.double( 6.0 ),
        MatchParameters = cms.PSet(
          TightMatchDT = cms.bool( False ),
          DTradius = cms.double( 0.01 ),
          TightMatchCSC = cms.bool( True ),
          CSCsegments = cms.InputTag( "hltCscSegments" ),
          DTsegments = cms.InputTag( "hltDt4DSegments" )
        ),
        debug = cms.bool( False ),
        DoWireCorr = cms.bool( False ),
        RequireBothProjections = cms.bool( False ),
        DTTimeOffset = cms.double( 2.7 ),
        PruneCut = cms.double( 10000.0 ),
        DTsegments = cms.InputTag( "hltDt4DSegments" ),
        UseSegmentT0 = cms.bool( False ),
        HitsMin = cms.int32( 5 ),
        DropTheta = cms.bool( True ),
        ServiceParameters = cms.PSet(
          RPCLayers = cms.bool( True ),
          Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' )
        )
      ),
      UseCSC = cms.bool( True ),
      CSCTimingParameters = cms.PSet(
        MatchParameters = cms.PSet(
          TightMatchDT = cms.bool( False ),
          DTradius = cms.double( 0.01 ),
          TightMatchCSC = cms.bool( True ),
          CSCsegments = cms.InputTag( "hltCscSegments" ),
          DTsegments = cms.InputTag( "hltDt4DSegments" )
        ),
        debug = cms.bool( False ),
        CSCWireTimeOffset = cms.double( 0.0 ),
        CSCStripError = cms.double( 7.0 ),
        CSCTimeOffset = cms.double( 0.0 ),
        CSCWireError = cms.double( 8.6 ),
        PruneCut = cms.double( 100.0 ),
        CSCsegments = cms.InputTag( "hltCscSegments" ),
        UseStripTime = cms.bool( True ),
        CSCStripTimeOffset = cms.double( 0.0 ),
        UseWireTime = cms.bool( True ),
        ServiceParameters = cms.PSet(
          RPCLayers = cms.bool( True ),
          Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' )
        )
      ),
      ErrorDT = cms.double( 6.0 ),
      EcalEnergyCut = cms.double( 0.4 ),
      UseECAL = cms.bool( True ),
      ErrorEB = cms.double( 2.085 ),
      UseDT = cms.bool( True ),
      ErrorEE = cms.double( 6.95 ),
      ErrorCSC = cms.double( 7.4 )
    ),
    inputCollectionTypes = cms.vstring( 'inner tracks',
      'links',
      'outer tracks' ),
    arbitrateTrackerMuons = cms.bool( False ),
    minCaloCompatibility = cms.double( 0.6 ),
    ecalDepositName = cms.string( "ecal" ),
    minP = cms.double( 10.0 ),
    fillIsolation = cms.bool( True ),
    jetDepositName = cms.string( "jets" ),
    hoDepositName = cms.string( "ho" ),
    writeIsoDeposits = cms.bool( False ),
    maxAbsPullX = cms.double( 4.0 ),
    maxAbsPullY = cms.double( 9999.0 ),
    minPt = cms.double( 10.0 ),
    TrackAssociatorParameters = cms.PSet(
      useMuon = cms.bool( True ),
      truthMatch = cms.bool( False ),
      usePreshower = cms.bool( False ),
      dRPreshowerPreselection = cms.double( 0.2 ),
      muonMaxDistanceSigmaY = cms.double( 0.0 ),
      useEcal = cms.bool( True ),
      muonMaxDistanceSigmaX = cms.double( 0.0 ),
      dRMuon = cms.double( 9999.0 ),
      dREcal = cms.double( 9999.0 ),
      CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
      DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
      EBRecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
      CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForAll" ),
      propagateAllDirections = cms.bool( True ),
      muonMaxDistanceY = cms.double( 5.0 ),
      useHO = cms.bool( True ),
      muonMaxDistanceX = cms.double( 5.0 ),
      trajectoryUncertaintyTolerance = cms.double( -1.0 ),
      useHcal = cms.bool( True ),
      HBHERecHitCollectionLabel = cms.InputTag( "hltHbhereco" ),
      accountForTrajectoryChangeCalo = cms.bool( False ),
      dREcalPreselection = cms.double( 0.05 ),
      useCalo = cms.bool( False ),
      dRMuonPreselection = cms.double( 0.2 ),
      EERecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
      dRHcal = cms.double( 9999.0 ),
      dRHcalPreselection = cms.double( 0.2 ),
      HORecHitCollectionLabel = cms.InputTag( "hltHoreco" )
    ),
    storeCrossedHcalRecHits = cms.bool( False ),
    JetExtractorPSet = cms.PSet(
      JetCollectionLabel = cms.InputTag( "hltAK4CaloJetsPFEt5" ),
      DR_Veto = cms.double( 0.1 ),
      DR_Max = cms.double( 1.0 ),
      ExcludeMuonVeto = cms.bool( True ),
      PrintTimeReport = cms.untracked.bool( False ),
      PropagatorName = cms.string( "hltESPFastSteppingHelixPropagatorAny" ),
      ComponentName = cms.string( "JetExtractor" ),
      ServiceParameters = cms.PSet(
        RPCLayers = cms.bool( False ),
        UseMuonNavigation = cms.untracked.bool( False ),
        Propagators = cms.untracked.vstring( 'hltESPFastSteppingHelixPropagatorAny' )
      ),
      TrackAssociatorParameters = cms.PSet(
        useMuon = cms.bool( False ),
        truthMatch = cms.bool( False ),
        usePreshower = cms.bool( False ),
        dRPreshowerPreselection = cms.double( 0.2 ),
        muonMaxDistanceSigmaY = cms.double( 0.0 ),
        useEcal = cms.bool( False ),
        muonMaxDistanceSigmaX = cms.double( 0.0 ),
        dRMuon = cms.double( 9999.0 ),
        dREcal = cms.double( 0.5 ),
        CSCSegmentCollectionLabel = cms.InputTag( "hltCscSegments" ),
        DTRecSegment4DCollectionLabel = cms.InputTag( "hltDt4DSegments" ),
        EBRecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
        CaloTowerCollectionLabel = cms.InputTag( "hltTowerMakerForAll" ),
        propagateAllDirections = cms.bool( True ),
        muonMaxDistanceY = cms.double( 5.0 ),
        useHO = cms.bool( False ),
        muonMaxDistanceX = cms.double( 5.0 ),
        trajectoryUncertaintyTolerance = cms.double( -1.0 ),
        useHcal = cms.bool( False ),
        HBHERecHitCollectionLabel = cms.InputTag( "hltHbhereco" ),
        accountForTrajectoryChangeCalo = cms.bool( False ),
        dREcalPreselection = cms.double( 0.5 ),
        useCalo = cms.bool( True ),
        dRMuonPreselection = cms.double( 0.2 ),
        EERecHitCollectionLabel = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
        dRHcal = cms.double( 0.5 ),
        dRHcalPreselection = cms.double( 0.5 ),
        HORecHitCollectionLabel = cms.InputTag( "hltHoreco" )
      ),
      Threshold = cms.double( 5.0 )
    ),
    fillGlobalTrackQuality = cms.bool( False ),
    minPCaloMuon = cms.double( 1.0E9 ),
    maxAbsDy = cms.double( 9999.0 ),
    fillCaloCompatibility = cms.bool( True ),
    fillMatching = cms.bool( True ),
    MuonCaloCompatibility = cms.PSet(
      delta_eta = cms.double( 0.02 ),
      delta_phi = cms.double( 0.02 ),
      allSiPMHO = cms.bool( False ),
      MuonTemplateFileName = cms.FileInPath( "RecoMuon/MuonIdentification/data/MuID_templates_muons_lowPt_3_1_norm.root" ),
      PionTemplateFileName = cms.FileInPath( "RecoMuon/MuonIdentification/data/MuID_templates_pions_lowPt_3_1_norm.root" )
    ),
    fillTrackerKink = cms.bool( False ),
    ShowerDigiFillerParameters = cms.PSet(
      cscDigiCollectionLabel = cms.InputTag( 'muonCSCDigis','MuonCSCStripDigi' ),
      dtDigiCollectionLabel = cms.InputTag( "muonDTDigis" ),
      digiMaxDistanceX = cms.double( 25.0 )
    ),
    hcalDepositName = cms.string( "hcal" ),
    sigmaThresholdToFillCandidateP4WithGlobalFit = cms.double( 2.0 ),
    inputCollectionLabels = cms.VInputTag( 'hltPFMuonMerging','hltMuonLinks','hltL2Muons' ),
    trackDepositName = cms.string( "tracker" ),
    maxAbsDx = cms.double( 3.0 ),
    ptThresholdToFillCandidateP4WithGlobalFit = cms.double( 200.0 ),
    minNumberOfMatches = cms.int32( 1 )
)
fragment.hltEcalPreshowerDigis = cms.EDProducer( "ESRawToDigi",
    sourceTag = cms.InputTag( "rawDataCollector" ),
    debugMode = cms.untracked.bool( False ),
    InstanceES = cms.string( "" ),
    ESdigiCollection = cms.string( "" ),
    LookupTable = cms.FileInPath( "EventFilter/ESDigiToRaw/data/ES_lookup_table.dat" )
)
fragment.hltEcalPreshowerRecHit = cms.EDProducer( "ESRecHitProducer",
    ESRecoAlgo = cms.int32( 0 ),
    ESrechitCollection = cms.string( "EcalRecHitsES" ),
    algo = cms.string( "ESRecHitWorker" ),
    ESdigiCollection = cms.InputTag( "hltEcalPreshowerDigis" )
)
fragment.hltParticleFlowRecHitECALUnseeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet(
      cms.PSet(  src = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
        srFlags = cms.InputTag( "" ),
        name = cms.string( "PFEBRecHitCreator" ),
        qualityTests = cms.VPSet(
          cms.PSet(  name = cms.string( "PFRecHitQTestDBThreshold" ),
            applySelectionsToAllCrystals = cms.bool( True )
          ),
          cms.PSet(  topologicalCleaning = cms.bool( True ),
            skipTTRecoveredHits = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            name = cms.string( "PFRecHitQTestECAL" ),
            timingCleaning = cms.bool( True )
          )
        )
      ),
      cms.PSet(  src = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
        srFlags = cms.InputTag( "" ),
        name = cms.string( "PFEERecHitCreator" ),
        qualityTests = cms.VPSet(
          cms.PSet(  name = cms.string( "PFRecHitQTestDBThreshold" ),
            applySelectionsToAllCrystals = cms.bool( True )
          ),
          cms.PSet(  topologicalCleaning = cms.bool( True ),
            skipTTRecoveredHits = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            name = cms.string( "PFRecHitQTestECAL" ),
            timingCleaning = cms.bool( True )
          )
        )
      )
    ),
    navigator = cms.PSet(
      barrel = cms.PSet(  ),
      endcap = cms.PSet(  ),
      name = cms.string( "PFRecHitECALNavigator" )
    )
)
fragment.hltParticleFlowRecHitHBHE = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet(
      cms.PSet(  src = cms.InputTag( "hltHbhereco" ),
        name = cms.string( "PFHBHERecHitCreator" ),
        qualityTests = cms.VPSet(
          cms.PSet(  threshold = cms.double( 0.8 ),
            name = cms.string( "PFRecHitQTestThreshold" ),
            cuts = cms.VPSet(
              cms.PSet(  depth = cms.vint32( 1, 2, 3, 4 ),
                threshold = cms.vdouble( 0.8, 0.8, 0.8, 0.8 ),
                detectorEnum = cms.int32( 1 )
              ),
              cms.PSet(  depth = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
                threshold = cms.vdouble( 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8 ),
                detectorEnum = cms.int32( 2 )
              )
            )
          ),
          cms.PSet(  flags = cms.vstring( 'Standard' ),
            cleaningThresholds = cms.vdouble( 0.0 ),
            name = cms.string( "PFRecHitQTestHCALChannel" ),
            maxSeverities = cms.vint32( 11 )
          )
        )
      )
    ),
    navigator = cms.PSet(
      name = cms.string( "PFRecHitHCALNavigator" ),
      sigmaCut = cms.double( 4.0 ),
      timeResolutionCalc = cms.PSet(
        corrTermLowE = cms.double( 0.0 ),
        threshLowE = cms.double( 2.0 ),
        noiseTerm = cms.double( 8.64 ),
        constantTermLowE = cms.double( 6.0 ),
        noiseTermLowE = cms.double( 0.0 ),
        threshHighE = cms.double( 8.0 ),
        constantTerm = cms.double( 1.92 )
      )
    )
)
fragment.hltParticleFlowRecHitHF = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet(
      cms.PSet(  thresh_HF = cms.double( 0.4 ),
        LongFibre_Fraction = cms.double( 0.1 ),
        src = cms.InputTag( "hltHfreco" ),
        EMDepthCorrection = cms.double( 22.0 ),
        ShortFibre_Fraction = cms.double( 0.01 ),
        HADDepthCorrection = cms.double( 25.0 ),
        HFCalib29 = cms.double( 1.07 ),
        LongFibre_Cut = cms.double( 120.0 ),
        name = cms.string( "PFHFRecHitCreator" ),
        qualityTests = cms.VPSet(
          cms.PSet(  flags = cms.vstring( 'Standard',
  'HFLong',
  'HFShort' ),
            cleaningThresholds = cms.vdouble( 0.0, 120.0, 60.0 ),
            name = cms.string( "PFRecHitQTestHCALChannel" ),
            maxSeverities = cms.vint32( 11, 9, 9 )
          ),
          cms.PSet(  name = cms.string( "PFRecHitQTestHCALThresholdVsDepth" ),
            cuts = cms.VPSet(
              cms.PSet(  depth = cms.vint32( 1, 2 ),
                threshold = cms.vdouble( 1.2, 1.8 ),
                detectorEnum = cms.int32( 4 )
              )
            )
          )
        ),
        ShortFibre_Cut = cms.double( 60.0 )
      )
    ),
    navigator = cms.PSet(
      barrel = cms.PSet(  ),
      endcap = cms.PSet(  ),
      name = cms.string( "PFRecHitHCALNavigator" )
    )
)
fragment.hltParticleFlowRecHitPSUnseeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet(
      cms.PSet(  src = cms.InputTag( 'hltEcalPreshowerRecHit','EcalRecHitsES' ),
        name = cms.string( "PFPSRecHitCreator" ),
        qualityTests = cms.VPSet(
          cms.PSet(  threshold = cms.double( 7.0E-6 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          )
        )
      )
    ),
    navigator = cms.PSet(  name = cms.string( "PFRecHitPreshowerNavigator" ) )
)
fragment.hltParticleFlowClusterECALUncorrectedUnseeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet(
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet(
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 9 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.08 ),
        minFractionInCalc = cms.double( 1.0E-9 ),
        timeResolutionCalcBarrel = cms.PSet(
          corrTermLowE = cms.double( 0.0510871 ),
          threshLowE = cms.double( 0.5 ),
          noiseTerm = cms.double( 1.10889 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 1.31883 ),
          threshHighE = cms.double( 5.0 ),
          constantTerm = cms.double( 0.428192 )
        ),
        timeResolutionCalcEndcap = cms.PSet(
          corrTermLowE = cms.double( 0.0 ),
          threshLowE = cms.double( 1.0 ),
          noiseTerm = cms.double( 5.72489999999 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 6.92683000001 ),
          threshHighE = cms.double( 10.0 ),
          constantTerm = cms.double( 0.0 )
        )
      ),
      maxIterations = cms.uint32( 50 ),
      positionCalcForConvergence = cms.PSet(
        minAllowedNormalization = cms.double( 0.0 ),
        T0_ES = cms.double( 1.2 ),
        algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" ),
        T0_EE = cms.double( 3.1 ),
        T0_EB = cms.double( 7.4 ),
        X0 = cms.double( 0.89 ),
        minFractionInCalc = cms.double( 0.0 ),
        W0 = cms.double( 4.2 )
      ),
      allCellsPositionCalc = cms.PSet(
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.08 ),
        minFractionInCalc = cms.double( 1.0E-9 ),
        timeResolutionCalcBarrel = cms.PSet(
          corrTermLowE = cms.double( 0.0510871 ),
          threshLowE = cms.double( 0.5 ),
          noiseTerm = cms.double( 1.10889 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 1.31883 ),
          threshHighE = cms.double( 5.0 ),
          constantTerm = cms.double( 0.428192 )
        ),
        timeResolutionCalcEndcap = cms.PSet(
          corrTermLowE = cms.double( 0.0 ),
          threshLowE = cms.double( 1.0 ),
          noiseTerm = cms.double( 5.72489999999 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 6.92683000001 ),
          threshHighE = cms.double( 10.0 ),
          constantTerm = cms.double( 0.0 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet(
        cms.PSet(  recHitEnergyNorm = cms.double( 0.08 ),
          detector = cms.string( "ECAL_BARREL" )
        ),
        cms.PSet(  recHitEnergyNorm = cms.double( 0.3 ),
          detector = cms.string( "ECAL_ENDCAP" )
        )
      ),
      showerSigma = cms.double( 1.5 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True )
    ),
    positionReCalc = cms.PSet(
      minAllowedNormalization = cms.double( 0.0 ),
      T0_ES = cms.double( 1.2 ),
      algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" ),
      T0_EE = cms.double( 3.1 ),
      T0_EB = cms.double( 7.4 ),
      X0 = cms.double( 0.89 ),
      minFractionInCalc = cms.double( 0.0 ),
      W0 = cms.double( 4.2 )
    ),
    initialClusteringStep = cms.PSet(
      thresholdsByDetector = cms.VPSet(
        cms.PSet(  gatheringThreshold = cms.double( 0.08 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_BARREL" )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.3 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_ENDCAP" )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( True )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet(
    ),
    seedFinder = cms.PSet(
      thresholdsByDetector = cms.VPSet(
        cms.PSet(  seedingThresholdPt = cms.double( 0.15 ),
          seedingThreshold = cms.double( 0.6 ),
          detector = cms.string( "ECAL_ENDCAP" )
        ),
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 0.23 ),
          detector = cms.string( "ECAL_BARREL" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 8 )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitECALUnseeded" )
)
fragment.hltParticleFlowClusterPSUnseeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet(
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet(
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 6.0E-5 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      maxIterations = cms.uint32( 50 ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet(
        cms.PSet(  recHitEnergyNorm = cms.double( 6.0E-5 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  recHitEnergyNorm = cms.double( 6.0E-5 ),
          detector = cms.string( "PS2" )
        )
      ),
      showerSigma = cms.double( 0.3 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet(
      thresholdsByDetector = cms.VPSet(
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( False )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet(
    ),
    seedFinder = cms.PSet(
      thresholdsByDetector = cms.VPSet(
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.2E-4 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.2E-4 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 4 )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitPSUnseeded" )
)
fragment.hltParticleFlowClusterECALUnseeded = cms.EDProducer( "CorrectedECALPFClusterProducer",
    inputPS = cms.InputTag( "hltParticleFlowClusterPSUnseeded" ),
    minimumPSEnergy = cms.double( 0.0 ),
    energyCorrector = cms.PSet(
      algoName = cms.string( "PFClusterEMEnergyCorrector" ),
      applyCrackCorrections = cms.bool( False )
    ),
    inputECAL = cms.InputTag( "hltParticleFlowClusterECALUncorrectedUnseeded" )
)
fragment.hltParticleFlowClusterHBHE = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet(
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet(
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.8 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      maxIterations = cms.uint32( 50 ),
      minChi2Prob = cms.double( 0.0 ),
      allCellsPositionCalc = cms.PSet(
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.8 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet(
        cms.PSet(  detector = cms.string( "HCAL_BARREL1" ),
          depths = cms.vint32( 1, 2, 3, 4 ),
          recHitEnergyNorm = cms.vdouble( 0.8, 0.8, 0.8, 0.8 )
        ),
        cms.PSet(  detector = cms.string( "HCAL_ENDCAP" ),
          depths = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
          recHitEnergyNorm = cms.vdouble( 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8 )
        )
      ),
      maxNSigmaTime = cms.double( 10.0 ),
      showerSigma = cms.double( 10.0 ),
      timeSigmaEE = cms.double( 10.0 ),
      clusterTimeResFromSeed = cms.bool( False ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True ),
      timeResolutionCalcBarrel = cms.PSet(
        corrTermLowE = cms.double( 0.0 ),
        threshLowE = cms.double( 6.0 ),
        noiseTerm = cms.double( 21.86 ),
        constantTermLowE = cms.double( 4.24 ),
        noiseTermLowE = cms.double( 8.0 ),
        threshHighE = cms.double( 15.0 ),
        constantTerm = cms.double( 2.82 )
      ),
      timeResolutionCalcEndcap = cms.PSet(
        corrTermLowE = cms.double( 0.0 ),
        threshLowE = cms.double( 6.0 ),
        noiseTerm = cms.double( 21.86 ),
        constantTermLowE = cms.double( 4.24 ),
        noiseTermLowE = cms.double( 8.0 ),
        threshHighE = cms.double( 15.0 ),
        constantTerm = cms.double( 2.82 )
      ),
      timeSigmaEB = cms.double( 10.0 )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet(
      thresholdsByDetector = cms.VPSet(
        cms.PSet(  detector = cms.string( "HCAL_BARREL1" ),
          depths = cms.vint32( 1, 2, 3, 4 ),
          gatheringThreshold = cms.vdouble( 0.8, 0.8, 0.8, 0.8 ),
          gatheringThresholdPt = cms.vdouble( 0.0, 0.0, 0.0, 0.0 )
        ),
        cms.PSet(  detector = cms.string( "HCAL_ENDCAP" ),
          depths = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
          gatheringThreshold = cms.vdouble( 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8 ),
          gatheringThresholdPt = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( True )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet(
    ),
    seedFinder = cms.PSet(
      thresholdsByDetector = cms.VPSet(
        cms.PSet(  detector = cms.string( "HCAL_BARREL1" ),
          depths = cms.vint32( 1, 2, 3, 4 ),
          seedingThreshold = cms.vdouble( 1.0, 1.0, 1.0, 1.0 ),
          seedingThresholdPt = cms.vdouble( 0.0, 0.0, 0.0, 0.0 )
        ),
        cms.PSet(  detector = cms.string( "HCAL_ENDCAP" ),
          depths = cms.vint32( 1, 2, 3, 4, 5, 6, 7 ),
          seedingThreshold = cms.vdouble( 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1 ),
          seedingThresholdPt = cms.vdouble( 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 4 )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitHBHE" )
)
fragment.hltParticleFlowClusterHCAL = cms.EDProducer( "PFMultiDepthClusterProducer",
    pfClusterBuilder = cms.PSet(
      allCellsPositionCalc = cms.PSet(
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.8 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      algoName = cms.string( "PFMultiDepthClusterizer" ),
      nSigmaPhi = cms.double( 2.0 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      nSigmaEta = cms.double( 2.0 )
    ),
    energyCorrector = cms.PSet(  ),
    positionReCalc = cms.PSet(  ),
    clustersSource = cms.InputTag( "hltParticleFlowClusterHBHE" )
)
fragment.hltParticleFlowClusterHF = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet(
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet(
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 5 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.8 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      maxIterations = cms.uint32( 50 ),
      allCellsPositionCalc = cms.PSet(
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.8 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet(
        cms.PSet(  recHitEnergyNorm = cms.double( 0.8 ),
          detector = cms.string( "HF_EM" )
        ),
        cms.PSet(  recHitEnergyNorm = cms.double( 0.8 ),
          detector = cms.string( "HF_HAD" )
        )
      ),
      showerSigma = cms.double( 0.0 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet(
      thresholdsByDetector = cms.VPSet(
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HF_EM" )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.8 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "HF_HAD" )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( False )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet(
    ),
    seedFinder = cms.PSet(
      thresholdsByDetector = cms.VPSet(
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.4 ),
          detector = cms.string( "HF_EM" )
        ),
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.4 ),
          detector = cms.string( "HF_HAD" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 0 )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitHF" )
)
fragment.hltLightPFTracks = cms.EDProducer( "LightPFTrackProducer",
    TrackQuality = cms.string( "none" ),
    UseQuality = cms.bool( False ),
    TkColList = cms.VInputTag( 'hltPFMuonMerging' )
)
fragment.hltParticleFlowBlockForTaus = cms.EDProducer( "PFBlockProducer",
    debug = cms.untracked.bool( False ),
    linkDefinitions = cms.VPSet(
      cms.PSet(  linkType = cms.string( "PS1:ECAL" ),
        useKDTree = cms.bool( True ),
        linkerName = cms.string( "PreshowerAndECALLinker" )
      ),
      cms.PSet(  linkType = cms.string( "PS2:ECAL" ),
        useKDTree = cms.bool( True ),
        linkerName = cms.string( "PreshowerAndECALLinker" )
      ),
      cms.PSet(  linkType = cms.string( "TRACK:ECAL" ),
        useKDTree = cms.bool( True ),
        linkerName = cms.string( "TrackAndECALLinker" )
      ),
      cms.PSet(  linkType = cms.string( "TRACK:HCAL" ),
        useKDTree = cms.bool( True ),
        linkerName = cms.string( "TrackAndHCALLinker" )
      ),
      cms.PSet(  linkType = cms.string( "ECAL:HCAL" ),
        useKDTree = cms.bool( False ),
        linkerName = cms.string( "ECALAndHCALLinker" )
      ),
      cms.PSet(  linkType = cms.string( "HFEM:HFHAD" ),
        useKDTree = cms.bool( False ),
        linkerName = cms.string( "HFEMAndHFHADLinker" )
      )
    ),
    elementImporters = cms.VPSet(
      cms.PSet(  muonSrc = cms.InputTag( "hltMuons" ),
        source = cms.InputTag( "hltLightPFTracks" ),
        NHitCuts_byTrackAlgo = cms.vuint32( 3, 3, 3, 3, 3, 3 ),
        useIterativeTracking = cms.bool( False ),
        importerName = cms.string( "GeneralTracksImporter" ),
        DPtOverPtCuts_byTrackAlgo = cms.vdouble( 20.0, 20.0, 20.0, 20.0, 20.0, 20.0 )
      ),
      cms.PSet(  source = cms.InputTag( "hltParticleFlowClusterECALUnseeded" ),
        importerName = cms.string( "ECALClusterImporter" ),
        BCtoPFCMap = cms.InputTag( "" )
      ),
      cms.PSet(  source = cms.InputTag( "hltParticleFlowClusterHCAL" ),
        importerName = cms.string( "GenericClusterImporter" )
      ),
      cms.PSet(  source = cms.InputTag( "hltParticleFlowClusterHF" ),
        importerName = cms.string( "GenericClusterImporter" )
      ),
      cms.PSet(  source = cms.InputTag( "hltParticleFlowClusterPSUnseeded" ),
        importerName = cms.string( "GenericClusterImporter" )
      )
    ),
    verbose = cms.untracked.bool( False )
)
fragment.hltParticleFlowForTaus = cms.EDProducer( "PFProducer",
    photon_SigmaiEtaiEta_endcap = cms.double( 0.034 ),
    minPtForPostCleaning = cms.double( 20.0 ),
    electron_protectionsForBadHcal = cms.PSet(
      dEta = cms.vdouble( 0.0064, 0.01264 ),
      dPhi = cms.vdouble( 0.0547, 0.0394 ),
      enableProtections = cms.bool( False ),
      eInvPInv = cms.vdouble( 0.184, 0.0721 ),
      full5x5_sigmaIetaIeta = cms.vdouble( 0.0106, 0.0387 )
    ),
    pf_nsigma_ECAL = cms.double( 0.0 ),
    electron_ecalDrivenHademPreselCut = cms.double( 0.15 ),
    GedPhotonValueMap = cms.InputTag( 'tmpGedPhotons','valMapPFEgammaCandToPhoton' ),
    sumPtTrackIsoForPhoton = cms.double( -1.0 ),
    goodPixelTrackDeadHcal_ptErrRel = cms.double( 1.0 ),
    calibrationsLabel = cms.string( "HLT" ),
    metFactorForFakes = cms.double( 4.0 ),
    muon_HO = cms.vdouble( 0.9, 0.9 ),
    electron_missinghits = cms.uint32( 1 ),
    metSignificanceForCleaning = cms.double( 3.0 ),
    usePFPhotons = cms.bool( False ),
    maxDeltaPhiPt = cms.double( 7.0 ),
    nTrackIsoForEgammaSC = cms.uint32( 2 ),
    pf_nsigma_HCAL = cms.double( 1.0 ),
    cosmicRejectionDistance = cms.double( 1.0 ),
    goodTrackDeadHcal_ptErrRel = cms.double( 0.2 ),
    useEGammaFilters = cms.bool( False ),
    useEGammaElectrons = cms.bool( False ),
    nsigma_TRACK = cms.double( 1.0 ),
    useEGammaSupercluster = cms.bool( False ),
    goodTrackDeadHcal_dxy = cms.double( 0.5 ),
    eventFractionForCleaning = cms.double( 0.5 ),
    usePFDecays = cms.bool( False ),
    rejectTracks_Step45 = cms.bool( False ),
    eventFractionForRejection = cms.double( 0.8 ),
    photon_MinEt = cms.double( 10.0 ),
    usePFNuclearInteractions = cms.bool( False ),
    maxSignificance = cms.double( 2.5 ),
    electron_iso_mva_endcap = cms.double( -0.1075 ),
    debug = cms.untracked.bool( False ),
    pf_convID_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_pfConversionAug0411.txt" ),
    calibHF_eta_step = cms.vdouble( 0.0, 2.9, 3.0, 3.2, 4.2, 4.4, 4.6, 4.8, 5.2, 5.4 ),
    ptErrorScale = cms.double( 8.0 ),
    goodPixelTrackDeadHcal_maxLost3Hit = cms.int32( 0 ),
    minSignificance = cms.double( 2.5 ),
    minMomentumForPunchThrough = cms.double( 100.0 ),
    pf_conv_mvaCut = cms.double( 0.0 ),
    useCalibrationsFromDB = cms.bool( True ),
    usePFElectrons = cms.bool( False ),
    electron_iso_combIso_endcap = cms.double( 10.0 ),
    photon_combIso = cms.double( 10.0 ),
    goodTrackDeadHcal_validFr = cms.double( 0.5 ),
    electron_iso_mva_barrel = cms.double( -0.1875 ),
    postHFCleaning = cms.bool( False ),
    factors_45 = cms.vdouble( 10.0, 100.0 ),
    cleanedHF = cms.VInputTag( 'hltParticleFlowRecHitHF:Cleaned','hltParticleFlowClusterHF:Cleaned' ),
    coneEcalIsoForEgammaSC = cms.double( 0.3 ),
    minSignificanceReduction = cms.double( 1.4 ),
    photon_SigmaiEtaiEta_barrel = cms.double( 0.0125 ),
    calibHF_b_HADonly = cms.vdouble( 1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 0.94348, 0.9437, 1.0034, 1.0444, 1.0444 ),
    minPixelHits = cms.int32( 1 ),
    maxDPtOPt = cms.double( 1.0 ),
    useHO = cms.bool( False ),
    pf_electron_output_col = cms.string( "electrons" ),
    electron_noniso_mvaCut = cms.double( -0.1 ),
    goodPixelTrackDeadHcal_minEta = cms.double( 2.3 ),
    useVerticesForNeutral = cms.bool( True ),
    trackQuality = cms.string( "highPurity" ),
    PFEGammaCandidates = cms.InputTag( "particleFlowEGamma" ),
    goodTrackDeadHcal_layers = cms.uint32( 4 ),
    sumPtTrackIsoSlopeForPhoton = cms.double( -1.0 ),
    goodPixelTrackDeadHcal_dxy = cms.double( 0.02 ),
    coneTrackIsoForEgammaSC = cms.double( 0.3 ),
    GedElectronValueMap = cms.InputTag( "gedGsfElectronsTmp" ),
    goodPixelTrackDeadHcal_chi2n = cms.double( 2.0 ),
    punchThroughMETFactor = cms.double( 4.0 ),
    useProtectionsForJetMET = cms.bool( True ),
    metFactorForRejection = cms.double( 4.0 ),
    sumPtTrackIsoForEgammaSC_endcap = cms.double( 4.0 ),
    calibHF_use = cms.bool( False ),
    verbose = cms.untracked.bool( False ),
    usePFConversions = cms.bool( False ),
    calibPFSCEle_endcap = cms.vdouble( 1.153, -16.5975, 5.668, -0.1772, 16.22, 7.326, 0.0483, -4.068, 9.406 ),
    metFactorForCleaning = cms.double( 4.0 ),
    eventFactorForCosmics = cms.double( 10.0 ),
    egammaElectrons = cms.InputTag( "" ),
    electron_maxElePtForOnlyMVAPresel = cms.double( 50.0 ),
    minEnergyForPunchThrough = cms.double( 100.0 ),
    minTrackerHits = cms.int32( 8 ),
    iCfgCandConnector = cms.PSet(
      nuclCalibFactors = cms.vdouble( 0.8, 0.15, 0.5, 0.5, 0.05 ),
      bCalibSecondary = cms.bool( False ),
      bCorrect = cms.bool( False ),
      bCalibPrimary = cms.bool( False )
    ),
    rejectTracks_Bad = cms.bool( False ),
    pf_electronID_crackCorrection = cms.bool( False ),
    pf_Res_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFRes_14Dec2011.root" ),
    sumPtTrackIsoForEgammaSC_barrel = cms.double( 4.0 ),
    calibHF_a_EMonly = cms.vdouble( 0.96945, 0.96701, 0.76309, 0.82268, 0.87583, 0.89718, 0.98674, 1.4681, 1.458, 1.458 ),
    pf_locC_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFClusterLCorr_14Dec2011.root" ),
    metFactorForHighEta = cms.double( 25.0 ),
    minHFCleaningPt = cms.double( 5.0 ),
    photon_protectionsForBadHcal = cms.PSet(
      solidConeTrkIsoSlope = cms.double( 0.3 ),
      enableProtections = cms.bool( False ),
      solidConeTrkIsoOffset = cms.double( 10.0 )
    ),
    pf_electron_mvaCut = cms.double( -0.1 ),
    ptFactorForHighEta = cms.double( 2.0 ),
    goodPixelTrackDeadHcal_maxPt = cms.double( 50.0 ),
    dptRel_DispVtx = cms.double( 10.0 ),
    pf_electronID_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/MVAnalysis_BDT.weights_PfElectrons23Jan_IntToFloat.txt" ),
    goodTrackDeadHcal_chi2n = cms.double( 5.0 ),
    sumEtEcalIsoForEgammaSC_endcap = cms.double( 2.0 ),
    goodPixelTrackDeadHcal_dz = cms.double( 0.05 ),
    calibHF_b_EMHAD = cms.vdouble( 1.27541, 0.85361, 0.86333, 0.89091, 0.94348, 0.94348, 0.9437, 1.0034, 1.0444, 1.0444 ),
    pf_GlobC_mvaWeightFile = cms.string( "RecoParticleFlow/PFProducer/data/TMVARegression_BDTG_PFGlobalCorr_14Dec2011.root" ),
    photon_HoE = cms.double( 0.05 ),
    sumEtEcalIsoForEgammaSC_barrel = cms.double( 1.0 ),
    calibPFSCEle_Fbrem_endcap = cms.vdouble( 0.9, 6.5, -0.0692932, 0.101776, 0.995338, -0.00236548, 0.874998, 1.653, -0.0750184, 0.147, 0.923165, 4.74665E-4, 1.10782 ),
    punchThroughFactor = cms.double( 3.0 ),
    algoType = cms.uint32( 0 ),
    electron_iso_combIso_barrel = cms.double( 10.0 ),
    muons = cms.InputTag( "hltMuons" ),
    goodPixelTrackDeadHcal_maxLost4Hit = cms.int32( 1 ),
    postMuonCleaning = cms.bool( True ),
    minDeltaMet = cms.double( 0.4 ),
    calibPFSCEle_barrel = cms.vdouble( 1.004, -1.536, 22.88, -1.467, 0.3555, 0.6227, 14.65, 2051.0, 25.0, 0.9932, -0.5444, 0.0, 0.5438, 0.7109, 7.645, 0.2904, 0.0 ),
    electron_protectionsForJetMET = cms.PSet(
      maxEeleOverPoutRes = cms.double( 0.5 ),
      maxEleHcalEOverEcalE = cms.double( 0.1 ),
      maxEcalEOverPRes = cms.double( 0.2 ),
      maxHcalEOverP = cms.double( 1.0 ),
      maxE = cms.double( 50.0 ),
      maxTrackPOverEele = cms.double( 1.0 ),
      maxDPhiIN = cms.double( 0.1 ),
      maxEcalEOverP_2 = cms.double( 0.2 ),
      maxEcalEOverP_1 = cms.double( 0.5 ),
      maxEeleOverPout = cms.double( 0.2 ),
      maxHcalEOverEcalE = cms.double( 0.1 ),
      maxHcalE = cms.double( 10.0 ),
      maxNtracks = cms.double( 3.0 )
    ),
    electron_iso_pt = cms.double( 10.0 ),
    isolatedElectronID_mvaWeightFile = cms.string( "RecoEgamma/ElectronIdentification/data/TMVA_BDTSimpleCat_17Feb2011.weights.xml" ),
    vertexCollection = cms.InputTag( "hltPixelVertices" ),
    X0_Map = cms.string( "RecoParticleFlow/PFProducer/data/allX0histos.root" ),
    calibPFSCEle_Fbrem_barrel = cms.vdouble( 0.6, 6.0, -0.0255975, 0.0576727, 0.975442, -5.46394E-4, 1.26147, 25.0, -0.02025, 0.04537, 0.9728, -8.962E-4, 1.172 ),
    blocks = cms.InputTag( "hltParticleFlowBlockForTaus" ),
    pt_Error = cms.double( 1.0 ),
    metSignificanceForRejection = cms.double( 4.0 ),
    photon_protectionsForJetMET = cms.PSet(
      sumPtTrackIsoSlope = cms.double( 0.001 ),
      sumPtTrackIso = cms.double( 2.0 )
    ),
    usePhotonReg = cms.bool( False ),
    dzPV = cms.double( 0.2 ),
    calibHF_a_EMHAD = cms.vdouble( 1.42215, 1.00496, 0.68961, 0.81656, 0.98504, 0.98504, 1.00802, 1.0593, 1.4576, 1.4576 ),
    muon_HCAL = cms.vdouble( 3.0, 3.0 ),
    useRegressionFromDB = cms.bool( False ),
    muon_ECAL = cms.vdouble( 0.5, 0.5 ),
    usePFSCEleCalib = cms.bool( True )
)
fragment.hltAK4PFJetsForTaus = cms.EDProducer( "FastjetJetProducer",
    Active_Area_Repeats = cms.int32( 5 ),
    useMassDropTagger = cms.bool( False ),
    doAreaFastjet = cms.bool( False ),
    muMin = cms.double( -1.0 ),
    Ghost_EtaMax = cms.double( 6.0 ),
    maxBadHcalCells = cms.uint32( 9999999 ),
    doAreaDiskApprox = cms.bool( True ),
    subtractorName = cms.string( "" ),
    dRMax = cms.double( -1.0 ),
    useExplicitGhosts = cms.bool( False ),
    puWidth = cms.double( 0.0 ),
    maxRecoveredEcalCells = cms.uint32( 9999999 ),
    R0 = cms.double( -1.0 ),
    jetType = cms.string( "PFJet" ),
    muCut = cms.double( -1.0 ),
    subjetPtMin = cms.double( -1.0 ),
    csRParam = cms.double( -1.0 ),
    MinVtxNdof = cms.int32( 0 ),
    minSeed = cms.uint32( 0 ),
    voronoiRfact = cms.double( -9.0 ),
    doRhoFastjet = cms.bool( False ),
    jetAlgorithm = cms.string( "AntiKt" ),
    writeCompound = cms.bool( False ),
    muMax = cms.double( -1.0 ),
    nSigmaPU = cms.double( 1.0 ),
    GhostArea = cms.double( 0.01 ),
    Rho_EtaMax = cms.double( 4.4 ),
    restrictInputs = cms.bool( False ),
    useDynamicFiltering = cms.bool( False ),
    nExclude = cms.uint32( 0 ),
    maxRecoveredHcalCells = cms.uint32( 9999999 ),
    maxBadEcalCells = cms.uint32( 9999999 ),
    yMin = cms.double( -1.0 ),
    jetCollInstanceName = cms.string( "" ),
    useFiltering = cms.bool( False ),
    maxInputs = cms.uint32( 1 ),
    rFiltFactor = cms.double( -1.0 ),
    useDeterministicSeed = cms.bool( True ),
    doPVCorrection = cms.bool( False ),
    rFilt = cms.double( -1.0 ),
    yMax = cms.double( -1.0 ),
    zcut = cms.double( -1.0 ),
    useTrimming = cms.bool( False ),
    puCenters = cms.vdouble(  ),
    MaxVtxZ = cms.double( 15.0 ),
    rParam = cms.double( 0.4 ),
    csRho_EtaMax = cms.double( -1.0 ),
    UseOnlyVertexTracks = cms.bool( False ),
    dRMin = cms.double( -1.0 ),
    gridSpacing = cms.double( -1.0 ),
    doFastJetNonUniform = cms.bool( False ),
    usePruning = cms.bool( False ),
    maxDepth = cms.int32( -1 ),
    yCut = cms.double( -1.0 ),
    useSoftDrop = cms.bool( False ),
    DzTrVtxMax = cms.double( 0.0 ),
    UseOnlyOnePV = cms.bool( False ),
    maxProblematicHcalCells = cms.uint32( 9999999 ),
    correctShape = cms.bool( False ),
    rcut_factor = cms.double( -1.0 ),
    src = cms.InputTag( "hltParticleFlowForTaus" ),
    gridMaxRapidity = cms.double( -1.0 ),
    sumRecHits = cms.bool( False ),
    jetPtMin = cms.double( 0.0 ),
    puPtMin = cms.double( 10.0 ),
    srcPVs = cms.InputTag( "hltTrimmedPixelVertices" ),
    verbosity = cms.int32( 0 ),
    inputEtMin = cms.double( 0.0 ),
    useConstituentSubtraction = cms.bool( False ),
    beta = cms.double( -1.0 ),
    trimPtFracMin = cms.double( -1.0 ),
    radiusPU = cms.double( 0.4 ),
    nFilt = cms.int32( -1 ),
    useKtPruning = cms.bool( False ),
    DxyTrVtxMax = cms.double( 0.0 ),
    maxProblematicEcalCells = cms.uint32( 9999999 ),
    useCMSBoostedTauSeedingAlgorithm = cms.bool( False ),
    doPUOffsetCorr = cms.bool( False ),
    writeJetsWithConst = cms.bool( False ),
    inputEMin = cms.double( 0.0 )
)
fragment.hltTauPFJets08Region = cms.EDProducer( "RecoTauJetRegionProducer",
    src = cms.InputTag( "hltAK4PFJetsForTaus" ),
    deltaR = cms.double( 0.8 ),
    pfCandAssocMapSrc = cms.InputTag( "" ),
    verbosity = cms.int32( 0 ),
    maxJetAbsEta = cms.double( 99.0 ),
    minJetPt = cms.double( -1.0 ),
    pfCandSrc = cms.InputTag( "hltParticleFlowForTaus" )
)
fragment.hltHpsTauPFJetsRecoTauChargedHadronsWithNeutrals = cms.EDProducer( "PFRecoTauChargedHadronProducer",
    ranking = cms.VPSet(
      cms.PSet(  selectionFailValue = cms.double( 1000.0 ),
        plugin = cms.string( "PFRecoTauChargedHadronStringQuality" ),
        selection = cms.string( "algoIs(\'kChargedPFCandidate\')" ),
        name = cms.string( "ChargedPFCandidate" ),
        selectionPassFunction = cms.string( "-pt" )
      ),
      cms.PSet(  selectionFailValue = cms.double( 1000.0 ),
        plugin = cms.string( "PFRecoTauChargedHadronStringQuality" ),
        selection = cms.string( "algoIs(\'kPFNeutralHadron\')" ),
        name = cms.string( "ChargedPFCandidate" ),
        selectionPassFunction = cms.string( "-pt" )
      )
    ),
    verbosity = cms.int32( 0 ),
    maxJetAbsEta = cms.double( 99.0 ),
    outputSelection = cms.string( "pt > 0.5" ),
    minJetPt = cms.double( -1.0 ),
    jetSrc = cms.InputTag( "hltAK4PFJetsForTaus" ),
    builders = cms.VPSet(
      cms.PSet(  minBlockElementMatchesNeutralHadron = cms.int32( 2 ),
        dRmergeNeutralHadronWrtNeutralHadron = cms.double( 0.01 ),
        dRmergePhotonWrtNeutralHadron = cms.double( 0.01 ),
        dRmergePhotonWrtOther = cms.double( 0.005 ),
        qualityCuts = cms.PSet(
          vertexTrackFiltering = cms.bool( False ),
          primaryVertexSrc = cms.InputTag( "hltPixelVertices" ),
          recoverLeadingTrk = cms.bool( False ),
          signalQualityCuts = cms.PSet(
            minNeutralHadronEt = cms.double( 30.0 ),
            maxDeltaZ = cms.double( 0.2 ),
            minTrackPt = cms.double( 0.0 ),
            minGammaEt = cms.double( 0.5 ),
            minTrackHits = cms.uint32( 3 ),
            minTrackPixelHits = cms.uint32( 0 ),
            maxTrackChi2 = cms.double( 1000.0 ),
            maxTransverseImpactParameter = cms.double( 0.2 ),
            useTracksInsteadOfPFHadrons = cms.bool( False )
          ),
          vxAssocQualityCuts = cms.PSet(
            minTrackPt = cms.double( 0.0 ),
            minGammaEt = cms.double( 0.5 ),
            minTrackHits = cms.uint32( 3 ),
            minTrackPixelHits = cms.uint32( 0 ),
            maxTrackChi2 = cms.double( 1000.0 ),
            maxTransverseImpactParameter = cms.double( 0.2 ),
            useTracksInsteadOfPFHadrons = cms.bool( False )
          ),
          pvFindingAlgo = cms.string( "closestInDeltaZ" )
        ),
        dRmergeNeutralHadronWrtOther = cms.double( 0.005 ),
        maxUnmatchedBlockElementsNeutralHadron = cms.int32( 1 ),
        dRmergePhotonWrtElectron = cms.double( 0.005 ),
        minMergeGammaEt = cms.double( 0.0 ),
        minBlockElementMatchesPhoton = cms.int32( 2 ),
        dRmergePhotonWrtChargedHadron = cms.double( 0.005 ),
        plugin = cms.string( "PFRecoTauChargedHadronFromPFCandidatePlugin" ),
        dRmergeNeutralHadronWrtChargedHadron = cms.double( 0.005 ),
        minMergeChargedHadronPt = cms.double( 100.0 ),
        maxUnmatchedBlockElementsPhoton = cms.int32( 1 ),
        name = cms.string( "chargedPFCandidates" ),
        dRmergeNeutralHadronWrtElectron = cms.double( 0.05 ),
        chargedHadronCandidatesParticleIds = cms.vint32( 1, 2, 3 ),
        minMergeNeutralHadronEt = cms.double( 0.0 )
      ),
      cms.PSet(  minBlockElementMatchesNeutralHadron = cms.int32( 2 ),
        dRmergeNeutralHadronWrtNeutralHadron = cms.double( 0.01 ),
        dRmergePhotonWrtNeutralHadron = cms.double( 0.01 ),
        dRmergePhotonWrtOther = cms.double( 0.005 ),
        qualityCuts = cms.PSet(
          vertexTrackFiltering = cms.bool( False ),
          primaryVertexSrc = cms.InputTag( "hltPixelVertices" ),
          recoverLeadingTrk = cms.bool( False ),
          signalQualityCuts = cms.PSet(
            minNeutralHadronEt = cms.double( 30.0 ),
            maxDeltaZ = cms.double( 0.2 ),
            minTrackPt = cms.double( 0.0 ),
            minGammaEt = cms.double( 0.5 ),
            minTrackHits = cms.uint32( 3 ),
            minTrackPixelHits = cms.uint32( 0 ),
            maxTrackChi2 = cms.double( 1000.0 ),
            maxTransverseImpactParameter = cms.double( 0.2 ),
            useTracksInsteadOfPFHadrons = cms.bool( False )
          ),
          vxAssocQualityCuts = cms.PSet(
            minTrackPt = cms.double( 0.0 ),
            minGammaEt = cms.double( 0.5 ),
            minTrackHits = cms.uint32( 3 ),
            minTrackPixelHits = cms.uint32( 0 ),
            maxTrackChi2 = cms.double( 1000.0 ),
            maxTransverseImpactParameter = cms.double( 0.2 ),
            useTracksInsteadOfPFHadrons = cms.bool( False )
          ),
          pvFindingAlgo = cms.string( "closestInDeltaZ" )
        ),
        dRmergeNeutralHadronWrtOther = cms.double( 0.005 ),
        dRmergePhotonWrtElectron = cms.double( 0.005 ),
        minMergeGammaEt = cms.double( 0.0 ),
        dRmergePhotonWrtChargedHadron = cms.double( 0.005 ),
        plugin = cms.string( "PFRecoTauChargedHadronFromPFCandidatePlugin" ),
        dRmergeNeutralHadronWrtChargedHadron = cms.double( 0.005 ),
        minMergeChargedHadronPt = cms.double( 0.0 ),
        maxUnmatchedBlockElementsPhoton = cms.int32( 1 ),
        name = cms.string( "PFNeutralHadrons" ),
        dRmergeNeutralHadronWrtElectron = cms.double( 0.05 ),
        chargedHadronCandidatesParticleIds = cms.vint32( 5 ),
        minMergeNeutralHadronEt = cms.double( 0.0 ),
        maxUnmatchedBlockElementsNeutralHadron = cms.int32( 1 ),
        minBlockElementMatchesPhoton = cms.int32( 2 )
      )
    )
)
fragment.hltPFTauPiZeros = cms.EDProducer( "RecoTauPiZeroProducer",
    massHypothesis = cms.double( 0.136 ),
    ranking = cms.VPSet(
      cms.PSet(  selectionFailValue = cms.double( 1000.0 ),
        plugin = cms.string( "RecoTauPiZeroStringQuality" ),
        selection = cms.string( "algoIs('kStrips')" ),
        name = cms.string( "InStrip" ),
        selectionPassFunction = cms.string( "abs(mass() - 0.13579)" )
      )
    ),
    verbosity = cms.int32( 0 ),
    maxJetAbsEta = cms.double( 99.0 ),
    outputSelection = cms.string( "pt > 0" ),
    minJetPt = cms.double( -1.0 ),
    jetSrc = cms.InputTag( "hltAK4PFJetsForTaus" ),
    builders = cms.VPSet(
      cms.PSet(  minGammaEtStripSeed = cms.double( 0.5 ),
        applyElecTrackQcuts = cms.bool( False ),
        stripCandidatesParticleIds = cms.vint32( 2, 4 ),
        makeCombinatoricStrips = cms.bool( False ),
        stripPhiAssociationDistance = cms.double( 0.2 ),
        qualityCuts = cms.PSet(
          vertexTrackFiltering = cms.bool( False ),
          primaryVertexSrc = cms.InputTag( "hltPixelVertices" ),
          recoverLeadingTrk = cms.bool( False ),
          signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double( 0.2 ),
            minTrackPt = cms.double( 0.0 ),
            minGammaEt = cms.double( 0.5 ),
            minTrackHits = cms.uint32( 3 ),
            minTrackPixelHits = cms.uint32( 0 ),
            maxTrackChi2 = cms.double( 1000.0 ),
            maxTransverseImpactParameter = cms.double( 0.2 ),
            useTracksInsteadOfPFHadrons = cms.bool( False )
          ),
          pvFindingAlgo = cms.string( "closestInDeltaZ" )
        ),
        maxStripBuildIterations = cms.int32( -1 ),
        updateStripAfterEachDaughter = cms.bool( False ),
        stripEtaAssociationDistance = cms.double( 0.05 ),
        minStripEt = cms.double( 1.0 ),
        plugin = cms.string( "RecoTauPiZeroStripPlugin2" ),
        minGammaEtStripAdd = cms.double( 0.0 ),
        name = cms.string( "s" )
      )
    )
)
fragment.hltHpsCombinatoricRecoTaus = cms.EDProducer( "RecoTauProducer",
    piZeroSrc = cms.InputTag( "hltPFTauPiZeros" ),
    jetRegionSrc = cms.InputTag( "hltTauPFJets08Region" ),
    verbosity = cms.int32( 0 ),
    maxJetAbsEta = cms.double( 2.5 ),
    outputSelection = cms.string( "leadPFChargedHadrCand().isNonnull()" ),
    chargedHadronSrc = cms.InputTag( "hltHpsTauPFJetsRecoTauChargedHadronsWithNeutrals" ),
    minJetPt = cms.double( 14.0 ),
    jetSrc = cms.InputTag( "hltAK4PFJetsForTaus" ),
    builders = cms.VPSet(
      cms.PSet(  decayModes = cms.VPSet(
  cms.PSet(  maxPiZeros = cms.uint32( 0 ),
    maxTracks = cms.uint32( 6 ),
    nPiZeros = cms.uint32( 0 ),
    nCharged = cms.uint32( 1 )
  ),
  cms.PSet(  maxPiZeros = cms.uint32( 6 ),
    maxTracks = cms.uint32( 6 ),
    nCharged = cms.uint32( 1 ),
    nPiZeros = cms.uint32( 1 )
  ),
  cms.PSet(  maxPiZeros = cms.uint32( 5 ),
    maxTracks = cms.uint32( 6 ),
    nCharged = cms.uint32( 1 ),
    nPiZeros = cms.uint32( 2 )
  ),
  cms.PSet(  maxPiZeros = cms.uint32( 0 ),
    maxTracks = cms.uint32( 6 ),
    nCharged = cms.uint32( 2 ),
    nPiZeros = cms.uint32( 0 )
  ),
  cms.PSet(  maxPiZeros = cms.uint32( 3 ),
    maxTracks = cms.uint32( 6 ),
    nCharged = cms.uint32( 2 ),
    nPiZeros = cms.uint32( 1 )
  ),
  cms.PSet(  maxPiZeros = cms.uint32( 0 ),
    maxTracks = cms.uint32( 6 ),
    nCharged = cms.uint32( 3 ),
    nPiZeros = cms.uint32( 0 )
  ),
  cms.PSet(  maxPiZeros = cms.uint32( 3 ),
    maxTracks = cms.uint32( 6 ),
    nCharged = cms.uint32( 3 ),
    nPiZeros = cms.uint32( 1 )
  )
),
        isolationConeSize = cms.double( 0.5 ),
        minAbsPhotonSumPt_insideSignalCone = cms.double( 2.5 ),
        minAbsPhotonSumPt_outsideSignalCone = cms.double( 1.0E9 ),
        minRelPhotonSumPt_insideSignalCone = cms.double( 0.1 ),
        minRelPhotonSumPt_outsideSignalCone = cms.double( 1.0E9 ),
        name = cms.string( "combinatoric" ),
        pfCandSrc = cms.InputTag( "hltParticleFlowForTaus" ),
        plugin = cms.string( "RecoTauBuilderCombinatoricPlugin" ),
        qualityCuts = cms.PSet(
          isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double( 0.2 ),
            maxTrackChi2 = cms.double( 100.0 ),
            maxTransverseImpactParameter = cms.double( 0.03 ),
            minGammaEt = cms.double( 1.5 ),
            minTrackHits = cms.uint32( 3 ),
            minTrackPixelHits = cms.uint32( 0 ),
            minTrackPt = cms.double( 1.0 ),
            minTrackVertexWeight = cms.double( -1.0 )
          ),
          leadingTrkOrPFCandOption = cms.string( "leadPFCand" ),
          primaryVertexSrc = cms.InputTag( "hltPixelVertices" ),
          pvFindingAlgo = cms.string( "closestInDeltaZ" ),
          recoverLeadingTrk = cms.bool( False ),
          signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double( 0.4 ),
            maxTrackChi2 = cms.double( 1000.0 ),
            maxTransverseImpactParameter = cms.double( 0.2 ),
            minGammaEt = cms.double( 0.5 ),
            minNeutralHadronEt = cms.double( 30.0 ),
            minTrackHits = cms.uint32( 3 ),
            minTrackPixelHits = cms.uint32( 0 ),
            minTrackPt = cms.double( 0.5 ),
            minTrackVertexWeight = cms.double( -1.0 )
          ),
          vertexTrackFiltering = cms.bool( False ),
          vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double( 1000.0 ),
            maxTransverseImpactParameter = cms.double( 0.2 ),
            minGammaEt = cms.double( 0.5 ),
            minTrackHits = cms.uint32( 3 ),
            minTrackPixelHits = cms.uint32( 0 ),
            minTrackPt = cms.double( 0.5 ),
            minTrackVertexWeight = cms.double( -1.0 )
          )
        ),
        signalConeSize = cms.string( "max(min(0.1, 3.0/pt()), 0.05)" )
      )
    ),
    buildNullTaus = cms.bool( False ),
    modifiers = cms.VPSet(
      cms.PSet(  DataType = cms.string( "AOD" ),
        EcalStripSumE_deltaEta = cms.double( 0.03 ),
        EcalStripSumE_deltaPhiOverQ_maxValue = cms.double( 0.5 ),
        EcalStripSumE_deltaPhiOverQ_minValue = cms.double( -0.1 ),
        EcalStripSumE_minClusEnergy = cms.double( 0.1 ),
        ElectronPreIDProducer = cms.InputTag( "elecpreid" ),
        maximumForElectrionPreIDOutput = cms.double( -0.1 ),
        name = cms.string( "elec_rej" ),
        plugin = cms.string( "RecoTauElectronRejectionPlugin" ),
        ElecPreIDLeadTkMatch_maxDR = cms.double( 0.01 )
      ),
      cms.PSet(  name = cms.string( "tau_mass" ),
        plugin = cms.string( "PFRecoTauMassPlugin" ),
        verbosity = cms.int32( 0 )
      )
    )
)
fragment.hltHpsSelectionDiscriminator = cms.EDProducer( "PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag( "hltHpsCombinatoricRecoTaus" ),
    verbosity = cms.int32( 0 ),
    minTauPt = cms.double( 0.0 ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    matchingCone = cms.double( 0.5 ),
    decayModes = cms.VPSet(
      cms.PSet(  maxMass = cms.string( "1." ),
        nPiZeros = cms.uint32( 0 ),
        minMass = cms.double( -1000.0 ),
        nChargedPFCandsMin = cms.uint32( 1 ),
        nTracksMin = cms.uint32( 1 ),
        nCharged = cms.uint32( 1 ),
        applyBendCorrection = cms.PSet(
          phi = cms.bool( True ),
          eta = cms.bool( True ),
          mass = cms.bool( True )
        )
      ),
      cms.PSet(  maxMass = cms.string( "max(1.72, min(1.72*sqrt(pt/100.), 4.2))" ),
        nPiZeros = cms.uint32( 1 ),
        minMass = cms.double( 0.0 ),
        nChargedPFCandsMin = cms.uint32( 1 ),
        nTracksMin = cms.uint32( 1 ),
        nCharged = cms.uint32( 1 ),
        assumeStripMass = cms.double( 0.1349 ),
        applyBendCorrection = cms.PSet(
          phi = cms.bool( True ),
          eta = cms.bool( True ),
          mass = cms.bool( True )
        )
      ),
      cms.PSet(  minPi0Mass = cms.double( 0.0 ),
        maxMass = cms.string( "max(1.72, min(1.72*sqrt(pt/100.), 4.0))" ),
        maxPi0Mass = cms.double( 0.8 ),
        nPiZeros = cms.uint32( 2 ),
        minMass = cms.double( 0.4 ),
        nChargedPFCandsMin = cms.uint32( 1 ),
        nTracksMin = cms.uint32( 1 ),
        nCharged = cms.uint32( 1 ),
        assumeStripMass = cms.double( 0.0 ),
        applyBendCorrection = cms.PSet(
          phi = cms.bool( True ),
          eta = cms.bool( True ),
          mass = cms.bool( True )
        )
      ),
      cms.PSet(  maxMass = cms.string( "1.2" ),
        nPiZeros = cms.uint32( 0 ),
        minMass = cms.double( 0.0 ),
        nChargedPFCandsMin = cms.uint32( 1 ),
        nTracksMin = cms.uint32( 2 ),
        nCharged = cms.uint32( 2 ),
        applyBendCorrection = cms.PSet(
          phi = cms.bool( True ),
          eta = cms.bool( False ),
          mass = cms.bool( True )
        )
      ),
      cms.PSet(  maxMass = cms.string( "max(1.6, min(1.6*sqrt(pt/100.), 4.0))" ),
        minMass = cms.double( 0.0 ),
        nCharged = cms.uint32( 2 ),
        nChargedPFCandsMin = cms.uint32( 1 ),
        nPiZeros = cms.uint32( 1 ),
        nTracksMin = cms.uint32( 2 ),
        applyBendCorrection = cms.PSet(
          eta = cms.bool( False ),
          phi = cms.bool( True ),
          mass = cms.bool( True )
        )
      ),
      cms.PSet(  maxMass = cms.string( "1.6" ),
        minMass = cms.double( 0.7 ),
        nCharged = cms.uint32( 3 ),
        nChargedPFCandsMin = cms.uint32( 1 ),
        nPiZeros = cms.uint32( 0 ),
        nTracksMin = cms.uint32( 2 ),
        applyBendCorrection = cms.PSet(
          eta = cms.bool( False ),
          phi = cms.bool( True ),
          mass = cms.bool( True )
        )
      ),
      cms.PSet(  nCharged = cms.uint32( 3 ),
        nPiZeros = cms.uint32( 1 ),
        nTracksMin = cms.uint32( 2 ),
        minMass = cms.double( 0.9 ),
        maxMass = cms.string( "1.6" ),
        applyBendCorrection = cms.PSet(
          eta = cms.bool( False ),
          phi = cms.bool( False ),
          mass = cms.bool( False )
        ),
        nChargedPFCandsMin = cms.uint32( 1 )
      )
    ),
    minPixelHits = cms.int32( 0 ),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool( False )
)
fragment.hltHpsPFTauProducerSansRefs = cms.EDProducer( "RecoTauCleaner",
    outputSelection = cms.string( "" ),
    src = cms.InputTag( "hltHpsCombinatoricRecoTaus" ),
    verbosity = cms.int32( 0 ),
    cleaners = cms.VPSet(
      cms.PSet(  name = cms.string( "HPS_Select" ),
        plugin = cms.string( "RecoTauDiscriminantCleanerPlugin" ),
        src = cms.InputTag( "hltHpsSelectionDiscriminator" )
      ),
      cms.PSet(  name = cms.string( "killSoftTwoProngTaus" ),
        plugin = cms.string( "RecoTauSoftTwoProngTausCleanerPlugin" ),
        minTrackPt = cms.double( 5.0 )
      ),
      cms.PSet(  name = cms.string( "ChargedHadronMultiplicity" ),
        plugin = cms.string( "RecoTauChargedHadronMultiplicityCleanerPlugin" )
      ),
      cms.PSet(  name = cms.string( "Pt" ),
        plugin = cms.string( "RecoTauStringCleanerPlugin" ),
        selection = cms.string( "leadPFCand().isNonnull()" ),
        selectionFailValue = cms.double( 1000.0 ),
        selectionPassFunction = cms.string( "-pt()" ),
        tolerance = cms.double( 0.01 )
      ),
      cms.PSet(  name = cms.string( "StripMultiplicity" ),
        plugin = cms.string( "RecoTauStringCleanerPlugin" ),
        selection = cms.string( "leadPFCand().isNonnull()" ),
        selectionFailValue = cms.double( 1000.0 ),
        selectionPassFunction = cms.string( "-signalPiZeroCandidates().size()" )
      ),
      cms.PSet(  name = cms.string( "CombinedIsolation" ),
        plugin = cms.string( "RecoTauStringCleanerPlugin" ),
        selection = cms.string( "leadPFCand().isNonnull()" ),
        selectionFailValue = cms.double( 1000.0 ),
        selectionPassFunction = cms.string( "isolationPFChargedHadrCandsPtSum() + isolationPFGammaCandsEtSum()" )
      )
    )
)
fragment.hltHpsPFTauProducer = cms.EDProducer( "RecoTauPiZeroUnembedder",
    src = cms.InputTag( "hltHpsPFTauProducerSansRefs" )
)
fragment.hltHpsPFTauDiscriminationByDecayModeFindingNewDMs = cms.EDProducer( "PFRecoTauDiscriminationByHPSSelection",
    PFTauProducer = cms.InputTag( "hltHpsPFTauProducer" ),
    verbosity = cms.int32( 0 ),
    minTauPt = cms.double( 18.0 ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    matchingCone = cms.double( 0.5 ),
    decayModes = cms.VPSet(
      cms.PSet(  maxMass = cms.string( "1." ),
        nPiZeros = cms.uint32( 0 ),
        minMass = cms.double( -1000.0 ),
        nChargedPFCandsMin = cms.uint32( 1 ),
        nTracksMin = cms.uint32( 1 ),
        nCharged = cms.uint32( 1 ),
        applyBendCorrection = cms.PSet(
          phi = cms.bool( True ),
          eta = cms.bool( True ),
          mass = cms.bool( True )
        )
      ),
      cms.PSet(  maxMass = cms.string( "max(1.72, min(1.72*sqrt(pt/100.), 4.2))" ),
        nPiZeros = cms.uint32( 1 ),
        minMass = cms.double( 0.0 ),
        nChargedPFCandsMin = cms.uint32( 1 ),
        nTracksMin = cms.uint32( 1 ),
        nCharged = cms.uint32( 1 ),
        assumeStripMass = cms.double( 0.1349 ),
        applyBendCorrection = cms.PSet(
          phi = cms.bool( True ),
          eta = cms.bool( True ),
          mass = cms.bool( True )
        )
      ),
      cms.PSet(  minPi0Mass = cms.double( 0.0 ),
        maxMass = cms.string( "max(1.72, min(1.72*sqrt(pt/100.), 4.0))" ),
        maxPi0Mass = cms.double( 0.8 ),
        nPiZeros = cms.uint32( 2 ),
        minMass = cms.double( 0.4 ),
        nChargedPFCandsMin = cms.uint32( 1 ),
        nTracksMin = cms.uint32( 1 ),
        nCharged = cms.uint32( 1 ),
        assumeStripMass = cms.double( 0.0 ),
        applyBendCorrection = cms.PSet(
          phi = cms.bool( True ),
          eta = cms.bool( True ),
          mass = cms.bool( True )
        )
      ),
      cms.PSet(  maxMass = cms.string( "1.2" ),
        nPiZeros = cms.uint32( 0 ),
        minMass = cms.double( 0.0 ),
        nChargedPFCandsMin = cms.uint32( 1 ),
        nTracksMin = cms.uint32( 2 ),
        nCharged = cms.uint32( 2 ),
        applyBendCorrection = cms.PSet(
          phi = cms.bool( True ),
          eta = cms.bool( False ),
          mass = cms.bool( True )
        )
      ),
      cms.PSet(  maxMass = cms.string( "max(1.6, min(1.6*sqrt(pt/100.), 4.0))" ),
        minMass = cms.double( 0.0 ),
        nCharged = cms.uint32( 2 ),
        nChargedPFCandsMin = cms.uint32( 1 ),
        nPiZeros = cms.uint32( 1 ),
        nTracksMin = cms.uint32( 2 ),
        applyBendCorrection = cms.PSet(
          eta = cms.bool( False ),
          phi = cms.bool( True ),
          mass = cms.bool( True )
        )
      ),
      cms.PSet(  maxMass = cms.string( "1.6" ),
        minMass = cms.double( 0.7 ),
        nCharged = cms.uint32( 3 ),
        nChargedPFCandsMin = cms.uint32( 1 ),
        nPiZeros = cms.uint32( 0 ),
        nTracksMin = cms.uint32( 2 ),
        applyBendCorrection = cms.PSet(
          eta = cms.bool( False ),
          phi = cms.bool( True ),
          mass = cms.bool( True )
        )
      ),
      cms.PSet(  nCharged = cms.uint32( 3 ),
        nPiZeros = cms.uint32( 1 ),
        nTracksMin = cms.uint32( 2 ),
        minMass = cms.double( 0.9 ),
        maxMass = cms.string( "1.6" ),
        applyBendCorrection = cms.PSet(
          eta = cms.bool( False ),
          phi = cms.bool( False ),
          mass = cms.bool( False )
        ),
        nChargedPFCandsMin = cms.uint32( 1 )
      )
    ),
    minPixelHits = cms.int32( 0 ),
    requireTauChargedHadronsToBeChargedPFCands = cms.bool( False )
)
fragment.hltHpsPFTauTrackFindingDiscriminator = cms.EDProducer( "PFRecoTauDiscriminationByLeadingObjectPtCut",
    UseOnlyChargedHadrons = cms.bool( True ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    PFTauProducer = cms.InputTag( "hltHpsPFTauProducer" ),
    MinPtLeadingObject = cms.double( 0.0 )
)
fragment.hltHpsSelectedPFTausTrackFinding = cms.EDFilter( "PFTauSelector",
    discriminators = cms.VPSet(
      cms.PSet(  discriminator = cms.InputTag( "hltHpsPFTauTrackFindingDiscriminator" ),
        selectionCut = cms.double( 0.5 )
      )
    ),
    cut = cms.string( "pt > 0" ),
    src = cms.InputTag( "hltHpsPFTauProducer" )
)
fragment.hltHpsPFTauTrack = cms.EDFilter( "HLT1PFTau",
    saveTags = cms.bool( True ),
    MaxMass = cms.double( -1.0 ),
    MinN = cms.int32( 1 ),
    MaxEta = cms.double( 2.5 ),
    MinEta = cms.double( -1.0 ),
    MinMass = cms.double( -1.0 ),
    inputTag = cms.InputTag( "hltHpsPFTauProducer" ),
    MinE = cms.double( -1.0 ),
    triggerType = cms.int32( 84 ),
    MinPt = cms.double( 0.0 )
)

#new part
fragment.HLTIter0PSetTrajectoryFilterIT = cms.PSet(
  minimumNumberOfHits = cms.int32( 4 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 0 ),
  minPt = cms.double( 0.3 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 4 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTIter0GroupedCkfTrajectoryBuilderIT = cms.PSet(
  keepOriginalIfRebuildFails = cms.bool( False ),
  lockHits = cms.bool( True ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0PSetTrajectoryFilterIT" ) ),
  doSeedingRegionRebuilding = cms.bool( False ),
  useHitsSplitting = cms.bool( False ),
  maxCand = cms.int32( 2 ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator9" ),
  intermediateCleaning = cms.bool( True ),
  bestHitOnly = cms.bool( True ),
  useSameTrajFilter = cms.bool( True ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  lostHitPenalty = cms.double( 30.0 ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  alwaysUseInvalidHits = cms.bool( False ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0PSetTrajectoryFilterIT" ) ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" )
)
fragment.HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT = cms.PSet(
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.9 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 10.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  maxLostHits = cms.int32( 999 )
)
fragment.HLTIter0IterL3MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "" ),
  keepOriginalIfRebuildFails = cms.bool( True ),
  lostHitPenalty = cms.double( 1.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  minNrOfHitsForRebuild = cms.int32( 2 ),
  maxCand = cms.int32( 5 ),
  alwaysUseInvalidHits = cms.bool( True ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0IterL3MuonGroupedCkfTrajectoryFilterIT" ) ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 1000.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)
fragment.HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT = cms.PSet(
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.9 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 10.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 0.1 ),
  maxLostHits = cms.int32( 999 )
)
fragment.HLTIter0IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "" ),
  keepOriginalIfRebuildFails = cms.bool( True ),
  lostHitPenalty = cms.double( 1.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  minNrOfHitsForRebuild = cms.int32( 2 ),
  maxCand = cms.int32( 5 ),
  alwaysUseInvalidHits = cms.bool( True ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter0IterL3FromL1MuonGroupedCkfTrajectoryFilterIT" ) ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 1000.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)
fragment.HLTIter1PSetTrajectoryFilterIT = cms.PSet(
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 0 ),
  minPt = cms.double( 0.2 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTIter1GroupedCkfTrajectoryBuilderIT = cms.PSet(
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltIter1ESPMeasurementTracker" ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter1PSetTrajectoryFilterIT" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxCand = cms.int32( 2 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)
fragment.HLTSeedFromProtoTracks = cms.PSet(
  TTRHBuilder = cms.string( "hltESPTTRHBuilderPixelOnly" ),
  SeedMomentumForBOFF = cms.double( 5.0 ),
  propagator = cms.string( "PropagatorWithMaterialParabolicMf" ),
  forceKinematicWithRegionDirection = cms.bool( False ),
  magneticField = cms.string( "ParabolicMf" ),
  OriginTransverseErrorMultiplier = cms.double( 1.0 ),
  ComponentName = cms.string( "SeedFromConsecutiveHitsCreator" ),
  MinOneOverPtError = cms.double( 1.0 )
)
fragment.HLTPSetMuonCkfTrajectoryFilter = cms.PSet(
  minimumNumberOfHits = cms.int32( 5 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.9 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( -1 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTPSetMuonCkfTrajectoryBuilder = cms.PSet(
  rescaleErrorIfFail = cms.double( 1.0 ),
  ComponentType = cms.string( "MuonCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  lostHitPenalty = cms.double( 30.0 ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTPSetMuonCkfTrajectoryFilter" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterial" ),
  maxCand = cms.int32( 5 ),
  alwaysUseInvalidHits = cms.bool( True ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  intermediateCleaning = cms.bool( False ),
  propagatorProximity = cms.string( "SteppingHelixPropagatorAny" ),
  updator = cms.string( "hltESPKFUpdator" ),
  deltaEta = cms.double( -1.0 ),
  useSeedLayer = cms.bool( False ),
  deltaPhi = cms.double( -1.0 )
)
fragment.HLTIter2IterL3FromL1MuonPSetTrajectoryFilterIT = cms.PSet(
  minimumNumberOfHits = cms.int32( 5 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.3 ),
  maxConsecLostHits = cms.int32( 3 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTIter2IterL3FromL1MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltIter2HighPtTkMuESPMeasurementTracker" ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( False ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2IterL3FromL1MuonPSetTrajectoryFilterIT" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxCand = cms.int32( 2 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 1000.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)
fragment.HLTIter2PSetTrajectoryFilterIT = cms.PSet(
  minimumNumberOfHits = cms.int32( 3 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 1 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 0 ),
  minPt = cms.double( 0.3 ),
  maxConsecLostHits = cms.int32( 1 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTIter2GroupedCkfTrajectoryBuilderIT = cms.PSet(
  keepOriginalIfRebuildFails = cms.bool( False ),
  lockHits = cms.bool( True ),
  maxDPhiForLooperReconstruction = cms.double( 2.0 ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2PSetTrajectoryFilterIT" ) ),
  doSeedingRegionRebuilding = cms.bool( False ),
  useHitsSplitting = cms.bool( False ),
  maxCand = cms.int32( 2 ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator16" ),
  intermediateCleaning = cms.bool( True ),
  bestHitOnly = cms.bool( True ),
  useSameTrajFilter = cms.bool( True ),
  MeasurementTrackerName = cms.string( "hltESPMeasurementTracker" ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  lostHitPenalty = cms.double( 30.0 ),
  requireSeedHitsInRebuild = cms.bool( True ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  maxPtForLooperReconstruction = cms.double( 0.7 ),
  cleanTrajectoryAfterInOut = cms.bool( False ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  alwaysUseInvalidHits = cms.bool( False ),
  inOutTrajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2PSetTrajectoryFilterIT" ) ),
  foundHitBonus = cms.double( 5.0 ),
  updator = cms.string( "hltESPKFUpdator" )
)
fragment.HLTPSetPvClusterComparerForIT = cms.PSet(
  track_chi2_max = cms.double( 20.0 ),
  track_pt_max = cms.double( 20.0 ),
  track_prob_min = cms.double( -1.0 ),
  track_pt_min = cms.double( 1.0 )
)
fragment.HLTSiStripClusterChargeCutNone = cms.PSet(  value = cms.double( -1.0 ) )
fragment.HLTIter2IterL3MuonPSetTrajectoryFilterIT = cms.PSet(
  minimumNumberOfHits = cms.int32( 5 ),
  ComponentType = cms.string( "CkfBaseTrajectoryFilter" ),
  seedExtension = cms.int32( 0 ),
  chargeSignificance = cms.double( -1.0 ),
  pixelSeedExtension = cms.bool( False ),
  strictSeedExtension = cms.bool( False ),
  nSigmaMinPt = cms.double( 5.0 ),
  maxCCCLostHits = cms.int32( 9999 ),
  minPt = cms.double( 0.3 ),
  maxConsecLostHits = cms.int32( 3 ),
  extraNumberOfHitsBeforeTheFirstLoop = cms.int32( 4 ),
  constantValueForLostHitsFractionFilter = cms.double( 1.0 ),
  seedPairPenalty = cms.int32( 0 ),
  maxNumberOfHits = cms.int32( 100 ),
  minNumberOfHitsForLoopers = cms.int32( 13 ),
  minGoodStripCharge = cms.PSet(  refToPSet_ = cms.string( "HLTSiStripClusterChargeCutNone" ) ),
  minNumberOfHitsPerLoop = cms.int32( 4 ),
  minHitsMinPt = cms.int32( 3 ),
  maxLostHitsFraction = cms.double( 999.0 ),
  maxLostHits = cms.int32( 1 )
)
fragment.HLTIter2IterL3MuonPSetGroupedCkfTrajectoryBuilderIT = cms.PSet(
  useSameTrajFilter = cms.bool( True ),
  ComponentType = cms.string( "GroupedCkfTrajectoryBuilder" ),
  MeasurementTrackerName = cms.string( "hltIter2HighPtTkMuESPMeasurementTracker" ),
  keepOriginalIfRebuildFails = cms.bool( False ),
  lostHitPenalty = cms.double( 30.0 ),
  lockHits = cms.bool( True ),
  requireSeedHitsInRebuild = cms.bool( False ),
  TTRHBuilder = cms.string( "hltESPTTRHBWithTrackAngle" ),
  propagatorOpposite = cms.string( "PropagatorWithMaterialParabolicMfOpposite" ),
  trajectoryFilter = cms.PSet(  refToPSet_ = cms.string( "HLTIter2IterL3MuonPSetTrajectoryFilterIT" ) ),
  propagatorAlong = cms.string( "PropagatorWithMaterialParabolicMf" ),
  minNrOfHitsForRebuild = cms.int32( 5 ),
  maxCand = cms.int32( 2 ),
  alwaysUseInvalidHits = cms.bool( False ),
  estimator = cms.string( "hltESPChi2ChargeMeasurementEstimator30" ),
  intermediateCleaning = cms.bool( True ),
  foundHitBonus = cms.double( 1000.0 ),
  updator = cms.string( "hltESPKFUpdator" ),
  bestHitOnly = cms.bool( True )
)

from RecoTauTag.RecoTau.PFRecoTauDiscriminationByIsolation_cfi import *
from RecoTauTag.RecoTau.RecoTauDiscriminantCutMultiplexer_cfi import *
from RecoTauTag.RecoTau.PFRecoTauQualityCuts_cfi import PFTauQualityCuts


fragment.hltFixedGridRhoFastjetAll = cms.EDProducer( "FixedGridRhoProducerFastjet",
    gridSpacing = cms.double( 0.55 ),
    maxRapidity = cms.double( 5.0 ),
    pfCandidatesTag = cms.InputTag( "hltParticleFlowReg" )
)
fragment.hltRechitInRegionsECAL = cms.EDProducer( "HLTEcalRecHitInAllL1RegionsProducer",
    l1InputRegions = cms.VPSet(
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "EGamma" ),
        minEt = cms.double( 5.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      ),
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','Jet' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "Jet" ),
        minEt = cms.double( 170.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      ),
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','Tau' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "Tau" ),
        minEt = cms.double( 100.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      )
    ),
    recHitLabels = cms.VInputTag( 'hltEcalRecHit:EcalRecHitsEB','hltEcalRecHit:EcalRecHitsEE' ),
    productLabels = cms.vstring( 'EcalRecHitsEB',
      'EcalRecHitsEE' )
)
fragment.hltParticleFlowRecHitECALL1Seeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet(
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEB' ),
        srFlags = cms.InputTag( "" ),
        name = cms.string( "PFEBRecHitCreator" ),
        qualityTests = cms.VPSet(
          cms.PSet(  name = cms.string( "PFRecHitQTestDBThreshold" ),
            applySelectionsToAllCrystals = cms.bool( True )
          ),
          cms.PSet(  topologicalCleaning = cms.bool( True ),
            skipTTRecoveredHits = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            name = cms.string( "PFRecHitQTestECAL" ),
            timingCleaning = cms.bool( True )
          )
        )
      ),
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsECAL','EcalRecHitsEE' ),
        srFlags = cms.InputTag( "" ),
        name = cms.string( "PFEERecHitCreator" ),
        qualityTests = cms.VPSet(
          cms.PSet(  name = cms.string( "PFRecHitQTestDBThreshold" ),
            applySelectionsToAllCrystals = cms.bool( True )
          ),
          cms.PSet(  topologicalCleaning = cms.bool( True ),
            skipTTRecoveredHits = cms.bool( True ),
            cleaningThreshold = cms.double( 2.0 ),
            name = cms.string( "PFRecHitQTestECAL" ),
            timingCleaning = cms.bool( True )
          )
        )
      )
    ),
    navigator = cms.PSet(
      barrel = cms.PSet(  ),
      endcap = cms.PSet(  ),
      name = cms.string( "PFRecHitECALNavigator" )
    )
)
fragment.hltParticleFlowClusterECALUncorrectedL1Seeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet(
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet(
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( 9 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.08 ),
        minFractionInCalc = cms.double( 1.0E-9 ),
        timeResolutionCalcBarrel = cms.PSet(
          corrTermLowE = cms.double( 0.0510871 ),
          threshLowE = cms.double( 0.5 ),
          noiseTerm = cms.double( 1.10889 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 1.31883 ),
          threshHighE = cms.double( 5.0 ),
          constantTerm = cms.double( 0.428192 )
        ),
        timeResolutionCalcEndcap = cms.PSet(
          corrTermLowE = cms.double( 0.0 ),
          threshLowE = cms.double( 1.0 ),
          noiseTerm = cms.double( 5.72489999999 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 6.92683000001 ),
          threshHighE = cms.double( 10.0 ),
          constantTerm = cms.double( 0.0 )
        )
      ),
      maxIterations = cms.uint32( 50 ),
      positionCalcForConvergence = cms.PSet(
        minAllowedNormalization = cms.double( 0.0 ),
        T0_ES = cms.double( 1.2 ),
        algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" ),
        T0_EE = cms.double( 3.1 ),
        T0_EB = cms.double( 7.4 ),
        X0 = cms.double( 0.89 ),
        minFractionInCalc = cms.double( 0.0 ),
        W0 = cms.double( 4.2 )
      ),
      allCellsPositionCalc = cms.PSet(
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 0.08 ),
        minFractionInCalc = cms.double( 1.0E-9 ),
        timeResolutionCalcBarrel = cms.PSet(
          corrTermLowE = cms.double( 0.0510871 ),
          threshLowE = cms.double( 0.5 ),
          noiseTerm = cms.double( 1.10889 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 1.31883 ),
          threshHighE = cms.double( 5.0 ),
          constantTerm = cms.double( 0.428192 )
        ),
        timeResolutionCalcEndcap = cms.PSet(
          corrTermLowE = cms.double( 0.0 ),
          threshLowE = cms.double( 1.0 ),
          noiseTerm = cms.double( 5.72489999999 ),
          constantTermLowE = cms.double( 0.0 ),
          noiseTermLowE = cms.double( 6.92683000001 ),
          threshHighE = cms.double( 10.0 ),
          constantTerm = cms.double( 0.0 )
        )
      ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet(
        cms.PSet(  recHitEnergyNorm = cms.double( 0.08 ),
          detector = cms.string( "ECAL_BARREL" )
        ),
        cms.PSet(  recHitEnergyNorm = cms.double( 0.3 ),
          detector = cms.string( "ECAL_ENDCAP" )
        )
      ),
      showerSigma = cms.double( 1.5 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True )
    ),
    positionReCalc = cms.PSet(
      minAllowedNormalization = cms.double( 0.0 ),
      T0_ES = cms.double( 1.2 ),
      algoName = cms.string( "ECAL2DPositionCalcWithDepthCorr" ),
      T0_EE = cms.double( 3.1 ),
      T0_EB = cms.double( 7.4 ),
      X0 = cms.double( 0.89 ),
      minFractionInCalc = cms.double( 0.0 ),
      W0 = cms.double( 4.2 )
    ),
    initialClusteringStep = cms.PSet(
      thresholdsByDetector = cms.VPSet(
        cms.PSet(  gatheringThreshold = cms.double( 0.08 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_BARREL" )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 0.3 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "ECAL_ENDCAP" )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( True )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet(
    ),
    seedFinder = cms.PSet(
      thresholdsByDetector = cms.VPSet(
        cms.PSet(  seedingThresholdPt = cms.double( 0.15 ),
          seedingThreshold = cms.double( 0.6 ),
          detector = cms.string( "ECAL_ENDCAP" )
        ),
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 0.23 ),
          detector = cms.string( "ECAL_BARREL" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 8 )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitECALL1Seeded" )
)
fragment.hltRechitInRegionsES = cms.EDProducer( "HLTEcalRecHitInAllL1RegionsProducer",
    l1InputRegions = cms.VPSet(
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','EGamma' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "EGamma" ),
        minEt = cms.double( 5.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      ),
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','Jet' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "Jet" ),
        minEt = cms.double( 170.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      ),
      cms.PSet(  inputColl = cms.InputTag( 'hltGtStage2Digis','Tau' ),
        regionEtaMargin = cms.double( 0.9 ),
        type = cms.string( "Tau" ),
        minEt = cms.double( 100.0 ),
        regionPhiMargin = cms.double( 1.2 ),
        maxEt = cms.double( 999999.0 )
      )
    ),
    recHitLabels = cms.VInputTag( 'hltEcalPreshowerRecHit:EcalRecHitsES' ),
    productLabels = cms.vstring( 'EcalRecHitsES' )
)
fragment.hltParticleFlowRecHitPSL1Seeded = cms.EDProducer( "PFRecHitProducer",
    producers = cms.VPSet(
      cms.PSet(  src = cms.InputTag( 'hltRechitInRegionsES','EcalRecHitsES' ),
        name = cms.string( "PFPSRecHitCreator" ),
        qualityTests = cms.VPSet(
          cms.PSet(  threshold = cms.double( 7.0E-6 ),
            name = cms.string( "PFRecHitQTestThreshold" )
          )
        )
      )
    ),
    navigator = cms.PSet(  name = cms.string( "PFRecHitPreshowerNavigator" ) )
)
fragment.hltParticleFlowClusterPSL1Seeded = cms.EDProducer( "PFClusterProducer",
    pfClusterBuilder = cms.PSet(
      minFracTot = cms.double( 1.0E-20 ),
      stoppingTolerance = cms.double( 1.0E-8 ),
      positionCalc = cms.PSet(
        minAllowedNormalization = cms.double( 1.0E-9 ),
        posCalcNCrystals = cms.int32( -1 ),
        algoName = cms.string( "Basic2DGenericPFlowPositionCalc" ),
        logWeightDenominator = cms.double( 6.0E-5 ),
        minFractionInCalc = cms.double( 1.0E-9 )
      ),
      maxIterations = cms.uint32( 50 ),
      algoName = cms.string( "Basic2DGenericPFlowClusterizer" ),
      recHitEnergyNorms = cms.VPSet(
        cms.PSet(  recHitEnergyNorm = cms.double( 6.0E-5 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  recHitEnergyNorm = cms.double( 6.0E-5 ),
          detector = cms.string( "PS2" )
        )
      ),
      showerSigma = cms.double( 0.3 ),
      minFractionToKeep = cms.double( 1.0E-7 ),
      excludeOtherSeeds = cms.bool( True )
    ),
    positionReCalc = cms.PSet(  ),
    initialClusteringStep = cms.PSet(
      thresholdsByDetector = cms.VPSet(
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  gatheringThreshold = cms.double( 6.0E-5 ),
          gatheringThresholdPt = cms.double( 0.0 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "Basic2DGenericTopoClusterizer" ),
      useCornerCells = cms.bool( False )
    ),
    energyCorrector = cms.PSet(  ),
    recHitCleaners = cms.VPSet(
    ),
    seedFinder = cms.PSet(
      thresholdsByDetector = cms.VPSet(
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.2E-4 ),
          detector = cms.string( "PS1" )
        ),
        cms.PSet(  seedingThresholdPt = cms.double( 0.0 ),
          seedingThreshold = cms.double( 1.2E-4 ),
          detector = cms.string( "PS2" )
        )
      ),
      algoName = cms.string( "LocalMaximumSeedFinder" ),
      nNeighbours = cms.int32( 4 )
    ),
    recHitsSource = cms.InputTag( "hltParticleFlowRecHitPSL1Seeded" )
)
fragment.hltParticleFlowClusterECALL1Seeded = cms.EDProducer( "CorrectedECALPFClusterProducer",
    inputPS = cms.InputTag( "hltParticleFlowClusterPSL1Seeded" ),
    minimumPSEnergy = cms.double( 0.0 ),
    energyCorrector = cms.PSet(
      algoName = cms.string( "PFClusterEMEnergyCorrector" ),
      applyCrackCorrections = cms.bool( False )
    ),
    inputECAL = cms.InputTag( "hltParticleFlowClusterECALUncorrectedL1Seeded" )
)
fragment.hltParticleFlowSuperClusterECALL1Seeded = cms.EDProducer( "PFECALSuperClusterProducer",
    PFSuperClusterCollectionEndcap = cms.string( "hltParticleFlowSuperClusterECALEndcap" ),
    doSatelliteClusterMerge = cms.bool( False ),
    BeamSpot = cms.InputTag( "hltOnlineBeamSpot" ),
    PFBasicClusterCollectionBarrel = cms.string( "hltParticleFlowBasicClusterECALBarrel" ),
    useRegression = cms.bool( True ),
    satelliteMajorityFraction = cms.double( 0.5 ),
    isOOTCollection = cms.bool( False ),
    thresh_PFClusterEndcap = cms.double( 0.5 ),
    ESAssociation = cms.InputTag( "hltParticleFlowClusterECALL1Seeded" ),
    PFBasicClusterCollectionPreshower = cms.string( "hltParticleFlowBasicClusterECALPreshower" ),
    use_preshower = cms.bool( True ),
    thresh_PFClusterBarrel = cms.double( 0.5 ),
    thresh_SCEt = cms.double( 4.0 ),
    etawidth_SuperClusterEndcap = cms.double( 0.04 ),
    phiwidth_SuperClusterEndcap = cms.double( 0.6 ),
    verbose = cms.untracked.bool( False ),
    useDynamicDPhiWindow = cms.bool( True ),
    PFSuperClusterCollectionBarrel = cms.string( "hltParticleFlowSuperClusterECALBarrel" ),
    regressionConfig = cms.PSet(
      uncertaintyKeyEB = cms.string( "pfscecal_EBUncertainty_online" ),
      ecalRecHitsEE = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEE' ),
      ecalRecHitsEB = cms.InputTag( 'hltEcalRecHit','EcalRecHitsEB' ),
      regressionKeyEE = cms.string( "pfscecal_EECorrection_online" ),
      regressionKeyEB = cms.string( "pfscecal_EBCorrection_online" ),
      uncertaintyKeyEE = cms.string( "pfscecal_EEUncertainty_online" ),
      isHLT = cms.bool( True )
    ),
    applyCrackCorrections = cms.bool( False ),
    satelliteClusterSeedThreshold = cms.double( 50.0 ),
    endcapRecHits = cms.InputTag( 'ecalRecHit','EcalRecHitsEB' ),
    etawidth_SuperClusterBarrel = cms.double( 0.04 ),
    PFBasicClusterCollectionEndcap = cms.string( "hltParticleFlowBasicClusterECALEndcap" ),
    barrelRecHits = cms.InputTag( 'ecalRecHit','EcalRecHitsEE' ),
    thresh_PFClusterSeedBarrel = cms.double( 1.0 ),
    ClusteringType = cms.string( "Mustache" ),
    dropUnseedable = cms.bool( False ),
    EnergyWeight = cms.string( "Raw" ),
    PFClusters = cms.InputTag( "hltParticleFlowClusterECALL1Seeded" ),
    thresh_PFClusterSeedEndcap = cms.double( 1.0 ),
    phiwidth_SuperClusterBarrel = cms.double( 0.6 ),
    thresh_PFClusterES = cms.double( 0.5 ),
    seedThresholdIsET = cms.bool( True ),
    PFSuperClusterCollectionEndcapWithPreshower = cms.string( "hltParticleFlowSuperClusterECALEndcapWithPreshower" )
)
fragment.hltEgammaCandidates = cms.EDProducer( "EgammaHLTRecoEcalCandidateProducers",
    scIslandEndcapProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALEndcapWithPreshower' ),
    scHybridBarrelProducer = cms.InputTag( 'hltParticleFlowSuperClusterECALL1Seeded','hltParticleFlowSuperClusterECALBarrel' ),
    recoEcalCandidateCollection = cms.string( "" )
)

file_names = [
                'core:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_core.pb',
                'inner:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_inner.pb',
                'outer:RecoTauTag/TrainingFiles/data/DeepTauId/deepTau_2017v2p6_e6_outer.pb',
            ]

from RecoTauTag.RecoTau.PFTauPrimaryVertexProducer_cfi      import *
from RecoTauTag.RecoTau.PFTauSecondaryVertexProducer_cfi    import *
from RecoTauTag.RecoTau.PFTauTransverseImpactParameters_cfi import *

## Selection of taus that pass the HPS selections: pt > 15, mass cuts, tauCone cut
from RecoTauTag.RecoTau.PFRecoTauDiscriminationByHPSSelection_cfi import hpsSelectionDiscriminator, decayMode_1Prong0Pi0, decayMode_1Prong1Pi0, decayMode_1Prong2Pi0, decayMode_2Prong0Pi0, decayMode_2Prong1Pi0, decayMode_3Prong0Pi0, decayMode_3Prong1Pi0

fragment.hpsPFTauDiscriminationByDecayModeFindingNewDMs = hpsSelectionDiscriminator.clone(
    PFTauProducer = cms.InputTag('hltHpsPFTauProducerReg'),
    #----------------------------------------------------------------------------
    # CV: disable 3Prong1Pi0 decay mode
    decayModes = cms.VPSet(
        decayMode_1Prong0Pi0,
        decayMode_1Prong1Pi0,
        decayMode_1Prong2Pi0,
        decayMode_2Prong0Pi0,
        decayMode_2Prong1Pi0,
        decayMode_3Prong0Pi0,
        decayMode_3Prong1Pi0,
    )
    #----------------------------------------------------------------------------
)

fragment.hpsPFTauPrimaryVertexProducer = PFTauPrimaryVertexProducer.clone(
    PFTauTag = cms.InputTag("hltHpsPFTauProducerReg"),
    ElectronTag = cms.InputTag("hltEgammaCandidates"),
    MuonTag = cms.InputTag("hltMuonsReg"),
    PVTag = cms.InputTag("hltPixelVertices"),
    beamSpot = cms.InputTag("hltOnlineBeamSpot"),
    Algorithm = cms.int32(0),
    useBeamSpot = cms.bool(True),
    RemoveMuonTracks = cms.bool(False),
    RemoveElectronTracks = cms.bool(False),
    useSelectedTaus = cms.bool(False),
    discriminators = cms.VPSet(
        cms.PSet(
            discriminator = cms.InputTag('hpsPFTauDiscriminationByDecayModeFindingNewDMs'),
            selectionCut = cms.double(0.5)
        )
    ),
    cut = cms.string("pt > 18.0 & abs(eta) < 2.4"),
    qualityCuts = cms.PSet(
        isolationQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.2),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.03),
            minGammaEt = cms.double(1.5),
            minTrackHits = cms.uint32(8),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(1.0),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        leadingTrkOrPFCandOption = cms.string('leadPFCand'),
        primaryVertexSrc = cms.InputTag("hltPixelVertices"),
        pvFindingAlgo = cms.string('closestInDeltaZ'),
        recoverLeadingTrk = cms.bool(False),
        signalQualityCuts = cms.PSet(
            maxDeltaZ = cms.double(0.4),
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minNeutralHadronEt = cms.double(30.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        ),
        vertexTrackFiltering = cms.bool(False),
        vxAssocQualityCuts = cms.PSet(
            maxTrackChi2 = cms.double(100.0),
            maxTransverseImpactParameter = cms.double(0.1),
            minGammaEt = cms.double(1.0),
            minTrackHits = cms.uint32(3),
            minTrackPixelHits = cms.uint32(0),
            minTrackPt = cms.double(0.5),
            minTrackVertexWeight = cms.double(-1.0)
        )
    )
)

fragment.hpsPFTauSecondaryVertexProducer = PFTauSecondaryVertexProducer.clone(
    PFTauTag = cms.InputTag("hltHpsPFTauProducerReg")
)
fragment.hpsPFTauTransverseImpactParameters = PFTauTransverseImpactParameters.clone(
    PFTauTag = cms.InputTag("hltHpsPFTauProducerReg"),
    PFTauPVATag = cms.InputTag("hpsPFTauPrimaryVertexProducer"),
    PFTauSVATag = cms.InputTag("hpsPFTauSecondaryVertexProducer"),
    useFullCalculation = cms.bool(True)
)

from RecoTauTag.RecoTau.TauDiscriminatorTools import noPrediscriminants
from RecoTauTag.RecoTau.PFRecoTauDiscriminationByLeadingObjectPtCut_cfi import pfRecoTauDiscriminationByLeadingObjectPtCut

fragment.pfRecoTauDiscriminationByLeadingTrackFinding = pfRecoTauDiscriminationByLeadingObjectPtCut.clone(
    # Tau collection to discriminate
    PFTauProducer = cms.InputTag('hltHpsPFTauProducerReg'),

    # Only look for charged PFCandidates
    UseOnlyChargedHadrons = cms.bool(True),

    # no pre-reqs for this cut
    Prediscriminants = noPrediscriminants,

    # Any *existing* charged PFCandidate will meet this requirement - so it is
    # a test for existence, not pt
    MinPtLeadingObject = cms.double(0.0)
)

PFTauQualityCuts.primaryVertexSrc = cms.InputTag("hltPixelVertices")

fragment.chargedIsoPtSum = pfRecoTauDiscriminationByIsolation.clone(
    PFTauProducer = cms.InputTag('hltHpsPFTauProducerReg'),
    particleFlowSrc = cms.InputTag("hltParticleFlowReg"),
    vertexSrc = PFTauQualityCuts.primaryVertexSrc,
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    applyOccupancyCut = cms.bool(False),
    applySumPtCut = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(False),
    storeRawSumPt = cms.bool(True),
    storeRawPUsumPt = cms.bool(False),
    customOuterCone = cms.double(0.5),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    verbosity = cms.int32(0)
)
fragment.chargedIsoPtSumdR03 = pfRecoTauDiscriminationByIsolation.clone(
    PFTauProducer = cms.InputTag('hltHpsPFTauProducerReg'),
    particleFlowSrc = cms.InputTag("hltParticleFlowReg"),
    vertexSrc = PFTauQualityCuts.primaryVertexSrc,
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    applyOccupancyCut = cms.bool(False),
    applySumPtCut = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(False),
    storeRawSumPt = cms.bool(True),
    storeRawPUsumPt = cms.bool(False),
    customOuterCone = cms.double(0.3),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    verbosity = cms.int32(0)
)
fragment.neutralIsoPtSum = pfRecoTauDiscriminationByIsolation.clone(
    PFTauProducer = cms.InputTag('hltHpsPFTauProducerReg'),
    particleFlowSrc = cms.InputTag("hltParticleFlowReg"),
    vertexSrc = cms.InputTag("hltPixelVertices"),
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applySumPtCut = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(False),
    storeRawSumPt = cms.bool(True),
    storeRawPUsumPt = cms.bool(False),
    customOuterCone = cms.double(0.5),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    verbosity = cms.int32(0)
)
fragment.neutralIsoPtSumdR03 = pfRecoTauDiscriminationByIsolation.clone(
    PFTauProducer = cms.InputTag('hltHpsPFTauProducerReg'),
    particleFlowSrc = cms.InputTag("hltParticleFlowReg"),
    vertexSrc = cms.InputTag("hltPixelVertices"),
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applySumPtCut = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(False),
    storeRawSumPt = cms.bool(True),
    storeRawPUsumPt = cms.bool(False),
    customOuterCone = cms.double(0.3),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    verbosity = cms.int32(0)
)
fragment.puCorrPtSum = pfRecoTauDiscriminationByIsolation.clone(
    PFTauProducer = cms.InputTag('hltHpsPFTauProducerReg'),
    particleFlowSrc = cms.InputTag("hltParticleFlowReg"),
    vertexSrc = cms.InputTag("hltPixelVertices"),
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applySumPtCut = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(True),
    storeRawSumPt = cms.bool(False),
    storeRawPUsumPt = cms.bool(True),
    customOuterCone = cms.double(0.5),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    verbosity = cms.int32(0)
)
requireDecayMode = cms.PSet(
    BooleanOperator = cms.string("and"),
    decayMode = cms.PSet(
        Producer = cms.InputTag('hpsPFTauDiscriminationByDecayModeFindingNewDMs'),
        cut = cms.double(0.5)
    )
)
fragment.footprintCorrection = pfRecoTauDiscriminationByIsolation.clone(
    PFTauProducer = cms.InputTag('hltHpsPFTauProducerReg'),
    particleFlowSrc = cms.InputTag("hltParticleFlowReg"),
    vertexSrc = cms.InputTag("hltPixelVertices"),
    Prediscriminants = requireDecayMode.clone(),
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applySumPtCut = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(True),
    storeRawSumPt = cms.bool(False),
    storeRawPUsumPt = cms.bool(False),
    storeRawFootprintCorrection = cms.bool(True),
    customOuterCone = cms.double(0.5),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    verbosity = cms.int32(0)
)
fragment.footprintCorrectiondR03 = pfRecoTauDiscriminationByIsolation.clone(
    PFTauProducer = cms.InputTag('hltHpsPFTauProducerReg'),
    particleFlowSrc = cms.InputTag("hltParticleFlowReg"),
    vertexSrc = cms.InputTag("hltPixelVertices"),
    Prediscriminants = requireDecayMode.clone(),
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applySumPtCut = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(True),
    storeRawSumPt = cms.bool(False),
    storeRawPUsumPt = cms.bool(False),
    storeRawFootprintCorrection = cms.bool(True),
    customOuterCone = cms.double(0.3),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    verbosity = cms.int32(0)
)

fragment.neutralIsoPtSumWeight = pfRecoTauDiscriminationByIsolation.clone(
    PFTauProducer = cms.InputTag('hltHpsPFTauProducerReg'),
    particleFlowSrc = cms.InputTag("hltParticleFlowReg"),
    vertexSrc = cms.InputTag("hltPixelVertices"),
    Prediscriminants = requireDecayMode.clone(),
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    UseAllPFCandsForWeights = cms.bool(True),
    applyOccupancyCut = cms.bool(False),
    applySumPtCut = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(False),
    storeRawSumPt = cms.bool(True),
    storeRawPUsumPt = cms.bool(False),
    customOuterCone = cms.double(0.5),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    verbosity = cms.int32(0)
)

fragment.neutralIsoPtSumWeightdR03 = pfRecoTauDiscriminationByIsolation.clone(
    PFTauProducer = cms.InputTag('hltHpsPFTauProducerReg'),
    particleFlowSrc = cms.InputTag("hltParticleFlowReg"),
    vertexSrc = cms.InputTag("hltPixelVertices"),
    Prediscriminants = requireDecayMode.clone(),
    ApplyDiscriminationByECALIsolation = cms.bool(True),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    UseAllPFCandsForWeights = cms.bool(True),
    applyOccupancyCut = cms.bool(False),
    applySumPtCut = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(False),
    storeRawSumPt = cms.bool(True),
    storeRawPUsumPt = cms.bool(False),
    customOuterCone = cms.double(0.5),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    verbosity = cms.int32(0)
)

fragment.photonPtSumOutsideSignalCone = pfRecoTauDiscriminationByIsolation.clone(
    PFTauProducer = cms.InputTag('hltHpsPFTauProducerReg'),
    particleFlowSrc = cms.InputTag("hltParticleFlowReg"),
    vertexSrc = cms.InputTag("hltPixelVertices"),
    Prediscriminants = requireDecayMode.clone(),
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applySumPtCut = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(False),
    storeRawSumPt = cms.bool(False),
    storeRawPUsumPt = cms.bool(False),
    storeRawPhotonSumPt_outsideSignalCone = cms.bool(True),
    customOuterCone = cms.double(0.5),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    verbosity = cms.int32(0)
)
fragment.photonPtSumOutsideSignalConedR03 = pfRecoTauDiscriminationByIsolation.clone(
    PFTauProducer = cms.InputTag('hltHpsPFTauProducerReg'),
    particleFlowSrc = cms.InputTag("hltParticleFlowReg"),
    vertexSrc = cms.InputTag("hltPixelVertices"),
    Prediscriminants = requireDecayMode.clone(),
    ApplyDiscriminationByECALIsolation = cms.bool(False),
    ApplyDiscriminationByTrackerIsolation = cms.bool(False),
    applyOccupancyCut = cms.bool(False),
    applySumPtCut = cms.bool(False),
    applyDeltaBetaCorrection = cms.bool(False),
    storeRawSumPt = cms.bool(False),
    storeRawPUsumPt = cms.bool(False),
    storeRawPhotonSumPt_outsideSignalCone = cms.bool(True),
    customOuterCone = cms.double(0.3),
    isoConeSizeForDeltaBeta = cms.double(0.8),
    verbosity = cms.int32(0)
)


fragment.deepTauProducer = cms.EDProducer("DeepTauId",
    electrons                       = cms.InputTag('hltEgammaCandidates'), #boh!
    muons                           = cms.InputTag('hltMuonsReg'),
    taus                            = cms.InputTag("hltHpsPFTauProducerReg"),
    pfcands                         = cms.InputTag('hltParticleFlowReg'),
    vertices                        = cms.InputTag('hltPixelVertices'),
    rho                             = cms.InputTag('hltFixedGridRhoFastjetAll'),
    graph_file                      = cms.vstring(file_names),
    mem_mapped                      = cms.bool(True),
    version                         = cms.uint32(2),
    debug_level                     = cms.int32(0),
    disable_dxy_pca                 = cms.bool(True),
    pfTauTransverseImpactParameters = cms.InputTag('hpsPFTauTransverseImpactParameters'),
    chargedIsoPtSum                 = cms.InputTag('chargedIsoPtSum'),
    chargedIsoPtSumdR03             = cms.InputTag('chargedIsoPtSumdR03'),
    neutralIsoPtSum                 = cms.InputTag('neutralIsoPtSum'),
    neutralIsoPtSumdR03             = cms.InputTag('neutralIsoPtSumdR03'),
    puCorrPtSum                     = cms.InputTag('puCorrPtSum'),
    footprintCorrection             = cms.InputTag('footprintCorrection'),
    neutralIsoPtSumWeight           = cms.InputTag('neutralIsoPtSumWeight'),
    neutralIsoPtSumWeightdR03       = cms.InputTag('neutralIsoPtSumWeightdR03'),
    photonPtSumOutsideSignalCone    = cms.InputTag('photonPtSumOutsideSignalCone')
)
tauJetdR = 0.2
objectdR = 0.5

fragment.tauTupleProducer = cms.EDAnalyzer('TauTupleProducer',
    isMC                            = cms.bool(True), #from outside
    minJetPt                        = cms.double(10.),
    maxJetEta                       = cms.double(3.),
    forceTauJetMatch                = cms.bool(False),
    storeJetsWithoutTau             = cms.bool(False),
    tauJetMatchDeltaRThreshold      = cms.double(tauJetdR),
    objectMatchDeltaRThresholdTau   = cms.double(objectdR),
    objectMatchDeltaRThresholdJet   = cms.double(tauJetdR + objectdR),
    requireGenMatch                 = cms.bool(False), #from outside

    lheEventProduct = cms.InputTag('externalLHEProducer'),
    genEvent        = cms.InputTag('generator'),
    genParticles    = cms.InputTag('genParticles'),
    puInfo          = cms.InputTag('slimmedAddPileupInfo'),
    vertices        = cms.InputTag('hltPixelVertices'),
    rho             = cms.InputTag('hltFixedGridRhoFastjetAll'),
    electrons       = cms.InputTag('hltEgammaCandidates'),
    muons           = cms.InputTag('hltMuonsReg'),
    taus            = cms.InputTag("hltHpsPFTauProducerReg"),
    #jets            = cms.InputTag('hltAK4PFJetsReg'),
    pfCandidates    = cms.InputTag('hltParticleFlowReg'),
    decayModeFindingNewDM           = cms.InputTag('hpsPFTauDiscriminationByDecayModeFindingNewDMs'),
    pfTauTransverseImpactParameters = cms.InputTag('hpsPFTauTransverseImpactParameters'),
    chargedIsoPtSum                 = cms.InputTag('chargedIsoPtSum'),
    chargedIsoPtSumdR03             = cms.InputTag('chargedIsoPtSumdR03'),
    neutralIsoPtSum                 = cms.InputTag('neutralIsoPtSum'),
    neutralIsoPtSumdR03             = cms.InputTag('neutralIsoPtSumdR03'),
    footprintCorrection             = cms.InputTag('footprintCorrection'),
    footprintCorrectiondR03         = cms.InputTag('footprintCorrectiondR03'),
    neutralIsoPtSumWeight           = cms.InputTag('neutralIsoPtSumWeight'),
    neutralIsoPtSumWeightdR03       = cms.InputTag('neutralIsoPtSumWeightdR03'),
    photonPtSumOutsideSignalCone    = cms.InputTag('photonPtSumOutsideSignalCone'),
    photonPtSumOutsideSignalConedR03 = cms.InputTag('photonPtSumOutsideSignalConedR03'),
    puCorrPtSum                     = cms.InputTag('puCorrPtSum'),
    deepTauVSe                      = cms.InputTag('deepTauProducer','VSe'),
    deepTauVSmu                     = cms.InputTag('deepTauProducer','VSmu'),
    deepTauVSjet                    = cms.InputTag('deepTauProducer','VSjet'),
    looseIsoAbs                     = cms.InputTag('hltHpsPFTauLooseAbsoluteChargedIsolationDiscriminator'),
    looseIsoRel                     = cms.InputTag('hltHpsPFTauLooseRelativeChargedIsolationDiscriminator'),
    mediumIsoAbs                    = cms.InputTag('hltHpsPFTauMediumAbsoluteChargedIsolationDiscriminatorReg'),
    mediumIsoRel                    = cms.InputTag('hltHpsPFTauMediumRelativeChargedIsolationDiscriminatorReg'),
    tightIsoAbs                     = cms.InputTag('hltHpsPFTauTightAbsoluteChargedIsolationDiscriminatorReg'),
    tightIsoRel                     = cms.InputTag('hltHpsPFTauTightRelativeChargedIsolationDiscriminatorReg')
)
fragment.hltHpsPFTauLooseAbsoluteChargedIsolationDiscriminator = cms.EDProducer( "PFRecoTauDiscriminationByIsolation",
    applyRhoCorrection = cms.bool( False ),
    PFTauProducer = cms.InputTag( "hltHpsPFTauProducerReg" ),
    storeRawOccupancy = cms.bool( False ),
    maximumSumPtCut = cms.double( 3.9 ),
    qualityCuts = cms.PSet(
      vertexTrackFiltering = cms.bool( False ),
      isolationQualityCuts = cms.PSet(
        maxDeltaZ = cms.double( 0.2 ),
        minTrackPt = cms.double( 0.5 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 100.0 ),
        maxTransverseImpactParameter = cms.double( 0.1 ),
        useTracksInsteadOfPFHadrons = cms.bool( False )
      ),
      primaryVertexSrc = cms.InputTag( "hltPixelVertices" ),
      recoverLeadingTrk = cms.bool( False ),
      signalQualityCuts = cms.PSet(
        maxDeltaZ = cms.double( 0.2 ),
        minTrackPt = cms.double( 0.0 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        maxTransverseImpactParameter = cms.double( 0.2 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        minNeutralHadronEt = cms.double( 1.0 )
      ),
      vxAssocQualityCuts = cms.PSet(
        minTrackPt = cms.double( 0.0 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        maxTransverseImpactParameter = cms.double( 0.2 ),
        useTracksInsteadOfPFHadrons = cms.bool( False )
      ),
      pvFindingAlgo = cms.string( "closestInDeltaZ" )
    ),
    minTauPtForNoIso = cms.double( -99.0 ),
    vertexSrc = cms.InputTag( "NotUsed" ),
    applySumPtCut = cms.bool( True ),
    rhoConeSize = cms.double( 0.5 ),
    ApplyDiscriminationByTrackerIsolation = cms.bool( True ),
    storeRawPhotonSumPt_outsideSignalCone = cms.bool( False ),
    rhoUEOffsetCorrection = cms.double( 1.0 ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAllCaloForMuons" ),
    deltaBetaFactor = cms.string( "0.38" ),
    applyFootprintCorrection = cms.bool( False ),
    UseAllPFCandsForWeights = cms.bool( False ),
    relativeSumPtCut = cms.double( 0.03 ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    applyOccupancyCut = cms.bool( False ),
    applyDeltaBetaCorrection = cms.bool( False ),
    WeightECALIsolation = cms.double( 1.0 ),
    applyRelativeSumPtCut = cms.bool( False ),
    storeRawPUsumPt = cms.bool( False ),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool( False ),
    maximumOccupancy = cms.uint32( 0 ),
    deltaBetaPUTrackPtCutOverride = cms.bool( True ),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool( False ),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double( 1.0E9 ),
    maxRelPhotonSumPt_outsideSignalCone = cms.double( 0.1 ),
    deltaBetaPUTrackPtCutOverride_val = cms.double( 0.5 ),
    ApplyDiscriminationByECALIsolation = cms.bool( False ),
    isoConeSizeForDeltaBeta = cms.double( 0.3 ),
    storeRawSumPt = cms.bool( False ),
    verbosity = cms.int32( 0 ),
    storeRawFootprintCorrection = cms.bool( False ),
    relativeSumPtOffset = cms.double( 0.0 ),
    customOuterCone = cms.double( -1.0 ),
    particleFlowSrc = cms.InputTag( "hltParticleFlowForTaus" ),
    footprintCorrections = cms.VPSet(
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 0" )
      ),
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 1 || decayMode() = 2" )
      ),
      cms.PSet(  offset = cms.string( "2.7" ),
        selection = cms.string( "decayMode() = 5" )
      ),
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 6" )
      ),
      cms.PSet(  offset = cms.string( "max(2.0, 0.22*pt() - 2.0)" ),
        selection = cms.string( "decayMode() = 10" )
      )
    )
)
fragment.hltHpsPFTauLooseRelativeChargedIsolationDiscriminator = cms.EDProducer( "PFRecoTauDiscriminationByIsolation",
    applyRhoCorrection = cms.bool( False ),
    PFTauProducer = cms.InputTag( "hltHpsPFTauProducerReg" ),
    storeRawOccupancy = cms.bool( False ),
    maximumSumPtCut = cms.double( 3.0 ),
    qualityCuts = cms.PSet(
      vertexTrackFiltering = cms.bool( False ),
      isolationQualityCuts = cms.PSet(
        maxDeltaZ = cms.double( 0.2 ),
        minTrackPt = cms.double( 0.5 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 100.0 ),
        maxTransverseImpactParameter = cms.double( 0.1 ),
        useTracksInsteadOfPFHadrons = cms.bool( False )
      ),
      primaryVertexSrc = cms.InputTag( "hltPixelVertices" ),
      recoverLeadingTrk = cms.bool( False ),
      signalQualityCuts = cms.PSet(
        maxDeltaZ = cms.double( 0.2 ),
        minTrackPt = cms.double( 0.0 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        maxTransverseImpactParameter = cms.double( 0.2 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        minNeutralHadronEt = cms.double( 1.0 )
      ),
      vxAssocQualityCuts = cms.PSet(
        minTrackPt = cms.double( 0.0 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        maxTransverseImpactParameter = cms.double( 0.2 ),
        useTracksInsteadOfPFHadrons = cms.bool( False )
      ),
      pvFindingAlgo = cms.string( "closestInDeltaZ" )
    ),
    minTauPtForNoIso = cms.double( -99.0 ),
    vertexSrc = cms.InputTag( "NotUsed" ),
    applySumPtCut = cms.bool( False ),
    rhoConeSize = cms.double( 0.5 ),
    ApplyDiscriminationByTrackerIsolation = cms.bool( True ),
    storeRawPhotonSumPt_outsideSignalCone = cms.bool( False ),
    rhoUEOffsetCorrection = cms.double( 1.0 ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAll" ),
    deltaBetaFactor = cms.string( "0.38" ),
    applyFootprintCorrection = cms.bool( False ),
    UseAllPFCandsForWeights = cms.bool( False ),
    relativeSumPtCut = cms.double( 0.05 ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    applyOccupancyCut = cms.bool( False ),
    applyDeltaBetaCorrection = cms.bool( False ),
    WeightECALIsolation = cms.double( 1.0 ),
    applyRelativeSumPtCut = cms.bool( True ),
    storeRawPUsumPt = cms.bool( False ),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool( False ),
    maximumOccupancy = cms.uint32( 0 ),
    deltaBetaPUTrackPtCutOverride = cms.bool( True ),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool( False ),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double( 1.0E9 ),
    maxRelPhotonSumPt_outsideSignalCone = cms.double( 0.1 ),
    deltaBetaPUTrackPtCutOverride_val = cms.double( 0.5 ),
    ApplyDiscriminationByECALIsolation = cms.bool( False ),
    isoConeSizeForDeltaBeta = cms.double( 0.3 ),
    storeRawSumPt = cms.bool( False ),
    verbosity = cms.int32( 0 ),
    storeRawFootprintCorrection = cms.bool( False ),
    relativeSumPtOffset = cms.double( 50.0 ),
    customOuterCone = cms.double( -1.0 ),
    particleFlowSrc = cms.InputTag( "hltParticleFlowForTaus" ),
    footprintCorrections = cms.VPSet(
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 0" )
      ),
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 1 || decayMode() = 2" )
      ),
      cms.PSet(  offset = cms.string( "2.7" ),
        selection = cms.string( "decayMode() = 5" )
      ),
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 6" )
      ),
      cms.PSet(  offset = cms.string( "max(2.0, 0.22*pt() - 2.0)" ),
        selection = cms.string( "decayMode() = 10" )
      )
    )
)
fragment.hltHpsPFTauMediumAbsoluteChargedIsolationDiscriminatorReg = cms.EDProducer( "PFRecoTauDiscriminationByIsolation",
    applyRhoCorrection = cms.bool( False ),
    PFTauProducer = cms.InputTag( "hltHpsPFTauProducerReg" ),
    storeRawOccupancy = cms.bool( False ),
    maximumSumPtCut = cms.double( 3.7 ),
    qualityCuts = cms.PSet(
      vertexTrackFiltering = cms.bool( False ),
      isolationQualityCuts = cms.PSet(
        maxDeltaZ = cms.double( 0.2 ),
        minTrackPt = cms.double( 0.5 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 100.0 ),
        maxTransverseImpactParameter = cms.double( 0.1 ),
        useTracksInsteadOfPFHadrons = cms.bool( False )
      ),
      primaryVertexSrc = cms.InputTag( "hltPixelVertices" ),
      recoverLeadingTrk = cms.bool( False ),
      signalQualityCuts = cms.PSet(
        maxDeltaZ = cms.double( 0.2 ),
        minTrackPt = cms.double( 0.0 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        maxTransverseImpactParameter = cms.double( 0.2 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        minNeutralHadronEt = cms.double( 1.0 )
      ),
      vxAssocQualityCuts = cms.PSet(
        minTrackPt = cms.double( 0.0 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        maxTransverseImpactParameter = cms.double( 0.2 ),
        useTracksInsteadOfPFHadrons = cms.bool( False )
      ),
      pvFindingAlgo = cms.string( "closestInDeltaZ" )
    ),
    minTauPtForNoIso = cms.double( -99.0 ),
    vertexSrc = cms.InputTag( "NotUsed" ),
    applySumPtCut = cms.bool( True ),
    rhoConeSize = cms.double( 0.357 ),
    ApplyDiscriminationByTrackerIsolation = cms.bool( True ),
    storeRawPhotonSumPt_outsideSignalCone = cms.bool( False ),
    rhoUEOffsetCorrection = cms.double( 0.0 ),
    rhoProducer = cms.InputTag( "NotUsed" ),
    deltaBetaFactor = cms.string( "0.38" ),
    applyFootprintCorrection = cms.bool( False ),
    UseAllPFCandsForWeights = cms.bool( False ),
    relativeSumPtCut = cms.double( 0.03 ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    applyOccupancyCut = cms.bool( False ),
    applyDeltaBetaCorrection = cms.bool( False ),
    WeightECALIsolation = cms.double( 0.33333 ),
    applyRelativeSumPtCut = cms.bool( False ),
    storeRawPUsumPt = cms.bool( False ),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool( False ),
    maximumOccupancy = cms.uint32( 0 ),
    deltaBetaPUTrackPtCutOverride = cms.bool( True ),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool( False ),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double( 1.0E9 ),
    maxRelPhotonSumPt_outsideSignalCone = cms.double( 0.1 ),
    deltaBetaPUTrackPtCutOverride_val = cms.double( 0.5 ),
    ApplyDiscriminationByECALIsolation = cms.bool( False ),
    isoConeSizeForDeltaBeta = cms.double( 0.3 ),
    storeRawSumPt = cms.bool( False ),
    verbosity = cms.int32( 0 ),
    storeRawFootprintCorrection = cms.bool( False ),
    relativeSumPtOffset = cms.double( 0.0 ),
    customOuterCone = cms.double( -1.0 ),
    particleFlowSrc = cms.InputTag( "hltParticleFlowReg" ),
    footprintCorrections = cms.VPSet(
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 0" )
      ),
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 1 || decayMode() = 2" )
      ),
      cms.PSet(  offset = cms.string( "2.7" ),
        selection = cms.string( "decayMode() = 5" )
      ),
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 6" )
      ),
      cms.PSet(  offset = cms.string( "max(2.0, 0.22*pt() - 2.0)" ),
        selection = cms.string( "decayMode() = 10" )
      )
    )
)
fragment.hltHpsPFTauMediumRelativeChargedIsolationDiscriminatorReg = cms.EDProducer( "PFRecoTauDiscriminationByIsolation",
    applyRhoCorrection = cms.bool( False ),
    PFTauProducer = cms.InputTag( "hltHpsPFTauProducerReg" ),
    storeRawOccupancy = cms.bool( False ),
    maximumSumPtCut = cms.double( 2.0 ),
    qualityCuts = cms.PSet(
      vertexTrackFiltering = cms.bool( False ),
      isolationQualityCuts = cms.PSet(
        maxDeltaZ = cms.double( 0.2 ),
        minTrackPt = cms.double( 0.5 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 100.0 ),
        maxTransverseImpactParameter = cms.double( 0.1 ),
        useTracksInsteadOfPFHadrons = cms.bool( False )
      ),
      primaryVertexSrc = cms.InputTag( "hltPixelVertices" ),
      recoverLeadingTrk = cms.bool( False ),
      signalQualityCuts = cms.PSet(
        maxDeltaZ = cms.double( 0.2 ),
        minTrackPt = cms.double( 0.0 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        maxTransverseImpactParameter = cms.double( 0.2 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        minNeutralHadronEt = cms.double( 1.0 )
      ),
      vxAssocQualityCuts = cms.PSet(
        minTrackPt = cms.double( 0.0 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        maxTransverseImpactParameter = cms.double( 0.2 ),
        useTracksInsteadOfPFHadrons = cms.bool( False )
      ),
      pvFindingAlgo = cms.string( "closestInDeltaZ" )
    ),
    minTauPtForNoIso = cms.double( -99.0 ),
    vertexSrc = cms.InputTag( "NotUsed" ),
    applySumPtCut = cms.bool( False ),
    rhoConeSize = cms.double( 0.5 ),
    ApplyDiscriminationByTrackerIsolation = cms.bool( True ),
    storeRawPhotonSumPt_outsideSignalCone = cms.bool( False ),
    rhoUEOffsetCorrection = cms.double( 1.0 ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAll" ),
    deltaBetaFactor = cms.string( "0.38" ),
    applyFootprintCorrection = cms.bool( False ),
    UseAllPFCandsForWeights = cms.bool( False ),
    relativeSumPtCut = cms.double( 0.05 ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    applyOccupancyCut = cms.bool( False ),
    applyDeltaBetaCorrection = cms.bool( False ),
    WeightECALIsolation = cms.double( 1.0 ),
    applyRelativeSumPtCut = cms.bool( True ),
    storeRawPUsumPt = cms.bool( False ),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool( False ),
    maximumOccupancy = cms.uint32( 0 ),
    deltaBetaPUTrackPtCutOverride = cms.bool( True ),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool( False ),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double( 1.0E9 ),
    maxRelPhotonSumPt_outsideSignalCone = cms.double( 0.1 ),
    deltaBetaPUTrackPtCutOverride_val = cms.double( 0.5 ),
    ApplyDiscriminationByECALIsolation = cms.bool( False ),
    isoConeSizeForDeltaBeta = cms.double( 0.3 ),
    storeRawSumPt = cms.bool( False ),
    verbosity = cms.int32( 0 ),
    storeRawFootprintCorrection = cms.bool( False ),
    relativeSumPtOffset = cms.double( 60.0 ),
    customOuterCone = cms.double( -1.0 ),
    particleFlowSrc = cms.InputTag( "hltParticleFlowReg" ),
    footprintCorrections = cms.VPSet(
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 0" )
      ),
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 1 || decayMode() = 2" )
      ),
      cms.PSet(  offset = cms.string( "2.7" ),
        selection = cms.string( "decayMode() = 5" )
      ),
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 6" )
      ),
      cms.PSet(  offset = cms.string( "max(2.0, 0.22*pt() - 2.0)" ),
        selection = cms.string( "decayMode() = 10" )
      )
    )
)
fragment.hltHpsPFTauTightAbsoluteChargedIsolationDiscriminatorReg = cms.EDProducer( "PFRecoTauDiscriminationByIsolation",
    applyRhoCorrection = cms.bool( False ),
    PFTauProducer = cms.InputTag( "hltHpsPFTauProducerReg" ),
    storeRawOccupancy = cms.bool( False ),
    maximumSumPtCut = cms.double( 3.2 ),
    qualityCuts = cms.PSet(
      vertexTrackFiltering = cms.bool( False ),
      isolationQualityCuts = cms.PSet(
        maxDeltaZ = cms.double( 0.2 ),
        minTrackPt = cms.double( 0.5 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 100.0 ),
        maxTransverseImpactParameter = cms.double( 0.1 ),
        useTracksInsteadOfPFHadrons = cms.bool( False )
      ),
      primaryVertexSrc = cms.InputTag( "hltPixelVertices" ),
      recoverLeadingTrk = cms.bool( False ),
      signalQualityCuts = cms.PSet(
        maxDeltaZ = cms.double( 0.2 ),
        minTrackPt = cms.double( 0.0 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        maxTransverseImpactParameter = cms.double( 0.2 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        minNeutralHadronEt = cms.double( 1.0 )
      ),
      vxAssocQualityCuts = cms.PSet(
        minTrackPt = cms.double( 0.0 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        maxTransverseImpactParameter = cms.double( 0.2 ),
        useTracksInsteadOfPFHadrons = cms.bool( False )
      ),
      pvFindingAlgo = cms.string( "closestInDeltaZ" )
    ),
    minTauPtForNoIso = cms.double( -99.0 ),
    vertexSrc = cms.InputTag( "NotUsed" ),
    applySumPtCut = cms.bool( True ),
    rhoConeSize = cms.double( 0.357 ),
    ApplyDiscriminationByTrackerIsolation = cms.bool( True ),
    storeRawPhotonSumPt_outsideSignalCone = cms.bool( False ),
    rhoUEOffsetCorrection = cms.double( 0.0 ),
    rhoProducer = cms.InputTag( "NotUsed" ),
    deltaBetaFactor = cms.string( "0.38" ),
    applyFootprintCorrection = cms.bool( False ),
    UseAllPFCandsForWeights = cms.bool( False ),
    relativeSumPtCut = cms.double( 0.03 ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    applyOccupancyCut = cms.bool( False ),
    applyDeltaBetaCorrection = cms.bool( False ),
    WeightECALIsolation = cms.double( 0.33333 ),
    applyRelativeSumPtCut = cms.bool( False ),
    storeRawPUsumPt = cms.bool( False ),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool( False ),
    maximumOccupancy = cms.uint32( 0 ),
    deltaBetaPUTrackPtCutOverride = cms.bool( True ),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool( False ),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double( 1.0E9 ),
    maxRelPhotonSumPt_outsideSignalCone = cms.double( 0.1 ),
    deltaBetaPUTrackPtCutOverride_val = cms.double( 0.5 ),
    ApplyDiscriminationByECALIsolation = cms.bool( False ),
    isoConeSizeForDeltaBeta = cms.double( 0.3 ),
    storeRawSumPt = cms.bool( False ),
    verbosity = cms.int32( 0 ),
    storeRawFootprintCorrection = cms.bool( False ),
    relativeSumPtOffset = cms.double( 0.0 ),
    customOuterCone = cms.double( -1.0 ),
    particleFlowSrc = cms.InputTag( "hltParticleFlowReg" ),
    footprintCorrections = cms.VPSet(
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 0" )
      ),
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 1 || decayMode() = 2" )
      ),
      cms.PSet(  offset = cms.string( "2.7" ),
        selection = cms.string( "decayMode() = 5" )
      ),
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 6" )
      ),
      cms.PSet(  offset = cms.string( "max(2.0, 0.22*pt() - 2.0)" ),
        selection = cms.string( "decayMode() = 10" )
      )
    )
)
fragment.hltHpsPFTauTightRelativeChargedIsolationDiscriminatorReg = cms.EDProducer( "PFRecoTauDiscriminationByIsolation",
    applyRhoCorrection = cms.bool( False ),
    PFTauProducer = cms.InputTag( "hltHpsPFTauProducerReg" ),
    storeRawOccupancy = cms.bool( False ),
    maximumSumPtCut = cms.double( 2.0 ),
    qualityCuts = cms.PSet(
      vertexTrackFiltering = cms.bool( False ),
      isolationQualityCuts = cms.PSet(
        maxDeltaZ = cms.double( 0.2 ),
        minTrackPt = cms.double( 0.5 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 100.0 ),
        maxTransverseImpactParameter = cms.double( 0.1 ),
        useTracksInsteadOfPFHadrons = cms.bool( False )
      ),
      primaryVertexSrc = cms.InputTag( "hltPixelVertices" ),
      recoverLeadingTrk = cms.bool( False ),
      signalQualityCuts = cms.PSet(
        maxDeltaZ = cms.double( 0.2 ),
        minTrackPt = cms.double( 0.0 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        maxTransverseImpactParameter = cms.double( 0.2 ),
        useTracksInsteadOfPFHadrons = cms.bool( False ),
        minNeutralHadronEt = cms.double( 1.0 )
      ),
      vxAssocQualityCuts = cms.PSet(
        minTrackPt = cms.double( 0.0 ),
        minGammaEt = cms.double( 0.5 ),
        minTrackHits = cms.uint32( 3 ),
        minTrackPixelHits = cms.uint32( 0 ),
        maxTrackChi2 = cms.double( 1000.0 ),
        maxTransverseImpactParameter = cms.double( 0.2 ),
        useTracksInsteadOfPFHadrons = cms.bool( False )
      ),
      pvFindingAlgo = cms.string( "closestInDeltaZ" )
    ),
    minTauPtForNoIso = cms.double( -99.0 ),
    vertexSrc = cms.InputTag( "NotUsed" ),
    applySumPtCut = cms.bool( False ),
    rhoConeSize = cms.double( 0.5 ),
    ApplyDiscriminationByTrackerIsolation = cms.bool( True ),
    storeRawPhotonSumPt_outsideSignalCone = cms.bool( False ),
    rhoUEOffsetCorrection = cms.double( 1.0 ),
    rhoProducer = cms.InputTag( "hltFixedGridRhoFastjetAll" ),
    deltaBetaFactor = cms.string( "0.38" ),
    applyFootprintCorrection = cms.bool( False ),
    UseAllPFCandsForWeights = cms.bool( False ),
    relativeSumPtCut = cms.double( 0.04 ),
    Prediscriminants = cms.PSet(  BooleanOperator = cms.string( "and" ) ),
    applyOccupancyCut = cms.bool( False ),
    applyDeltaBetaCorrection = cms.bool( False ),
    WeightECALIsolation = cms.double( 1.0 ),
    applyRelativeSumPtCut = cms.bool( True ),
    storeRawPUsumPt = cms.bool( False ),
    applyPhotonPtSumOutsideSignalConeCut = cms.bool( False ),
    maximumOccupancy = cms.uint32( 0 ),
    deltaBetaPUTrackPtCutOverride = cms.bool( True ),
    ApplyDiscriminationByWeightedECALIsolation = cms.bool( False ),
    maxAbsPhotonSumPt_outsideSignalCone = cms.double( 1.0E9 ),
    maxRelPhotonSumPt_outsideSignalCone = cms.double( 0.1 ),
    deltaBetaPUTrackPtCutOverride_val = cms.double( 0.5 ),
    ApplyDiscriminationByECALIsolation = cms.bool( False ),
    isoConeSizeForDeltaBeta = cms.double( 0.3 ),
    storeRawSumPt = cms.bool( False ),
    verbosity = cms.int32( 0 ),
    storeRawFootprintCorrection = cms.bool( False ),
    relativeSumPtOffset = cms.double( 70.0 ),
    customOuterCone = cms.double( -1.0 ),
    particleFlowSrc = cms.InputTag( "hltParticleFlowReg" ),
    footprintCorrections = cms.VPSet(
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 0" )
      ),
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 1 || decayMode() = 2" )
      ),
      cms.PSet(  offset = cms.string( "2.7" ),
        selection = cms.string( "decayMode() = 5" )
      ),
      cms.PSet(  offset = cms.string( "0.0" ),
        selection = cms.string( "decayMode() = 6" )
      ),
      cms.PSet(  offset = cms.string( "max(2.0, 0.22*pt() - 2.0)" ),
        selection = cms.string( "decayMode() = 10" )
      )
    )
)

#end new part
fragment.hltBoolEnd = cms.EDFilter( "HLTBool",
    result = cms.bool( True )
)
fragment.hltFEDSelector = cms.EDProducer( "EvFFEDSelector",
    inputTag = cms.InputTag( "rawDataCollector" ),
    fedList = cms.vuint32( 1023, 1024 )
)
fragment.hltTriggerSummaryAOD = cms.EDProducer( "TriggerSummaryProducerAOD",
    moduleLabelPatternsToSkip = cms.vstring(  ),
    processName = cms.string( "@" ),
    moduleLabelPatternsToMatch = cms.vstring( 'hlt*' ),
    throw = cms.bool( False )
)
fragment.hltTriggerSummaryRAW = cms.EDProducer( "TriggerSummaryProducerRAW",
    processName = cms.string( "@" )
)
fragment.hltPreHLTAnalyzerEndpath = cms.EDFilter( "HLTPrescaler",
    L1GtReadoutRecordTag = cms.InputTag( "hltGtStage2Digis" ),
    offset = cms.uint32( 0 )
)
fragment.hltL1TGlobalSummary = cms.EDAnalyzer( "L1TGlobalSummary",
    ExtInputTag = cms.InputTag( "hltGtStage2Digis" ),
    MaxBx = cms.int32( 0 ),
    DumpRecord = cms.bool( False ),
    psFileName = cms.string( "prescale_L1TGlobal.csv" ),
    ReadPrescalesFromFile = cms.bool( False ),
    AlgInputTag = cms.InputTag( "hltGtStage2Digis" ),
    MinBx = cms.int32( 0 ),
    psColumn = cms.int32( 0 ),
    DumpTrigResults = cms.bool( False ),
    DumpTrigSummary = cms.bool( True )
)
fragment.hltTrigReport = cms.EDAnalyzer( "HLTrigReport",
    ReferencePath = cms.untracked.string( "HLTriggerFinalPath" ),
    ReferenceRate = cms.untracked.double( 100.0 ),
    serviceBy = cms.untracked.string( "never" ),
    resetBy = cms.untracked.string( "never" ),
    reportBy = cms.untracked.string( "job" ),
    HLTriggerResults = cms.InputTag( 'TriggerResults','','@currentProcess' )
)

fragment.HLTL1UnpackerSequence = cms.Sequence( fragment.hltGtStage2Digis + fragment.hltGtStage2ObjectMap )
fragment.HLTBeamSpot = cms.Sequence( fragment.hltScalersRawToDigi + fragment.hltOnlineBeamSpot )
fragment.HLTBeginSequence = cms.Sequence( fragment.hltTriggerType + fragment.HLTL1UnpackerSequence + fragment.HLTBeamSpot )
fragment.HLTMuonLocalRecoSequence = cms.Sequence( fragment.hltMuonDTDigis + fragment.hltDt1DRecHits + fragment.hltDt4DSegments + fragment.hltMuonCSCDigis + fragment.hltCsc2DRecHits + fragment.hltCscSegments + fragment.hltMuonRPCDigis + fragment.hltRpcRecHits )
fragment.HLTL2muonrecoNocandSequence = cms.Sequence( fragment.HLTMuonLocalRecoSequence + fragment.hltL2OfflineMuonSeeds + fragment.hltL2MuonSeeds + fragment.hltL2Muons )
fragment.HLTL2muonrecoSequence = cms.Sequence( fragment.HLTL2muonrecoNocandSequence + fragment.hltL2MuonCandidates )
fragment.HLTDoLocalPixelSequence = cms.Sequence( fragment.hltSiPixelDigis + fragment.hltSiPixelClusters + fragment.hltSiPixelClustersCache + fragment.hltSiPixelRecHits )
fragment.HLTDoLocalStripSequence = cms.Sequence( fragment.hltSiStripExcludedFEDListProducer + fragment.hltSiStripRawToClustersFacility + fragment.hltSiStripClusters )
fragment.HLTIterL3OImuonTkCandidateSequence = cms.Sequence( fragment.hltIterL3OISeedsFromL2Muons + fragment.hltIterL3OITrackCandidates + fragment.hltIterL3OIMuCtfWithMaterialTracks + fragment.hltIterL3OIMuonTrackCutClassifier + fragment.hltIterL3OIMuonTrackSelectionHighPurity + fragment.hltL3MuonsIterL3OI )
fragment.HLTIterL3MuonRecoPixelTracksSequence = cms.Sequence( fragment.hltIterL3MuonPixelTracksFilter + fragment.hltIterL3MuonPixelTracksFitter + fragment.hltIterL3MuonPixelTracksTrackingRegions + fragment.hltIterL3MuonPixelLayerQuadruplets + fragment.hltIterL3MuonPixelTracksHitDoublets + fragment.hltIterL3MuonPixelTracksHitQuadruplets + fragment.hltIterL3MuonPixelTracks )
fragment.HLTIterL3MuonRecopixelvertexingSequence = cms.Sequence( fragment.HLTIterL3MuonRecoPixelTracksSequence + fragment.hltIterL3MuonPixelVertices + fragment.hltIterL3MuonTrimmedPixelVertices )
fragment.HLTIterativeTrackingIteration0ForIterL3Muon = cms.Sequence( fragment.hltIter0IterL3MuonPixelSeedsFromPixelTracks + fragment.hltIter0IterL3MuonCkfTrackCandidates + fragment.hltIter0IterL3MuonCtfWithMaterialTracks + fragment.hltIter0IterL3MuonTrackCutClassifier + fragment.hltIter0IterL3MuonTrackSelectionHighPurity )
fragment.HLTIterativeTrackingIteration2ForIterL3Muon = cms.Sequence( fragment.hltIter2IterL3MuonClustersRefRemoval + fragment.hltIter2IterL3MuonMaskedMeasurementTrackerEvent + fragment.hltIter2IterL3MuonPixelLayerTriplets + fragment.hltIter2IterL3MuonPixelClusterCheck + fragment.hltIter2IterL3MuonPixelHitDoublets + fragment.hltIter2IterL3MuonPixelHitTriplets + fragment.hltIter2IterL3MuonPixelSeeds + fragment.hltIter2IterL3MuonCkfTrackCandidates + fragment.hltIter2IterL3MuonCtfWithMaterialTracks + fragment.hltIter2IterL3MuonTrackCutClassifier + fragment.hltIter2IterL3MuonTrackSelectionHighPurity )
fragment.HLTIterativeTrackingIteration3ForIterL3Muon = cms.Sequence( fragment.hltIter3IterL3MuonClustersRefRemoval + fragment.hltIter3IterL3MuonMaskedMeasurementTrackerEvent + fragment.hltIter3IterL3MuonPixelLayerPairs + fragment.hltIter3IterL3MuonL2Candidates + fragment.hltIter3IterL3MuonTrackingRegions + fragment.hltIter3IterL3MuonPixelClusterCheck + fragment.hltIter3IterL3MuonPixelHitDoublets + fragment.hltIter3IterL3MuonPixelSeeds + fragment.hltIter3IterL3MuonCkfTrackCandidates + fragment.hltIter3IterL3MuonCtfWithMaterialTracks + fragment.hltIter3IterL3MuonTrackCutClassifier + fragment.hltIter3IterL3MuonTrackSelectionHighPurity )
fragment.HLTIterativeTrackingIter023ForIterL3Muon = cms.Sequence( fragment.HLTIterativeTrackingIteration0ForIterL3Muon + fragment.HLTIterativeTrackingIteration2ForIterL3Muon + fragment.hltIter2IterL3MuonMerged + fragment.HLTIterativeTrackingIteration3ForIterL3Muon + fragment.hltIter3IterL3MuonMerged )
fragment.HLTIterL3IOmuonTkCandidateSequence = cms.Sequence( fragment.HLTIterL3MuonRecopixelvertexingSequence + fragment.HLTIterativeTrackingIter023ForIterL3Muon + fragment.hltL3MuonsIterL3IO )
fragment.HLTIterL3OIAndIOFromL2muonTkCandidateSequence = cms.Sequence( fragment.HLTIterL3OImuonTkCandidateSequence + fragment.hltIterL3OIL3MuonsLinksCombination + fragment.hltIterL3OIL3Muons + fragment.hltIterL3OIL3MuonCandidates + fragment.hltL2SelectorForL3IO + fragment.HLTIterL3IOmuonTkCandidateSequence + fragment.hltIterL3MuonsFromL2LinksCombination )
fragment.HLTRecoPixelTracksSequenceForIterL3FromL1Muon = cms.Sequence( fragment.hltIterL3FromL1MuonPixelTracksTrackingRegions + fragment.hltIterL3FromL1MuonPixelLayerQuadruplets + fragment.hltIterL3FromL1MuonPixelTracksHitDoublets + fragment.hltIterL3FromL1MuonPixelTracksHitQuadruplets + fragment.hltIterL3FromL1MuonPixelTracks )
fragment.HLTRecopixelvertexingSequenceForIterL3FromL1Muon = cms.Sequence( fragment.HLTRecoPixelTracksSequenceForIterL3FromL1Muon + fragment.hltIterL3FromL1MuonPixelVertices + fragment.hltIterL3FromL1MuonTrimmedPixelVertices )
fragment.HLTIterativeTrackingIteration0ForIterL3FromL1Muon = cms.Sequence( fragment.hltIter0IterL3FromL1MuonPixelSeedsFromPixelTracks + fragment.hltIter0IterL3FromL1MuonCkfTrackCandidates + fragment.hltIter0IterL3FromL1MuonCtfWithMaterialTracks + fragment.hltIter0IterL3FromL1MuonTrackCutClassifier + fragment.hltIter0IterL3FromL1MuonTrackSelectionHighPurity )
fragment.HLTIterativeTrackingIteration2ForIterL3FromL1Muon = cms.Sequence( fragment.hltIter2IterL3FromL1MuonClustersRefRemoval + fragment.hltIter2IterL3FromL1MuonMaskedMeasurementTrackerEvent + fragment.hltIter2IterL3FromL1MuonPixelLayerTriplets + fragment.hltIter2IterL3FromL1MuonPixelClusterCheck + fragment.hltIter2IterL3FromL1MuonPixelHitDoublets + fragment.hltIter2IterL3FromL1MuonPixelHitTriplets + fragment.hltIter2IterL3FromL1MuonPixelSeeds + fragment.hltIter2IterL3FromL1MuonCkfTrackCandidates + fragment.hltIter2IterL3FromL1MuonCtfWithMaterialTracks + fragment.hltIter2IterL3FromL1MuonTrackCutClassifier + fragment.hltIter2IterL3FromL1MuonTrackSelectionHighPurity )
fragment.HLTIterativeTrackingIteration3ForIterL3FromL1Muon = cms.Sequence( fragment.hltIter3IterL3FromL1MuonClustersRefRemoval + fragment.hltIter3IterL3FromL1MuonMaskedMeasurementTrackerEvent + fragment.hltIter3IterL3FromL1MuonPixelLayerPairs + fragment.hltIter3IterL3FromL1MuonTrackingRegions + fragment.hltIter3IterL3FromL1MuonPixelClusterCheck + fragment.hltIter3IterL3FromL1MuonPixelHitDoublets + fragment.hltIter3IterL3FromL1MuonPixelSeeds + fragment.hltIter3IterL3FromL1MuonCkfTrackCandidates + fragment.hltIter3IterL3FromL1MuonCtfWithMaterialTracks + fragment.hltIter3IterL3FromL1MuonTrackCutClassifier + fragment.hltIter3IterL3FromL1MuonTrackSelectionHighPurity )
fragment.HLTIterativeTrackingIter023ForIterL3FromL1Muon = cms.Sequence( fragment.HLTIterativeTrackingIteration0ForIterL3FromL1Muon + fragment.HLTIterativeTrackingIteration2ForIterL3FromL1Muon + fragment.hltIter2IterL3FromL1MuonMerged + fragment.HLTIterativeTrackingIteration3ForIterL3FromL1Muon + fragment.hltIter3IterL3FromL1MuonMerged )
fragment.HLTIterL3IOmuonFromL1TkCandidateSequence = cms.Sequence( fragment.HLTRecopixelvertexingSequenceForIterL3FromL1Muon + fragment.HLTIterativeTrackingIter023ForIterL3FromL1Muon )
fragment.HLTIterL3muonTkCandidateSequence = cms.Sequence( fragment.HLTDoLocalPixelSequence + fragment.HLTDoLocalStripSequence + fragment.HLTIterL3OIAndIOFromL2muonTkCandidateSequence + fragment.hltL1MuonsPt0 + fragment.HLTIterL3IOmuonFromL1TkCandidateSequence )
fragment.HLTL3muonrecoNocandSequence = cms.Sequence( fragment.HLTIterL3muonTkCandidateSequence + fragment.hltIterL3MuonMerged + fragment.hltIterL3MuonAndMuonFromL1Merged + fragment.hltIterL3GlbMuon + fragment.hltIterL3MuonsNoID + fragment.hltIterL3Muons + fragment.hltL3MuonsIterL3Links + fragment.hltIterL3MuonTracks )
fragment.HLTL3muonrecoSequence = cms.Sequence( fragment.HLTL3muonrecoNocandSequence + fragment.hltIterL3MuonCandidates )
fragment.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence = cms.Sequence( fragment.hltEcalDigis + fragment.hltEcalUncalibRecHit + fragment.hltEcalDetIdToBeRecovered + fragment.hltEcalRecHit )
fragment.HLTDoLocalHcalSequence = cms.Sequence( fragment.hltHcalDigis + fragment.hltHbhePhase1Reco + fragment.hltHbhereco + fragment.hltHfprereco + fragment.hltHfreco + fragment.hltHoreco )
fragment.HLTDoCaloSequencePF = cms.Sequence( fragment.HLTDoFullUnpackingEgammaEcalWithoutPreshowerSequence + fragment.HLTDoLocalHcalSequence + fragment.hltTowerMakerForAll )
fragment.HLTRecoJetSequenceAK4UncorrectedPF = cms.Sequence( fragment.HLTDoCaloSequencePF + fragment.hltAK4CaloJetsPF )
fragment.HLTRecoJetSequenceAK4PrePF = cms.Sequence( fragment.HLTRecoJetSequenceAK4UncorrectedPF + fragment.hltAK4CaloJetsPFEt5 )
fragment.HLTRecoPixelTracksSequence = cms.Sequence( fragment.hltPixelTracksFilter + fragment.hltPixelTracksFitter + fragment.hltPixelTracksTrackingRegions + fragment.hltPixelLayerQuadruplets + fragment.hltPixelTracksHitDoublets + fragment.hltPixelTracksHitQuadruplets + fragment.hltPixelTracks )
fragment.HLTRecopixelvertexingSequence = cms.Sequence( fragment.HLTRecoPixelTracksSequence + fragment.hltPixelVertices + fragment.hltTrimmedPixelVertices )
fragment.HLTIterativeTrackingIteration0 = cms.Sequence( fragment.hltIter0PFLowPixelSeedsFromPixelTracks + fragment.hltIter0PFlowCkfTrackCandidates + fragment.hltIter0PFlowCtfWithMaterialTracks + fragment.hltIter0PFlowTrackCutClassifier + fragment.hltIter0PFlowTrackSelectionHighPurity )
fragment.HLTIterativeTrackingIteration1 = cms.Sequence( fragment.hltIter1ClustersRefRemoval + fragment.hltIter1MaskedMeasurementTrackerEvent + fragment.hltIter1PixelLayerQuadruplets + fragment.hltIter1PFlowPixelTrackingRegions + fragment.hltIter1PFlowPixelClusterCheck + fragment.hltIter1PFlowPixelHitDoublets + fragment.hltIter1PFlowPixelHitQuadruplets + fragment.hltIter1PixelTracks + fragment.hltIter1PFLowPixelSeedsFromPixelTracks + fragment.hltIter1PFlowCkfTrackCandidates + fragment.hltIter1PFlowCtfWithMaterialTracks + fragment.hltIter1PFlowTrackCutClassifierPrompt + fragment.hltIter1PFlowTrackCutClassifierDetached + fragment.hltIter1PFlowTrackCutClassifierMerged + fragment.hltIter1PFlowTrackSelectionHighPurity )
fragment.HLTIter1TrackAndTauJets4Iter2Sequence = cms.Sequence( fragment.hltIter1TrackRefsForJets4Iter2 + fragment.hltAK4Iter1TrackJets4Iter2 + fragment.hltIter1TrackAndTauJets4Iter2 )
fragment.HLTIterativeTrackingIteration2 = cms.Sequence( fragment.hltIter2ClustersRefRemoval + fragment.hltIter2MaskedMeasurementTrackerEvent + fragment.hltIter2PixelLayerTriplets + fragment.hltIter2PFlowPixelTrackingRegions + fragment.hltIter2PFlowPixelClusterCheck + fragment.hltIter2PFlowPixelHitDoublets + fragment.hltIter2PFlowPixelHitTriplets + fragment.hltIter2PFlowPixelSeeds + fragment.hltIter2PFlowCkfTrackCandidates + fragment.hltIter2PFlowCtfWithMaterialTracks + fragment.hltIter2PFlowTrackCutClassifier + fragment.hltIter2PFlowTrackSelectionHighPurity )
fragment.HLTIterativeTrackingDoubletRecovery = cms.Sequence( fragment.hltDoubletRecoveryClustersRefRemoval + fragment.hltDoubletRecoveryMaskedMeasurementTrackerEvent + fragment.hltDoubletRecoveryPixelLayersAndRegions + fragment.hltDoubletRecoveryPFlowPixelClusterCheck + fragment.hltDoubletRecoveryPFlowPixelHitDoublets + fragment.hltDoubletRecoveryPFlowPixelSeeds + fragment.hltDoubletRecoveryPFlowCkfTrackCandidates + fragment.hltDoubletRecoveryPFlowCtfWithMaterialTracks + fragment.hltDoubletRecoveryPFlowTrackCutClassifier + fragment.hltDoubletRecoveryPFlowTrackSelectionHighPurity )
fragment.HLTIterativeTrackingIter02 = cms.Sequence( fragment.HLTIterativeTrackingIteration0 + fragment.HLTIterativeTrackingIteration1 + fragment.hltIter1Merged + fragment.HLTIter1TrackAndTauJets4Iter2Sequence + fragment.HLTIterativeTrackingIteration2 + fragment.hltIter2Merged + fragment.HLTIterativeTrackingDoubletRecovery + fragment.hltMergedTracks )
fragment.HLTTrackReconstructionForPF = cms.Sequence( fragment.HLTDoLocalPixelSequence + fragment.HLTRecopixelvertexingSequence + fragment.HLTDoLocalStripSequence + fragment.HLTIterativeTrackingIter02 + fragment.hltPFMuonMerging + fragment.hltMuonLinks + fragment.hltMuons )
fragment.HLTPreshowerSequence = cms.Sequence( fragment.hltEcalPreshowerDigis + fragment.hltEcalPreshowerRecHit )
fragment.HLTParticleFlowSequenceForTaus = cms.Sequence( fragment.HLTPreshowerSequence + fragment.hltParticleFlowRecHitECALUnseeded + fragment.hltParticleFlowRecHitHBHE + fragment.hltParticleFlowRecHitHF + fragment.hltParticleFlowRecHitPSUnseeded + fragment.hltParticleFlowClusterECALUncorrectedUnseeded + fragment.hltParticleFlowClusterPSUnseeded + fragment.hltParticleFlowClusterECALUnseeded + fragment.hltParticleFlowClusterHBHE + fragment.hltParticleFlowClusterHCAL + fragment.hltParticleFlowClusterHF + fragment.hltLightPFTracks + fragment.hltParticleFlowBlockForTaus + fragment.hltParticleFlowForTaus )
fragment.HLTGlobalPFTriggerSequenceForTau = cms.Sequence( fragment.HLTL2muonrecoSequence + fragment.HLTL3muonrecoSequence + fragment.HLTRecoJetSequenceAK4PrePF + fragment.hltTauJet5 + fragment.HLTTrackReconstructionForPF + fragment.HLTParticleFlowSequenceForTaus + fragment.hltAK4PFJetsForTaus )
fragment.HLTPFTauHPS = cms.Sequence( fragment.hltTauPFJets08Region + fragment.hltHpsTauPFJetsRecoTauChargedHadronsWithNeutrals + fragment.hltPFTauPiZeros + fragment.hltHpsCombinatoricRecoTaus + fragment.hltHpsSelectionDiscriminator + fragment.hltHpsPFTauProducerSansRefs + fragment.hltHpsPFTauProducer + fragment.hltHpsPFTauDiscriminationByDecayModeFindingNewDMs + fragment.hltHpsPFTauTrackFindingDiscriminator + fragment.hltHpsSelectedPFTausTrackFinding + fragment.hltHpsPFTauTrack )
fragment.HLTGlobalPFTauHPSSequence = cms.Sequence( fragment.hltStripTrackerHVOn + fragment.hltPixelTrackerHVOn + fragment.HLTGlobalPFTriggerSequenceForTau + fragment.HLTPFTauHPS )
fragment.HLTEndSequence = cms.Sequence( fragment.hltBoolEnd )

fragment.HLTriggerFirstPath = cms.Path( fragment.hltGetConditions + fragment.hltGetRaw + fragment.hltBoolFalse )
fragment.HLT_IsoMu20_eta2p1_MediumChargedIsoPFTauHPS27_eta2p1_CrossL1_v1 = cms.Path( fragment.HLTBeginSequence + fragment.HLTGlobalPFTauHPSSequence + fragment.hltFixedGridRhoFastjetAll + fragment.hltHpsPFTauLooseAbsoluteChargedIsolationDiscriminator + fragment.hltHpsPFTauLooseRelativeChargedIsolationDiscriminator + fragment.hltHpsPFTauMediumAbsoluteChargedIsolationDiscriminatorReg + fragment.hltHpsPFTauMediumRelativeChargedIsolationDiscriminatorReg +fragment.hltHpsPFTauTightAbsoluteChargedIsolationDiscriminatorReg + fragment.hltHpsPFTauTightRelativeChargedIsolationDiscriminatorReg + fragment.hltRechitInRegionsECAL + fragment.hltParticleFlowRecHitECALL1Seeded + fragment.hltParticleFlowClusterECALUncorrectedL1Seeded + fragment.hltRechitInRegionsES + fragment.hltParticleFlowRecHitPSL1Seeded + fragment.hltParticleFlowClusterPSL1Seeded + fragment.hltParticleFlowClusterECALL1Seeded + fragment.hltParticleFlowSuperClusterECALL1Seeded + fragment.hltEgammaCandidates + fragment.hpsPFTauDiscriminationByDecayModeFindingNewDMs + fragment.hpsPFTauPrimaryVertexProducer + fragment.hpsPFTauSecondaryVertexProducer + fragment.hpsPFTauTransverseImpactParameters + fragment.pfRecoTauDiscriminationByLeadingTrackFinding + fragment.chargedIsoPtSum + fragment.chargedIsoPtSumdR03 + fragment.neutralIsoPtSum + fragment.neutralIsoPtSumdR03 + fragment.puCorrPtSum + fragment.footprintCorrection + fragment.footprintCorrectiondR03 + fragment.neutralIsoPtSumWeight + fragment.neutralIsoPtSumWeightdR03 + fragment.photonPtSumOutsideSignalCone + fragment.photonPtSumOutsideSignalConedR03 + fragment.deepTauProducer + fragment.tauTupleProducer + fragment.HLTEndSequence )
fragment.HLTriggerFinalPath = cms.Path( fragment.hltGtStage2Digis + fragment.hltScalersRawToDigi + fragment.hltFEDSelector + fragment.hltTriggerSummaryAOD + fragment.hltTriggerSummaryRAW + fragment.hltBoolFalse )
fragment.HLTAnalyzerEndpath = cms.EndPath( fragment.hltGtStage2Digis + fragment.hltPreHLTAnalyzerEndpath + fragment.hltL1TGlobalSummary + fragment.hltTrigReport )


fragment.HLTSchedule = cms.Schedule( *(fragment.HLTriggerFirstPath, fragment.HLT_IsoMu20_eta2p1_MediumChargedIsoPFTauHPS27_eta2p1_CrossL1_v1, fragment.HLTriggerFinalPath, fragment.HLTAnalyzerEndpath ))


# dummyfy hltGetConditions in cff's
if 'hltGetConditions' in fragment.__dict__ and 'HLTriggerFirstPath' in fragment.__dict__ :
    fragment.hltDummyConditions = cms.EDFilter( "HLTBool",
        result = cms.bool( True )
    )
    fragment.HLTriggerFirstPath.replace(fragment.hltGetConditions,fragment.hltDummyConditions)

# add specific customizations
from HLTrigger.Configuration.customizeHLTforALL import customizeHLTforAll
fragment = customizeHLTforAll(fragment,"GRun")

from HLTrigger.Configuration.customizeHLTforCMSSW import customizeHLTforCMSSW
fragment = customizeHLTforCMSSW(fragment,"GRun")

# Eras-based customisations
from HLTrigger.Configuration.Eras import modifyHLTforEras
modifyHLTforEras(fragment)
