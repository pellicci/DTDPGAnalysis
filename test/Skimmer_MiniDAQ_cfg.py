import FWCore.ParameterSet.Config as cms

process = cms.Process("Skim")

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

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )

process.source = cms.Source("NewEventStreamFileReader",
           fileNames = cms.untracked.vstring(
           'file:Minidaq.dat'
         )
)

process.output = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('drop *', 
        'keep *_dt4DSegments_*_*',
        'keep *_dt2DSegments_*_*',
        'keep *_dt1DRecHits_*_*',
        'keep *_muonDTDigis_*_*',
        'keep *_dttfunpacker_*_*',
        'keep *_dtunpacker_*_*',
        'keep *_gtDigis_*_*',
        'keep *_offlinePrimaryVertices_*_*',
        'keep *_cscSegments_*_*',
        'keep *_rpcRecHits_*_*',
        'keep *_muons_*_*',
        'keep recoTracks_standAloneMuons_*_*',
        'keep recoTrackExtras_standAloneMuons_*_*',
        'keep TrackingRecHitsOwned_standAloneMuons_*_*', 
        'keep recoTracks_globalMuons_*_*',
        'keep recoTrackExtras_globalMuons_*_*',
        'keep TrackingRecHitsOwned_globalMuons_*_*',
        'keep recoTracks_generalTracks_*_*',
        'keep *_offlineBeamSpot_*_*',
        'keep *_TriggerResults_*_*',
        'keep LumiScalerss_*_*_*',
        'keep LumiDetails_lumiProducer_*_*',
	'keep *_MEtoEDMConverter_*_*'),
    fileName = cms.untracked.string('DTFiltered.root'),
     # put this if you have a filter
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('p')
    ),
                                 
)

#for RAW
process.p = cms.Path(process.RawToDigi * process.reconstructionCosmics * process.dtunpacker * process.dttfunpacker * process.lumiProducer)

process.e = cms.EndPath(process.output)
