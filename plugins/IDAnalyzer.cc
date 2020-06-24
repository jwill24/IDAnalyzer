// -*- C++ -*-
//
// Package:    ID/IDAnalyzer
// Class:      IDAnalyzer
//
/**\class IDAnalyzer IDAnalyzer.cc ID/IDAnalyzer/plugins/IDAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Justin Williams
//         Created:  Wed, 24 Jun 2020 05:30:29 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/one/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "DataFormats/PatCandidates/interface/Photon.h"

//
// class declaration
//


class IDAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit IDAnalyzer(const edm::ParameterSet&);
      ~IDAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------
      edm::EDGetTokenT<edm::View<pat::Photon>> photonsToken_;
};


int numerator = 0;


//
// static data member definitions
//

//
// constructors and destructor
//
IDAnalyzer::IDAnalyzer(const edm::ParameterSet& iConfig)
 :
  photonsToken_(consumes<edm::View<pat::Photon>>(iConfig.getParameter<edm::InputTag>("photons")))

{
   //now do what ever initialization is needed

}


IDAnalyzer::~IDAnalyzer()
{

   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
IDAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace std;
   
   //std::vector<bool> passing;
   bool passing = true;


   for(const auto& pho : iEvent.get(photonsToken_) ) {
          
     //cout << "Photon pt: " << pho.pt() << endl;
     if (pho.pt() < 500) {
       passing = false;
       break;
     }

   }



   if (passing) numerator += 1;


}


// ------------ method called once each job just before starting event loop  ------------
void
IDAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
IDAnalyzer::endJob()
{
  std::cout << "Count: " << numerator << std::endl;
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
IDAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

  //Specify that only 'tracks' is allowed
  //To use, remove the default given above and uncomment below
  //ParameterSetDescription desc;
  //desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
  //descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(IDAnalyzer);