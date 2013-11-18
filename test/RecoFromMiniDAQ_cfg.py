import FWCore.ParameterSet.Config as cms

process = cms.Process("DTDPGAnalyis")


process.load("UserCode.DTDPGAnalysis.dt_dpganalysis_common_cff_cosmics_miniDAQ")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("NewEventStreamFileReader",
           fileNames = cms.untracked.vstring(
           'file:Minidaq.dat'
         )
)

from CondCore.DBCommon.CondDBSetup_cfi import *

process.ttrigsource = cms.ESSource("PoolDBESSource",
    CondDBSetup,
    timetype = cms.string('runnumber'),
    toGet = cms.VPSet(cms.PSet(record = cms.string('DTTtrigRcd'),
                               label = cms.untracked.string('cosmics'),  ## ONLY if using cosmic reconstruction  
                               tag = cms.string('ttrig')
                               )
                      ),
    connect = cms.string('sqlite_file:/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DT/OfflineCode/LocalDataBases/ttrig_residuals_198230-Inf.db'),

    authenticationMethod = cms.untracked.uint32(0)
    )

process.es_prefer_ttrigsource = cms.ESPrefer('PoolDBESSource','ttrigsource')

# MAGNETIC FIELD
#### B = 0 Tesla ###############################################################
process.load("Configuration.StandardSequences.MagneticField_0T_cff")
##process.SteppingHelixPropagator.useInTeslaFromMagField = True
##process.SteppingHelixPropagator.SetVBFPointer = True
#### B = 3.8 Tesla #############################################################
##process.load("Configuration.StandardSequences.MagneticField_38T_cff")

#--------------------------------------------------------

#--------------------------------------------------------
process.UpdaterService = cms.Service("UpdaterService")  ###  Only needed for STA reco
#--------------------------------------------------------


process.out = cms.OutputModule("PoolOutputModule",
                               outputCommands = cms.untracked.vstring('keep *'),
                               fileName = cms.untracked.string('RecoMiniDAQ.root')
                               )

### IF ONLY RAW, NEED TO PERFORM RECONSTRUCTION 
#Without including STA 
#process.p = cms.Path( process.dtunpacker * process.dttfunpacker * process.reco + process.sources + process.MEtoEDMConverter ) 
#including STA 
process.p = cms.Path( process.dtunpacker * process.dttfunpacker * process.reco * process.globalreco + process.sources) 
### RAW+RECO DATASET
#process.p = cms.Path( process.dtunpacker * process.dttfunpacker + process.sources + process.MEtoEDMConverter) 

process.ep = cms.EndPath( process.out )

