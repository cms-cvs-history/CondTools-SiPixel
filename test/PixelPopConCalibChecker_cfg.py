"""
PixelPopConCalibChecker_cfg.py

Python configuration file to run PixelPopConCalibChecker EDanalyzer, which 
checks calib configuration objects transferred into the database.

M. Eads
Aug 2008
"""

import FWCore.ParameterSet.Config as cms

process = cms.Process("TEST")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source('EmptyIOVSource',
                            timetype = cms.string('runnumber'),
                            firstRun = cms.untracked.uint32(1),
                            lastRun = cms.untracked.uint32(1),
                            interval = cms.uint32(1)
)

from CondTools.SiPixel.SiPixelCalibConfiguration_cfi import *
sipixelcalib_essource.connect = 'sqlite_file:/afs/cern.ch/user/m/meads/scratch0/CMSSW_2_1_2/src/testExample.db'
sipixelcalib_essource.toGet = cms.VPSet(cms.PSet(record = cms.string('SiPixelCalibConfigurationRcd'),
                                                 tag = cms.string('mytest')
                                                 )
                                        )
process.sipixelcalib_essource = sipixelcalib_essource


process.demo = cms.EDAnalyzer('PixelPopConCalibChecker',
                              filename = cms.string('/afs/cern.ch/user/m/meads/test_calib.dat'),
                              messageLevel = cms.untracked.int32(2)
                              )


process.p = cms.Path(process.demo)
