import FWCore.ParameterSet.Config as cms

process = cms.Process("PixelPopConDCSTest")

process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.load("CondTools.SiPixel.PixelPopConDCSAnalyzer_cfi")

process.source = cms.Source("EmptyIOVSource",

  firstValue = cms.uint64(1),
  lastValue = cms.uint64(1),
  interval = cms.uint64(1),
  timetype = cms.string('runnumber')
)

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

process.p = cms.Path(process.PixelCaenChannel)
