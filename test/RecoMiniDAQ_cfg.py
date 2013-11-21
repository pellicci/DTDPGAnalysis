import FWCore.ParameterSet.Config as cms

process = cms.Process("RECO")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration/StandardSequences/Services_cff')

process.load('Configuration.Geometry.GeometryIdeal_cff')
process.load('Configuration.EventContent.EventContent_cff')

process.load('RecoLuminosity.LumiProducer.lumiProducer_cff')

process.load("EventFilter.DTTFRawToDigi.dttfunpacker_cfi")
process.load("EventFilter.DTRawToDigi.dtunpackerDDUGlobal_cfi")
process.dttfunpacker.DTTF_FED_Source = "rawDataCollector"
process.dtunpacker.readOutParameters.debug = False
process.dtunpacker.readOutParameters.rosParameters.debug = False

#for RAW
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load("Configuration.StandardSequences.ReconstructionCosmics_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "GR_P_V41::All"

process.load('EventFilter.ScalersRawToDigi.ScalersRawToDigi_cfi')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("NewEventStreamFileReader",
           fileNames = cms.untracked.vstring(
           '/store/caf/user/dtdqm/InputMiniDAQRuns/dat/INPUTNAME'
         )
)

process.output = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('keep *'), 
    fileName = cms.untracked.string('file:/tmp/OUTPUTNAME'),
     # put this if you have a filter
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('p')
    ),
                                 
)

process.myRawToDigi = cms.Sequence(process.csctfDigis + process.dttfDigis + process.gctDigis + process.muonCSCDigis + process.muonDTDigis + process.muonRPCDigis + process.scalersRawToDigi)

process.p = cms.Path(process.myRawToDigi * process.dtunpacker * process.dttfunpacker * process.muonlocalreco * process.lumiProducer)
process.e = cms.EndPath(process.output)
