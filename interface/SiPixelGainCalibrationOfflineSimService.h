#ifndef CondTools_SiPixel_SiPixelGainCalibrationOfflineSimService_H
#define CondTools_SiPixel_SiPixelGainCalibrationOfflineSimService_H

// ************************************************************************
// ************************************************************************
// *******     SiPixelOfflineCalibrationOfflineSimService           *******
// *******     Author:   Freya Blekman                              *******
// *******     based on code by:   Evan Friis (evan.friis@cern.ch)  *******
// *******                                                          *******
// *******     Retrives gain calibration data from offline DB       *******
// *******     at medium  (gain:column,pedestal:pixel) granularity  *******
// *******                                                          *******
// ************************************************************************
// ************************************************************************

// Gain CalibrationOffline base class
#include "CondTools/SiPixel/interface/SiPixelGainCalibrationServiceBase.h"

#include "CondFormats/SiPixelObjects/interface/SiPixelGainCalibrationOffline.h" 
#include "CondFormats/DataRecord/interface/SiPixelGainCalibrationOfflineSimRcd.h"

class SiPixelGainCalibrationOfflineSimService : public SiPixelGainCalibrationServicePayloadGetter<SiPixelGainCalibrationOffline,SiPixelGainCalibrationOfflineSimRcd>
{

 public:
  explicit SiPixelGainCalibrationOfflineSimService(const edm::ParameterSet& conf) : SiPixelGainCalibrationServicePayloadGetter<SiPixelGainCalibrationOffline,SiPixelGainCalibrationOfflineSimRcd>(conf){};
  ~SiPixelGainCalibrationOfflineSimService(){};

  // pixel granularity
  float   getPedestal  ( const uint32_t& detID,const int& col, const int& row);
  float   getGain      ( const uint32_t& detID,const int& col, const int& row);
  bool    isDead       ( const uint32_t& detID,const int& col, const int& row);
  bool    isDeadColumn ( const uint32_t& detID,const int& col, const int& row);
  bool    isNoisy       ( const uint32_t& detID,const int& col, const int& row);
  bool    isNoisyColumn ( const uint32_t& detID,const int& col, const int& row);
};
#endif