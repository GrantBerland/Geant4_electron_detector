//
// ********************************************************************
// * License and Disclaimer                                           *
// *                                                                  *
// * The  Geant4 software  is  copyright of the Copyright Holders  of *
// * the Geant4 Collaboration.  It is provided  under  the terms  and *
// * conditions of the Geant4 Software License,  included in the file *
// * LICENSE and available at  http://cern.ch/geant4/license .  These *
// * include a list of copyright holders.                             *
// *                                                                  *
// * Neither the authors of this software system, nor their employing *
// * institutes,nor the agencies providing financial support for this *
// * work  make  any representation or  warranty, express or implied, *
// * regarding  this  software system or assume any liability for its *
// * use.  Please see the license in the file  LICENSE  and URL above *
// * for the full disclaimer and the limitation of liability.         *
// *                                                                  *
// * This  code  implementation is the result of  the  scientific and *
// * technical work of the GEANT4 collaboration.                      *
// * By using,  copying,  modifying or  distributing the software (or *
// * any work based  on the software)  you  agree  to acknowledge its *
// * use  in  resulting  scientific  publications,  and indicate your *
// * acceptance of all terms of the Geant4 Software license.          *
// ********************************************************************
//
// $Id: SteppingAction.cc 74483 2013-10-09 13:37:06Z gcosmo $
//
/// \file SteppingAction.cc
/// \brief Implementation of the SteppingAction class

#include "SteppingAction.hh"
#include "EventAction.hh"
#include "DetectorConstruction.hh"
// #include "DetectorAnalysis.hh"
#include "G4Step.hh"
#include "G4Track.hh"
#include "G4Event.hh"
#include "G4RunManager.hh"
#include "G4LogicalVolume.hh"
#include "G4SystemOfUnits.hh"
#include "G4AutoLock.hh"

#include <fstream>

namespace { G4Mutex myParticleLog = G4MUTEX_INITIALIZER; }

SteppingAction::SteppingAction(EventAction* eventAction)
: G4UserSteppingAction(),
  fEventAction(eventAction)
{}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

SteppingAction::~SteppingAction()
{}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void SteppingAction::UserSteppingAction(const G4Step* step)
{

  G4bool isEnteringDetector1, isEnteringDetector2;
  G4String volName, nextVolName;
  
  G4Track* track = step->GetTrack();
  const G4StepPoint* postPoint = step->GetPostStepPoint();

 
  if (track->GetVolume()) {volName = track->GetVolume()->GetName();}
  if (track->GetNextVolume()) {nextVolName = track->GetNextVolume()->GetName();}


  isEnteringDetector1 = (volName != "detector1" && nextVolName == "detector1");
  isEnteringDetector2 = (volName != "detector2" && nextVolName == "detector2");

  // Detector 1 particles
  if (isEnteringDetector1){

    // Gather data about hit event (position, energy)
    G4ThreeVector pos = postPoint->GetPosition();
    G4double ene = postPoint->GetKineticEnergy();
    G4String fileName_detector1 = "../data1/hits.csv";     
    
    // Write event data to file
    LogParticle(pos, ene, fileName_detector1);

  }


  // Detector 2 particles
  if (isEnteringDetector2){

    fEventAction->incrementDetector2Flag();

    G4ThreeVector pos = postPoint->GetPosition();
    G4double ene = postPoint->GetKineticEnergy();
    G4String fileName_detector2 = "../data2/hits.csv"; 
    LogParticle(pos, ene, fileName_detector2);

  }

}

void SteppingAction::LogParticle(G4ThreeVector pos, G4double ene, G4String detectorFileName)
{
    
    G4AutoLock lock(&myParticleLog);
    
    std::ofstream hitFile_detector;
    hitFile_detector.open(detectorFileName, std::ios_base::app);
    
    hitFile_detector  << pos.x()/cm << "," << pos.y()/cm << "," 
	    	      << pos.z()/cm << "," << ene/keV << "\n";
    
    hitFile_detector.close();
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
