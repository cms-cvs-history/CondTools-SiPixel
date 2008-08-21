"""
testPixelPopConCalibAnalyzer_cfg.py

Python configuration file to do the popcon transfer of the calibration configuration file.__class__

M. Eads
Aug 2008
"""


import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.MessageLogger=cms.Service("MessageLogger",
                              destinations=cms.untracked.vstring("cout"),
                              cout=cms.untracked.PSet(
                              treshold=cms.untracked.string("INFO")
                              )
)

process.load("CondCore.DBCommon.CondDBCommon_cfi")
process.CondDBCommon.connect = cms.string('sqlite_file:testExample.db')
process.CondDBCommon.DBParameters.authenticationPath = cms.untracked.string('/afs/cern.ch/cms/DB/conddb')

process.source = cms.Source("EmptyIOVSource",
    timetype = cms.string('runnumber'),
    firstRun = cms.untracked.uint32(1),
    lastRun = cms.untracked.uint32(1),
    interval = cms.uint32(1)
)

process.PoolDBOutputService = cms.Service("PoolDBOutputService",
    process.CondDBCommon,
    timetype = cms.untracked.string('runnumber'),
    toPut = cms.VPSet(cms.PSet(
        record = cms.string('SiPixelCalibConfigurationRcd'),
        tag = cms.string('mytest')
         )),
    logconnect= cms.untracked.string('sqlite_file:logtestExample.db')                                     
)

process.mytest = cms.EDAnalyzer("PixelPopConCalibAnalyzer",
    record = cms.string('SiPixelCalibConfigurationRcd'),
    loggingOn= cms.untracked.bool(True),
    SinceAppendMode=cms.bool(True),
    Source=cms.PSet(firstSince=cms.untracked.double(300),
                    #connectString = cms.string('oracle://CMS_PXL_INT2R_LB/CMS_PXL_PRTTYPE_PIXEL_READER'),
                    connectString = cms.string('file:///afs/cern.ch/user/m/meads/test_calib.dat'),
                    schemaName = cms.string('CMS_PXL_PIXEL_VIEW_OWNER'),
                    viewName = cms.string('CONF_KEY_PIXEL_CALIB_V'),
                    runNumber = cms.int32(-1),
                    configKeyName = cms.string('pixel-config-key-demo2'),
                    sinceIOV = cms.uint32(1)
                    )
                                 
)

process.p = cms.Path(process.mytest)
