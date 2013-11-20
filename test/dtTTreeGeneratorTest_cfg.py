import FWCore.ParameterSet.Config as cms

process = cms.Process("myDTNtuple")

#only for RAW and RAW-RECO
#process.load("EventFilter.DTRawToDigi.dtunpackerDDUGlobal_cfi")
#process.dtunpacker.readOutParameters.debug = False
#process.dtunpacker.readOutParameters.rosParameters.debug = False
#process.load("EventFilter.DTTFRawToDigi.dttfunpacker_cfi")
#process.dttfunpacker.DTTF_FED_Source = "rawDataCollector"

#process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
#process.load("Configuration.StandardSequences.Reconstruction_cff")
#process.load('Configuration/EventContent/EventContent_cff')


process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.Geometry.GeometryIdeal_cff')

process.load("RecoMuon.TrackingTools.MuonServiceProxy_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "GR_P_V41::All"

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
        skipEvents = cms.untracked.uint32(0),
        fileNames = cms.untracked.vstring(
       '/store/caf/user/pellicci/DPG/MiniDAQReco/Minidaq.00214419.0001.A.storageManager.00.0001.root'
    )
)

process.load("UserCode/DTDPGAnalysis/DTTTreGenerator_cfi")
process.myDTNtuple.outputFile = "DTTree_tmp.root"
process.myDTNtuple.runOnMiniDAQ = True

#for RAW
#process.p = cms.Path(process.RawToDigi * process.dtunpacker * process.dttfunpacker * process.reconstruction * process.myDTNtuple)

#for RAW-RECO
#process.p = cms.Path(process.muonDTDigis * process.myDTNtuple)

#for RECO and SKIM
process.p = cms.Path(process.myDTNtuple)

