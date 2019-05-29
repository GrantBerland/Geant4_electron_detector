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
// $Id: PrimaryGeneratorAction.cc 94307 2015-11-11 13:42:46Z gcosmo $
//
/// \file PrimaryGeneratorAction.cc
/// \brief Implementation of the PrimaryGeneratorAction class

#include "PrimaryGeneratorAction.hh"

#include "G4LogicalVolumeStore.hh"
#include "G4LogicalVolume.hh"
#include "G4Box.hh"
#include "G4RunManager.hh"
#include "G4ParticleGun.hh"
//#include "G4GeneralParticleSource.hh"
#include "G4ParticleTable.hh"
#include "G4ParticleDefinition.hh"
#include "G4SystemOfUnits.hh"
#include "G4UnitsTable.hh"
#include "Randomize.hh"
#include <math.h>

#include <fstream>


PrimaryGeneratorAction::PrimaryGeneratorAction()
: G4VUserPrimaryGeneratorAction(),
  fParticleGun(0)
{
  fParticleGun  = new G4ParticleGun();
  G4ParticleDefinition* electronParticle = G4ParticleTable::GetParticleTable()->FindParticle("e-");

  // Selects electron for particle type
  fParticleGun->SetParticleDefinition(electronParticle);
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

PrimaryGeneratorAction::~PrimaryGeneratorAction()
{
  delete fParticleGun;
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......

void PrimaryGeneratorAction::GeneratePrimaries(G4Event* anEvent)
{

  G4double PI = 3.14159265358979323846; 

  // Allocating variables for particle and simulation state 
  G4double xPos, yPos, zPos, xDir, yDir, zDir;
  G4double energy;
  G4double particleAngle_theta, particleAngle_phi;
  G4int    nParticles;
 
  
  std::fstream configFile;
  configFile.open("./part_energy_theta_phi_nPart.txt", std::ios_base::in);

  configFile >> energy >> particleAngle_theta >> particleAngle_phi >> nParticles;

  energy *= keV; 		   // input in keV
  particleAngle_theta *= PI/180.;  // conversion to radians
  particleAngle_phi *= PI/180.;    // conversion to radians

  configFile.close();

  // Static (x,y,z) position that allows for up to +/- 45 deg incident angle
  xPos = 0; yPos = -4 * cm; zPos = 0;  
  // Momentum direction of particle (not normalized!)
  yDir = 1;
  zDir = yDir * tan(particleAngle_theta);
  xDir = yDir * tan(particleAngle_phi);

  // Generate nParticles events with the above parameters
  for(G4int i = 0; i<nParticles; i++){

    fParticleGun->SetParticlePosition(G4ThreeVector(xPos, yPos, zPos));
    fParticleGun->SetParticleMomentumDirection(G4ThreeVector(xDir, yDir, zDir));
    fParticleGun->SetParticleEnergy(energy);
    fParticleGun->GeneratePrimaryVertex(anEvent);
  }

}


