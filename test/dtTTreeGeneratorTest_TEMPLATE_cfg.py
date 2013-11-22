import FWCore.ParameterSet.Config as cms

process = cms.Process("myDTNtuple")

process.load('Configuration.Geometry.GeometryIdeal_cff')
process.load("Configuration.StandardSequences.MagneticField_cff")

process.load("RecoMuon.TrackingTools.MuonServiceProxy_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "GR_P_V41::All"

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
        skipEvents = cms.untracked.uint32(0),
        fileNames = cms.untracked.vstring(
       '/store/caf/user/pellicci/DPG/MiniDAQReco/INPUTNAME'
    )
)

process.load("UserCode/DTDPGAnalysis/DTTTreGenerator_cfi")
process.myDTNtuple.outputFile = "/tmp/OUTPUTNAME"
process.myDTNtuple.runOnMiniDAQ = True

process.p = cms.Path(process.myDTNtuple)

