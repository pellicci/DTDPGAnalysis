#include "FWCore/Framework/interface/MakerMacros.h"

#include "DTDPGAnalysis/src/DTDPGCreateSummary.h"
DEFINE_FWK_MODULE(DTDPGCreateSummary);

#include "DTDPGAnalysis/src/DTDPGCreateWheelSummary.h"
DEFINE_FWK_MODULE(DTDPGCreateWheelSummary);

#include "DTDPGAnalysis/src/CheckDeadChannels.h"
DEFINE_FWK_MODULE(CheckDeadChannels);

#include "DTDPGAnalysis/src/DTDPGCreateAnalyzerSummary.h"
DEFINE_FWK_MODULE(DTDPGCreateAnalyzerSummary);

#include "DTDPGAnalysis/interface/DTMuonSelection.h"
DEFINE_FWK_MODULE(DTMuonSelection);

#include "DTDPGAnalysis/src/DTOfflineAnalyzer.h"
DEFINE_FWK_MODULE(DTOfflineAnalyzer);

#include "DTDPGAnalysis/src/DTEffOfflineAnalyzer.h"
DEFINE_FWK_MODULE(DTEffOfflineAnalyzer);

#include "DTDPGAnalysis/src/STAOfflineAnalyzer.h"
DEFINE_FWK_MODULE(STAOfflineAnalyzer);

#include "DTDPGAnalysis/src/GlobalMuTriggerFilter.h"
DEFINE_FWK_MODULE(GlobalMuTriggerFilter);

