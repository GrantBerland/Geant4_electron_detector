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

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

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

  G4bool isEnteringDetector1;
  G4bool isEnteringDetector2;

  G4Track* track = step->GetTrack();

  G4String volName;
  if (track->GetVolume()) {volName = track->GetVolume()->GetName();}
  G4String nextVolName;
  if (track->GetNextVolume()) {nextVolName = track->GetNextVolume()->GetName();}

  isEnteringDetector1 = (volName != "detector1" && nextVolName == "detector1");
  isEnteringDetector2 = (volName != "detector2" && nextVolName == "detector2");

  if (isEnteringDetector1){
    G4ThreeVector momentum = track->GetMomentumDirection();
    G4ThreeVector position = track->GetPosition();

    // TODO: change these names later
    G4double x = position.x();
    G4double y = position.y();
    G4double z = position.z();

    // Computes momentum magnitude and direction (wrt to simulation axes?)
    G4double mom_x = momentum.x();
    G4double mom_y = momentum.y();
    G4double mom_z = momentum.z();
    G4double mom_mag = sqrt(pow(mom_x, 2)+pow(mom_y, 2)+pow(mom_z, 2));

    G4double angle_x = acos(mom_x/mom_mag);
    G4double angle_y = acos(mom_y/mom_mag);
    G4double angle_z = acos(mom_z/mom_mag);

    // write angle and position to file? plots? histo?
  }

  if (isEnteringDetector2){
    G4ThreeVector momentum = track->GetMomentumDirection();
    G4ThreeVector position = track->GetPosition();

    // change these names later
    G4double x = position.x();
    G4double y = position.y();
    G4double z = position.z();

    // write angle and position to file
  }


  // Collect energy deposited in this step
  G4double edepStep = step->GetTotalEnergyDeposit();


}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
