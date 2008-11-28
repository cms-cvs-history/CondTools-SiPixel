import FWCore.ParameterSet.Config as cms

process = cms.Process("PixelPopConTest")

process.source = cms.Source("EmptyIOVSource",

  firstValue = cms.uint64(1),
  lastValue = cms.uint64(1),
  interval = cms.uint64(1),
  timetype = cms.string('runnumber')
)

process.load("CondCore.DBCommon.CondDBSetup_cfi")
#process.CondDBSetup.DBParameters.authenticationPath = '/afs/cern.ch/cms/DB/conddb'

process.PoolDBOutputService = cms.Service("PoolDBOutputService",

  process.CondDBSetup,

  connect = cms.string('sqlite_file:pixelPVSSCond.db'),
  timetype = cms.untracked.string('runnumber'),
  logconnect = cms.untracked.string('sqlite_file:log.db'),

  toPut = cms.VPSet
  (
    cms.PSet( record = cms.string('PixelCaenChannelIsOnRcd'), tag = cms.string('IsOn') ),
    cms.PSet( record = cms.string('PixelCaenChannelIMonRcd'), tag = cms.string('IMon') )
  )
)

process.PixelCaenChannelIsOn = cms.EDAnalyzer("PixelPopConBoolAnalyzer",

  record = cms.string('PixelCaenChannelIsOnRcd'),
  loggingOn = cms.untracked.bool(True),
  SinceAppendMode = cms.bool(True),

  Source = cms.PSet
  (
    dbName = cms.string('CMSONR'),
    user = cms.string('CMS_PXL_PIXEL_R'),
    table = cms.string('DCSLASTVALUE_ON'),
    column = cms.string('ACTUAL_ISON'),
  )
)

process.PixelCaenChannelIMon = cms.EDAnalyzer("PixelPopConFloatAnalyzer",

  record = cms.string('PixelCaenChannelIMonRcd'),
  loggingOn = cms.untracked.bool(True),
  SinceAppendMode = cms.bool(True),

  Source = cms.PSet
  (
    dbName = cms.string('CMSONR'),
    user = cms.string('CMS_PXL_PIXEL_R'),
    table = cms.string('DCSLASTVALUE_CURRENT'),
    column = cms.string('ACTUAL_IMON'),
  )
)

process.p = cms.Path(process.PixelCaenChannelIsOn*process.PixelCaenChannelIMon)
