#ifndef DTEFFOFFLINEANALYZER_H
#define DTEFFOFFLINEANALYZER_H

/** \class DTEffOfflineAnalyzer
 *
 * Description:
 *  
 *  detailed description
 *
 * \author : Stefano Lacaprara - INFN LNL <stefano.lacaprara@pd.infn.it>
 * $date   : 20/11/2006 16:51:04 CET $
 *
 * Modification:
 *
 */

/* Base Class Headers */
#include "FWCore/Framework/interface/EDAnalyzer.h"
namespace edm {
  class ParameterSet;
  class Event;
  class EventSetup;
}

/* Collaborating Class Declarations */
#include "DataFormats/Common/interface/Handle.h"
#include "FWCore/Framework/interface/ESHandle.h"
class TFile;
class DQMStore;
class TH1F;
class TH2F;
class DTLayerId;
class DTSuperLayerId;
class DTChamberId;
#include "Geometry/DTGeometry/interface/DTGeometry.h"
#include "DataFormats/DTRecHit/interface/DTRecSegment4DCollection.h"
class DTTTrigBaseSync;

/* C++ Headers */
#include <iosfwd>
#include <bitset>

/* ====================================================================== */

/* Class DTEffOfflineAnalyzer Interface */

class DTEffOfflineAnalyzer : public edm::EDAnalyzer {

  public:

/* Constructor */ 
    DTEffOfflineAnalyzer(const edm::ParameterSet& pset) ;

/* Destructor */ 
    ~DTEffOfflineAnalyzer() ;

/* Operations */ 

    void analyze(const edm::Event & event, const edm::EventSetup& eventSetup);
    void beginJob(const edm::EventSetup&);

  private:

    TH1F* histo(const std::string& name) const;
    TH2F* histo2d(const std::string& name) const;

    enum LCTType { DT, CSC, RPC_W1, RPC_W2 };
    bool getLCT(LCTType) const;
    bool selectEvent() const ;
    void effSegments(const edm::Event & event,
                     const edm::EventSetup& eventSetup);
    
    const DTRecSegment4D& getBestSegment(const DTRecSegment4DCollection::range& segs) const;
    const DTRecSegment4D* getBestSegment(const DTRecSegment4D* s1,
                                         const DTRecSegment4D* s2) const;
    bool isGoodSegment(const DTRecSegment4D& seg) const;
    LocalPoint interpolate(const DTRecSegment4D& seg1,
                           const DTRecSegment4D& seg3,
                           const DTChamberId& MB2) const;

    void evaluateEff(const DTChamberId& MidId,
                     int bottom,
                     int top) const ;

    void createTH1F(const std::string& name,
                    const std::string& title,
                    const std::string& suffix,
                    int nbin, const double& binMin, const double& binMax) const;

    void createTH2F(const std::string& name,
                    const std::string& title,
                    const std::string& suffix,
                    int nBinX,
                    const double& binXMin,
                    const double& binXMax,
                    int nBinY,
                    const double& binYMin,
                    const double& binYMax) const ;

    std::string toString(const DTChamberId& id) const;
    template<class T> std::string hName(const std::string& s, const T& id) const;
  private:
    bool LCT_RPC, LCT_DT, LCT_CSC;
    bool debug;
    std::string theRootFileName;
    DQMStore *theDQMStore;
    std::string theDTLocalTriggerLabel;
    std::string theRecHits4DLabel;
    std::string theRecHits2DLabel;     
    std::string theRecHits1DLabel;     
    std::string theSTAMuonLabel;
    bool mc;
    unsigned int theMinHitsSegment;
    double theMinChi2NormSegment;
    double theMinCloseDist;

    std::bitset<6> LCT;

    bool init;

    edm::ESHandle<DTGeometry> dtGeom;
    edm::Handle<DTRecSegment4DCollection> segs;
  protected:

};
#endif // DTANALYZER_H

