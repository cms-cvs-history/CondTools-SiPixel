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
    cms.PSet( record = cms.string('PixelCaenChannelIMonRcd'), tag = cms.string('IMon') ),
    cms.PSet( record = cms.string('PixelCaenChannelRcd'), tag = cms.string('All') )
  )
)

process.PixelCaenChannelIsOn = cms.EDAnalyzer("PixelPopConBoolAnalyzer",

  record = cms.string('PixelCaenChannelIsOnRcd'),
  loggingOn = cms.untracked.bool(True),
  SinceAppendMode = cms.bool(True),

  Source = cms.PSet
  (
    authenticationPath = cms.string('.'),
    dbName = cms.string('CMSONR'),
    tables = cms.vstring('DCSLASTVALUE_ON')
  )
)

process.PixelCaenChannelIMon = cms.EDAnalyzer("PixelPopConFloatAnalyzer",

  record = cms.string('PixelCaenChannelIMonRcd'),
  loggingOn = cms.untracked.bool(True),
  SinceAppendMode = cms.bool(True),

  Source = cms.PSet
  (
    authenticationPath = cms.string('.'),
    dbName = cms.string('CMSONR'),
    tables = cms.vstring('DCSLASTVALUE_CURRENT')
  )
)

process.PixelCaenChannel = cms.EDAnalyzer("PixelPopConCaenChannelAnalyzer",

  record = cms.string('PixelCaenChannelRcd'),
  loggingOn = cms.untracked.bool(True),
  SinceAppendMode = cms.bool(True),

  Source = cms.PSet
  (
    authenticationPath = cms.string('.'),
    dbName = cms.string('CMSONR'),
    tables = cms.vstring('DCSLASTVALUE_ON', 'DCSLASTVALUE_CURRENT', 'DCSLASTVALUE_VOLTAGE')
  )
)

process.p = cms.Path(process.PixelCaenChannel)
